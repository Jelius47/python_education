from dataclasses import dataclass


# 3rd party functionality we cannot modify this functionality at all no way
@dataclass 
class DisplayDataType:
    index: float
    data: str

class DisplayData:
    def __init__(self,display_data: DisplayDataType):
        self.display_data = display_data
    
    def show_data(self):
        print(f"3rd party functionality {self.display_data.index} -- {self.display_data.data}")

# our code lets say here is where we are starting from
@dataclass
class DatabaseDataType:
    position: int
    amount: int

class StoreDatabaseData:  
    def __init__(self,database_data: DatabaseDataType):
        self.database_data = database_data

    def store_data(self,data):
        print(f"Database data stored : {self.database_data.position} --- {self.database_data.amount}")


class DisplayDataAdapter(StoreDatabaseData,DisplayData):
    def __init__(self, data):
        self.data = data

    def store_data(self, data):
        print("Call our code but use 3rd party code")

        for item in self.data:
            ddt = DisplayDataType(float(item.position),str(item.amount))
            self.display_data = ddt
            self.show_data()
        
def generate_data():
    data = list()
    data.append(DisplayDataType(2,2))
    data.append(DisplayDataType(2,2))
    data.append(DisplayDataType(3,7))
    data.append(DisplayDataType(26,28))
    