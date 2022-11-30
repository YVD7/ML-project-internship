
# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# reading source file
df = pd.read_csv('/home/yash/project/ineuron_internship_projects/ML-project-internship/Concrete_file_path/concrete_data.csv')

# converting into dataframe
df = pd.DataFrame(df)

df

df.info # checking info

df.isna().sum() # checking if their is any null value or not

col = df.columns.to_list() # checking for list of columns
col

# plotting histogram
df.hist(figsize=(15,20),color='green')
# plt.show()

# Now creating boxplot to if any outliers exists or not
i = 1
plt.figure(figsize=(15,20))
for col in df.columns:
    plt.subplot(4,3,i)
    sns.boxplot(x = df[col], data = df)
    i+=1


# BRAVIATE ANALYSIS

i = 1

plt.figure(figsize=(18,18))
for col in df.columns:
    plt.subplot(4,3,i)
    sns.scatterplot(data=df, x='concrete_compressive_strength',y=col)
    i+=1

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),linewidths=1,cmap='PuBuGn_r',annot=True)

correlation = df.corr()['concrete_compressive_strength'].sort_values()
correlation.plot(kind='barh',color='green')

df.to_csv('/home/yash/project/ineuron_internship_projects/ML-project-internship/Concrete_file_path/Preprocessing_Data.csv')