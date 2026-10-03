# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# load data set
nobel = pd.read_csv("C:/Users/OMT/Downloads/nobel.csv")

# mode of sex and birth country column
top_gender = nobel['sex'].mode().iloc[0]
top_country = nobel['birth_country'].mode().iloc[0]
print(top_gender)
print(top_country)

# create us born and decade column
nobel['US_born'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = np.floor(nobel['year']/10)*10

# Group by 'decade' and calculate the mean of 'US_born'
decade_USA = nobel.groupby('decade', as_index=False)['US_born'].mean()
max_decade_usa= int(decade_USA.sort_values('US_born', ascending=False)['decade'].values[0])
print(max_decade_usa)


nobel['female_laureates']= nobel['sex']=='Female'
female_decade=nobel.groupby(['decade', 'category'], as_index=False)['female_laureates'].mean()
max_female_row=female_decade.sort_values('female_laureates', ascending=False).iloc[0]

max_female_dict={
 int(max_female_row['decade']): max_female_row['category']   
}
print(max_female_dict)

# filter nobel for female
female_nobel=nobel[nobel['female_laureates']==True].sort_values('year')
first_woman_name=female_nobel['full_name'].iloc[0]
first_woman_category= female_nobel['category'].iloc[0]
print(first_woman_name)
print(first_woman_category)

# get list of repeat winners
repeat_count = nobel['full_name'].value_counts()
repeat_list = list(repeat_count[repeat_count > 1].index)

print(repeat_list)