import pandas as pd
import lightgbm as lgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# read Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# deal with outlier
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# feature engineering
features = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
df = df[features + ["Survived"]]

# Label encoding
encoder = LabelEncoder()
df["Sex"] = encoder.fit_transform(df["Sex"])
df["Embarked"] = encoder.fit_transform(df["Embarked"])


X = df[features]
y = df["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train LightGBM model
train_data = lgb.Dataset(X_train, label=y_train)
params = {"objective": "binary", "metric": "binary_logloss"}
model = lgb.train(params, train_data, num_boost_round=100)

# save model
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "encoder.pkl")

print("model training complete!!")