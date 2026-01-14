#/usr/bin/env python3
from __init__ import CONN, CURSOR
from department import Department
import ipdb

# 1. Reset state
Department.drop_table()
Department.create_table()

# 2. Add records
payroll = Department.create("Payroll", "Building A, 5th Floor")
hr = Department.create("Human Resource", "Building C, East Wing")
legal = Department.create("Legal", "Building c")


hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
payroll.delete()
print(payroll)
CONN.commit() 




ipdb.set_trace()