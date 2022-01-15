# bajillion

bajillion is a simple app to help people relate to obscene wealth. This app is meant as an exmple for the Data Analysis with Python 1 course at [Code Louisville](https://www.codelouisville.org/).

## The Question / The Big Idea

The concept is simple: Relate a billionaire's wealth to things that the rest of us might purchase.

| Size of Purchase | Cost | Example |
| ---------------- | ---- | ------- |
| X-Large | $100K - $1M | House | 
| Large | $10 - $99K | Car |
| Medium | $1K - $9K | Disney Vacation |
| Small | $100 - $900 | TV |
| X-Small | $10 - $90 | X-mas Tree |
| XX-Small | $1 - $9 | Coffee |

Let's take an example following the Oprah model: Everybody gets a Car!

What if a Billionaire bought everyone in your town a Corvette? I live in Louisville, KY along with about 600K other people. A Corvet costs about $60K. It would cost $36 billion to buy a Corvette for every person in Louisville. 

`600K people x $60K per Corvette = $36B`

But let's make it more specific. Elon Musk is a Billionaire. Specifically, he has $268 Billion dollars in Net Worth as of 1/15/2022. 

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

`$268 billion - 36 billion = ~ $232 billion`

Elon Musk could buy every man, woman, and child in Louisville KY a brand new Corvette and still have over $232 billion dollars. It would cost him 13.5% of his Net Worth.

I have a sense for how big Lousiville is. I've seen a corvette and have a sense for how much they cost. This helps me relate to how absurd this amount of money is for one person.

What would the equivalant purchase be for the average household in Louisville?

| State | Median Household Income |
| ----- | ----------------------- |
| KY | $50,589 |
| US Median | $65,712 |

`$50,589 * 13.5% = $6,793`

That means that Elon Musk spending 36 billion dollars to  buy a corvette for every person in Louisville, KY would be similar to someone from Louisville taking the family to Disney World.

After binging Downton Abbey and Succession, it quickly becomes clear that the wealthiest people inhabit a different world than the rest of us. It's hard to relate to a large number like $268 Billion. 

This app will help bridge that gap by relating a Billionaire's wealth in terms of typical consumer purchases.
## Data Sources

1. [Forbes List of Billionaires](https://www.forbes.com/real-time-billionaires/)

1. [US Census Population by City](https://www.census.gov/data/tables/time-series/demo/popest/2010s-total-cities-and-towns.html#ds)

1. [Median Household Income by State](https://worldpopulationreview.com/state-rankings/median-household-income-by-state)

1. [Median Home Price by State](https://worldpopulationreview.com/state-rankings/median-home-price-by-state)


...

## Project Backlog
- [x] Document the Problem / Question in the README
- [x] Find the data
- [ ] Describe the raw data
- [ ] Create Python script to clean the data
- [ ] Create CLI app to display the Data

