# post.py
# /user경로로 GET요청이 들어오면 "유저입니다" 출력

from fastapi import APIRouter

post_router = router = APIRouter()


@router.get("/")
async def getHelloPost():
    return "Hello, Post!"


# Param 예제
from typing import Optional

"""
Param은 Http Request를 보낼 때, 해당 요청에 대한 추가정보를 전달한다는 점에서 
Query와 비슷하다.

하지만 Param은 ?로 구분해서 전달하지 않고, 
/로 구분을 해서 전달한다는 점이 다르다. 
그리고 key-value 형식이 아니라 그냥 값만 적는다.

예를들어, http://127.0.0.1:3000/api/post/1 이라는 주소가 있다고 해보자. 
여기서 1은 param이다. 바로 앞의 녀석에 대한 부가 정보를 제공한다.

param은 리소스(user나 post같은 것들)에 대해 직접적인 연관이 있는 경우
(게시글 번호, 유저이름 등)는 param으로 적는 편이고,
 
부가적인 정보(user의 age나 height, weight 혹은 post의 작성자, author) 
같은 경우는 query로 적는 편입니다.

여기서 isArticle 매개변수에 = False 라는 기본 값을 넣어주면, 
isArticle 이라는 query가 없어도 자동으로 false가 들어간다.

또한 content의 경우 Optional으로 타입힌트를 주었기 때문에, 
content가 없으면 null 값이 들어간다. (null 값을 넣으려면 optional을 사용하자)

"""


# Param
@router.get("/{number}")
async def getPost(number: int, content: Optional[str] = None, isArticle: bool = False):
    return {
        "message": f"{number} 번째 포스트입니다.",
        "content": content,
        "isArticle": isArticle,
    }
