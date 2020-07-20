# Aitrics 코딩 테스트

## 1. 개발환경
- Language : Python 3.6 / Flask
- Database : MariaDB 10.1.44
- Tool : Visual-Studio-Code

## 2. DB 테이블 설계
```
/* 환자 정보 테이블 */
CREATE TABLE Patient(
    patient_code      INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  /* 환자코드 */
    patient_name      VARCHAR(10) NOT NULL ,                    /* 환자이름 */
    vital_code        VARCHAR(20) ,                             /* 바이탈 코드 */
    vital_value       INT(50) ,                                 /* 바이탈 수치 */
    alert_info        VARCHAR(20) ,                             /* 환자 알람 정보 */
    admission_date    datetime NOT NULL                         /* 입원 날짜 */    
) CHARSET=utf8;

```

```
/* 바이탈 정보 테이블 */
CREATE TABLE Vital_Info(    
    vital_code       VARCHAR(20) NOT NULL PRIMARY KEY,  /* 바이탈 코드 */
    vital_name       VARCHAR(20)                       /* 바이탈 이름 */
) CHARSET=utf8;
```

```
/* 환자 알람 발생 정보 테이블 */
CREATE TABLE Paient_Alert_Info(
    patient_code      INT NOT NULL PRIMARY KEY, /* 환자코드 */
    alert_info        VARCHAR(20),              /* 환자 알람 정보 */
    create_date       datetime NOT NULL         /* 알람 발생 날짜 */    
) CHARSET=utf8;

```

## 3. REST API URI 설계
### ● http://localhost:5000/api/users  		 (GET)
### ● http://localhost:5000/api/users/:code  (GET)
