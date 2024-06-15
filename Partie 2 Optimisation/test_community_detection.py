# Make your tests here
reseau={
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}

reseau2={'Yasmine': ['Muriel', 'Joël', 'Thomas'],
 'Muriel': ['Yasmine', 'Joël'],
 'Joël': ['Yasmine', 'Muriel', 'Nassim', 'Ali', 'Andrea'],
 'Thomas': ['Yasmine', 'Daria', 'Carole'],
 'Nassim': ['Joël', 'Ali', 'Andrea'],
 'Andrea': ['Ali', 'Joël', 'Nassim', 'Valentin'],
 'Ali': ['Andrea', 'Joël', 'Nassim'],
 'Daria': ['Thomas'],
 'Carole': ['Thomas'],
 'Thierry': ['Axel', 'Léo'],
 'Axel': ['Thierry', 'Léo'],
 'Léo': ['Thierry', 'Axel', 'Valentin'],
 'Valentin': ['Léo', 'Andrea']}

 amis = ["Alice", "Bob","Charlie","Bob", "Alice", "Dominique", "Bob", "Dominique"]

 
def test_create_network():
    create_network(amis)=={'Alice': ['Bob', 'Dominique'],
 'Bob': ['Alice', 'Charlie', 'Dominique'],
 'Charlie': ['Bob'],
 'Dominique': ['Alice', 'Bob']}
    print("Le test de la fonction create_network est : OK")
test_create_network()


def test_get_people():
    assert get_people(reseau)==['Alice', 'Bob', 'Charlie', 'Dominique']
    assert not get_people(reseau2)==['Yasmine','Muriel','Joël','Thomas','Nassim','Andrea']
    print("Le test de la fonction get_people ets : OK")
test_get_people()


def test_are_friends():
    assert are_friends(reseau,"Bob","Alice")==True
    assert are_friends(reseau, "Alice","Bob")==True
    assert are_friends(reseau,"Alice","Charlie")==False
    assert are_friends(reseau2,"Yasmine","Muriel")==True
    print("Le test de la fonction are_friends est : OK")
test_are_friends()

def test_all_his_friends():
    assert all_his_friends(reseau,"Alice",["Bob","Dominique"])==True 
    assert all_his_friends(reseau,"Alice",["Bob","Charlie"])==False
    assert all_his_friends(reseau2, "Yasmine",["Muriel", "Joël"])==True
    print("Le test de la fonction all_his_friends est : OK")
test_all_his_friends()

def test_is_a_community():
    assert is_a_community(reseau,["Alice", "Bob", "Dominique"])==True
    assert is_a_community(reseau,["Alice", "Bob", "Charlie"])==False
    assert is_a_community(reseau2,["Yasmine","Muriel","Joël"])==True
    print("Le test de la fonction is_a_community est : OK")
test_is_a_community()

def test_find_community():
    assert find_community(reseau,["Alice", "Bob", "Charlie", "Dominique"])==["Alice", "Bob", "Dominique"]
    assert find_community(reseau,["Charlie", "Alice", "Bob", "Dominique"])==["Charlie", "Bob"]
    assert find_community(reseau,["Charlie", "Alice", "Dominique"])==["Charlie"]
    assert find_community(reseau2,["Yasmine","Muriel","Joël"])==['Yasmine', 'Muriel', 'Joël']
    
    reseau3=create_network(lecture_reseau("files/Communaute1.csv"))
    assert find_community(reseau3,['Barbra','Cloe','Louis'])                       
                           
    print("Le test de la fonction find_community est : OK")
    
test_find_community()

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(reseau,["Alice","Charlie","Bob"])==['Bob', 'Alice', 'Charlie']
    assert order_by_decreasing_popularity(reseau,['Dominique', 'Alice', 'Charlie'])==['Dominique', 'Alice', 'Charlie']
    assert order_by_decreasing_popularity(reseau,['Alice','Bob'])==['Bob','Alice']
    assert order_by_decreasing_popularity(reseau, ["Alice", "Charlie", "Dominique"])==["Alice","Dominique","Charlie"]
    assert order_by_decreasing_popularity(reseau2,["Yasmine","Muriel","Joël"])==['Joël', 'Yasmine', 'Muriel']
    
    reseau3=create_network(lecture_reseau("files/Communaute1.csv"))
    assert order_by_decreasing_popularity(reseau3,['Barbra','Cloe','Louis'])==['Barbra', 'Cloe', 'Louis']
    print("Le test de la fonction order_by_decreasing_popularity est : OK")
test_order_by_decreasing_popularity()

def test_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(reseau)==['Bob', 'Alice', 'Dominique']
    assert find_community_by_decreasing_popularity(reseau2)==['Joël', 'Andrea', 'Nassim', 'Ali']
    print("Le test de la fonction community_by_deccreasing_popularity est : OK")
test_community_by_decreasing_popularity()


def test_community_from_person():
    assert find_community_from_person(reseau,"Alice")==['Alice', 'Bob', 'Dominique']
    assert find_community_from_person(reseau, "Charlie")==['Charlie', 'Bob']
    assert find_community_from_person(reseau, "Dominique")==["Dominique","Bob","Alice"]
    assert find_community_from_person(reseau,"Bob")==["Bob","Alice","Dominique"]
    assert find_community_from_person(reseau2,"Yasmine")==['Yasmine', 'Joël', 'Muriel']
    assert not find_community_from_person(reseau2,"Joël")==['Joël', 'Andrea', 'Nassim']
    print("Le test de la fonction find_community_from_person est : OK")
test_community_from_person()


def test_find_max_community():
    assert find_max_community(reseau)==['Alice', 'Bob', 'Dominique']
    assert find_max_community(reseau2)==['Joël', 'Andrea', 'Nassim', 'Ali']
    print("Le test de la fonction find_max_community est : OK")
    
test_find_max_community()
