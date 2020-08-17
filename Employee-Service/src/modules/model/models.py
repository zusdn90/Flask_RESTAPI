import datetime

from server import app as mainApp
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy(app=mainApp)

# 사원 정보 테애블
class Employee(db.Model):
    column = ['employee_code', 'employee_name','dept_code','rank_code', 'address', 'salary', 'phone_number', 'date']
    employee_code = Column(db.String(50), primary_key=True)
    employee_name = Column(db.String(50), nullable=False, default='')
    dept_code = Column(db.String(50), nullable=False, default='')
    rank_code = Column(db.String(50), nullable=False, default='')
    address = Column(db.String(50), nullable=False, default='')
    salary = Column(db.Integer, nullable=False, default=0)
    date = Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, employee_name, dept_code, rank_code, address, salary, date):
        self.employee_name = employee_name
        self.dept_code = dept_code
        self.rank_code = rank_code
        self.address = address
        self.salary = salary
        self.date = date        
        
# 부서 정보 테이블
class Department(db.Model):
    column = ['dept_code', 'dept_name']
    dept_code = Column(db.String(50), primary_key=True)
    dept_name = Column(db.String(50), nullable=False)

    def __init__(self, dept_name):        
        self.dept_name = dept_name

# 직급 정보 테이블
class Rank(db.Model):
    column = ['rank_code', 'rank_name']
    rank_code = Column(db.String(50), primary_key=True)
    rank_name = Column(db.String(50), nullable=False)

    def __init__(self, rank_name):
        self.rank_name = rank_name


if __name__ == "__main__":
    # 테이블 생성
    db.create_all()
    