# 주석에 대해서는 잘 이해가 안갈수도 있지만, 그냥 아~ 그렇구나라고 생각만하자.

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np


# Boston 집 값 관련 데이터 로드. 해당 데이터로 모델을 학습할 예정이다.
boston = fetch_openml(name="boston")

# 데이터를 불러와서, column을 feature names로 두고, DataFrame 형식으로 저장한다.
df = pd.DataFrame(boston.data, columns=boston.feature_names)

# MEDV는 집 값이다.
df["MEDV"] = boston.target

# CHAS와 RAD는 str로 불러와지기 때문에 int타입으로 형변환 시켜준다.
df["CHAS"] = df["CHAS"].astype("int")
df["RAD"] = df["RAD"].astype("int")

# df에 존재하는 MEDV(집 값) column을 제거하여 X에 대입한다. (예측 되는 집 값은 y 값으로 쓸 것이기 때문)
X = df.drop("MEDV", axis=1)

# y에 MEDV(집 값)을 대입한다.
y = df["MEDV"]

# 데이터 분할. 테스트를 위한 데이터와 학습을 위한 데이터를 분할한다. 비율은 8:2 (train:test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 생성
model = xgb.XGBRegressor(
    objective="reg:squarederror",
    colsample_bytree=0.3,
    learning_rate=0.1,
    max_depth=5,
    alpha=10,
    n_estimators=10,
)

# 모델 학습
model.fit(X_train._get_numeric_data(), np.ravel(y_train, order="C"))

# 모델 저장. xgb_model.json 이라는 이름으로 모델을 저장한다.
model.save_model("xgb_model.json")


# 새 모델 인스턴스 생성 및 모델 로드
loaded_model = xgb.XGBRegressor()
loaded_model.load_model("xgb_model.json")
print("-------------------------")

# 예측
y_pred = loaded_model.predict(X_test)

# 평가. 값이 0에 가까울 수록 정확하다는 뜻이다...!
rmse = mean_squared_error(y_test, y_pred, squared=False)
print("RMSE: %.2f" % rmse)
