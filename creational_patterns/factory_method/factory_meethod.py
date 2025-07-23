# Sincee python doesnt support abstract class
from abc import ABC,abstractstaticmethod

# Defining abstract class with basic or common functionalities
class Country:
    pass
# Defining interface implementation classes

class USA(Country):
    pass

class Spain(Country):
    pass

class Japan(Country):
    pass

# The abstract method that will allow us to implement our factory
class CurrencyFactory(ABC):
    @abstractstaticmethod
    @staticmethod
    def currency_factory(self,country)->str:
        pass

# Defining our interfaces 

class FiatCurrencyFactory(CurrencyFactory):
    def currency_factory(self,country)->str:
        if country is USA:
            return "USD"
        elif country is Japan:
            return "JPY"
        else:
            return "EUR"
        
class VirtualCurrencyFactory(CurrencyFactory):
    def currency_factory(self,country)->str:
        if country is USA:
            return "Bitcoin"
        elif country is Japan:
            return "Etherium"
        else:
            return "DogeCoin"
        



