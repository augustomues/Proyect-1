# Project 1 - Shark Attacks

![MEME](https://dch81km8r5tow.cloudfront.net/wp-content/uploads/2015/07/Screen-Shot-2015-07-20-at-15.32.10-958x559.png)

## Index

### 1. Hypothesis/Goal

### 2. Visualizations

### 3. Conclutions

<br>
<br>

## 1. Hypothesis/Goal:

My goal is to get insightful information from a really mesy DataFrame related to Shark Attacks. This DataFrame is extracted from Kaggle: https://www.kaggle.com/datasets/teajay/global-shark-attacks

I would like to see the evolution of the shark attack on the last decades, trying to find reason behind the potential increase or decrease. For that i will review:

    1. Countries: Which are the countries that have increase/decrease the most on the last years?

    2. Fatality: If there is an increase/decrease of reports, are those in Fatal ones or not?
 
    3. Moment of the Day: Review if there has been a spike (or decrease) of attacks reported on specific moment of (Morning, Afternoon, Evening, Night)

    4. Season: Review the evolution of shark attacks reports per season
    
    5. Location: Review the evolution of shark attacks reports on specific locations 

    6. Investigator/Source: Review it there is any investigator or laboratory that during the last years have reported more (or less) than what were reporting

<br>

## 2. Analysis and Visualizations

After a deep cleaning done on the DataFrame, which can be found on the clean.ipynb file (functions encapsulated on the encapsulation.py file) we can quickly see that in the last 2 decades there has been an important spike on the shark attacks reported:


![ASD](Images/1.%20Shark%20Attacks%20Evolution.png)

As per the goal enaunced above, we will try to explain why such spike have happend
<br>
<br>

### <ins>**2.1. Countries**

Just considering the shark attacks reports done during the last 2 decades, and plotting the top 10 countries (accountbale for the 80% ot the reports done), we can see that USA is bar far the country that most reports has have, preciding by AUSTRALIA and SOUTH AFRICA:

![Alt text](Images/3.%20Top10%20Countries%20with%20most%20shark%20attacks%20(2020-2020).png)

In fact, these 3 countries are accounting for the 70% of the reports done on the last 2 decades.
<br>
<br>

### <ins>**2.2. Fatality**

Taking the data from 1900 till the present, as we can see on the chart below, the fatal shark accidents reports Decade over Decade have been considerably stable. We can see that clearly the spike of the last 2 decades is coming from non fatal shark attacks reports.
![Alt text](Images/2.%20Shark%20Attack%20Ev.%20per%20Fatality.png)

If we review the specific evolution for the top offender countries, we can see that indeed USA and AUSTRALIA are showing a conserning increase, while SOUTH AFRICA and the 'OTHER' countries, are more stable:

![Alt text](Images/4.%20Shark%20Attacks%20Ev.%20per%20Fatality%20per%20Top%20Countries.png)

This is why we will be **focusing in USA and AUSTRALIA**.
<br>
<br>

### <ins>**2.3. Moment of Day**
First of all, would be interesting to see how is the distribution of the shark attacks reports on the different moment of the days on the top 3 countries. We can clearly see that the afternoon (and also the morning) is when more accidents happen (obviously because is when most of the people are doing activities on the sea):

![Alt text](Images/7.%20Shark%20Attacks%20in%20top%203%20countries%20per%20Moment%20of%20Day.png)

See the evolution of this during the last decades, sadly we cannot find anything insightful (just worth to mention that in USA, the reports are high in the Afternoon, while in AUSTRALIA are more frequent in the morning):

![Alt text](Images/8.%20Shark%20Attack%20Ev.%20per%20moment%20of%20Day.png)

<br>
<br>

### <ins>**2.4. Season**

Similar to the Moment of the Day view, there is no much that we can say regarding the impact of the season in the evoultion of the sharks attack reports in USA and AUSTRALIA. The only thing that would be worth mentioning is that the different seasons in each country follows the same evolution as the overall evolution in the country. To see that, we should compare the below image with the one already showed in Fatality section.

![Alt text](Images/9.%20Shark%20Attack%20evolution%20per%20Season.png)

<br>
<br>

### <ins>**2.5. Location**
Only in USA was possible to spot several repetitions in terms of locations of the different reports. As we can see on the chart below, in the 2000 decade, there was an spike of shark attack reports, helping to explaing a little bit the overall spike of the shark attacks reports happened on that decade.

![Alt text](Images/11.%20Skark%20Attacks%20in%20USA%20per%20Location.png)

<br>
<br>

### <ins>**2.6. Investigator/Source**
After a deep exploration on this field, it was found that there were a common laboratory or group: GSAF (GSAF stands for 'Global Shark Attacks File': sharkattackfile.net/index.htm). That is why it was interesting to see if this specific group has started to report more and more accidents. And the answer? Absolutely:

![Alt text](Images/5.%20Shark%20Attacks%20reports%20Ev.%20done%20by%20GSAF.png)

And guess what! Which is the correspondent country responsable for that spike? If you said USA, you are right:

![Alt text](Images/6.%20Shark%20Attacks%20reports%20Ev.%20done%20by%20GSAF%20in%20USA%20and%20AUS.png)

<br>
<br>

## Conclusions

After the deep exploration and anlysis made, we are able to arrive to the following conclusions:

1. During the history, the fatal shark attack have been stable. The increse on the reports on the last 2 decades are in non-fatal shark attakcs accidents.
2. The countries responsible for the spike in the world of the shark attacks reports are mainly USA and AUSTRALIA (with a little contribution as well from SOUTH AFRICA). However, this last country, as well as the rest, has stayed more or less stable along the decades.
3. Neither the Moment of the Day (where the sharks attacks took place) nor the correspondet season of the attacks, helps us to explain the increase of the reports during the last 2 decades
4. In USA, during the 2000, there was an spike of reports in Volusia, helping to explain somehow the increase
5. Last but not least, GSAF group has reported x5 times reports in USA during the 2000 vs the 90s. They have reported about 250 reports more vs the ones they have reportes in the 90s.

What next?

1. It was not reviewed if there were dupicated reports reported by different source (or even the same one). We could review that.
2. On the description of the report, we could potentially look for words such as 'minor', 'no injurie', 'small'. Probably on the last decades we have started to report any incident, even if it was minor, while in the past we were reporting an attack just if there was a several injurie.
3. Get historic turism data from those countries. Probably the tourism has been increased drastically, thanks to the globalization, and it could be a reason for the spike

# THANKS!
![](https://media.tenor.com/7809giJ-B4kAAAAM/aplausos.gif)