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
joke.get_joke_type()
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
exemple d'utilisation :
```py
import BlagueApi

joke = BlagueApi.Joke('TOKEN')
rep = joke.get_joke_type()
print(rep) 
#{
#  "id": 1,
#  "type": "dev",
#  "joke": "Un développeur ne descend pas du métro.",
#  "answer": "Il libère la RAM..."
#}
#renvoie quelque chose de similaire
print(rep["joke"]) #renvoie Un développeur ne descend pas du métro.
print(rep["answer"]) #renvoie Il libère la RAM...
```
pour réavoir une autre blague il faut a nouveau définir rep donc mettre rep = joke.get_joke_type()

Si "id" est >0 alors il y a une erreur, faites rep["error"] pour en savoir plus.  

Un autre exemple :  
```py
joke.get_joke_type("de")
```
Renverra un blague de type développeur (faites BlagueApi.type_joke pour savoir tout les types) et même si c'est mal écrit il considèrera comme juste tant que ça y ressemble à 75%.  
Vous pouvez aussi avoir une version plus stricte.  
```py
joke.get_joke_type("dev")
```  
Il faut indiquer une catégorie exacte que vous pouvez avoir soit en faisant BlagueApi.type_joke ou BlagueApi.noir  
Voici les autres variables pour les catégories :  
général = 'global'  
développeur = 'dev'  
noir = "dark"  
limite = "limit"  
beauf = "beauf"  
blondes = "blondes"  

Vous pouvez trouvez une blague avec son id avec :  
```py
joke.get_joke_id(1)
```
L'id doit être un nombre positif strictement supérieur à 0  
```py
joke.get_joke_exclu_type()
```
Similaire à get_joke_genre() mais cette fois il faut mettre les genres qu'on ne veut pas avoir comme réponse.  

Il existe aussi une version stricte:  
```py
joke.get_joke_exclu_type_strict()
```
