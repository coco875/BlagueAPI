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
si "id" est >0 alors il y a une érreur faites rep["error"] pour en savoir plus;  

un autre exemple :  
```py
joke.get_blague_genre("de")
```
Renverra un blague de type développeur (faite BlagueApi.type_blague pour savoir tout les types) et même si c'est mal écrit il considèrera comme juste tant que ça y ressemble a 75%.  
vous pouvez aussi avoir une version plus stricte.  
```py
joke.get_blague_genre("dev")
```  
il faut indiqué une catégorie éxacte que vous pouvez avoir soit en faisant BlagueApi.type_blague ou BlagueApi.noir  
voici les autres variables pour les catégories  
général = 'global'  
développeur = 'dev'  
noir = "dark"  
limite = "limit"  
beauf = "beauf"  
blondes = "blondes"  

vous pouvez trouvez une blague avec son id avec :  
```py
joke.get_blague_id(1)
```
l'id doit être un nombre positif strictement supérieur a 0  
```py
joke.get_blague_exclu_genre()
```
similaire a get_blague_genre() mais cette fois il faut mettre les genres qu'on ne veut pas avoir comme réponse.  

il éxiste aussi une version stricte:
```py
joke.get_blague_exclu_genre_strict()
```
