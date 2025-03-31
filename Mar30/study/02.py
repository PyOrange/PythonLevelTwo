
# 비동기 I/O 코루틴 작업
# Generator -> 반복적인 객체 Return 사용
# Asyncio 웹 스크랩핑 실습
# Beautiful Soup : HTML과 XML 데이터를 쉽게 관리할 수 있는 파이썬 라이브러리
# 스케쥴러 사용시 주기적으로 데이터 수집 가능
# 수집 정보 DB 저장 : 파이썬 기초 강의 참고


import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 실행 시작 시간
start = timeit.default_timer()
# 웹사이트로 실습 
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://www.inflearn.com/']


async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    
    soup = BeautifulSoup(res.read(), 'html.parser')
    
    # 페이지 타이틀 정보 수집
    result_data = soup.title

    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return result_data

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    
    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료 까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)