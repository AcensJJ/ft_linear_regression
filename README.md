<p align="center">
    <img alt="42-lyon" src="https://user-images.githubusercontent.com/45235527/106354618-6ec65a00-62f3-11eb-8688-ba9e0f4e77de.jpg" />
</p>

# ft_linear_regression

<!-- <img alt="Note" src="https://user-images.githubusercontent.com/45235527/104627073-dc894980-5696-11eb-999d-e53798ea9ae4.png" width="250" height="200" /> -->

### <strong>Description</strong>

Ce projet vous servira a faire vos premiers pas dans l'IA et plus precisement le machine learning. Vous allez commencer par algo simple. Vous coderez un program qui peut predire le prix d une voiture en utilisant la regression lineaire avec un algorithme du gradient

# Partie Obligatoire 

Ce que vous devez faireImplémentez un algorithme de regression linéaire sur un seul element, en l’occurencele kilométrage d’une voiture Pour ce faire vous devez faire 2 programmes :

- Le premier programme sera utilisé pour prédire le prix d’une voiture en fonctionde son kilométrage. Quand vous lancerez le programme, celui ci vous demandera lekilométrage et devrait vous donner un prix approximatif de la voiture en utilisantl’hypothèse suivante :

![formule1](https://user-images.githubusercontent.com/45235527/140348830-b8275ec3-5908-4a12-9da1-bbdf166316a7.PNG)

Avant de lancer le programme d’entrainement, theta0 et theta1 auront pour valeur0.

- Le second programme sera utilisé pour entrainer votre modèle. Il lira le jeu dedonnées et fera une regression linéaire sur ces données.Une fois la regression linéaire terminée, vous sauvegarderez la valeur de theta0 ettheta1 pour pouvoir l’utiliser dans le premier programme.Vous utiliserez la formule suivante :

![formule2](https://user-images.githubusercontent.com/45235527/140348840-4d426b93-b304-44b0-8ab4-152e10ebe1e9.PNG)

Je vous laisse devinez ce à quoi m correspond :)

Veuillez noter que le prixEstime est la même chose que dans notre premier pro-gramme, mais ici il utilise vos valeures temporaires afin de calculer theta0 et theta1.Attention a bien mettre a jour theta0 et theta1 en même temps.

# Bonus

Voici des bonus qui pourrait être utiles :

- Visualiser les données sur un graph avec leur repartition.

- Afficher la ligne résultant de votre regression linéaire sur ce même graphe et voirsi ca marche !

- Un programme qui vérifie la precision de votre algorithme.

... Et n’importe quoi qui pourrait rendre cet exercice encore meilleur.

# Requirements

- python3.10
- lib:
    - pip3 install pandas
    - pip3 install matplotlib
    
# Results

<img alt="linear" src="https://user-images.githubusercontent.com/45235527/140805194-b31f35a2-dda6-405f-b2af-4555dc11250f.png">

<img alt="apprentisage" src="https://user-images.githubusercontent.com/45235527/140819537-ae9bf9e6-9897-4507-906e-444bb4fd4969.png">
