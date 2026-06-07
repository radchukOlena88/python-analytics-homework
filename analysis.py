import pandas as pd
from numpy.ma.extras import average

data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print(df)
average_sales = df['sales'].mean()
print('Середнє значення:', average_sales)
print("Це середній рівень продажу по трьох містах")
