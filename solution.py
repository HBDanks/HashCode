NumPizzas = 5 

Num2Teams = 1

Num3Teams = 2

Num4Teams = 1

#check remainder from number of pizzas/team size, if a valid team size is left (2,3,4) you're good to go

pizzas = [['onion', 'pepper', 'olive'], ['mushroom', 'tomato', 'basil'], ['chicken', 'mushroom', 'pepper'], ['tomato', 'mushroom', 'basil'], ['chicken', 'basil']]

teams = {"Num2Teams": 1, "Num3Teams" : 2, "Num4Teams": 1}

#start with teams - grab a 2 person team, give them a big ol' pizza, grab a 2nd pizza and check for unique ingredients and then move on to the next 2 person team OR 3 person and so on...2nd
#start with pizzas - grab the biggest pizza, give it to the biggest team? Or the middle team? Then check for another pizza with unique ingredients until all the people have a pizza in that team
def parseData(): 
    f_open = open('./a_test.in', 'r')
    text = f_open.read()
    f_open.close()
    team = text.split("\n", 1)[0]
    formattedTeams = team.split(" ")
    pizzas = text.split("\n")[1:]
    for i in range(0, len(pizzas)): 
        pizzas[i] = pizzas[i].split(" ")[1:]
    return teams, pizzas

def main():
    teams, pizzas = parseData()

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

def distribution(teams):
    pizzas = teams[0]
    canDeliver = [0, 0, 0]
    if(pizzas%4 and teams[3]):
        pizzas -= 4
        pizza[3] -= 1
        canDeliver[2] += 1
    elif(pizzas%3 and teams[2]):
        pizzas -= 3
        pizza[2] -= 1
        canDeliver[1] += 1
    else(pizzas%2 and teams[1]):
        pizzas -= 3
        pizza[2] -= 1
        canDeliver[1] += 1
        

def delivery(zas, teams):
    result = {
        "numOfDeliveries": 0, 
    }
    #where zas is the list of pizzas and teams is the number of each team

    if (teams["Num2Teams"]>=0):
        for team in range (teams["Num2Teams"]):
            unique = []
            result.update({f"Team{team}": [2]})
            for x in range(2): 
                unique = uniqueIngredients(unique, zas[x])
                if(unique):
                    result[f"Team{team}"].append(f"Pizza{x}")
            result["numOfDeliveries"] += 1
    
    return result


if __name__ == "__main__":
    main()    

                    
    
