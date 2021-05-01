# BlagueAPI

API python for jokes in French  
As the API is made for french people the rest of readme will be in french  
Pour l'installer, éxécuter la ligne ci-dessous dans le terminal

> pip install BlaguesApi

## Introduction

Pour l'importer, faites juste :

```py
import BlagueApi
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
# renvoie quelque chose de similaire
print(response["joke"]) # renvoie Un développeur ne descend pas du métro.
print(response["answer"]) # renvoie Il libère la RAM...
```

pour réavoir une autre blague il faut a nouveau définir response donc mettre response = joke.random()

Si "id" est > 0 alors il y a une erreur, faites response["error"] pour en savoir plus.

Un autre exemple :

```py
joke.get_joke_type("de")
```

Renverra un blague de type développeur (faites BlagueApi.type_joke pour savoir tout les types) et même si c'est mal écrit il considèrera comme juste tant que ça y ressemble à 75%.  
Vous pouvez aussi avoir une version plus stricte.

```py
joke.get_joke_type("dev")
```

Il faut indiquer une catégorie exacte que vous pouvez avoir soit en faisant BlagueApi.Types ou BlagueApi.Types.DARK  
Voici les autres variables pour les catégories :  
général = 'global'  
développeur = 'dev'  
noir = "dark"  
limite = "limit"  
beauf = "beauf"  
blondes = "blondes"

Vous pouvez trouvez une blague avec son id avec :

```py
Jokes.from_id(1)
```

L'id doit être un nombre positif strictement supérieur à 0

```py
Jokes.random_without()
```

Similaire à get_joke_genre() mais cette fois il faut mettre les genres qu'on ne veut pas avoir comme réponse.

Il existe aussi une version stricte:

```py
joke.get_joke_exclu_type_strict()
```
