NumPizzas = 5 

Num2Teams = 1

Num3Teams = 2

Num4Teams = 1

pizzas = [['onion', 'pepper', 'olive'], ['mushroom', 'tomato', 'basil'], ['chicken', 'mushroom', 'pepper'], ['tomato', 'mushroom', 'basil'], ['chicken', 'basil']]

#start with teams - grab a 2 person team, give them a big ol' pizza, grab a 2nd pizza and check for unique ingredients and then move on to the next 2 person team OR 3 person and so on...2nd
#start with pizzas - grab the biggest pizza, give it to the biggest team? Or the middle team? Then check for another pizza with unique ingredients until all the people have a pizza in that team

# NEEDS FIXING:
#   numbers for teams are actually strings (fix in parseData)

def parseData():
    f_open = open('./a_test.in','r')
    text = f_open.read()
    f_open.close()
    team = text.split("\n", 1)[0]
    teams = team.split(" ")[:-1]
    pizzas = text.split("\n")[1:]
    for i in range(0, len(pizzas)):
        pizzas[i] = pizzas[i].split(" ")[1:]
    return teams, pizzas

def distribution(zas):
    pass

def teamNumbers(teams):
    canDeliver = [0, 0, 0]
    while(teams[0] > 0):
        if teams[3] > 0 and teams[0]-4 > 1:
            teams[0] -= 4
            canDeliver[2] += 1
        elif teams[2] > 0 and teams[0]-3 > 1:
            teams[0] -= 4
            canDeliver[1] += 1
        elif teams[1] > 0 and teams[0]-2 > 1:
            teams[0] -= 4
            canDeliver[0] += 1
    print(canDeliver)

def main():
    teams, pizzas = parseData()
    teamNumbers(teams)

if __name__ == "__main__":
    main()