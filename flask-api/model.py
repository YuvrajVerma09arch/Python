import joblib
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
print("Brain LOCKED in")
df=pd.read_csv('flowers.csv')

print('Brain Loaded')
print(df.head())

x=df[['sepal_length','sepal_width','petal_length','petal_width','color_code','has_thorns']]
y=df['species_label']

model=KNeighborsClassifier(n_neighbors=1)
model.fit(x,y)
print('BRAINED')

joblib.dump(model,'flower_model.joblib')
print('BRAIN saved to flower_model.joblib')