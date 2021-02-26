from parser import read_file, write_file
from intersection import Intersection
# priority 1: max cars to destination
# priority 2: fastest time to get cars to destination 

def priority_routes(cars, streets_dict):
  #array of street names. Use len(arr) to get the number of streets
  for car in cars:
    priority_calc(car, streets_dict)
  
  # sort the cars by the last value in the returned array from priority_calc
  sorted(cars, key=lambda x: x[-1])
  
  return cars

# calculates the total duration for a cars travel
def priority_calc(route, streets_dict):
  # duration equals sum of street times
  real_route = route[1:]
  duration_car = 0
  for street in real_route:
    duration_car += streets_dict[street][-1]
  
  # adds on the duration to the end of the array for sorting
  route.append(duration_car)
  return route

#figure out stoplights based on the cars that are at each and duration of streets
def intersections(streets_dict, num_intersections):
  #initialize intersection
  intersections = []
  
  for intersection in range(0, num_intersections):
    intersections.append(Intersection(intersection))
  
  # add the ingoing
  for street in streets_dict:
    #1st number is start 2nd number is end
    #1st number add to outgoing of that intersection
    index = streets_dict[street][1]
    name = street
    intersections[index].add_incoming(name)
    #2nd number add to incoming of that Intersection

  return intersections
#set up output
def schedule(intersections):
  #need to start this with number of active traffic lights. Is this a count somewhere? Count of incoming streets on each thing? 
  res = [0]
  for intersection in intersections:
    #intersection.return_schedule()
    res[0] += 1
    
    sched = intersection.return_schedule()

    #0, 2, name num, name num
    res.append(f"{sched[0]}\n{sched[1]}\n")

    for street in sched[2:]:
      res.append(f"{street[0]} {street[1]} \n")
  
  res[0] = str(res[0]) + "\n"
  return res

def main():
  # returns: duration, intersections, streets, score, streets_dict, cars_arr
  files = ["a", "b", "c", "d", "e", "f"]
  for file in files:

    duration, num_intersections, num_streets, num_cars, score, streets_dict, cars_arr = read_file(file)

    #intersections(streets_dict, num_intersections)  
    # car starts at end of first street
    # needs to cover the rest of the streets
    cars_arr = priority_routes(cars_arr, streets_dict)
    #print(f"cars are {cars_arr}")

    # write to the result file
    write_file(file, schedule(intersections(streets_dict, num_intersections)))

if __name__=="__main__":
  main()