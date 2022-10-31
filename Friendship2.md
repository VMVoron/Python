Подключаем библиотеку запросов

```python
!pip install requests   
```

    Requirement already satisfied: requests in c:\programdata\anaconda3\lib\site-packages (2.26.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests) (2021.10.8)
    Requirement already satisfied: charset-normalizer~=2.0.0 in c:\programdata\anaconda3\lib\site-packages (from requests) (2.0.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests) (1.26.7)
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
access_token = "xxxxxxxxx"
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
    0       146504  01c77b55D9BQxMzZboBPcf97czWquUoiLAbDCfM0HHcIHS...    2   
    1       250557  90a74ed9HX_QigAB_Y7O4D3zulk07CEDoUpOtoX9jCWMrp...    2   
    2       404849  e8bba83em9sXrSbCFxTkVxwXMySNIQpGNVQKtZM78NLGMb...    2   
    3       429633  1d9e9dedyoVpevlEYh9MObgYEJVzCztXj__9IeEk2mCQTY...    1   
    4       562242  32a01ddaCniGcBoObb6m6M-0fRfiyXLghcbQCmzbCWXMJg...    1   
    ..         ...                                                ...  ...   
    522  679180055  18275d19QmeZl2CaklP0Pct_j6XWu-G-GmI8yJIJUiDYBf...    1   
    523  679501061  a2883868WUN4geFUjA_1xTPuemwr2NZMQbenX10G4WtAcd...    1   
    524  706962258  886cab5aSpcDZV9VhjREiM5NEEvibQTfOxkW1HxE18NUFh...    1   
    525  709338305  481032554r-EEkzgIkLlLbAWOxRt3Fz7l9DjsqvqQJN5qC...    2   
    526  731088348  d53764ee9673IbM_4BqRXmhylFYzUIFTDCcDhBCvXQj6T0...    1   
    
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
access_token = "xxxxxx"
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
user_id
```




    48166591


Приступим к построению графа
https://networkx.org/documentation/latest/auto_examples/index.html

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


for node in idz2:
    G.add_node(node, color='red')
    G.add_edges_from([(str(48166591), str(node))], length = 1e1000)
    
for friend in dic:
    for connect in dic[friend]:
        G.add_edges_from([(str(friend), str(connect))], length = 1e1000)

G.remove_nodes_from(list(nx.isolates(G)))
nx.draw(G, node_color='blue', edge_color='#6e6e6e', node_size=5, with_labels=False, font_color='blue', cmap=True)

plt.show()
```


 
![png](https://i.ibb.co/FVqw233/output-17-0.png)
    



```python
Добавим эго-центр
```


```python
import operator
```


```python
node_and_degree = G.degree()
(largest_hub, degree) = sorted(node_and_degree, key=operator.itemgetter(1))[-1]
hub_ego = nx.ego_graph(G, largest_hub)
pos = nx.spring_layout(hub_ego, seed=123)
nx.draw(hub_ego, pos, node_color="b", node_size=50, with_labels=False)

# Draw ego as large and red
options = {"node_size": 300, "node_color": "r"}
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], **options)
plt.show()
```

    
![png](https://i.ibb.co/dBFrqwQ/output-20-0.png)
    

Попробуем выделить группы друзей внутри графа и раскрасить их в разные цвета

```python
from networkx.algorithms.community import greedy_modularity_communities
c = greedy_modularity_communities(G)
print(len(c))
'''https://networkx.org/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities'''
```

    6
    




    'https://networkx.org/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities'




```python
colors = {0: '#0080ff', 1: '#eb6424', 2: '#8ac926', 3: '#ffea00', 4: '#ff5d8f', 5: '#bc00dd'}
#colors = ['red','orange', 'green', '7fc7ff', '0000ff', 'violet']
colormap = []

for node in G:
    for i in range(6):
        if str(node) in c[i]:
            colormap.append(str(colors[i]))
```


```python
node_and_degree = G.degree()
(largest_hub, degree) = sorted(node_and_degree, key=operator.itemgetter(1))[-1]
hub_ego = nx.ego_graph(G, largest_hub)
pos = nx.spring_layout(hub_ego, seed=123)
nx.draw(hub_ego, pos, node_color=colormap, edge_color='#191a19', node_size=32, with_labels=False)

# Draw ego as large and red
options = {"node_size": 300, "node_color": "r"}
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], **options)
plt.show()
```
    
![png](https://i.postimg.cc/9ftk3Fmh/output-24-0.png)
    



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

```python
user_id
```




    48166591




```python

```
