##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    """Retourne le dictionnaire correspondant au réseau en parcourant une seule fois le tableau."""
    network={}
    i=0
    while i<len(list_of_friends):
        if list_of_friends[i] not in network :
            tab=[]
            if i%2==0: #si l'indice est pair
                tab.append(list_of_friends[i+1])
            else:
                tab.append(list_of_friends[i-1])
            network[list_of_friends[i]]=tab
            
        else:
            tab2=network[list_of_friends[i]]
            if i%2==0:
                tab2.append(list_of_friends[i+1])
            else:
                tab2.append(list_of_friends[i-1])
            network[list_of_friends[i]]=tab2
        i+=1
    return network


def get_people(network):
    "Retourner la liste des personnes de ce réseau dans un tableau"
    return list(network)
    
    

def are_friends(network, person1, person2):
    """Retourner True si les deux personnes sont amis selon le réseau sinon retourner False"""
    return person1 in network[person2]


def all_his_friends(network, person, group):
    """Retourner True si la personne est ami avec tout les membres du groupe et False sinon"""
    #Retourner True si le tableau des amis est vide 
    if len(group)== 0 :
        return True
    i=0
    var=True
    while i<len(group):
        if not are_friends(network,person,group[i]):
            return False
        i+=1
    return var
    

def is_a_community(network, group):
    """Retourner True si le groupe est une communauté et False sinon"""
    j=0
    var=True
    while j<len(group):
        person=group[j]
        group2=group.copy()
        group2.remove(person)
        if not all_his_friends(network,person,group2):
            return False
        j+=1
    return var


def find_community(network, group):
    """Retourner une communauté en fonction de l'heuristique décrite"""
    communaute=[]    
    i=0
    while i<len(group):
        if all_his_friends(network,group[i],communaute):
            communaute.append(group[i])
        i+=1    
    return communaute 

def order_by_decreasing_popularity(network, group):
    """Retourner la communauté trouvée en appliquant l'heuristique de construction de communauté maximale"""
    #tri_a_bulle
    i=0
    statut=False
    while not statut :
        i=0
        while i<len(group)-1:
            if len(network[group[i]]) < len(network[group[i+1]]):
                statut=False
                group[i+1],group[i]=group[i],group[i+1]#échanger les valeurs
                i=-1 # reprendre le tableau depuis le début
            i+=1 
        statut=True
            
    return group


def find_community_by_decreasing_popularity(network):
    """Retourner la communauté en triant l'ensemble des personnes du réseau selon l'ordre décroissant de popularité et en appliquant l'heuristique de construction maximale"""
    people=get_people(network)
    people_trie=order_by_decreasing_popularity(network,people)
    return find_community(network,people_trie)

def find_community_from_person(network, person):
    """Retourner une communauté maximale contenant un sous-ensemble des amis de la personne plus elle-même selon l'heuristique décrite"""
    communaute=[]
    communaute.append(person)
    amis=order_by_decreasing_popularity(network,network[person])
    i=0
    while i<len(amis):
        if all_his_friends(network,amis[i],communaute):
            communaute.append(amis[i])
        i+=1    
    return communaute   

def find_max_community(network):
    """Retourner la plus grande communauté trouvée"""
    people=get_people(network)
    max=0
    i=0
    while i<len(people):
        community=find_community_from_person(network, people[i])
        if len(community)> max :
            max_community=community
            max=len(max_community)
        i+=1
    return max_community  
