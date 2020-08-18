import datetime

from server import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# 사원 정보 테애블
class Employee(db.Model):
    __tablename__ = 'Employee'

    column = ['employee_code', 'employee_name','dept_code','rank_code', 'address', 'salary', 'phone_number', 'date']
    employee_code = db.Column(db.String(50), primary_key=True)
    employee_name = db.Column(db.String(50), nullable=False, default='')
    dept_code = db.Column(db.String(50), nullable=False, default='')
    rank_code = db.Column(db.String(50), nullable=False, default='')
    address = db.Column(db.String(50), nullable=False, default='')
    salary = db.Column(db.Integer, nullable=False, default=0)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())


    def __init__(self, employee_code, employee_name, dept_code, rank_code, address, salary, date):
        self.employee_code = employee_code
        self.employee_name = employee_name
        self.dept_code = dept_code
        self.rank_code = rank_code
        self.address = address
        self.salary = salary
        self.date = date        
        
# 부서 정보 테이블
class Department(db.Model):
    __tablename__ = 'Department'

    column = ['dept_code', 'dept_name']
    dept_code = db.Column(db.String(50), primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)

    def __init__(self, dept_name):        
        self.dept_name = dept_name

# 직급 정보 테이블
class Rank(db.Model):
    __tablename__ = 'Rank'

    column = ['rank_code', 'rank_name']
    rank_code = db.Column(db.String(50), primary_key=True)
    rank_name = db.Column(db.String(50), nullable=False)

    def __init__(self, rank_name):
        self.rank_name = rank_name


if __name__ == "__main__":
    # 테이블 생성
    db.create_all()    
    