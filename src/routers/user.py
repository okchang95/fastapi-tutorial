# user.py
# /user경로로 GET요청이 들어오면 "유저입니다" 출력

from fastapi import APIRouter

"""
APIRouter: fastapi에서 url을 연결해주는 라이브러리

데코레이터(@): 뭘 꾸며줌..

@router.get("/")
async def getUser():
    return "유저입니다."

여기서 @router.get("/")은 바로 아래의 getUser() 함수를 꾸며줌
    = GET요청이 "/"경로로 들어오면 getUser() 함수를 실행 

그리고 getUser()가 실행되면 "유저입니다."를 반환

현재까지는 FastAPI에 적용되지 않고 따로놀고있음
=> 이 연결을 위해 다음 함수 사용
```app.include_router(router, prefix=prefix) 또는 router.include_router```
"""

user_router = router = APIRouter()


# @router.get("/")
# async def getUser():
#     return "유저입니다."


# Query: Fastapi의 경우에 함수에 인자(매개변수)를 넣어주면 자동적으로 query로 인식
@router.get("/")
async def getUser(nickname: str, age: int):
    return {"nickname": nickname, "age": age}


# Body,,,
"""
body는 Post나 Put, Patch 요청을 보낼 때 함께 보낼 수 있다.
Post는 생성 요청 
Put, Patch는 수정 요청이다.

생성, 수정에는 많은 정보가 필요하기 때문에 Request Body를 따로 추가하여 전달한다.

Fastapi에서는 pydantic 패키지를 사용하여 Body를 전달받고, validation할 수 있다.
    validation이란 "검사"라는 뜻으로, 
    Request body에 담긴 형식이 서버에서 원하는 형식과 동일한지 검증하는 과정을 말한다.

예를들면, 서버에서는 유저를 생성해달라는 요청을 받을 때,
name, age, height를 필요로 하는데 
Request body에는 name과 age만 담긴 경우, 
validation이 통과되지 못하고 해당 요청은 거부된다.

하지만 해당 강의에서는 DB와 연동은 하지 않을 예정이기 때문에 
일단 body에 전달한 요청을 약간 가공하여 리턴하는 함수를 만들어 보자.

먼저, user.py 파일로 가서 다음과 같은 함수를 작성해보자
"""
from pydantic import BaseModel


# Body의 타입을 정의한다.
class CreatePostBodyDto(BaseModel):
    name: str
    age: int
    height: int


@router.post("/")
async def createUser(body: CreatePostBodyDto):

    name = body.name
    age = body.age
    height = body.height

    processed_age = f"{age}살"
    processed_height = f"{height}cm"
    """
    브라우저에서 post요청할 때 요청 body에 입력할 조건을 주고, 
    그 조건을 만족할 경우(pydantic validation) return을 json으로 
    브라우저에 보내줌
    """
    return {"name": name, "age": processed_age, "height": processed_height}


"""
이번 과제는 http://127.0.0.1:8000/api/user 경로로 Post 요청을 날리면, 

    Param으로 username을 받게끔 하고,
    Query로 age를 받게끔하자.

그리고 Body로는 height와 weight를 받아서 이를 리턴하는 함수를 만들자.

ex) Post http://127.0.0.1:3000/api/user/suloth?age=20
Request body : { height: 170, weight: 60 }
으로 요청을 보내면

리턴 값 : { username: "suloth", age: 20, height: "170cm", weight: "60kg" }
을 리턴하게 만들면 된다
# """


class CreateUserByUsernameBodyDto(BaseModel):
    height: int
    weight: int


@router.post("/{username}")
async def test(body: CreateUserByUsernameBodyDto, username: str, age: int):

    height = body.height
    weight = body.weight

    processed_height = f"{height}cm"
    processed_weight = f"{weight}kg"

    return {
        "username": username,
        "age": age,
        "height": processed_height,
        "weight": processed_weight,
    }
