```python
!pip install requests   #подключаем библиотеку запросов
```

    Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (2.26.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests) (2021.10.8)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests) (1.26.7)
    Requirement already satisfied: charset-normalizer~=2.0.0 in c:\programdata\anaconda3\lib\site-packages (from requests) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests) (3.2)
    


```python
import requests
import pandas as pd
```
Обратимся к VK API, чтобы скачать список наших друзей
Свой персональный access_token можно получить по адресу https://vkhost.github.io/ (vk.com)
User_id - индентикифатор пользователя, вокруг которого будет строиться граф 
Обратите внимание, что форма запроса может измениться в результате обновлений метода или API VK
Если мы изменяем что-то в query_params, то нужно изменить ссылку в query

```python
domain = "https://api.vk.com/method/friends.get"
access_token = "вставьте сюда свой access token"
user_id = 48166591

query_params = {
    'domain' : domain,
    'access_token': access_token,
    'user_id': user_id,
    'fields' : 'sex'
}

query = "{domain}?access_token={access_token}&user_id={user_id}&fields={fields}&v=5.81".format(**query_params)
response = requests.get(query)
```
Получим ответ в формате json и превратим его в датафрейм. Выведем полученные данные на экран.

```python
import json
data = response.json()['response']['items']
friends = pd.json_normalize(data)
```


```python
print(friends)
```

                id                                         track_code  sex  \
    0       146504  9eb34e14tUvPl7c8CcpExmAwIk_gkR5sq-DqHSdCcJpbQ_...    2   
    1       250557  3fb7016cobbbgQi6ESWTigJggOjWoNUrF4_ZJhDTS9N9sY...    2   
    2       404849  69b7f0a2jttaFrErjcddsM9Nvid50mvGo9XV6gzY4v1URi...    2   
    3       429633  d9bb746e3XEQXaE5pItBsYFlkUX4YoER0WyGGOJWODfvhI...    1   
    4       562242  2f93ac73gI6Y5Aj2TRsZeIOzhzmQVdk-W7GzSpz31mIfzP...    1   
    ..         ...                                                ...  ...   
    522  679180055  3e852137dkY8D85h0p-qZgNrhKEmq4GhS_RpvsmovCtuM2...    1   
    523  679501061  b6596d00E7TQxcESpj5wOSs1Lxh1UFwmQFSAfpLhSw7LtU...    1   
    524  706962258  8e6cdf89YvFUuNH10h9-1IJhdbunmCWNKTL_VJM2T9C0FS...    1   
    525  709338305  0aa9481a7kJ2Wc1UJoSU4eXGAGca1PkNNR7NHFEi2FAtU2...    2   
    526  731088348  197f57d5C7P7uI6bVbQXxBnne9-xWsNmhgbLz6lkrrq7g7...    1   
    
        first_name     last_name lists deactivated  
    0      Дмитрiй       Бродинъ   NaN         NaN  
    1      Виталiй  Пасичниченко   NaN         NaN  
    2        Максъ    Nikiforoff   NaN         NaN  
    3        Алина      Назарова   NaN         NaN  
    4     Катерина         Орехъ  [25]         NaN  
    ..         ...           ...   ...         ...  
    522    Надежда       Иванова   NaN         NaN  
    523      Lydia     Trofimova   NaN      banned  
    524       Lisa         Minci   NaN         NaN  
    525       Paul         Scott   NaN         NaN  
    526       Anna            Li   NaN         NaN  
    
    [527 rows x 7 columns]
    
Создадим массив, состоящий из идентификаторов наших друзей
Также создадим словарь, куда будем записывать общих друзей с нашими друзьями
В пустом массиве error будем складировать те идентификаторы, где данные недоуступны (например, страница была удалена)

```python
idz = [int(i) for i in friends['id']]
dic = {}
error = []
```
Чтобы избежать слишком большого числа запросов к серверу, импортируем time и будем использовать функцию time.sleep()
В цикле переберем идентификаторы друзей, чтобы с помощью метода getMutual собрать общих друзей

```python
import time
```


```python
domain = "https://api.vk.com/method/friends.getMutual"
access_token = "вставьте сюда свой access token"
for i in idz:
    query_params = {
        'domain' : domain,
        'access_token': access_token,
        'source_uid': 48166591,
        'target_uid': i,
        }
    query = "{domain}?access_token={access_token}&source_uid={source_uid}&target_uid={target_uid}&v=5.81".format(**query_params)
    response = requests.get(query)
    if response.json().get('response', False) is False:
        error.append(i)
    else:
        dat = response.json()['response']
        if len(dat) != 0:
            dic[i] = dat
            time.sleep(0.33)
```
idz2 уже не содержит неактивных пользователей и закрытые страницы

```python
idz2 = list(set(idz).difference(set(error)))
```


```python
Приступим к построению графа
```


```python
import networkx as nx
import matplotlib.pyplot as plt

color_map = []

G = nx.Graph()
  
for node in idz2:
    G.add_node(node, color='red')
    
for i in idz:
    G.add_edges_from([(str(48166591), str(i))], length = 1e1000)
    
for friend in dic:
    for connect in dic[friend]:
        G.add_edges_from([(str(friend), str(connect))], length = 1e1000)

        

G.remove_nodes_from(list(nx.isolates(G)))
nx.draw(G, node_color='red', edge_color='#191a19', node_size=1, with_labels=False, font_color='blue', cmap=True)

plt.show()
```

![Image alt](https://i.ibb.co/GsRJdk6/output-15-0.png)
    

Попробуем выделить группы друзей внутри графа и раскрасить их в разные цвета

```python
from networkx.algorithms.community import greedy_modularity_communities
c = greedy_modularity_communities(G)
'''https://networkx.org/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities'''
```


```python
colormap = []
for node in G:
    if str(node) in c[0]:
        colormap.append('red')
    elif str(node) in c[1]:
        colormap.append('orange')
    elif str(node) in c[2]:
        colormap.append('green')
    elif str(node) in c[3]:
        colormap.append('blue')
    elif str(node) in c[4]:
        colormap.append('violet')
    elif str(node) in c[5]:
        colormap.append('purple')
```


```python
#graph = nx.draw_networkx(G, node_color=color_map) # node lables
nx.draw(G, node_color=colormap, edge_color='#191a19', node_size=2, with_labels=False, font_color='blue', cmap=True)
```


![Image alt](https://i.ibb.co/QNxsGRX/output-19-0.png)
    



```python
Также мы можем посмотреть на основные характеристики графа
```


```python
# Посмотрим на количество узлов в графе
print(G.number_of_nodes(), '- количество узлов')

# Посмотрим на количество связей в графе
print(G.number_of_edges(), '- количество связей')
# Плотность графа, отношение рёбер и узлов

print(nx.density(G), 'плотность графа')

# Коэффициент ассортативности (насколько вся сеть завязана на основных "хабах"):

print(nx.degree_pearson_correlation_coefficient(G), 'ассортативность')
```

    528 - количество узлов
    3647 - количество связей
    0.026213271232246566 плотность графа
    -0.13831952958554017 ассортативность
    


```python
### Центральности
# Так как наш граф ненаправленный, мы можем проделать не так много всего.
# Посчитаем 3 стандарные меры центральностей: betweenness, closeness, eigenvector
# На моем компьютере это заняло достаточно длительное время,
# networkx правда не идеален для таких больших графов.

# Betweenness centrality, или посредничество
# Эта мера показывает, насколько узел связывает несколько несвязанных сообществ,
# или занимает позицию "между"
bet_centr = nx.betweenness_centrality(G)

# Closeness centrality
# Эта мера показывает, насколько узел близок ко всем остальным узлам в сети
clo_centr = nx.closeness_centrality(G)

# Eigenvector centrality
# Эта мера показывает, насколько узел связан с узлами,
# которые сами имеют большое количество связей
eig_centr = nx.eigenvector_centrality(G)

# Получаем индидивидуальные меры посредничества, близости и eigenvector для каждого узла

```


```python
from statistics import mean
print(mean(bet_centr[k] for k in G)) # Betweenness centrality (average)
print(mean(clo_centr[k] for k in G)) # Closeness centrality (average)
print(mean(eig_centr[k] for k in G)) # Eigenvector centrality (average)
print(nx.average_shortest_path_length(G)) # returns average of shortest paths between all possible pairs of nodes
print("Diameter: ", nx.diameter(G))
print("Radius: ", nx.radius(G))
#print("Eccentricity: ", *nx.eccentricity(G))
#print("Preiphery: ", list(nx.periphery(G)))
print("Center: ", list(nx.center(G)))
```

    0.001851305567999533
    0.5071952124690835
    0.029016236787667318
    1.9737867287677535
    Diameter:  2
    Radius:  1
    Center:  ['48166591']
    
Эксцентриситет: для узла n в графе G эксцентриситетом n является максимально возможное расстояние кратчайшего пути между n и всеми другими узлами.
Диаметр : максимальное кратчайшее расстояние между парой узлов в графе G равно его диаметру. Это максимально возможное значение эксцентриситета узла.
Радиус: это минимальное значение эксцентриситета узла.
Периферия: это набор узлов, эксцентриситет которых равен их диаметру.
Центр: центр графа - это набор узлов, эксцентриситет которых равен радиусу графа.'''
