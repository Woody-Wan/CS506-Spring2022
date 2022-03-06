df.replace('male',1) # use 1 to replace 'male'
df.fillna() # replace the nans 
df.mean(axis=) #caculate the mean axixs=0 for row;
df.str.extract(regex, expand=False) regex:Regular Expression
df.groupby('Survived')['Age'].mean() # caculate the means of age for variable 'survived'
by_Survived.plot(kind ='bar')
df.boxplot(column='Fare',by='Survived', showfliers=False) # boxplot: y->Fare; x->Survived
df = df.select_dtypes(['number']) # remove all non-numerical columns from datafram
df.to_csv(path,head=1,index=0) # head=1 means showing the name of columns, index =0 means not show indexs
df.rename(columns={'volumeInfo.title':'Title','volumeInfo.authors':'Authors'})
# use Title and Authors to replace volumeInfo.title and volumeInfo,authors
df.loc[data['S'].str.contains('A')] # return all rows whose 'S' contain 'A', we can also apply regular expression here

