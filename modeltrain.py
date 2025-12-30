from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("cleandata.csv")

X = df[['age', 'study_hours', 'attendance', 'previous_score']]
y = df['result']

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=9)

model = LogisticRegression()
model.fit(x_train,y_train)

pre = model.predict(x_test)
score = accuracy_score(y_test,pre)
print("accuracy : ",score*100)
print(df['result'].value_counts())
ag = float(input("Enter Your Age : "))
st = float(input("Enter Your Study Hours : "))
at = float(input("Enter Your Attendance : "))
ps = float(input("Enter Your Previous Score : "))

result = model.predict([[ag,st,at,ps]])[0]


if result == 1 :
    print("U Are Pass :)")
    
else:
    print("Sorry U Are Faile :(")