import numpy as np
import pandas as pd

t = pd.read_csv('./arabica_ratings_raw.csv')

t = t.fillna(0)
len(t.columns)
t.columns
t['Country of Origin'].value_counts() #OK
t['Farm Name'].value_counts() 
t['In-Country Partner'].value_counts() #OK
t['Flavor'].value_counts()
t['Variety'].value_counts() #OK
t['Processing Method'].value_counts() #OK
t['Color'].value_counts() #not so OK
t['Company'].value_counts()
t['Owner.1'].value_counts()

t.Species.head()
t2 = pd.read_csv("./arabica_data_cleaned.csv")
t2['Cupper.Points'].value_counts()
t2['Total.Cup.Points'].value_counts()
t2['Moisture'].value_counts()
t2['Category.One.Defects'].value_counts()

t2['Country.of.Origin'].isna().value_counts() #OK
t2['Farm.Name'].value_counts() #
t2['In.Country.Partner'].value_counts() #OK
t2['Flavor'].value_counts()
t2['Variety'].value_counts() #OK
t2['Processing.Method'].isna().value_counts() #OK
t2['Color'].value_counts() #not so OK

t2 = t2.dropna(subset=['Country.of.Origin','In.Country.Partner','Total.Cup.Points','altitude_mean_meters','Region'])
t2.shape
t2.to_csv("./arabica_data_cleaned1.csv")

t2.columns
t2['Processing.Method'].head()
t2 = t2.reset_index(drop=True)
t2 = t2.dropna()
t2.head()



t2.to_csv("./arabica_cleaned.csv")

t3 = pd.read_csv("./arabica_data_cleaned1.csv")
g = t3['Total.Cup.Points'].groupby(t3['Processing.Method'])
t3['Processing.Method'].value_counts()
t3['Region'].value_counts()
g2 = t3['Total.Cup.Points'].groupby(t3['Region'])
g2.mean()

g3 = t3['Total.Cup.Points'].groupby(t3['Country.of.Origin'])
g3.mean()

#可以画line chart
t4 = t3[(t3['Country.of.Origin']  == 'Guatemala')]
t4["altitude_mean_meters"].value_counts()

#可画 柱状图或者map
g4 = t4['Total.Cup.Points'].groupby(t4['Region'])
g4.mean()
t4['Region'].value_counts()


t3['Country.of.Origin'].value_counts() #OK
t3['Farm.Name'].value_counts() # 
t3['In.Country.Partner'].value_counts() #OK
t2['Flavor'].value_counts()
t3['Variety'].value_counts() #OK
t3['Processing.Method'].value_counts() #OK
t3['Color'].value_counts() #not so OK
t3['Company'].value_counts()
t3['Owner.1'].value_counts()
t3.shape
t2.shape
t3.columns
t3['Certification.Contact'].value_counts()

t4['Country.of.Origin'].value_counts()
t4['In.Country.Partner'].value_counts()
t3['In.Country.Partner'].value_counts()
t3 = t3.dropna(subset=['Color'])
t3.to_csv("./arabica_data_cleaned2")
t5 = pd.read_csv("./arabica_data_cleaned2")
t5 = t5.rename(columns = {'Country.of.Origin':'Country','In.Country.Partner':'Parter','Total.Cup.Points':'Score'})
t5.to_csv('./arabica_cleaned2.csv')

