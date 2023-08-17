import pandas as pd

df = pd.read_excel('hitlist1.xlsx', sep='\t', names=['A', 'B'])
df_above_negative32 = df[df['A']<-32]
#print(df.corr(method='pearson'))
print(df_above_negative32)
print(df_above_negative32.corr(method='pearson'))
