import vk
import src.configuration    as conf
import src.helpers          as help

"""
Perfoms actions on API.
"""
class ApiVK:
    session = vk.Session()
    api = None
    
    def __init__(self):
        self.session = vk.AuthSession(access_token=conf.apikey, scope=['offline', 'messages', 'friends'])
        self.api = vk.API(self.session, v=conf.version)

    def get_friends(self, user_id : int):
        """
        Wrapper for API's method.
        Allows to get ids of friends.
        """
        user_info = self.get_user_info(user_id)

        #if user_info[0].get('deactivated') == "deleted" or user_info[0].get('deativated') == "banned" or user_info[0].get('is_closed') == True:
        #    return list()            

        try:
            users_id = self.api.friends.get(user_id=user_id, order='hints')
        except:
            return list() 

        
        #for x in users_id['items']:
            #help.delay()
            #tmp = self.api.users.get(user_id=x)
            #if tmp[0].get('city') != None:
        return users_id['items']

    def get_user_info(self, user_id : int):     
        """
        Get details about user.
        For more information look through 'fields', such
        as nickname, sex etc.
        """
        return self.api.users.get(user_id=user_id, fields='nickname, deativated, screen_name, is_closed, sex, bdate (birthdate), city, country, timezone, photo, photo_medium, photo_big, has_mobile, contacts, education, online, counters, relation, last_seen, activity, can_write_private_message, can_see_all_posts, can_post, universities')

    def map_ids_into_real_city(self, *args):
        """
        This method maps list of id's into city's list.
        It may be useful for detecting current location of person.
        """
        def most_common(lst):
            """
            Looks for the most common city of friends
            """
            return max(lst, key=lst.count)

        list_of_cities = []
        counter = 0 
        for x in args[0]:
            help.delay()
            user = self.get_user_info(args[0][counter])

            #user[0] is a dictionary!
            #but user is a list...
            if user[0].get('city') != None and user[0].get('city') != '':
                list_of_cities.append(user[0].get('city').get('title'))    
            counter += 1

        #list of cities. the most common citi is a real 
        #location of the person.
        comm_city =  most_common(list_of_cities)
        return comm_city

    def nothing():
        pass