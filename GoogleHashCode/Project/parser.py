def read_file(filename):
  print(f"Reading file {filename}...")
  text = open(f"../{filename}.txt", "r").read()
  duration, numIntersections, numStreets, numCars, score = [int(x) for x in text.split("\n", 1)[0].split(" ", 4)[0:5]]
  streets = {}
  cars = []
  for street in text.split("\n")[1: -numCars -1]:
      streets[street.split(" ")[2]] = [int(street.split(" ")[0]), int(street.split(" ")[1]), int(street.split(" ")[3])]
  for car in text.split("\n")[-numCars -1: -1]:
      cars.append(car.split(" ")[1:])
  print(f"Finished reading file {filename}...")
  return duration, numIntersections, numStreets, numCars, score, streets, cars

def write_file(filename, lines):
  print(f"Writing file {filename}_response...")
  file = open(f"../{filename}_response.txt", "w")
  #["this is a line \n", "This is a line \n"]
  #write
  file.writelines(lines)
  file.close()
  

  print(f"Finished writing file {filename}_response...")