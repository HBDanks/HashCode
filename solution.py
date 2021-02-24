import math

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

def parseData(file):
    f_open = open(file,'r')
    text = f_open.read()
    f_open.close()
    team = text.split("\n", 1)[0]
    teams = [int(x) for x in team.split(" ")]
    pizzas = text.split("\n")[1:]
    for i in range(0, len(pizzas)):
        pizzas[i] = pizzas[i].split(" ")[1:]
    print('data parsed')
    return teams, pizzas

def parseResult(file, result):
    f_open = open(file, 'w')
    f_open.writelines(result)
    f_open.close()

# def distribution2(zas, teams): 
#     # [1, 1, 0]
#     res = [str(sum(teams)) + '\n']
#     za = 0
    
#     #gives every team one pizza
#     for i in range(len(teams)):
#         for j in range(teams[i]):
#             delivery = [str(i+2)]
#             delivery.append(str(za))
#             za += 1
#             res.append(delivery)

#     for team in res
#     print(res)
#     return res

def distribution(zas, teams):
    #result to be dictionary [2, [2, 0, 1], [2, 2, 3], [3, 4, 5, 6]]
    #[1 team of 2, 1 team of 3, 0 team of 4]
    res = [str(sum(teams)) + "\n"]
    i = len(teams)-1 
    j = 0

    while (i >= 0): 
        if(teams[i] == 0): 
            i -= 1
        else:
            delivery = [str(i+2)]
            while (len(delivery) < i + 3): 
                delivery.append(str(j))
                j += 1
            delivery.append('\n')
            delivery = ' '.join(delivery)
            res.append(delivery)
            teams[i] -= 1
    
    print('pizza delivered')
    return res
            

def sortTeam(teams):
    # teams is [500, 65, 60, 60]
    canDeliver = [0, 0, 0] #[2top, 3top, 4top]

    # print(teams[0]%3)
    #set the number of 3 person teams first
    if(teams[0]%4 > 2 or teams[0]%4 == 0): 
        canDeliver[2] = min(math.floor(teams[0]/4), teams[3])
        teams[0] -= canDeliver[2] * 4
    if(teams[0]%3 >= 0):
        canDeliver[1] = min(math.floor(teams[0]/3), teams[2])
        teams[0] -= canDeliver[1] * 3
    if(teams[0]%2 >=0): 
        canDeliver[0] = min(math.floor(teams[0]/2), teams[1])
        teams[0] -= canDeliver[0]*2
    print('teams sorted')
    return(canDeliver)


# def teamNumbers(teams):
#     canDeliver = [0, 0, 0]
#     while(teams[0] > 1):
#         if teams[3] > 0 and teams[0]%teams[3]> :
#             teams[0] -= 4
#             teams[3] -= 1
#             canDeliver[2] += 1
#         elif teams[2] > 0 and teams[0]-3 > 1:
#             teams[0] -= 3
#             teams[2] -= 1
#             canDeliver[1] += 1
#         elif teams[1] > 0:
#             teams[0] -= 2
#             teams[2] -= 1
#             canDeliver[0] += 1
#     print(canDeliver)
#     return canDeliver

def main():
    print('Test A --------------------------------------------------------')
    teams, pizzas = parseData('./a_test.in')
    team_deliveries = sortTeam(teams)
    result = distribution(pizzas, team_deliveries)
    parseResult('./a_result.in', result)
    print('Test B -------------------------------------------------------')
    teams, pizzas = parseData('./b_little_bit_of_everything.in')
    team_deliveries = sortTeam(teams)
    result = distribution(pizzas, team_deliveries)
    parseResult('./b_result.in', result)
    print('Test C ------------------------------------------------------')
    teams, pizzas = parseData('./c_many_ingredients.in')
    team_deliveries = sortTeam(teams)
    result = distribution(pizzas, team_deliveries)
    parseResult('./c_result.in', result)
    print('Test D -----------------------------------------------------')
    teams, pizzas = parseData('./d_many_pizzas.in')
    team_deliveries = sortTeam(teams)
    result = distribution(pizzas, team_deliveries)
    parseResult('./d_result.in', result)
    print('Test E -----------------------------------------------------')
    teams, pizzas = parseData('./e_many_teams.in')
    team_deliveries = sortTeam(teams)
    result = distribution(pizzas, team_deliveries)
    parseResult('./e_result.in', result)

if __name__ == "__main__":
    main()
