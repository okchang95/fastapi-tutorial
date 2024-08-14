# index.py
# index.py: 모든 router를 모아놓은 파일
"""
주의할 점은 user_router를 import할 때, 절대경로를 사용하는데, 
from절에서 src파일부터 시작해야된다는 것이다.

"상대경로"를 사용하거나 "src부터 시작"하지 않으면 경로를 찾을 수 없다며 에러를 뱉는다.

아래 코드를 해석하자면,

나는 APIRouter를 불러와서 router 변수에 저장할건데,
APIRouter에 있는 router.include_router 함수를 사용해서 
아까 만든 user.py파일에 있는 user_router를 불러와서 
"/user" 경로로 이어 붙일 거야. 

라는 뜻이다.

== index.py가 user라는 경로를 통해서 user.py에 있는 user_router를 붙여주었다

이걸로 index.py, user.py 두개가 연결

GET /user/ 라는 url로 user.py의 getUser() 함수를 실행시킬 수 있음

이제 Fastapi 서버와 index.py를 연결하기만 하면 된다. 

    (index.py는 Router들을 모아놓는 파일이기 때문에 user.py와 main.py를 매개한다. 
    귀찮으면 main.py에서 바로 app.include_router 함수를 사용해서 
    user_router를 붙여줘도 된다.)

main.py로 가서 index_router를 연결해주자.
"""

from fastapi import APIRouter
from src.routers.user import user_router
from src.routers.post import post_router
from src.routers.house import house_router

index_router = router = APIRouter()

# router 클래스에 라우팅 추가
router.include_router(user_router, prefix="/user")
router.include_router(post_router, prefix="/post")
router.include_router(house_router, prefix="/house")
