import numpy as np
import pandas as pd
import os

data = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
data = data.iloc[:, 3:]
data.drop(columns=['Avg. Session Length'],inplace=True)


data = data[data['Length of Membership'] > 1]
data.to_csv(os.path.join('data', 'customer.csv'))
