import getconn

class Employee:
    def __init__(self):
        self.db = getconn.getconn()
        self.cur = self.db.cursor()

    def create_table(self):
        try:
            self.cur.execute("Create table Emp2 (Name varchar(20),Id int(4)primary key,Department varchar(20),Salary int(10))")
            #self.cur.execute("create table Records(username varchar(20), password int(10),Id int(4))")
        except Exception as err:
            print(err)
            print("Table already exist")

        else:
            print("Table created")
                                
                    
                    
    def insert_into(self):
        try:
            self.name = input("Enter your name:")
            self.id = int(input("Enter your id:"))
            self.department = input("Enter your department:")
            self.salary = int(input("Enter your salary:"))
            sql = "Insert into Emp2 values ('{}',{},'{}',{})".format(self.name,self.id,self.department,self.salary)
            self.cur.execute(sql)
            if self.cur.rowcount > 0:
                print("Successfully Inserted the values")
                self.db.commit()
            else:
                print("Record not inserted")
                self.db.rollback()
        except Exception as err:
            print(err,"could not insert values due to error in program")
        finally:
            print("Records were manipulated")#err
            self.db.close()


    def show_emp(self): # similare to display
        try:
            sql = "select Name,Id from Emp2"
            self.cur.execute(sql)
            records = self.cur.fetchall()
            for i in records:
                print(i)
                '''if len(i)<0:

                    print("Your table is empty")'''
                    

        except Exception as err:
            print(err,"could not displayed")
        finally:
            self.db.close()
            

    def update_sal(self):
        try:
            e_id = int(input("Enter the employee id where salary needs to be updated:"))
            sal = int(input("Enter the salary you wish to update:"))
            sql = "Update Emp2 set salary = {} where id = {}".format(sal,e_id)
            self.cur.execute(sql)
                              
            if self.cur.rowcount > 0:
                print("Updated Salary")
                self.db.commit()
            else:
                print("Not Updated")
                self.db.rollback()
        except Exception as err:
            print(err,"Not updated")
        finally:
            self.db.close()



    def update_dep(self):
        try:
            e_id = int(input("Enter the employee id where department needs to be updated:"))
            dep = input("Enter the department you wish to update:")
            depr = "Update Emp2 set department = '{}' where id = {}".format(dep,e_id)
            self.cur.execute(depr)
            if self.cur.rowcount > 0:
                print("Updated Department")
                self.db.commit()
            else:
                print("Not Updated")
                self.db.rollback()
        except Exception as err:
            print(err,"Not Updated")
        finally:
            self.db.close()


    
    def delete_emp(self):
        try:
            e_id = int(input("Enter the employee id where details you want to delete:"))
            #name = (input("Enter the name you wish to update:"))
            sql = "delete from Emp2 where id = {}".format(e_id)
            self.cur.execute(sql)
                              
            if self.cur.rowcount > 0:
                print("sucessfully Delete Details")
                self.db.commit()
            else:
                print("Not Deleted")
                self.db.rollback()
        except Exception as err:
            print(err,"Not Deleted")
        finally:
            self.db.close()













            














            
