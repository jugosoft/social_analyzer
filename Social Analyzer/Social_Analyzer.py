import src.api              as api
import src.visualisation    as gr

vk = api.ApiVK()

src_id = 367454545
users = vk.get_users(src_id)

graphics = gr.Graphics()

for dst_id in users:
    graphics.add_edge(src_id, dst_id)

graphics.draw()
