from bajillion import DataLoader

def main():
    cities = DataLoader.loadCities()
    billionaires = DataLoader.loadBillionaires()
    print(cities)
    print(billionaires)

if __name__ == '__main__':
    main()