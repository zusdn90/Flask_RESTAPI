# Flask REST API 서버 

## 1. 개발환경
- Language : Python 3.6 / Flask
- Database : MariaDB 10.1.44
- Tool : Visual-Studio-Code

## 2. DB 테이블 설계
```
/* 사원 정보 테이블 */
CREATE TABLE Employee(    
    employee_code        VARCHAR(50) PRIMARY KEY NOT NULL,   /* 사원 코드 */ --PK
    employee_name        VARCHAR(50) NOT NULL ,              /* 사원 이름 */
    address         	 VARCHAR(50) ,                       /* 주소 */	
	salary         	     INT(100) ,                       	 /* 연봉 */	
	phone_number         VARCHAR(50) ,                       /* 전화번호 */	
    date                 datetime NOT NULL                   /* 입사날짜 */    
) CHARSET=utf8;

```

```
/* 직원의 직급 정보 테이블 */
CREATE TABLE Rank(    
    rank_code       VARCHAR(20) NOT NULL PRIMARY KEY,  /* 직급 코드 */ --PK
	employee_code   VARCHAR(20) NOT NULL,			   /* 사원 코드 */ -- FK
    rank_name       VARCHAR(20)                        /* 직급 이름 */
) CHARSET=utf8;
```

```
/* 부서 정보 테이블 */
CREATE TABLE Department(
    dept_code      	VARCHAR(30) NOT NULL,     /* 부서코드 */ --PK
	employee_code	VARCHAR(20) NOT NULL,	  /* 사원코드 */ -- FK
    dept_name        VARCHAR(20),              /* 부서명 */    
) CHARSET=utf8;

```

```
/* 직급 정보 테이블 */
CREATE TABLE Rank(    
    rank_code       VARCHAR(20) NOT NULL PRIMARY KEY,  /* 직급 코드 */	--PK
    rank_name       VARCHAR(20)                        /* 직급 이름 */
) CHARSET=utf8;
```

## 3. REST API URI 설계
### ● http://localhost:5000/api/v01/database/create (POST) -데이터 생성
### ● http://localhost:5000/api/v01/insert          (POST) -데이터 저장

### ● http://localhost:5000/api/v01/users  		 (GET)    -유저 전체 리스트 조회
### ● http://localhost:5000/api/v01/users        (POST)   -회원가입
### ● http://localhost:5000/api/v01/users/id    (PUT)    -유저 정보 업데이트
### ● http://localhost:5000/api/v01/users/id    (DELETE) -유저 삭제

## 4. Data 생성
### ● python faker 라이브러리 사용

## 5. Test
### ● pytest라이브러리로 unit test

