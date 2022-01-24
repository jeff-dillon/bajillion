# bajillion

bajillion is a simple app to help relate to obscene wealth. This app is meant 
as an exmple for the Data Analysis with Python 1 course at 
[Code Louisville](https://www.codelouisville.org/).

## The Question / The Big Idea

How does a billionaire's wealth relate to things that the rest of us might purchase? 

Let's take an example following the Oprah model: Everybody gets a Car!

What if a Billionaire bought everyone in your town a Corvette? I live in Louisville, KY along with about 600K other people. A Corvette costs about $60K. 

`600K people x $60K per Corvette = $36B`

It would cost $36 billion to buy a Corvette for every person in Louisville. 

But let's make it more specific. Here's a list of the top ten Billionaires.  

| Rank | Name | Net Worth |
| ---- | ---- | --------- |
| 1 | Elon Musk | $268.1 B |
| 2 | Jeff Bezos | $188.0 B |
| 3 | Bernard Arnault & family | $186.6 B |
| 4 | Bill Gates | $134.5 B |
| 5 | Larry Ellison | $120.1 B |
| 6 | Larry Page | $119.4 B |
| 7 | Mark Zuckerberg | $117.5 B |
| 8 | Warren Buffett | $116.9 B |
| 9 | Sergey Brin | $115.1 B |
| 10 | Steve Ballmer | $98.5 B |

Elon Musk is a Billionaire. Specifically, he has $268 Billion dollars in Net Worth as of 1/15/2022.

`$268 billion - 36 billion = ~ $232 billion`

Elon Musk could buy every man, woman, and child in Louisville KY a brand new Corvette and still have over $232 billion dollars. 

`268B / 36B = 13.5%` 

It would cost Elon 13.5% of his Net Worth. What would the equivalant purchase be for someone in Louisville? The median household income in Kentucky is about $50K.

| State | Median Household Income |
| ----- | ----------------------- |
| KY | $50,589 |

13.5% of $50K is $6.7K.

`$50,589 * 13.5% = $6,793`

Here's an example scale of things normal people buy:

| Purchase Size | Range | % Income | Example |
| ------------- | ----- | -------- | ------- |
| X-Large | $100K+ | 200% + | House | 
| Large | $10 - $99K | 20% - 200%  | Car |
| Medium | $1K - $9K | 2% - 20%  | Disney Vacation |
| Small | $100 - $999 | .5% - 2% | TV |
| X-Small | $10 - $99 | .02% - .2% | X-mas Tree |
| XX-Small | $1 - $9 | .002% - .02% | Coffee |


That means that Elon Musk spending 36 billion dollars to  buy a corvette for every person in Louisville, KY would be similar to someone from Louisville taking the family to Disney World.

This app will help bridge that gap by relating a Billionaire's wealth in terms of typical consumer purchases. Instead of buying cars for a city, let's look at estimates for solving big problems:

| Problem | Estimate | Source |
| ----- | ---------- | ------ |
| Provide Electricity to Sub-Saharan Africa | $160B | [Source](https://www.sciencedirect.com/science/article/pii/S0140988312001144) |
| World Hunger [^1] | $45B | [Source](https://www.globalgiving.org/learn/how-much-would-it-cost-to-end-world-hunger/#:~:text=Learn%20more%20about%20the%20cost,Why%20such%20a%20big%20range%3F) |
| Homelessness in US | $20B | [Source](https://www.globalgiving.org/learn/how-much-would-it-cost-to-end-homelessness-in-america/) |
| Clean Water in Zimbabwe | $3B | [Source](https://www.wri.org/insights/it-could-only-cost-1-gdp-solve-global-water-crises) |
[^1]: average estimate for 1 year


Give the app a billionaire and a State, and the big problem to solve and the app will tell you the relative expense for the average person in your state.
## Data Sources

1. [Forbes List of Billionaires](https://www.forbes.com/real-time-billionaires/)

1. [Median Household Income by State](https://worldpopulationreview.com/state-rankings/median-household-income-by-state)

1. [Median Home Price by State](https://worldpopulationreview.com/state-rankings/median-home-price-by-state)

## Data Discovery & Cleaning

### billionares.csv

#### File Details
| | |
| ------ | --------|
| Source | manual web scraping from forbes.com| 
| Columns | Rank, Name, NetWorth, Change, Age, Industry, Country |
| Records | 164 items |
| Data Issues | Blank lines after every 10th row. Special characters in Change column.  | 

 #### Column Details
| Column | Description | Example |
| ------ | ----------- | ------- | 
|  Rank | Numeric values ranging from 1 - 150 | 1 |
| Name | String with Person's name or Family name | Elon Musk |
| NetWorth|  Net worth representee as string with "$", decimal number, and "B" ranging from 13.7B - 268.1B | $268.1 B | 
| Change | String with amount of change and % change  or "$0" if change can't be determined. | ▶ $4.1 B - 1.54%| 
| Age | integer age in years or blank | 50 | 
| Industry | Company or Industry. No blanks.| Tesla, SpaceX | 
| Country | String with full country name. No blanks. | United States |
 
#### Data Cleaning

Cleaning the list of billionaires from Forbes involved:
1. convert the forbes HTML table to CSV using online converter
1. remove blank lines
1. convert rank from string to int
1. parse the net worth ro remove characters and convert from float to int
1. omit the change column from the raw file


### HouseholdIncome.csv

#### File Details
| | |
| ------ | --------|
| Source | csv file | 
| Columns | State, MedianValue |
| Records | 50 items |
| Data Issues | none  | 

 #### Column Details
| Column | Description | Example |
| ------ | ----------- | ------- | 
|  State | String of state name | New Mexico |
| MedianValue | int with range between 45081 - 84805 | 171400 |
 
#### Data Cleaning

Cleaning the list of income from worldpopulationreview.com involved:
1. No data cleaning needed




 ### MedianHomeCost.csv

#### File Details
| | |
| ------ | --------|
| Source | csv file | 
| Columns | State, HouseholdIncome |
| Records | 50 items |
| Data Issues | none  | 

 #### Column Details
| Column | Description | Example |
| ------ | ----------- | ------- | 
|  State | String of state name | New Mexico |
| HouseholdIncome | int with range from 119000 - 615300 | 49754 |
 
#### Data Cleaning

Cleaning the list of home prices from worldpopulationreview.com involved:
1. No data cleaning needed


#

## Project Backlog
- [x] Document the Problem / Question in the README
- [x] Find the data
- [x] Describe the data
- [x] Create Python script to clean the data
- [ ] Create Python script to analyze the clean data
- [ ] Create Python script to show a visualization of the clean data

