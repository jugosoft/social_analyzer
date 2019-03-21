import vk
import src.configuration    as conf
import src.helpers          as help

class ApiVK:
    session = vk.Session()
    api = None
    
    def __init__(self):
        self.session = vk.AuthSession(access_token=conf.apikey, scope=['offline', 'messages', 'friends'])
        self.api = vk.API(self.session, v=conf.version)

    def get_friends(self, user_id : int):
        users_id = self.api.friends.get(user_id=user_id, order='hints')

        for x in users_id['items']:
            help.delay()
            tmp = self.api.users.get(user_id=x)
            #if tmp[0].get('city') != None:

        return users_id['items']

    def get_user_info(self, user_id : int):        
        help.delay()
        try:
            return self.api.users.get(user_id=user_id, fields='nickname, screen_name, sex, bdate (birthdate), city, country, timezone, photo, photo_medium, photo_big, has_mobile, contacts, education, online, counters, relation, last_seen, activity, can_write_private_message, can_see_all_posts, can_post, universities')
        catch: 

    def nothing():
        pass