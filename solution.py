NumPizzas = 5 

Num2Teams = 1

Num3Teams = 2

Num4Teams = 1

pizzas = [['onion', 'pepper', 'olive'], ['mushroom', 'tomato', 'basil'], ['chicken', 'mushroom', 'pepper'], ['tomato', 'mushroom', 'basil'], ['chicken', 'basil']]

#start with teams - grab a 2 person team, give them a big ol' pizza, grab a 2nd pizza and check for unique ingredients and then move on to the next 2 person team OR 3 person and so on...2nd
#start with pizzas - grab the biggest pizza, give it to the biggest team? Or the middle team? Then check for another pizza with unique ingredients until all the people have a pizza in that team

def distribution(zas):
    