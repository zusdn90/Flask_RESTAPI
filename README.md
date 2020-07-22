# Aitrics 코딩 테스트

## 1. 개발환경
- Language : Python 3.6 / Flask
- Database : MariaDB 10.1.44
- Tool : Visual-Studio-Code

## 2. DB 테이블 설계
```
/* 환자 정보 테이블 */
CREATE TABLE Patient(    
    patient_code            VARCHAR(50) PRIMARY KEY NOT NULL,   /* 환자코드 */
    patient_name            VARCHAR(50) NOT NULL ,              /* 환자이름 */
    vital_code              VARCHAR(20) ,                       /* 바이탈 코드 */
    vital_value             INT(50) ,                           /* 바이탈 수치 */
    alert_info              VARCHAR(20) ,                       /* 환자 알람 정보 */
    date                    datetime NOT NULL                   /* 입원 날짜 */    
) CHARSET=utf8;

```

```
/* 바이탈 정보 테이블 */
CREATE TABLE Vital_Info(    
    vital_code       VARCHAR(20) NOT NULL PRIMARY KEY,  /* 바이탈 코드 */
    vital_name       VARCHAR(20)                        /* 바이탈 이름 */
) CHARSET=utf8;
```

```
/* 환자 알람 발생 정보 테이블 */
CREATE TABLE Paient_Alert_Info(
    patient_code      VARCHAR(30) NOT NULL,     /* 환자코드 */
    alert_info        VARCHAR(20),              /* 환자 알람 정보 */
    create_date       datetime NOT NULL         /* 알람 발생 날짜 */    
) CHARSET=utf8;

```

## 3. REST API URI 설계
### ● http://localhost:5000/api/v01/database/create (POST) -데이터 생성
### ● http://localhost:5000/api/v01/insert          (POST) -데이터 저장

### ● http://localhost:5000/api/v01/users  		 (GET)    -입원 환자 전체 리스트 조회
### ● http://localhost:5000/api/v01/users/date  (GET)    -특정기간 내 인원 환자 리스트 조회
### ● http://localhost:5000/api/v01/users        (POST)   -입원환자 추가
### ● http://localhost:5000/api/v01/users/id    (PUT)    -입원환자 정보 업데이트
### ● http://localhost:5000/api/v01/users/id    (DELETE) -입원환자 삭제

## 4. Data 생성
### ● python faker 라이브러리 사용

## 5. Test
### ● pytest라이브러리로 unit test

