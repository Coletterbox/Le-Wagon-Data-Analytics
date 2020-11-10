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

# plot this with a Seaborn Countplot
sns.countplot(data=tips_df, x='day', order=['Thur', 'Fri', 'Sat', 'Sun'])
