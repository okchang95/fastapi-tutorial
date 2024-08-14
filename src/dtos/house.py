# Dto는 Data Transfer Object라는 뜻이다. 그냥 타입 정의했다고 생각
from pydantic import BaseModel


# router에 만들 예정인 getPredictionOfHousePrice2 에 대한 Body Dto 라는 뜻을 가진 class
# body의 타입으로 사용할 예정
class GetPredictionOfHousePrice2BodyDto(BaseModel):
    crim: float
    zn: float
    indus: float
    chas: int
    nox: float
    room: float
    age: float
    dis: float
    rad: int
    tax: float
    ptratio: float
    b: float
    lstat: float
