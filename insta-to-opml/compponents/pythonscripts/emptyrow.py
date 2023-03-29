import pandas as pd
df = pd.read_csv('/Users/lucytiffen/pythonscripts/following.csv')
df.to_csv('/Users/lucytiffen/pythonscripts/following.csv', index=False)