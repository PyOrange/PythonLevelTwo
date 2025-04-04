
# 비동기 실행 : 여러 작업을 동시에 실행 가능
# futures(동시성) : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# 지연시간 CPU 및 리소스 낭비 방지 -> (File)Network I/O 관련 작업 -> 동시성 활용 권장
# 적합한 프로그램일 경우 압도적으로 성능 향상
# 1. 멀티스레딩/멀티프로세싱 API 통일 -> 매우 사용하기 쉬움
# 2. 실행중이 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백추가, 동기화 코드 매우 쉽게 작성 가능


# GIL : 복수의 스레드가 동시에 실행 될 때 하나의 자원을 엑세스 하는 경우 -> 문제점을 방지하기 위해 사용
#       GIL 실행 , 리소스 전체에 락이 걸림

# GIL : 멀티프로세싱 사용, CPython

import time
from concurrent import futures

WORK_LIST = [100000, 1000000, 10000000, 10000000]

# 예시
# 누적 합산 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # 시작 시간
    start_tm = time.time()
    # 결과 건수
    # ProcessPoolExecutor : 어떤 반복작업 탈출
    with futures.ThreadPoolExecutor() as executor:
        # map -> 작업 순서 유지, 즉시 실행
        result = executor.map(sum_generator, WORK_LIST)
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 형식
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))
    
    import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

WORK_LIST = [10000, 100000, 1000000, 10000000]


# 예시
# 수를 계속 누적시키며 더하는 클래스(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait : 비동기 작업이 끝날 때까지 기다리기
# as_completed : 현재 진행중인 또는 진행된 작업의 여러가지 상태 
def main():
    
    # 시작 시간
    start_tm = time.time()
    # Futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor : 어떤 반복작업 탈출
    with ThreadPoolExecutor() as executor:
        for work in WORK_LIST:
            # future 반환
            future = executor.submit(sum_generator, work)
            # 일 맡기기기
            futures_list.append(future)
            # 일 맡긴거 확인
            print('Scheduled for {} : {}'.format(work, future))
            # print()
        
        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled
            
            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))
        
        
            
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포멧
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm))

# 실행
if __name__ == '__main__':
    main()