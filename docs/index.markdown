---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

# Introduction

Have you ever come across statements like: ["LEGO sets have proven to be a stable investment over time, with average returns of 10% annually, which is higher than stocks, bonds, gold, and many other collectible items."](https://www.nerdcube.eu/guides/investing-in-lego/#:~:text=some%20extra%20cash.-,LEGO%20sets%20have%20proven%20to%20be%20a%20stable%20investment%20over,passion%20and%20collecting%20for%20profit) or perhaps you've heard the bold claim that ["Investing in Lego is more lucrative than gold, art and wine."](https://www.theguardian.com/lifeandstyle/2021/dec/10/investing-in-lego-more-lucrative-than-gold-study-suggests). These intriguing snippets certainly catch our eye, making us wonder: are these claims brick-solid or just plastic fantastic? Let's dive in and crack the code on whether LEGO sets truly hold the keys to financial success.

<!-- ![Alt text](https://www.logodesignlove.com/wp-content/uploads/2017/07/lego-logo-13.jpg) -->
<div style="text-align:center">
    <img src="https://logos-world.net/wp-content/uploads/2020/09/LEGO-Logo.png" width="200" height="125">
</div>
<center><small>Figure 1: LEGO Logo</small></center>
<br>
We're diving headfirst into a massive dataset, which contains almost 2000 Lego sets from 2018 to 2023, comparing different LEGO products across different time periods and countries, including Germany, Canada, Poland, the United Kingdom, and the United States. We're uncovering insights into product demand, ownership trends, release timings throughout the year, and the duration a product remains available at the official LEGO store before hitting retail shelves. Join us on this adventure as we uncover fascinating patterns in this incredible game. Who knows, you might just discover the next set that proves to be a safe investment!

**How popular can a set be?**

If we compare the popularity of themes, we can see how we have a main one. It is [Star Wars](https://www.brickeconomy.com/sets/theme/star-wars), which has 49 subthemes and 937 different sets inside, and there is a considerable difference between the number of people who own a product of this theme and the number of people who want it.

{% include theme.html %}

<center><small>Figure 2: comparative graph between ownedyBy and wantedBy themes</small></center>
<br>
<br>

**Which subthemes would be the most wanted?**

We wanted to analyze the subthemes and discover which ones are the most wanted compared to the number of people who own them. These parameters could potentially increase the price of a particular set in the future.

 <!-- https://github.com/MarcusGalea/MarcusGalea.github.io/tree/master/subtheme.html -->

{% include subtheme.html %}

<center><small>Figure 3: comparative graph between ownedyBy and wantedBy top 20 subthemes</small></center>
<br>
If we look into the top 20 subthemes with the highest difference between owned and wanted, we can see how the top three are inside Star Wars theme, such as the Ultimate Collector Series, Episode I, or The Clone Wars.

**How much can a product's price change?**

Let's see it with the example of the most wanted subtheme, the Ultimate Collector Series, inside the Star Wars theme.
We can take the example of the [Death Star II (10143)](https://www.brickeconomy.com/set/10143-1/lego-star-wars-death-star-ii), inside the subtheme Ultimate Collector Series, that was realized in 2005, and it's now retired and has an annual growth of 10% on average.
<br>
{% include prices.html %}

<center><small>Figure 4: comparative price graph of the subtheme Ultimate Collector Series</small></center>
<br>
text 3 subthemes calendar or not
plot
<br>
text 4 example of an specific market
polish prices - going up - going down
plot

<br>
<br>

**Conclusion**

<br>
<br>

If you want to learn more:
[Download the DataSet here](https://mostwiedzy.pl/en/open-research-data/data-on-lego-sets-release-dates-and-retail-prices-combined-with-aftermarket-transaction-prices-betwe,10210741381038465-0)

<br>
