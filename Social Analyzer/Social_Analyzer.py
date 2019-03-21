import src.api              as api
import src.visualisation    as gr
import json

vk = api.ApiVK()

src_id = 
users = vk.get_friends(src_id)

counter = 0 
for x in users:
    user = vk.get_user_info(users[counter])

    #user[0] is a dictionary!
    if user[0].get('city') != None and user[0].get('city') != '':
        print(user[0].get('city').get('title'))
    
    counter += 1

#graphics = gr.Graphics()

#for dst_id in users:
#    graphics.add_edge(src_id, dst_id)

#graphics.draw()
