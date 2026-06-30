import pandas as pd

# 读取CSV文件
df = pd.read_csv('all_fng_csv4.csv')

# 获取B列从第100行到1000行的数据，且值不为0 3286:4920
b_column_values = df.iloc[3286:, 1].values
b_column_values = [round(value, 2) for value in b_column_values if value != 0]

# 将数据按照每20个数一行打印，以逗号分隔，每行开头有两个空格
for i in range(0, len(b_column_values), 20):
    line = ','.join(map(str, b_column_values[i:i+20])) + ','
    print('  ' + line)