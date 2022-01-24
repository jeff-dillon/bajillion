from dataclasses import dataclass
from dataclasses_json import dataclass_json
import json

@dataclass_json
@dataclass
class Billionaire:
    id : int
    name : str
    rank : int
    net_worth : int
    source : str
    country : str

@dataclass_json
@dataclass
class City:
    id : int
    name : str
    state : str
    population : int
    median_home_price : int
    household_income : int

class DataLoader:
    def loadBillionaires():
        file = open('./data/clean/billionaires.json')
        data = json.load(file)
        billionaire_list = []
        for b in data:
            billionaire_list.append(
                Billionaire(
                    id=b['id'],
                    name=b['name'],
                    rank=b['rank'],
                    net_worth=b['net_worth'],
                    source=b['source'],
                    country=b['country']
                )
            )
        file.close()
        return billionaire_list
    
    def loadCities():
        file = open('./data/clean/cities.json')
        data = json.load(file)
        city_list = []
        for b in data:
            city_list.append(
                City(
                    id=b['id'],
                    name=b['name'],
                    state=b['state'],
                    population=b['population'],
                    median_home_price=b['median_home_price'],
                    household_income=b['household_income']
                )
            )
        file.close()
        return city_list

