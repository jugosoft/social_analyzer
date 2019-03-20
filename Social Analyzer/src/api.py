import vk
import src.configuration    as conf
import src.helpers          as help

class ApiVK:
    session = vk.Session()
    api = None
    
    def __init__(self):
        self.session = vk.AuthSession(access_token=conf.apikey, scope=['offline', 'messages', 'friends'])
        self.api = vk.API(self.session, v=conf.version)

    def get_users(self, user_id : int):
        users_id = self.api.friends.get(user_id=user_id, order='hints')

        for x in users_id['items']:
            help.delay()
            print(self.api.users.get(user_id=x))
        
            return users_id['items']

    def nothing():
        pass