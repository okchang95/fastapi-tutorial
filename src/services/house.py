from typing import List
import xgboost as xgb
import pandas as pd

# XGBRegressor 모델을 불러온다.
loaded_model = xgb.XGBRegressor()

# colab에서 학습시킨 모델의 가중치 파일을 불러와서 모델에 적용시킨다.
loaded_model.load_model("src/models/xgb_model.json")


async def runModel(crim: float, room: float) -> List[float]:

    # 미리 준비된 input 데이터(임시). 나중에는 Http Request에 담아서 보낼 것이다.
    # 여기서 CRIM과 RM을 사용자로부터 입력을 받아서 집 값을 예측
    # CRIM과 RM에 각각 crim과 room 변수를 넣어준다.
    # CRIM = 범죄율, ROOM = 방 개수

    dic = {
        "CRIM": [crim],
        "ZN": [18.0],
        "INDUS": [22.37],
        "CHAS": [0],
        "NOX": [0.145],
        "RM": [room],
        "AGE": [66.7],
        "DIS": [4.291],
        "RAD": [13],
        "TAX": [333.333],
        "PTRATIO": [21.0],
        "B": [197.6],
        "LSTAT": [23.4],
    }

    # dictionary 형태를 DataFrame 형태로 변환한다.
    input = pd.DataFrame.from_dict(dic, orient="columns")

    # input 값을 이용해서 예측값을 만들고, z에 대입한다.
    z = loaded_model.predict(input)

    # 변수 z의 타입이 numpy이기 때문에 list로 바꿔준다.
    result: List[float] = z.tolist()

    return result


# 추가: runModel2
from src.dtos.house import GetPredictionOfHousePrice2BodyDto


async def runModel2(input: GetPredictionOfHousePrice2BodyDto) -> List[float]:

    dic = {
        "CRIM": [input.crim],
        "ZN": [input.zn],
        "INDUS": [input.indus],
        "CHAS": [input.chas],
        "NOX": [input.nox],
        "RM": [input.room],
        "AGE": [input.age],
        "DIS": [input.dis],
        "RAD": [input.rad],
        "TAX": [input.tax],
        "PTRATIO": [input.ptratio],
        "B": [input.b],
        "LSTAT": [input.lstat],
    }

    # dictionary 형태를 DataFrame 형태로 변환한다.
    input = pd.DataFrame.from_dict(dic, orient="columns")

    # input 값을 이용해서 예측값을 만들고, z에 대입한다.
    z = loaded_model.predict(input)

    # 변수 z의 타입이 numpy이기 때문에 list로 바꿔준다.
    result: List[float] = z.tolist()

    return result
