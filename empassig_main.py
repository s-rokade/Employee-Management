'''Create an Employee management database app with functions like
1) ADD EMPLOYEE (ID, NAME, DEPARTMENT, SALARY)
2) SHOW EMPLOYEES
3) UPDATE EMPLOYEE SALARY
4) UPDATE EMPLOYEE DEPARTMENT
5) DELETE EMPLOYEE'''

from empassig import Employee

while True:
    print("************Welcom to payroll********************")
    print("                                                 ")
    print("Please press the key for selection")
    print("\t1.Add Employee\n\t2.Show Employee \n\t3.Update Employee Salary\n\t4.Update Employee Department\n\t5.Delete")
    ch = input("Enter your choice:")
    e = Employee()
    if ch =='1':
        e.create_table()
        e.insert_into()

    elif ch =='2':
        e.show_emp()
    
    elif ch == '3':
        e.update_sal()

    elif ch == '4':
        e.update_dep()

    elif ch == '5':
        e.delete_emp()

    else:
        break
    
    
