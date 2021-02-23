NumPizzas = 5 

Num2Teams = 1

Num3Teams = 2

Num4Teams = 1

#check remainder from number of pizzas/team size, if a valid team size is left (2,3,4) you're good to go

pizzas = [['onion', 'pepper', 'olive'], ['mushroom', 'tomato', 'basil'], ['chicken', 'mushroom', 'pepper'], ['tomato', 'mushroom', 'basil'], ['chicken', 'basil']]

teams = {"Num2Teams": 1, "Num3Teams" : 2, "Num4Teams": 1}

#start with teams - grab a 2 person team, give them a big ol' pizza, grab a 2nd pizza and check for unique ingredients and then move on to the next 2 person team OR 3 person and so on...2nd
#start with pizzas - grab the biggest pizza, give it to the biggest team? Or the middle team? Then check for another pizza with unique ingredients until all the people have a pizza in that team

def uniqueIngredients(used, za):
    #where var used is an array of the ingredients used so far and za is the newest pizza
    count = 0; 
    for ing in za: 
        if ing not in used: 
            used.append(ing)
            count+=1
        
    if count >= 1: 
        return used
    else:
        return null
        

# NEEDS FIXING:
#   numbers for teams are actually strings (fix in parseData)

def parseData():
    f_open = open('./a_test.in','r')
    text = f_open.read()
    f_open.close()
    team = text.split("\n", 1)[0]
    teams = [int(x) for x in team.split(" ")[:-1]]
    pizzas = text.split("\n")[1:]
    for i in range(0, len(pizzas)):
        pizzas[i] = pizzas[i].split(" ")[1:]
    return teams, pizzas

def distribution(zas, teams):
    #result to be dictionary [2, [2, 0, 1], [2, 2, 3], [3, 4, 5, 6]]
    #[1 team of 2, 1 team of 3, 0 team of 4]
    res = [sum(teams)]
    i = len(teams)-1 
    j = 0

    while (i >= 0): 
        if(teams[i] == 0): 
            i -= 1
        else:
            delivery = [i+2]
            while (len(delivery) < i + 3): 
                delivery.append(j)
                j += 1
            res.append(delivery)
            teams[i] -= 1
    print(res)
    return res
            




def teamNumbers(teams):
    canDeliver = [0, 0, 0]
    while(teams[0] > 1):
        if teams[3] > 0 and teams[0]-4 > 1:
            teams[0] -= 4
            canDeliver[2] += 1
        elif teams[2] > 0 and teams[0]-3 > 1:
            teams[0] -= 3
            canDeliver[1] += 1
        elif teams[1] > 0:
            teams[0] -= 2
            canDeliver[0] += 1
    print(canDeliver)
    return canDeliver

def main():
    teams, pizzas = parseData()
    team_deliveries = teamNumbers(teams)
    distribution(pizzas, team_deliveries)

if __name__ == "__main__":
    main()
