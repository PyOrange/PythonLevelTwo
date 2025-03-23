# 패키지 설치 명령어 : pip install <패키지명>
import pendulum
from datetime import datetime

# 타임존 객체 설정
pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

print(type(pst))
print(type(ist))

# 타임존 시간 출력
print('Current Date Time in PST =', datetime.now(pst))
print('Current Date Time in IST =', datetime.now(ist))
