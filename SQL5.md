Открыть DB Browser for SQLite3
```
Сtrl + O
```
Выбрать исходный файл базы данных
```
.db
```
Открыть вкладку "SQL"
```SQL
SQL
```
Написать код:
```SQL
CREATE TABLE IF NOT EXISTS comments AS SELECT ID_vk AS gruppa, ABS(owner_id) AS party, COUNT(owner_id) as party_cnt FROM comments_links_final WHERE gruppa IS NOT NULL GROUP BY gruppa, party ORDER BY gruppa  DESC;
CREATE TABLE IF NOT EXISTS posts AS SELECT ABS(owner_id) AS gruppa, AVG(views) AS aver_gr_views FROM interest_groups_posts WHERE date BETWEEN '2018-03-18 23:59:59' AND '2019-05-02 23:59:59' GROUP BY gruppa ORDER BY gruppa DESC;
CREATE TABLE IF NOT EXISTS org_codes AS SELECT id AS gruppa, organization_2 AS code, name FROM organizations_final_codes WHERE code IN (67, 68, 69);
CREATE TABLE IF NOT EXISTS graph AS SELECT * FROM comments LEFT JOIN posts ON comments.gruppa = posts.gruppa LEFT JOIN org_codes on comments.gruppa = org_codes.gruppa;
```
Сохранить изменения: Ctrl+S
```
Ctrl+S
```
Если в создании таблиц что-то пошло не так, удалить таблицу можно коммандой: DROP TABLE название таблицы
```SQL
DROP TABLE table_example;
```
Следите, чтобы в конце запросов всегда был знак ";"

```python
import networkx as nx
import sqlite3
```


```python
Откроем соединение с БД для внесения изменений
```


```python
conn = sqlite3.connect('C:\interest_groups_parties.db')
c = conn.cursor()
```


```python
c.execute('SELECT name, gruppa, party, party_cnt, aver_gr_views, code from graph WHERE aver_gr_views IS NOT NULL AND code IS NOT NULL')
```




    <sqlite3.Cursor at 0x151008540a0>


Сохраним результат в виде списка кортежей

```python
spisok = [item for item in c.fetchall()]
```
Проверим обращение по индексу

```python
spisok[1]
```




    ('ЭкоБессрочка Архангельск', 180852861, 26362316, 1, 4887.592857142857, 67)




```python
spisok[0][1]
```
Применим изменения и закроем соединение.

```python
conn.commit()
conn.close()
```
Создадим networkx граф

```python
G = nx.Graph() 
```
Добавим вершины (nodes) и ребра (edges), а также их атрибуты
Документацию можно найти по адресу: https://networkx.org/documentation/stable/tutorial.html
Толщина линии -  количество связей
Размер круга - число просмотров 

```python
for i in range(len(spisok)): 
    G.add_node(spisok[i][1])
    G.nodes[spisok[i][1]]['views'] = int(spisok[i][4])
    G.nodes[spisok[i][1]]['type'] = spisok[i][5]
    G.add_node(spisok[i][2])
    G.nodes[spisok[i][2]]['cnt'] = int(spisok[i][3]) #не работает корректно
    G.add_edge(spisok[i][1], spisok[i][2], weight = int(spisok[i][3]))
```


```python
li = [*G.nodes.data()]
```
Предположу кодировку
Political associations - 68 - '#6666ff' - лаванда
Protest communities - 67 - '#336600' - зеленый
Human rights communities - 69 - '#ff5500' - оранж
Political parties - '#ff5d8f' - розовый

```python
colormap = []
c = [[] for i in range(4)]
colors = {0: '#ff5d8f', 1: '#6666ff', 2: '#336600', 3: '#ff5500'}
Political_associations = []
Protest_communities = []
Human_rights_communities = []
Political_parties = []
for i in range(len(li)):
    if 'type' in li[i][1].keys():
        if int(li[i][1]['type']) == 68:
            c[1].append(li[i][0])
        elif int(li[i][1]['type']) == 67:
            c[2].append(li[i][0])
        elif int(li[i][1]['type']) == 69:
            c[3].append(li[i][0])
    else:
        c[0].append(li[i][0])
```


```python
for node in G:
    for i in range(4):
        if node in c[i]:
            colormap.append(str(colors[i]))
```


```python
nodesizes = []
for i in range(len(li)):
    if 'views' in li[i][1].keys():
        nodesizes.append(int(li[i][1]['views'])**0.4)
    else:
        nodesizes.append(int(120))    # не поняла, откуда брать размер для полит партий
```


```python
weights = [1 if G[u][v] == {} else G[u][v]['weight']/10 for u,v in G.edges()]
```


```python
nx.draw(G, node_color=colormap, node_size = nodesizes, width=weights)
```


    
![png](https://i.ibb.co/7YBLnXr/output-24-0.png)
    



```python
nx.write_graphml_lxml(G, "parties.graphml", encoding='utf-8')
```


```python

```
