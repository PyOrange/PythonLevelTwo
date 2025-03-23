import pendulum
from datetime import datetime

# 모든 타임존 출력
timezones = pendulum.timezones
print(timezones)

# 복수의 타임존 객체로 리스트 만들기
timezone_list = []
timezone_list.append(pendulum.timezone('UTC'))
timezone_list.append(pendulum.timezone('Asia/Seoul'))
timezone_list.append(pendulum.timezone('Asia/Shanghai'))
timezone_list.append(pendulum.timezone('America/New_York'))
timezone_list.append(pendulum.timezone('America/Los_Angeles'))
timezone_list.append(pendulum.timezone('Indian/Maldives'))

# 각 리스트의 타임존 객체로 현재 시간 출력하기
for timezone in timezone_list:
    current_time = datetime.now(timezone)
    print(current_time)
    