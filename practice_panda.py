import pandas as pd

data = pd.read_csv('data.csv')
print(data)
print(data.loc[50])
# print(data.to_string())
print(data.info())

array = [1,2,5]
series = pd.Series(array, index=[1,2,3])
print(series[3])
print(series)

data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

dataframe = pd.DataFrame(data2)
print(dataframe)

cleaned_df = data.dropna()
print(cleaned_df.info())
data['Date'] = pd.to_datetime(data['Date'])