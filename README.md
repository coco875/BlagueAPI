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
si "id" est >0 alors il y a une érreur faiteS rep["error"] pour en savoir plus;

un autre exemple :
```py
joke.get_blague_genre("de")
```
Renverra un blague de type développeur (faite BlagueApi.type_blague pour savoir tout les types) et même si c'est mal écrit il considèrera comme juste.  
