import sys
import requests

from BlaguesApi.Constants import JokeTypes


class Jokes:
    def __init__(self, token, *args):
        self.token = token
        response = requests.get("https://www.blagues-api.fr/api/random",
                                headers={'Authorization': f'Bearer {self.token}'})
        if response.status_code == 401:
            print("Invalid token, program shutdown...")
            sys.exit(-1)
        first = True
        self.disallow = ""
        if len(args) > 0:
            for i in enumerate(args):
                type_detect = args[i]
                if len(type_detect) > 0:
                    if first:
                        self.disallow += f"?disallow={type_detect}"
                        first = False
                    else:
                        self.disallow += f"&disallow={type_detect}"

    def random(self):
        """get a random joke"""
        rep = requests.get(f"https://www.blagues-api.fr/api/random{self.disallow}", headers={
                           'Authorization': f'Bearer {self.token}'})
        return rep.json()

    def random_categorized(self, type_=None):
        """get a random joke with a specific type"""
        if not isinstance(type_, str):
            rep = requests.get(f"https://www.blagues-api.fr/api/random{self.disallow}", headers={
                               'Authorization': f'Bearer {self.token}'})
            return rep.json()
        for i in JokeTypes:
            if i == type_:
                rep = requests.get(f"https://www.blagues-api.fr/api/type/{type_}/random", headers={
                                   'Authorization': f'Bearer {self.token}'})
                return rep.json()
        return {"id": -1, "error": "type n'est pas égale a ceux existant"}

    def from_id(self, _id):
        """get a specific joke by id"""
        if isinstance(_id, int) and _id > 0:
            rep = requests.get(f"https://www.blagues-api.fr/api/id/{str(_id)}", headers={
                               'Authorization': f'Bearer {self.token}'})
            return rep.json()
        return {"id": -1, "error": "Merci de ne pas entrer un identifiant avec un nombre négatif (-1)."}

    def random_without(self, *args):
        """get jokes without a specific type"""
        first = True
        if len(args) > 0:
            params = ""
            for i in enumerate(args):
                for j in JokeTypes:
                    if first and args[i[0]] == j:
                        params += f"?disallow={j}"
                        first = False
                    elif args[i[0]] == j:
                        params += f"&disallow={j}"
            rep = requests.get(f"https://www.blagues-api.fr/api/random{params}", headers={
                               'Authorization': f'Bearer {self.token}'})
            return rep.json()
        rep = requests.get(f"https://www.blagues-api.fr/api/random{self.disallow}", headers={
                           'Authorization': f'Bearer {self.token}'})
        return rep.json()
