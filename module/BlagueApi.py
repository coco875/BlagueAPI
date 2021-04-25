import jaro
import requests


def comparaison_proche(mot, liste, ressemblance):
    aob = []
    for i in liste:

        aob.append([jaro.jaro_metric(mot, i), i])

    aob = sorted(aob, key=lambda student: student[0], reverse=True)


    if aob[0][0] > ressemblance:

        for i in range(len(liste)):

            if aob[0][1] == liste[i]:
                return liste[i]
        return []

type_blague = ["global", "dev", "dark","limit", "beauf", "blondes"]

général = 'global'
développeur = 'dev'
noir = "dark"
limite = "limit"
beauf = "beauf"
blondes = "blondes"

logo = "https://raw.githubusercontent.com/DraftProducts/blagues-api/master/src/public/Logo.200.png"

class Joke:
    def __init__(self, token, ressemblance=0.75, *args):
        """mettre son token obtenue sur https://www.blagues-api.fr/ et ressemblance est pour changer le pourcentage de ressemblance minimum pour considérer un genre appelé avec Joke.get_blague_genre(genre) comme valide, rajouter a la fin les genres que vous voulez pas que ça sorte quand il y a pas de genre indiqué (si il reconnait pas ou que le taux de ressemblence et inférieur a celui indiqué alors il passe)"""
        self.token = token
        self.warn = True
        self.ressemblance = ressemblance
        test = requests.get("https://www.blagues-api.fr/api/random", headers = {'Authorization': f'Bearer {self.token}'})
        test = test.json()
        sortie = False
        try:
            test["status"]
            print("votre token est invalide arrêt du programme")
            sortie = True
        except:
            pass
        if sortie:
            exit(-1)
        first = True
        if len(args)>0:
            txt = ""
            for i in range(len(args)):
                type_detect = comparaison_proche(args[i], type_blague, self.ressemblance)
                if len(type_detect)>0:
                    if first:
                        txt+=f"?disallow={type_detect}"
                        first=False
                    else:
                        txt+=f"&disallow={type_detect}"
        txt = ""    
        self.disallow = txt
    def get_blague_genre(self,genre=None):
        """permet d'obtenir une blague d'un certain genre même si il y a des fautes dans le type. c'est considérer comme valide si le mot d'après la Distance de Jaro-Winkler (un truc pour savoir la ressemblence) est ressemblant a 75%"""
        if type(genre) is not str:
            rep = requests.get(f"https://www.blagues-api.fr/api/random{self.disallow}", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
        else:
            type_detect = comparaison_proche(genre, type_blague, self.ressemblance)
            if len(type_detect)>0:
                rep = requests.get(f"https://www.blagues-api.fr/api/type/{type_detect}/random", headers = {'Authorization': f'Bearer {self.token}'})
                return rep.json()
            else:
                if self.warn:
                    print("Warning: rentré un nom plus rensemblent a un genre existant (vous pouvez savoir la liste a partir de ça BlagueApiFr.type_blague)")
                    self.warn = False
                return {"id" : -1, "error": "genre non rensemblant a ceux existant"}
    def get_blague_genre_strict(self, genre=None):
        """donnez le genre éxact"""
        if type(genre) is not str:
            rep = requests.get(f"https://www.blagues-api.fr/api/random{self.disallow}", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
        for i in type_blague:
            if i == genre:
                rep = requests.get(f"https://www.blagues-api.fr/api/type/{genre}/random", headers = {'Authorization': f'Bearer {self.token}'})
                return rep.json()
        return {"id" : -1, "error": "genre n'est pas égale a ceux existant"}
    def get_blague_id(self,id):
        """l'id doit être un nombre entier strictement supérieur a 0"""
        if type(id) is int and id > 0:
            rep = requests.get(f"https://www.blagues-api.fr/api/id/{str(id)}", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
        else:
            return {"id": -1, "error":"entré un nombre"}
    def get_blague_exclu_genre(self,*args):
        """donne une blague sans prendre en compte que les limites imposer lors de l'initialisation et en mettant d'autre limite"""
        first = True
        if len(args)>0:
            txt = ""
            for i in range(len(args)):
                type_detect = comparaison_proche(args[i], type_blague, self.ressemblance)
                if len(type_detect)>0:
                    if first:
                        txt+=f"?disallow={type_detect}"
                        first=False
                    else:
                        txt+=f"&disallow={type_detect}"
            rep = requests.get(f"https://www.blagues-api.fr/api/random{txt}", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
        else:
            rep = requests.get(f"https://www.blagues-api.fr/api/random", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
    def get_blague_exclu_genre_strict(self,*args):
        """donne une blague sans prendre en compte que les limites imposer lors de l'initialisation et en mettant d'autre limite mais plus stricte au niveau de la syntaxe"""
        first = True
        if len(args)>0:
            txt = ""
            for i in range(len(args)):
                for j in type_blague:
                    if first and args[i] == j:
                        txt+=f"?disallow={j}"
                        first=False
                    elif args[i] == j:
                        txt+=f"&disallow={j}"
            rep = requests.get(f"https://www.blagues-api.fr/api/random{txt}", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()
        else:
            rep = requests.get(f"https://www.blagues-api.fr/api/random", headers = {'Authorization': f'Bearer {self.token}'})
            return rep.json()