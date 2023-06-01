import pandas as pd

import fifthChart
import firstChart
import fourthChart
import secondChart
import thirdChart

df = pd.read_csv('data1.csv')

firstChart.create_first_chart(df)
secondChart.create_second_chart(df)
thirdChart.create_third_chart(df)
fourthChart.create_fourth_chart(df)
fifthChart.create_fifth_chart(df)
fifthChart.create_sixth_chart(df)
fifthChart.create_seventh_chart(df)
