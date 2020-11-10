import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# display first 10 rows
tips_df.head(10)

# find no. days per week that the restaurant is open
len(tips_df['day'].unique())

# find day of the week where there are more bills
tips_df['day'].value_counts()

# plot this with a Seaborn countplot
sns.countplot(data=tips_df, x='day', order=['Thur', 'Fri', 'Sat', 'Sun'])

# other countplots
# ...fix these
sns.countplot(data=tips_df, x='sex')
sns.countplot(data=tips_df, x='smoker')
sns.countplot(data=tips_df, x='time')

# plot the distribution of total_bill based on a given category
sns.catplot(data=tips_df, x='day', y='total_bill', kind="box")

# change the value of x with one of the categorical column of the dataset and the value of kind ("bar", "box", "violin", "boxen")
sns.catplot(data=tips_df, x='time', y='total_bill', kind="bar")

# change the value of y with one of the numerical column of the dataset
sns.catplot(data=tips_df, x='day', y='tip', kind="box")
