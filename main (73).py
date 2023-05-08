# Define a class for individual cows in the herd
class Cow:
    def __init__(self, id, age, breed):
        self.id = id
        self.age = age
        self.breed = breed
        self.health_status = "Healthy"
        self.last_milk_production = None
        self.last_milk_production_date = None
        
    def add_milk_production(self, gallons, date):
        self.last_milk_production = gallons
        self.last_milk_production_date = date
        
# Define a class for the entire herd
class DairyFarm:
    def __init__(self, name):
        self.name = name
        self.cows = []
        self.records = {}
        
    def add_cow(self, id, age, breed):
        cow = Cow(id, age, breed)
        self.cows.append(cow)
        self.records[id] = []
        
    def add_milk_production_record(self, id, gallons, date):
        cow = self.get_cow_by_id(id)
        cow.add_milk_production(gallons, date)
        self.records[id].append(('Milk Production', gallons, date))
        
    def add_health_record(self, id, status, date):
        cow = self.get_cow_by_id(id)
        cow.health_status = status
        self.records[id].append(('Health', status, date))
        
    def get_cow_by_id(self, id):
        for cow in self.cows:
            if cow.id == id:
                return cow
        return None
        
    def get_cow_records(self, id):
        if id in self.records:
            return self.records[id]
        else:
            return []
