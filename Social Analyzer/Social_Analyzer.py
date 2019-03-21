import src.api              as api
import src.visualisation    as gr
import src.helpers          as help
import json

vk = api.ApiVK()

src_id = 0

graphics = gr.Graphics()

graph = {}
friend_ids = vk.get_friends(src_id)  # ваш user id, для которого вы хотите построить граф друзей.
print(friend_ids)

for friend_id in friend_ids:
    print('grabbing id' + str(friend_id))
    help.delay()
    graph[friend_id] = vk.get_friends(friend_id)

for i in graph:
    graphics.add_node(i)
    for j in graph[i]:
        if i != j and i in friend_ids and j in friend_ids:
            graphics.add_edge(i, j)

graphics.draw()
