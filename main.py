import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('seaborn-v0_8-deep')

df = pd.read_csv('shopping_behavior_updated.csv')
df_clothes = df[df['Category'] == 'Clothing']

