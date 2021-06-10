# BlaguesAPI

API python for jokes in French  
As the API is made for french people the rest of readme will be in french  
Pour l'installer, éxécuter la ligne ci-dessous dans le terminal

> pip install BlaguesApi

## Introduction

Pour l'importer, faites juste :

```py
import BlaguesApi
```

Pour initialiser :

```py
Jokes = BlaguesApi.Jokes("TOKEN")
```

Le token est à obtenir sur [BlaguesApi](https://www.blagues-api.fr/)

```py
response = Jokes.random()
```

Renvoie une blague aléatoire :

```json
{
  "id": 1,
  "type": "dev",
  "joke": "Un développeur ne descend pas du métro.",
  "answer": "Il libère la RAM..."
}
```

Et pour obtenir les informations c'est :

```py
response["joke"] # renvoie si on prend l'exemple précédent "Un développeur ne descend pas du métro."
```

exemple d'utilisation :

```py
import BlaguesApi

Jokes = BlaguesApi.Jokes('TOKEN')
response = Jokes.random()
print(response)
# {
#   "id": 1,
#   "type": "dev",
#   "joke": "Un développeur ne descend pas du métro.",
#   "answer": "Il libère la RAM..."
# }
# renvoie ce 'dictionnaire' (c'est une class encore différent que une liste mais similaire)
print(response["joke"]) # renvoie Un développeur ne descend pas du métro.
print(response["answer"]) # renvoie Il libère la RAM...
```

pour réavoir une autre blague il faut a nouveau définir response donc remettre response = joke.random()

Si "id" est < 0 alors il y a une erreur, faites response["error"] pour en savoir plus.

autre fonctionalité:

```py
Joke.random_categorized(BlaguesApi.Types.DEV)
```
Renvoie une blague aléatoire dans la catégorie

Il faut indiquer une catégorie exacte que vous pouvez avoir soit en faisant BlaguesApi.JokeTypes (vous obtener une liste) ou BlaguesApi.Types.DARK pour avoir le thème noir
Voici les autres variables pour les catégories :  
GLOBAL = 'global'
DEV = 'dev'
DARK = "dark"
LIMIT = "limit"
BEAUF = "beauf"
BLONDES = "blondes"

vous pouvez faire en sorte qu'il accepte même si c'est pas exacte en remplacent `Jokes = BlaguesApi.Jokes('TOKEN')` par `Jokes = BlaguesApi.JokesAround('TOKEN')`

exemple:
```py
import BlaguesApi

Jokes = BlaguesApi.JokesAround('TOKEN') #initialisation en approximatif 
categorie = ""

while categorie != "exit": # permet de quitter la boucle quand on marque exit
    categorie = input("De quel catégorie vous voulez la blague : ")
    response = Jokes.random_categorized(categorie)
    if response['id'] < 0:
        print(response['error'])
    else:
        print(f"Blague : {response['joke']}\nréponse : {response['answer']}")
```

Vous pouvez trouvez une blague avec son id avec :
L'id doit être un nombre positif strictement supérieur à 0

```py
Jokes.from_id(1)
```

Vous pouvez aussi avoir une blague aléatoire mais en excluant une catégorie

```py
Jokes.random_without(BlaguesApi.Types.DARK)
```
la aussi en indiquent la/les catégorie(s) a enlever et aussi peut être aproximatif si on a définit avec JokesAround
