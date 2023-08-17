import glob
import pandas as pd
path="/Users/yukuan.song/Downloads/dataprocessing"

file_list = glob.glob(path + "/*.xlsx")
excl_list = []


for file in file_list:
    excl_list.append(pd.read_excel(file, names=["A", "B"]))

excl_merged = pd.DataFrame()

for excl_file in excl_list:
    excl_merged = excl_merged.append(excl_file, ignore_index=True)

df_above_negative32 = excl_merged[excl_merged['A'] < -32]
df_32_20 = excl_merged[(excl_merged['A'] > -32) & (excl_merged['A'] <= -20)]
df_20_0 = excl_merged[(excl_merged['A'] > -20) & (excl_merged['A'] <= 0)]
df_32_0 = excl_merged[(excl_merged['A'] > -32) & (excl_merged['A'] <= 0)]

print(df_32_0)

print('------ normal correlation -------------')
print(excl_merged.corr())
print('------ correlation < -32 -------------')
print(df_above_negative32.corr(method='pearson'))
print('------- correlation -20 >= data > -32 ')
print(df_32_20.corr(method='pearson'))
print('------- correlation 0 >= data > -20 ')
print(df_20_0.corr(method='pearson'))

print('------- correlation 0 >= data > -32 ')
print(df_32_0.corr(method='pearson'))