# BlagueAPI  
API python for jokes in French  
As the API is made for french people the rest of readme will be in french  
Pour l'installer, éxécuter la ligne ci-dessous dans le terminal  
> pip install BlagueApi  

Introduction  
---------------
Pour l'importer, faites juste :  
```py
import BlagueApi
```  
Pour initialiser :  
```py
joke = BlagueApi.Joke("TOKEN")
```
Le token est à obtenir sur [BlagueApi](https://www.blagues-api.fr/)  

```py
joke.get_blague_genre()
```
Renvoie une blague aléatoire :  
Renvoie un dictionaire de type :  
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
rep["joke"] #renvoie si on prend l'exemple précédent "Un développeur ne descend pas du métro."
```  
Si "id" est >0 alors il y a une erreur, faites rep["error"] pour en savoir plus.  

Un autre exemple :  
```py
joke.get_blague_genre("de")
```
Renverra un blague de type développeur (faites BlagueApi.type_blague pour savoir tout les types) et même si c'est mal écrit il considèrera comme juste tant que ça y ressemble à 75%.  
Vous pouvez aussi avoir une version plus stricte.  
```py
joke.get_blague_genre("dev")
```  
Il faut indiquer une catégorie exacte que vous pouvez avoir soit en faisant BlagueApi.type_blague ou BlagueApi.noir  
Voici les autres variables pour les catégories :  
général = 'global'  
développeur = 'dev'  
noir = "dark"  
limite = "limit"  
beauf = "beauf"  
blondes = "blondes"  

Vous pouvez trouvez une blague avec son id avec :  
```py
joke.get_blague_id(1)
```
L'id doit être un nombre positif strictement supérieur à 0  
```py
joke.get_blague_exclu_genre()
```
Similaire à get_blague_genre() mais cette fois il faut mettre les genres qu'on ne veut pas avoir comme réponse.  

Il existe aussi une version stricte:  
```py
joke.get_blague_exclu_genre_strict()
```
