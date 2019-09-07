import pandas as pd
df = pd.read_csv('mtcars')

X = df.mpg.values
X=X.reshape(-1,1)
y1 = df.wt.values
y1=y1.reshape(-1,1)
y2 = df.hp.values
y2=y2.reshape(-1,1)

import statsmodels.api as sm

#weight vs mpg
model1 = sm.OLS(y1, X).fit()
predictions1 = model1.predict(X)
predictions1
model1.summary()

#horsepower vs mpg
model2 = sm.OLS(y2, X).fit()
predictions2 = model2.predict(X)
predictions2
model2.summary()

