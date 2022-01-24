from bajillion import DataLoader

def getCity(cities, id):
    for c in cities:
        if c.id == id:
            return c

def getBillionaire(billionaires, id):
    for b in billionaires:
        if b.id == id:
            return b

def main():
    city_id = 29
    billionaire_id = 1
    car_cost = 60000
    cities = DataLoader.loadCities()
    billionaires = DataLoader.loadBillionaires()
    city = getCity(cities, city_id)
    billionaire = getBillionaire(billionaires, billionaire_id)

    print(f'There are {city.population:,}  people in {city.name}, {city.state}\n')
    print(f'A new car costs ${car_cost:,}\n')
    print(f'It would cost ${(car_cost * city.population):,} to buy a new car for everyone in the city.\n')
    print(f'{billionaire.name} has a net worth of ${billionaire.net_worth:,}.\n')
    print(f'They would still have ${(billionaire.net_worth - (car_cost * city.population)):,} left after buying everyone a new car.\n')
    print(f'It would only take {((car_cost * city.population) / billionaire.net_worth):.2%} of their net worth.\n')

if __name__ == '__main__':
    main()