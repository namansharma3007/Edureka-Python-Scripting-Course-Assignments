import pandas as pd

path = "C:/Users/naman/Desktop/Edureka Python/assignment4/{name}"

path1 = path.format(name = "DSScoreTerm1.csv")
path2 = path.format(name = "MathScoreTerm1.csv")
path3 = path.format(name = "PhysicsScoreTerm1.csv")

ds_score_data = pd.read_csv(path1)
print(ds_score_data)

math_score_data = pd.read_csv(path2)
print(math_score_data)

physics_score_data = pd.read_csv(path3)
print(physics_score_data)


ds_score_data.drop('Ethinicity',inplace=True,axis=1)
math_score_data.drop('Ethinicity',inplace=True,axis=1)
physics_score_data.drop('Ethinicity',inplace=True,axis=1)

print(ds_score_data)
print(math_score_data)
print(physics_score_data)
ds_score_data.to_csv(path1,index=False)
math_score_data.to_csv(path2,index=False)
physics_score_data.to_csv(path3,index=False)


ds_score_data.replace(r'^\s*$', 0, regex=True)
math_score_data.replace(r'^\s*$', 0, regex=True)
physics_score_data.replace(r'^\s*$', 0, regex=True)


newMergedFile = pd.concat(map(pd.read_csv,[path1,path2,path3]),ignore_index=True)
print(newMergedFile)

newMergedFile.to_csv("newMergedFile.csv",index=False)

newMergedFile['Sex'] = newMergedFile['Sex'].replace({'M':1})
newMergedFile['Sex'] = newMergedFile['Sex'].replace({'F':0})

newMergedFile.to_csv('ScoreFinal.csv',index=False)