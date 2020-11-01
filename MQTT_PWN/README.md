# Namki Project - Internet of Things
[MQTT 프로젝트 관련 자료 모음 ]

docker 브로커 설치
Docker 설치 URL :  https://docs.docker.com/install/

# 이미지 빌드
cd {디렉터리}
docker build -t {이름 명} .

# 브로커 컨테이너 실행
docker run -p 1883 : 1883 {이름}

#mqtt-pwn
URL : https://mqtt-pwn.readthedocs.io/en/latest/intro.html

#mqtt-pwn 명령 소개

# 사용자 이름 / 암호 인증을 사용하여 호스트에 연결
connect -o 0.0.0.0 -p 1883 USERPASS -u <username> -w <password>

# 10 초 동안 패킷 수신
discovery -t 10

# 브로커에 대한 정보를 출력
system_info

# 완료되었거나 진행중인 스캔 목록
scans

# 스캔 선택 1
scans -i 1

# 목록 주제
topics

# 주제에 "sensor"가 포함 된 메시지 나열
messages -tr sensor

# ID 107로 메시지 인쇄
messages -i107

# CSV 형식으로 메시지 내보내기
messages -e

#테스트 도구 사용법
Python3 필요하며, 권장 가상 환경은 pipenv, venv 추천.

# 여기서 pipenv를 사용하면 pip (venv 포함 또는 제외)를 사용할 수도 있습니다.
pipenv install -r requirements.txt
퍼징을 위해 radamsa 설치 : https://gitlab.com/akihe/radamsa

MQTT 패킷을 퍼징 하려면 'MQTT_fuzz-master' 디렉터리의 스크립트 사용

cd MQTT_PWN
파이썬 mqtt_logger.py --help
메시지를 보내고 선택적으로 일부 스트레스 테스트 및 퍼징 (페이로드에만 해당)을 수행하려면 인젝터를 사용하십시오.

cd MQTT_PWN
python mqtt_injector.py --help
MQTT 패킷을 퍼징하려면 mqtt_fuzz를 사용.


# MQTT CVE
https://www.cvedetails.com/vulnerability-list/vendor_id-10410/product_id-45945/Eclipse-Mosquitto.html