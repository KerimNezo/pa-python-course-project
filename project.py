#Projekat koji se pravio na kraju videa "Python Tutorial for Begginers"
import requests

class APICall:
    '''Base class to make basic API call with requests'''

    def call(self, method, api_url): #method(get,post,put,delete) i endpoint (tj api)
        if method.lower() == "get": #.lower() jer nismo sigurni hoce li biti upper ili lower
            r = requests.get(api_url) #pravimo get request sa api-jem

        match r.status_code:
            case 200 | 201 | 202:
                return r.json()["value"]
            case _:
                raise TypeError("API error")