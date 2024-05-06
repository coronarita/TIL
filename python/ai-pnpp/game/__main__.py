# 폴더 자체를 실행하려고(상위폴더에서)

from sound import echo

if __name__ == '__main__':
    print("Hello Game")
    print(echo.echo_play()) # 다른 폴더에 있는 여러 모듈, 함수도 불러올 수 있다. 