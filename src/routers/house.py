from fastapi import APIRouter
from pydantic import BaseModel
from src.services.house import runModel

house_router = router = APIRouter()

"""
@router.post 함수를 통해 url 경로를 붙여주고, 
services/house.py에서 runModel 함수를 불러와서 모델을 돌린 결과를 리턴하도록 한다.

그리고 routers/index.py 파일에 house_router만 붙여주면 끝이다.
"""


@router.get("/price/predict")  # post -> get
async def getPredictionOfHousePrice(crim: float, room: float):
    price = await runModel(crim, room)
    processed_price = str(round(price[0], 3)).replace(".", ",")
    processed_price = f"{processed_price} 달러"

    return processed_price


##########################################################

# runModel2도 불러와주자.
from src.services.house import runModel2

# dtos/house.py 경로에서 정의한 Body 타입을 가진 class를 불러온다.
from src.dtos.house import GetPredictionOfHousePrice2BodyDto

house_router = router = APIRouter()


# 추가된 코드. post 요청으로 model을 돌린다.
@router.post("/price/predict")
# body인자로 아까 만들었던 Dto class를 설정해준다.
async def getPredictionOfHousePrice2(body: GetPredictionOfHousePrice2BodyDto):
    price = await runModel2(body)
    processed_price = str(round(price[0], 3)).replace(".", ",")
    processed_price = f"{processed_price} 달러"

    return processed_price
