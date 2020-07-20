# Aitrics 코딩 테스트

## 1. 개발환경
- Language : Python 3.6 / Flask
- Database : MariaDB 10.1.44
- Tool : Visual-Studio-Code

## 2. DB 테이블 설계
```
/* 환자 정보 테이블 */
CREATE TABLE Patient(
    patient_code      INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    patient_name      VARCHAR(10) NOT NULL ,
    patient_age       VARCHAR(10) NOT NULL ,
    alert_info        VARCHAR(10) ,
    admission_date    datetime NOT NULL
) CHARSET=utf8;

```

```
/* 바이탈 정보 테이블 */
CREATE TABLE Vital_Info(
    patient_code     INT NOT NULL PRIMARY KEY,
    vital_code       VARCHAR(20),
    vital_name       VARCHAR(20),
    vital_value      INT(50),
    create_date       datetime NOT NULL
) CHARSET=utf8;
```

```
/* 알람 정보 테이블 */
CREATE TABLE Alert_Info(
    patient_code      INT NOT NULL PRIMARY KEY,
    alert_info        VARCHAR(10),
    period_date       datetime NOT NULL
) CHARSET=utf8;

```

## 3. REST API URI 설계
### ● http://localhost:5000/api/users  		 (GET)
### ● http://localhost:5000/api/users/:code  (GET)
