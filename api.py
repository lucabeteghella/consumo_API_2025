from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass

class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return (dado.get('id'), dado.get('name'))
        except:
            return None

class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('id'), data.get('name'), data.get('species'))
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API Rick and Morty: {e}")
            return None

class API_Star_Wars(API_consumer):
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('name'), [film_url for film_url in data.get('films', [])])
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API Star Wars: {e}")
            return None

class API_Ice_and_Fire(API_consumer):
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()
            return (data.get('name'), [season for season in data.get('tvSeries', [])])
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API Ice and Fire: {e}")
            return None

if __name__ == "__main__":
    # Testando as APIs
    pokemon_api = API_Pokemon()
    print("Consumo da API Pokemon")
    print("****************************************")
    for i in range(1, 3):
        print(pokemon_api.extract(i))

    rick_morty_api = API_Rick_Morty()
    print("\nConsumo da API Rick and Morty")
    print("****************************************")
    for i in range(1, 3):
        print(rick_morty_api.extract(i))

    star_wars_api = API_Star_Wars()
    print("\nConsumo da API Star Wars")
    print("****************************************")
    for i in range(1, 3):
        print(star_wars_api.extract(i))

    ice_and_fire_api = API_Ice_and_Fire()
    print("\nConsumo da API Crônicas do Gelo e do Fogo")
    print("****************************************")
    for i in range(1, 3):
        print(ice_and_fire_api.extract(i))
