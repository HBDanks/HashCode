# create a class for intersections
class Intersection:
  def __init__(self, identity):
      self.identifier = identity
      self.incoming_streets = []
      self.schedule = []
      self.num_incoming_streets = 0

  def add_incoming(self, street_name):
      self.incoming_streets.append(street_name)
      #hard code a timer of 1 to start for each light
      self.num_incoming_streets += 1
      self.schedule.append(1)

  def add_outgoing(self, street):
      self.outgoing_streets.append(street)

  def return_schedule(self):
      return_val = [self.identifier, self.num_incoming_streets]
      for i in range(len(self.incoming_streets)):
          return_val.append([self.incoming_streets[i], self.schedule[i]])
      return return_val
