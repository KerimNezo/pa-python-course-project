#Projekat koji se pravio na kraju videa "Python Tutorial for Begginers"
import requests

class APICall:
    '''Base class to make basic API call with requests''' #text literal __doc__
    
    def call(self, method, api_url): #method(get,post,put,delete) i endpoint (tj api)
        if method.lower() == "get": #.lower() jer nismo sigurni hoce li biti upper ili lower
            r = requests.get(api_url) #pravimo get request sa api-jem

        match r.status_code: #provjera da li je api call success
            case 200 | 201 | 202: 
                return r.json()["value"]
            case _:
                raise TypeError("API error")

class ChuckNorris(APICall): #izvedena klasa gdje cemo pozivati call metodu
    '''This is the Chuck Norris API''' #text literal __doc__
    url = "https://api.chucknorris.io/jokes/random?category=" 
    #specificno za klasu pa stavljamo je kao klasnu var
    categories = ["animal", "dev"] #kategorije koje idu u link

    def __init__(self, category): #konstruktor dundor/magicna metoda
        self.category = category #ovo nam dozvoljava da instanciramo klasu sa kategorijom
        if not self.category in self.categories: #just in case
            raise TypeError("category options ['animal', 'dev']")

    def get(self): #get request za izvedenu klasu, zavisi sta/kako pravimo pa imamo ostale
        api_url = f'{self.url}{self.category}' #f-string zbog placeholdera
        #ovdje spajamo url sa linije 19 i kategoriju da dobijemo joke ig
        return self.call("GET",api_url)#moze GET zbog .lower() linija 8