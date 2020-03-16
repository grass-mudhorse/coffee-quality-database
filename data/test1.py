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
t2['Total.Cup.Points']

t2['Country.of.Origin'].value_counts() #OK
t2['Farm.Name'].value_counts() # 
t2['In.Country.Partner'].value_counts() #OK
t2['Flavor'].value_counts()
t2['Variety'].value_counts() #OK
t2['Processing.Method'].value_counts() #OK
t2['Color'].value_counts() #not so OK
t2['Company'].value_counts()
t2['Owner.1'].value_counts()
t2.columns
t2['Processing.Method'].head()
t2 = t2.reset_index(drop=True)
t2 = t2.dropna()
t2.head()


t2.to_csv("./arabica_cleaned.csv")