import pandas as pd
import numpy as np
import glob

path = #r'PATH\TO\Datasets'
writePath = #r'PATH\TO\processed.txt' 
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df.drop(['AuthorID', 'Date', 'Attachments', 'Reactions'], axis=1, inplace=True)

user = #USERNAME GOES HERE e.g. Discord#1234  

new_df = pd.DataFrame()
newest_df = pd.DataFrame()
new_df['Input'] = df.loc[(df['Author'].shift(-1) == user) & (df['Author'] != user), 'Content'].reset_index(drop=True)
new_df['Output'] = df.loc[(df['Author'].shift(-1) != user) & (df['Author'] == user), 'Content'].reset_index(drop=True)
new_df.insert(0, 'Start', '<|startoftext|>')
new_df.insert(3, 'End', '<|endoftext|>')
new_df.fillna('(image)',inplace=True)
new_df.replace(to_replace = 'https:\/\/cdn\.discordapp.com\/attachments.*', value = '(image)', regex=True, inplace=True)
new_df.replace(to_replace = 'http\S+', value = '(link)', regex=True, inplace=True)
new_df.replace(to_replace = ':.+:', value = '(emoji)', regex=True, inplace=True)

new_df['Input'] = 'YOU:' + new_df['Input'].astype(str)
new_df['Output'] = 'ME:' + new_df['Output'].astype(str)


np.savetxt(writePath, new_df.values, fmt='%s', delimiter='\n', encoding='utf-8')
