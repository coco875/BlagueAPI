# BlagueAPI  
API python for Joke in French  
as the API is made for french people the rest of readme will be in french  
pour l'installer éxécuter la ligne ci-dessous dans le terminal  
> pip install BlagueApi  

Introduction
---------------
pour l'importer faite juste
```py
import BlagueApi
```  
pour initialiser
```py
joke = BlagueApi.Joke("TOKEN")
```
le token est a obtenire sur [BlagueApi](https://www.blagues-api.fr/)  

```py
joke.get_blague_genre()
```
renvoie une blague aléatoire  
renvoie un dictionaire de type  
```json
{
  "id": 1,
  "type": "dev",
  "joke": "Un développeur ne descend pas du métro.",
  "answer": "Il libère la RAM..."
}
```
et pour obtenir les informations c'est 
```py
rep["joke"] #renvoie si on prend l'exemple précédent "Un développeur ne descend pas du métro."
```
si "id" est >0 alors il y a une érreur faite rep["error"] pour en savoir plus

un autre exemple  
```py
joke.get_blague_genre("de")
```
renvoira un blague de type développeur (faite BlagueApi.type_blague pour savoir tout les types) et même si c'est mal écris il considère comme juste.  