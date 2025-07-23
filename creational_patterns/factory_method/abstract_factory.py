from abc import ABC,abstractmethod


# Creating abstract classes 
'''sceenario is we want to order food we want irrespective of 
    the restaurtant ......... :)
'''
class FoodType:
    french = 1
    american = 2


# absract factory
class Restaurant(ABC):
    @abstractmethod
    def make_food(self):
        pass
    @abstractmethod
    def make_drink(self):
        pass


class FrenchRestaurant(Restaurant):
    def make_food(self):
        print("Cordon bleu")
        # return super().make_food()

    def make_drink(self):
        print("Merlot")
        # return super().make_drink()
        
class AmericanRestaurant(Restaurant):
    def make_food(self):
        print("Hamburger")
        # return super().make_food()
    def make_drink(self):
        print("coca colaaaaaa !!!")
        # return super().make_drink()

# Defining the abstract class 
class RestaurantFactory:
    def suggest_restaurant(r_type: FoodType):
        if r_type == FoodType.french:
            return FrenchRestaurant()
        elif r_type == FoodType.american:
            return AmericanRestaurant()
        
    

def dine_at(restaurant : Restaurant):
    print("For dinner we are having : ")
    restaurant.make_food()
    restaurant.make_drink()

if __name__ == "__main__":
    suggestion1 = RestaurantFactory.suggest_restaurant(FoodType.french)
    suggestion2 = RestaurantFactory.suggest_restaurant(FoodType.american)

    dine_at(suggestion1)
    dine_at(suggestion2)