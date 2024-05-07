---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: "Cracking the Code: What Makes a LEGO Set Sell?"
---

## Introduction

Have you ever come across statements like: ["LEGO sets have proven to be a stable investment over time, with average returns of 10% annually, which is higher than stocks, bonds, gold, and many other collectible items."](https://www.nerdcube.eu/guides/investing-in-lego/#:~:text=some%20extra%20cash.-,LEGO%20sets%20have%20proven%20to%20be%20a%20stable%20investment%20over,passion%20and%20collecting%20for%20profit) or perhaps you've heard the bold claim that ["Investing in Lego is more lucrative than gold, art and wine."](https://www.theguardian.com/lifeandstyle/2021/dec/10/investing-in-lego-more-lucrative-than-gold-study-suggests). These intriguing snippets certainly catch our eye, making us wonder: are these claims brick-solid or just plastic fantastic? Let's dive in and crack the code on whether LEGO sets truly hold the keys to financial success.

<!-- ![Alt text](https://www.logodesignlove.com/wp-content/uploads/2017/07/lego-logo-13.jpg) -->
<div style="text-align:center">
    <img src="https://logos-world.net/wp-content/uploads/2020/09/LEGO-Logo.png" width="200" height="125">
</div>
<center><small>Figure 1: LEGO Logo</small></center>
<br>
We're diving headfirst into a massive dataset, which contains almost 2000 Lego sets from 2018 to 2023, comparing different LEGO products across different time periods and countries, including Germany, Canada, Poland, the United Kingdom, and the United States. We're uncovering insights into product demand, ownership trends, release timings throughout the year, and the duration a product remains available at the official LEGO store before hitting retail shelves. Join us on this adventure as we uncover fascinating patterns in this incredible game. Who knows, you might just discover the next set that proves to be a safe investment!
<br>
<br>

## Data Analysis

**How popular can a set be?**

How can you find some of these gems? Let's start talking about popularity. If we compare the different themes, we can see how we have a main one. It is [Star Wars](https://www.brickeconomy.com/sets/theme/star-wars), which has 49 subthemes and 937 different sets inside, and there is a considerable difference between the number of people who own a product of this theme and the number of people who want it. Let's see if this insight also corresponds with the following subtheme analysis.

{% include theme.html %}

<center><small>Figure 2: interactive graph between ownedyBy and wantedBy themes <br>
(Select and deselect by clicking on the legend on the top right part of the graph)
</small></center>
<br>
<br>

**Which subthemes would be the most wanted?**

Themes can be pretty big, so we wanted to analyze the subthemes and discover the most wanted ones. However, the amount of subthemes was too large to compare them. That's why we selected the top 20 subthemes with the highest difference between owned and wanted. These parameters could potentially increase the price of a particular set in the future!

 <!-- https://github.com/MarcusGalea/MarcusGalea.github.io/tree/master/subtheme.html -->

{% include subtheme.html %}

<center><small>Figure 3: interactive graph between ownedyBy and wantedBy top 20 subthemes <br>
(Select and deselect by clicking on the legend on the top right part of the graph)
</small></center>
<br>
If we look into the top 20 subthemes, we can see how the top three are inside Star Wars theme, such as the Ultimate Collector Series, Episode I, or The Clone Wars. This result can't surprise you if you remember our previous graph.
<br>

**How many realizes LEGO have per year?**

It is an interesting factor to take into consideration. How many chances per year could I have a new product? In the following figure, we analyze the information from 2018 until 2022 and cross it with the most popular subtheme, the Ultimate Collector Series.

{% include calendar.html %}

<center><small>Figure 4: comparative calendar graph between the subtheme Ultimate Collector Series and released dates </small></center>
<br>

As we can see in the figure, the only months that have released products are May (5), June (6), and July (7). However, there are fewer releases each year than in the previous one. According to our analysis, 2018 is the year with the most releases. Now you know when to pay attention to the LEGO website to make your purchases.
<br>

**How is my time window?**

Another interesting factor to take into account is the amount of time you have to buy the product for its original price. Let's take a look at the example in Figure 5, where we can see the time window in which the products of the most wanted subtheme were available and by country.
{% include timewindow.html %}

<center><small>Figure 5: time window were a product of Ultimate Collector Series was available</small></center>
<br>

Observing the graph, we can see how the average to buy a product is around 2-3 years, with the clear exception of [Death Star](https://www.brickeconomy.com/set/10188-1/lego-star-wars-death-star), which was realized in 2008 and was available for many years.

<br>

**How much can a product's price change?**

Let's see it with the example of the most wanted subtheme, the [Ultimate Collector Series](https://www.brickeconomy.com/sets/theme/star-wars/subtheme/ultimate-collector-series), inside the Star Wars theme. We can take the example of the [Assault on Hoth](https://www.brickeconomy.com/set/75098-1/lego-star-wars-assault-on-hoth) or [Slave I](https://www.brickeconomy.com/set/75060-1/lego-star-wars-slave-i), inside the subtheme Ultimate Collector Series, they were realized in 2016 and 2015 respectively. Now, both are retired, with an average annual growth of 7.5% and 17.5%.
<br>
{% include prices.html %}

<center><small>Figure 6: interactive price graph of the subtheme Ultimate Collector Series<br>
(Select and deselect by clicking on the legend on the top right part of the graph)
</small></center>
<br>
<br>

## Conclusion

Let's wrap this up. If you're eyeing LEGO sets as your next big investment move, you're into something cool, especially with those sets that have a pop culture twist. Think Star Wars – it's not just about nostalgia; it's about smart money moves. Remember, you've typically got a 2 to 3-year window to grab these sets at their original price before they become rare gems. And guess what? The prime time to watch out for these releases is between May and July each year. Now, let's talk about the price climb. Over time, some of these sets start to skyrocket in value. Imagine grabbing a set, sitting tight, and then watching its price go up like a rocket. So, if you're all about making smart picks that blend your love for pop culture with a keen investment eye, keeping these pointers in mind could lead you to some pretty exciting scores. Happy LEGO hunting!

<br>
<br>

If you want to learn more: <br>
[Download the DataSet here](https://mostwiedzy.pl/en/open-research-data/data-on-lego-sets-release-dates-and-retail-prices-combined-with-aftermarket-transaction-prices-betwe,10210741381038465-0) <br>
[Brickeconomy, the economy of LEGO](https://www.brickeconomy.com/) <br>
[LEGO website](https://www.lego.com/da-dk)
<br>
