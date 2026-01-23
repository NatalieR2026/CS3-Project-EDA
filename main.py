import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('seaborn-v0_8-ticks')
# print(plt.style.available)

# Graph 1: Is there a correlation between seasons and clothing item purchased?

df = pd.read_csv('shopping_behavior_updated.csv')
df_clothes = df[df['Category'] == 'Clothing']

pivot_df = df_clothes.pivot_table(index='Season', columns='Item Purchased', values='Customer ID', aggfunc='count', fill_value=0)

pivot_df.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Clothing Items by Season')
plt.xlabel('Season')
plt.ylabel('Amount')
plt.legend(title='Item Purchased')
plt.savefig('stacked_bar_clothes.png', bbox_inches='tight')

# Graph 2: more specific

