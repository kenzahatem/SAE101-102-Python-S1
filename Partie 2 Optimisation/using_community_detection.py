## Question 2 : Comparaison théorique :
Pour comparer les deux fonctions `dico_reseau` et `create_network` il faut analyser la complexité asymptotique des deux fonctions:

La compléxité asymptotique de la fonction dico_reseau est quadratique 
=> la fonction contient une boucle while qui sera éxecuté n fois , et chaque itération appelle la fonction list_amis qui 
parcours le tableau des amis et qui est de compléxité asymptotique linéaire , du coup O(n)n => O(n^2)

la compléxité asymptotique de la fonction create_network est linéaire O(n)
=> la fonction parcours une seule fois le tableau (contient une seule boucle
while qui sera exécuté  n fois et un nombre d opération élémentaires qui est négligeable)

## Comparaison expérimentale :
from cummunity_detection import *
from time import time
from random import *

def mesure_temps(fonction,n):
    i=0
    tic1=time()
    while i<n:
        fonction(amis)
        i+=1
    tac1=time()
    return round(((tac1-tic1)*1000),6)

print("Le temps moyen nécessaire pour la création un dictionnaire",  100000, "fois :")
print("\t", mesure_temps(dico_reseau, 100000), "ms pour la fonction dico_reseau")
print("\t", mesure_temps(create_network, 100000), "ms pour la fonction create_network")

## Question 11 : Comparaison théorique :

la fonction `find_community_by_decreasing_popularity` retourne la liste des personnes de ce réseau O(n) et les trient par décroissance de popularité, de compléxité de O(n log n). Ensuite trier la communauté selon l heuristique de compléxité O(n^2). La compléxité totale de la fonction est donc de compléxité O(n log n) + O(n^2) + O(n) .

La fonction `find_community_from_person` trie en premier les amis de la personne donnée de compléxité O(n log n), ensuite une boucle while qui à chaque itération appelle la fonction all_his_friend , ce qui a une compléxité de O(n^2). La compléxité totale de la fonction ets donc de O(n^2) +O(n log n).

## Comparaison expérimentale :
departure1=time()
i=0
while i<10000 :
    find_community_by_decreasing_popularity(reseau)
    i+=1
end1=time()
print("le temps nécessaire pour l'éxecusion de la fonction find_community_by_decreasing_popularity est",round((end1-departure1)*1000/10000,6), "ms")


departure2=time()
i=0
tab=les_plus_pop(reseau)
while i<10000 :
    find_community_from_person(reseau, tab[0])
    i+=1
end2=time()
print("le temps nécessaire pour l'éxecusion de la fonction find_community_from_person est",round((end2-departure2)*1000/10000,6), "ms")

