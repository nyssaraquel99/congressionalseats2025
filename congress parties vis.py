# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 22:36:22 2025

@author: nyssa
"""

#%% imports
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#%% web stuff
#set up headless browser for webscraping
options=webdriver.ChromeOptions()
options.add_argument("--headless")
driver=webdriver.Chrome(options=options)

#create beautifulsoup object from wiki page
url="https://en.wikipedia.org/wiki/Party_divisions_of_United_States_Congresses"
driver.get(url)
html=driver.page_source
soup=BeautifulSoup(html,"html.parser")

#close connection
driver.quit()

#%% analyze soup
tables=soup.find_all("table")
party_div_html=tables[0]

#go through each row then column in table and append to dataframe
dictionary={}
i=1
for row in party_div_html.tbody.find_all("tr"):
    columns=row.find_all("td")
    row_data=[]
    if columns !=[]:
        for cell in columns:
            row_data.append(cell.text.strip())
        dictionary[i]=row_data
        i+=1      
df=pd.DataFrame.from_dict(dictionary,orient="index")

#%% clean dataframe
df.replace("—","0",inplace=True)

#%% break up dataframe by parties present
#congresses 1-3
con_1789_1795=df.iloc[0:3]
con_1789_1795.columns=["Congress","Years",
                       "S Total","S Anti-Admin","S Pro-Admin","S Others","S Vacancies",
                       "H Total","H Anti-Admin","H Pro-Admin","H Others","H Vacancies",
                       "President","Trifecta"]
#extract first year from years column
con_1789_1795.insert(2,"Year",con_1789_1795["Years"].str.slice(stop=4))
#drop superfluous columns
con_1789_1795=con_1789_1795[["Year",
                            "S Anti-Admin","S Pro-Admin","S Others","S Vacancies",
                            "H Anti-Admin","H Pro-Admin","H Others","H Vacancies"]]
con_1789_1795=con_1789_1795.astype(int)
#split into senate and house
sen_1789_1795=con_1789_1795[["Year",
                             "S Anti-Admin","S Pro-Admin","S Others","S Vacancies"]]
hou_1789_1795=con_1789_1795[["Year",
                             "H Anti-Admin","H Pro-Admin","H Others","H Vacancies"]]

#congresses 4-18
con_1795_1825=df.iloc[3:18]
con_1795_1825.columns=["Congress","Years",
                       "S Total","S Democratic-Republicans","S Federalists","S Others","S Vacancies",
                       "H Total","H Democratic-Republicans","H Federalists","H Others","H Vacancies",
                       "President","Trifecta"]
#extract first year from years column
con_1795_1825.insert(2,"Year",con_1795_1825["Years"].str.slice(stop=4))
#drop superfluous columns
con_1795_1825=con_1795_1825[["Year",
                             "S Democratic-Republicans","S Federalists","S Others","S Vacancies",
                             "H Democratic-Republicans","H Federalists","H Others","H Vacancies"]]
con_1795_1825=con_1795_1825.astype(int)
#split into senate and house
sen_1795_1825=con_1795_1825[["Year",
                             "S Democratic-Republicans","S Federalists","S Others","S Vacancies"]]
hou_1795_1825=con_1795_1825[["Year",
                             "H Democratic-Republicans","H Federalists","H Others","H Vacancies"]]

#congresses 19-24
con_1825_1837=df.iloc[18:24]
con_1825_1837.columns=["Congress","Years",
                       "S Total","S Jacksonian","S Anti-Jacksonian","S Others","S Vacancies",
                       "H Total","H Jacksonian","H Anti-Jacksonian","H Others","H Vacancies",
                       "President","Trifecta"]
#extract first year from years column
con_1825_1837.insert(2,"Year",con_1825_1837["Years"].str.slice(stop=4))
#drop superfluous columns
con_1825_1837=con_1825_1837[["Year",
                             "S Jacksonian","S Anti-Jacksonian","S Others","S Vacancies",
                             "H Jacksonian","H Anti-Jacksonian","H Others","H Vacancies"]]
con_1825_1837=con_1825_1837.astype(int)
#split into senate and house
sen_1825_1837=con_1825_1837[["Year",
                             "S Jacksonian","S Anti-Jacksonian","S Others","S Vacancies"]]
hou_1825_1837=con_1825_1837[["Year",
                             "H Jacksonian","H Anti-Jacksonian","H Others","H Vacancies"]]

#congresses 25-33
con_1837_1855=df.iloc[24:33]
con_1837_1855.columns=["Congress","Years",
                       "S Total","S Democrats","S Whigs","S Others","S Vacancies",
                       "H Total","H Democrats","H Whigs","H Others","H Vacancies",
                       "President","Trifecta"]
#extract first year from years column
con_1837_1855.insert(2,"Year",con_1837_1855["Years"].str.slice(stop=4))
#drop superfluous columns
con_1837_1855=con_1837_1855[["Year",
                             "S Democrats","S Whigs","S Others","S Vacancies",
                             "H Democrats","H Whigs","H Others","H Vacancies"]]
con_1837_1855=con_1837_1855.astype(int)
#split into senate and house
sen_1837_1855=con_1837_1855[["Year",
                             "S Democrats","S Whigs","S Others","S Vacancies"]]
hou_1837_1855=con_1837_1855[["Year",
                             "H Democrats","H Whigs","H Others","H Vacancies"]]

#congress 34
con_1855_1857=pd.DataFrame(df.iloc[34]).transpose()
con_1855_1857.columns=["Congress","Years",
                       "S Total","S Democrats","S Opposition","S Others","S Vacancies",
                       "H Total","H Democrats","H Opposition","H Others","H Vacancies",
                       "President","Trifecta"]
#set year
con_1855_1857.insert(2,"Year","1855")
#drop superfluous columns
con_1855_1857=con_1855_1857[["Year",
                             "S Democrats","S Opposition","S Others","S Vacancies",
                             "H Democrats","H Opposition","H Others","H Vacancies"]]
con_1855_1857=con_1855_1857.astype(int)
#split into senate and house
sen_1855_1857=con_1855_1857[["Year",
                             "S Democrats","S Opposition","S Others","S Vacancies"]]
hou_1855_1857=con_1855_1857[["Year",
                             "H Democrats","H Opposition","H Others","H Vacancies"]]

#congresses 35-119
con_1857_2027=df.iloc[34:119]
con_1857_2027.columns=["Congress","Years",
                       "S Total","ZS Democrats","ZS Republicans","ZS Others","ZS Vacancies",
                       "H Total","ZH Democrats","ZH Republicans","ZH Others","ZH Vacancies",
                       "President","Trifecta"]
#extract first year from years column and clean up other columns with annotations
con_1857_2027.insert(2,"Year",con_1857_2027["Years"].str.slice(stop=4))
con_1857_2027.insert(5,"S Democrats",con_1857_2027["ZS Democrats"].str.slice(stop=2))
con_1857_2027.insert(7,"S Republicans",con_1857_2027["ZS Republicans"].str.slice(stop=2))
con_1857_2027.insert(9,"S Others",con_1857_2027["ZS Others"].str.slice(stop=1))
con_1857_2027.insert(11,"S Vacancies",con_1857_2027["ZS Vacancies"].str.slice(stop=1))
con_1857_2027.insert(14,"H Democrats",con_1857_2027["ZH Democrats"].str.slice(stop=3))
con_1857_2027.insert(16,"H Republicans",con_1857_2027["ZH Republicans"].str.slice(stop=3))
con_1857_2027.insert(18,"H Others",con_1857_2027["ZH Others"].str.slice(stop=-4))
con_1857_2027.insert(20,"H Vacancies",con_1857_2027["ZH Vacancies"].str.slice(stop=1))
#drop superfluous columns
con_1857_2027=con_1857_2027[["Year",
                             "S Democrats","S Republicans","S Others","S Vacancies",
                             "H Democrats","H Republicans","H Others","H Vacancies"]]
con_1857_2027.replace("","0",inplace=True)
con_1857_2027=con_1857_2027.astype(int)
#split into senate and house
sen_1857_2027=con_1857_2027[["Year",
                             "S Democrats","S Republicans","S Others","S Vacancies"]]
hou_1857_2027=con_1857_2027[["Year",
                             "H Democrats","H Republicans","H Others","H Vacancies"]]

#combine all dataframes into one dataframe which accounts for shared party names
us_congress=pd.concat([con_1789_1795,con_1795_1825,con_1825_1837,
                       con_1837_1855,con_1855_1857,con_1857_2027],
                      ignore_index=True,sort=False)
#senate data
us_senate=pd.concat([sen_1789_1795,sen_1795_1825,sen_1825_1837,
                     sen_1837_1855,sen_1855_1857,sen_1857_2027],
                    ignore_index=True,sort=False)
#reorganize columns to have others and vacancies last
cols=list(us_senate.columns)
cols=cols[0:3]+cols[5:]+cols[3:5]
us_senate=us_senate[cols]
#house data
us_house=pd.concat([hou_1789_1795,hou_1795_1825,hou_1825_1837,
                    hou_1837_1855,hou_1855_1857,hou_1857_2027],
                   ignore_index=True,sort=False)
#reorganize columns to have others and vacancies last
cols=list(us_house.columns)
cols=cols[0:3]+cols[5:]+cols[3:5]
us_house=us_house[cols]
#%% plot congress seat data
#senate
colors=["khaki","darkgray","skyblue","gray","darkseagreen","pink","royalblue",
        "gold","olive","orangered","seagreen","maroon"]

us_senate.plot(x="Year", kind="bar", stacked=True,
               figsize=(12,8),width=1,color=colors,
               title="United States Senate Seats 1789 - 2027"
               )
us_house.plot(x="Year", kind="bar", stacked=True,
              figsize=(12,8), width=1, color=colors,
              title="United States House of Representatives Seats 1789 - 2027"
              )

#%% export cleaned dataset
import os

path=os.path.dirname(__file__)

us_congress.fillna(0,inplace=True)
us_congress.to_csv(f"{path}\\us_congress.csv",index=False)
us_senate.fillna(0,inplace=True)
us_senate.to_csv(f"{path}\\us_senate.csv",index=False)
us_house.fillna(0,inplace=True)
us_house.to_csv(f"{path}\\us_house.csv",index=False)