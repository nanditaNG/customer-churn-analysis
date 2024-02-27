import pandas as pd

churn_data = pd.read_csv('Customer-Churn-Records.csv')
df = pd.DataFrame(churn_data)

# counting the unique number of Customer Ids in the data set
distinct_ids = len(pd.unique(df['CustomerId']))
print("Number of unique values:", distinct_ids)