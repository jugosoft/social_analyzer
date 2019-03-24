import src.api              as api
import src.visualisation    as gr
import src.helpers          as help
import json
import time

vk = api.ApiVK()
#use it for gathering info
src_id = 

graphics = gr.Graphics()
graph = {}
friend_ids = vk.get_friends(src_id)  # ваш user id, для которого вы хотите построить граф друзей.
friend_ids.append(src_id)

#
print('Process is started...')
#
start = time.time()

counter = 0
length = len(friend_ids)
for friend_id in friend_ids:
    print('#' + str(counter) + ' Processing ' + ' id' + str(friend_id) + '. Finished ' + 
          '{0:.2f}'.format(round(counter / length * 100, 2)) + '%')

    #because of the resctrictions of VK's API
    help.delay()

    #clears screen
    help.clear()

    counter += 1
    graph[friend_id] = vk.get_friends(friend_id)


counter = 0
node_counter = 0
root_node_found = 0

for i in graph:
    #if i == src_id:
    #    pass
    #    graphics.add_node(src_id, '#ff0000')
    #else:
    graphics.add_node(i, '#0047ab')
    
    counter += 1
    for j in graph[i]:
        if i != j and i in friend_ids and j in friend_ids:
            if i == src_id:
                graphics.add_edge(i, j, '#ff0000')
            else:
                graphics.add_edge(i, j)

#this code is going to find
#an index of root element and 
#paint it RED))                
try:
    start_counter = 0
    for k, v in graphics.G.nodes._nodes.items():
        if k == src_id:
            root_node_found = 1
            index = start_counter
            graphics.node_colours[index] = '#ff0000'
        start_counter += 1 
except ValueError:
    pass

end = time.time()

print('Elapsed time is ' + str(end - start))
print('...')
print('Now we are going to look for the location.')
print('Wait for a moment.')
print('It should not take a lot of time...')
start = time.time()

#output...
#prints suggested current location
#of the person src_id
print('Suggested location is ' + str(vk.map_ids_into_real_city(friend_ids) + '.'))
end = time.time()
print('Elapsed time of the socond operation is ' + str(end - start))

graphics.draw()
