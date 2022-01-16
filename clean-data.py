import csv, json, re
from bajillion import Billionaire, City

"""
    Script to clean the raw csv data and save as json

    billionaires cleaning
    1. remove blank lines
    2. convert rank from string to int
    3. parse the net worth ro remove characters and convert from float to int

    cities cleaning
    1. start with the population file
    2. split the city and state into two fields
    3. strip leading and trailing spaces from city and state
    4. convert the population to an int

    median home cost file is clean

    household income file is clean

"""

def parseNetWorth(nw_str):
    list_of_char = ['$', ' ', 'B','.']
    pattern = '[' + ''.join(list_of_char) + ']'
    clean_str = re.sub(pattern,'', nw_str)
    int_val = int(clean_str) * 100000000
    return int_val


def loadRawBillionaires():
    income = loadIncome()
    home_price = loadHomePrices()
    billionaires = []
    with open('./data/raw/billionaires.csv', newline='') as csvfile:
        popreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        i = 1    
        for row in popreader:
            if row['Name'] != '': # omit the blank rows
                b = Billionaire(
                    id=i,
                    name=row['Name'], 
                    rank=int(row['Rank']), # convert the rank to an int 
                    net_worth=parseNetWorth(row['NetWorth']), # convert the net worth to an int
                    source=row['Industry'],
                    country=row['Country'])
                billionaires.append(b)
                i = i + 1
    return billionaires


def saveCleanBillionaires(b):
    with open("./data/clean/billionaires.json", "w") as file:
        json.dump([ob.__dict__ for ob in b], file)


def parsePopulation(nw_str):
    list_of_char = ['$', ' ', 'B','.',',']
    pattern = '[' + ''.join(list_of_char) + ']'
    clean_str = re.sub(pattern,'', nw_str)
    int_val = int(clean_str)
    return int_val

def loadIncome():
    incomes = []
    with open('./data/raw/HouseholdIncome.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            incomes.append(
                { 'state' : row['State'],
                'income' : row['HouseholdIncome']
                })
    return incomes

def loadHomePrices():
    prices = []
    with open('./data/raw/MedianHomeCost.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            prices.append(
                { 'state' : row['State'],
                'price' : row['MedianValue']
                })
    return prices


def loadRawCities():
    incomes = loadIncome()

    fields = [
        'rank','geo','census','base',
        '2010','2011','2012','2013',
        '2014','2015','2016','2017',
        '2018','2019']
    cities = []
    incomes = loadIncome()
    prices = loadHomePrices()
    with open('./data/raw/population.csv', newline='') as csvfile:
        popreader = csv.DictReader(csvfile, fieldnames=fields, delimiter=',', quotechar='"')
        i = 1    
        for row in popreader:
            if row['rank'].isnumeric():

                # look up the median household income and convertit to int
                inc = 0
                
                for x in incomes:
                    if x['state'] == row['geo'].split(',')[1].strip():
                        inc = int(x['income'])

                # look up the median home price and convert it to int
                price = 0
                
                for x in prices:
                    if x['state'] == row['geo'].split(',')[1].strip():
                        price = int(x['price'])
                
                # add the city to the list
                cities.append(City(
                    id=i,
                    name=row['geo'].split(',')[0].strip(),
                    state=row['geo'].split(',')[1].strip(),
                    population=parsePopulation(row['2019']),
                    median_home_price=price,
                    household_income=inc
                    ))
                i = i + 1
    return cities


def saveCleanCities(c):
    with open("./data/clean/cities.json", "w") as file:
        json.dump([ob.__dict__ for ob in c], file)


def main():

    # clean the billionaire data
    blist = loadRawBillionaires()
    saveCleanBillionaires(blist)

    # clean the cities data
    clist = loadRawCities()
    print(clist)
    saveCleanCities(clist)


if __name__ == '__main__':
    main()
