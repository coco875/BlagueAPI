import sys
import jaro
import requests

from BlaguesApi.Constants import JokeTypes

def comparaison_proche(mot, liste, ressemblance):
    aob = []
    for i in liste:

        aob.append([jaro.jaro_metric(mot, i), i])

    aob = sorted(aob, key=lambda student: student[0], reverse=True)


    if aob[0][0] > ressemblance:

        for i in enumerate(liste):

            if aob[0][1] == liste[i[0]]:
                return liste[i[0]]
        return []
    return []

class JokesAround:
    def __init__(self, token, ressemblance=0.75, *args):
        self.token = token
        self.warn = True
        self.ressemblance = ressemblance
        response = requests.get("https://www.blagues-api.fr/api/random",
                                headers={'Authorization': f'Bearer {self.token}'})
        if response.status_code == 401:
            print("Invalid token, program shutdown...")
            sys.exit(-1)
        first = True
        self.disallow = ""
        if len(args) > 0:
            for i in enumerate(args):
                type_detect = comparaison_proche(
                    args[i[0]], JokeTypes, self.ressemblance)
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
        else:
            type_detect = comparaison_proche(
                type_, JokeTypes, self.ressemblance)
            if len(type_detect) > 0:
                rep = requests.get(f"https://www.blagues-api.fr/api/type/{type_detect}/random", headers={
                                   'Authorization': f'Bearer {self.token}'})
                return rep.json()
            else:
                if self.warn:
                    print(
                        "Warning: rentré un nom plus rensemblent a un genre existant (vous pouvez savoir la liste a partir de ça BlaguesApi.JokeTypes)")
                    self.warn = False
                return {"id": -1, "error": "type non rensemblant a ceux existant"}

    def from_id(self, _id):
        """get a specific joke by id"""
        if isinstance(_id, int) and _id > 0:
            rep = requests.get(f"https://www.blagues-api.fr/api/id/{str(_id)}", headers={
                               'Authorization': f'Bearer {self.token}'})
            return rep.json()
        return {"id": -1, "error": "entré un nombre"}

    def random_without(self, *args):
        """donne une blague sans prendre en compte que les limites imposer lors de l'initialisation et en mettant d'autre limite"""
        first = True
        if len(args) > 0:
            txt = ""
            for i in range(len(args)):
                type_detect = comparaison_proche(
                    args[i], JokeTypes, self.ressemblance)
                if len(type_detect) > 0:
                    if first:
                        txt += f"?disallow={type_detect}"
                        first = False
                    else:
                        txt += f"&disallow={type_detect}"
            rep = requests.get(f"https://www.blagues-api.fr/api/random{txt}", headers={
                               'Authorization': f'Bearer {self.token}'})
            return rep.json()
        else:
            rep = requests.get("https://www.blagues-api.fr/api/random",
                               headers={'Authorization': f'Bearer {self.token}'})
            return rep.json()
