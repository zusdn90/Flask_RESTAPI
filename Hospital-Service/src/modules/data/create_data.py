import schedule
import openpyxl
from openpyxl import Workbook
from faker import Faker

# 5분마다 100개의 랜덤 데이터 생성(1. 환자 입원  2. 입원 환자의 바이탈 수치 변화)
def create(self):
    faker = Faker()
    
    write_wb = Workbook()

    write_ws = write_wb.active
    write_ws['A1'] = 'patient_code'
    write_ws['B1'] = 'patient_name'
    write_ws['C1'] = 'vital_code'
    write_ws['D1'] = 'vital_value'
    write_ws['E1'] = 'alert_info'
    write_ws['F1'] = 'admission_date'
    
    write_ws.append([1,2,3])
    write_wb.save('user_data.xlsx')

    



#schedule.every(5).minute.do(job)



