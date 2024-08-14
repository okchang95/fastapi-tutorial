# uvicorn src.main:app --host=0.0.0.0 --port=3000 --reload
# https://suloth.tistory.com/195
# 그냥 uvicorn main:app 으로 실행시키면, No module named 'src' 에러가 발생
from fastapi import FastAPI
from src.routers.index import index_router

# swagger 문서는 /docs 경로로, openapi 문서는 /open-api-docs 경로로 설정한다.
app = FastAPI(docs_url="/docs", openapi_url="/open-api-docs")


# /api라는 경로로 index_router를 붙인다.
"""
여기서는 APIRouter를 불러오지 않고 app자체에 include_router함수를 사용한다.
    app이라는 변수 = Fastapi 서버 
라고 보면 되는데, 
이 app에 router를 붙여줘야 서버에 연결되기 때문이다.

나는 /api 경로를 통해 index_router를 탈 수 있도록 해주었다.
"""
app.include_router(index_router, prefix="/api")


# / 라는 url로 GET 요청이 들어오면 getHello함수를 실행시키겠다.
"""
이제는 http://host:port/api/user/ 로 GET 요청이 들어온다면, 
user.py에 있는 getUser함수가 실행되면서 
사용자에게 "유저입니다." 라는 문자열을 리턴할 것이다
"""


@app.get("/")
async def getHello():
    return "Hello, World"
