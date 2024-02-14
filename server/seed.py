from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():

      print("Clearning out tables")

      Franchise.query.delete()
      Employee.query.delete()

      print("Seeding Franchise table...")

      new_franchise_1 = Franchise(
         branch_name = "Downtown Baltimore",
         franchise_no = 1
      )

      db.session.add(new_franchise_1)
      db.session.commit()

      new_franchise_2 = Franchise(
         branch_name = "Inner Harbor",
         franchise_no = 2
      )

      db.session.add(new_franchise_2)
      db.session.commit()

      new_franchise_3 = Franchise(
         branch_name = "Catonsville",
         franchise_no = 3
      )

      db.session.add(new_franchise_3)
      db.session.commit()

      new_franchise_4 = Franchise(
         branch_name = "Elicott City",
         franchise_no = 4
      )

      db.session.add(new_franchise_4)
      db.session.commit()

      new_franchise_5 = Franchise(
         branch_name = "Columbia",
         franchise_no = 5
      )

      db.session.add(new_franchise_5)
      db.session.commit()

      new_franchise_6 = Franchise(
         branch_name = "College Park",
         franchise_no = 6
      )

      db.session.add(new_franchise_6)
      db.session.commit()

      new_franchise_7 = Franchise(
         branch_name = "Laurel",
         franchise_no = 7
      )

      db.session.add(new_franchise_7)
      db.session.commit()

      new_franchise_8 = Franchise(
         branch_name = "Bethesda",
         franchise_no = 8
      )

      db.session.add(new_franchise_8)
      db.session.commit()

      new_franchise_9 = Franchise(
         branch_name = "Rockville",
         franchise_no = 9
      )

      db.session.add(new_franchise_9)
      db.session.commit()

      new_franchise_10 = Franchise(
         branch_name = "Silver Springs",
         franchise_no = 10
      )

      db.session.add(new_franchise_10)
      db.session.commit()


      print("Seeding Employees table...")

      new_employees_f1 = [
         Employee(
         name = "Ronnie",
         job = "Frier",
         franchise_id = new_franchise_1.id
       ),
        Employee(
         name = "Johnny",
         job = "Manager",
         franchise_id = new_franchise_1.id
       ),
        Employee(
         name = "Lonnie",
         job = "Cashier",
         franchise_id = new_franchise_1.id
       ), 
      ]

      db.session.add_all(new_employees_f1)
      db.session.commit()

      new_employees_f2 = [
         Employee(
         name = "Tom",
         job = "Frier",
         franchise_id = new_franchise_2.id
       ),
        Employee(
         name = "Dom",
         job = "Manager",
         franchise_id = new_franchise_2.id
       ),
        Employee(
         name = "Rom",
         job = "Cashier",
         franchise_id = new_franchise_2.id
       ), 
      ]

      db.session.add_all(new_employees_f2)
      db.session.commit()

      new_employees_f3 = [
         Employee(
         name = "Pam",
         job = "Frier",
         franchise_id = new_franchise_3.id
       ),
        Employee(
         name = "Ham",
         job = "Manager",
         franchise_id = new_franchise_3.id
       ),
        Employee(
         name = "Cam",
         job = "Cashier",
         franchise_id = new_franchise_3.id
       ), 
      ]

      db.session.add_all(new_employees_f3)
      db.session.commit()

      new_employees_f4 = [
         Employee(
         name = "Hayley",
         job = "Frier",
         franchise_id = new_franchise_4.id
       ),
        Employee(
         name = "Kaeley",
         job = "Manager",
         franchise_id = new_franchise_4.id
       ),
        Employee(
         name = "Bailey",
         job = "Cashier",
         franchise_id = new_franchise_4.id
       ), 
      ]

      db.session.add_all(new_employees_f4)
      db.session.commit()

      new_employees_f5 = [
         Employee(
         name = "Addison",
         job = "Frier",
         franchise_id = new_franchise_5.id
       ),
        Employee(
         name = "Alison",
         job = "Manager",
         franchise_id = new_franchise_5.id
       ),
        Employee(
         name = "Madison",
         job = "Cashier",
         franchise_id = new_franchise_5.id
       ), 
      ]

      db.session.add_all(new_employees_f5)
      db.session.commit()

      new_employees_f6 = [
         Employee(
         name = "Ben",
         job = "Frier",
         franchise_id = new_franchise_6.id
       ),
        Employee(
         name = "Gwen",
         job = "Manager",
         franchise_id = new_franchise_6.id
       ),
        Employee(
         name = "Len",
         job = "Cashier",
         franchise_id = new_franchise_6.id
       ), 
      ]

      db.session.add_all(new_employees_f6)
      db.session.commit()

      new_employees_f7 = [
         Employee(
         name = "Aiden",
         job = "Frier",
         franchise_id = new_franchise_7.id
       ),
        Employee(
         name = "Caden",
         job = "Manager",
         franchise_id = new_franchise_7.id
       ),
        Employee(
         name = "Jaden",
         job = "Cashier",
         franchise_id = new_franchise_7.id
       ), 
      ]

      db.session.add_all(new_employees_f7)
      db.session.commit()

      new_employees_f8 = [
         Employee(
         name = "Ryan",
         job = "Frier",
         franchise_id = new_franchise_8.id
       ),
        Employee(
         name = "Bryan",
         job = "Manager",
         franchise_id = new_franchise_8.id
       ),
        Employee(
         name = "Wayan",
         job = "Cashier",
         franchise_id = new_franchise_8.id
       ), 
      ]

      db.session.add_all(new_employees_f8)
      db.session.commit()

      new_employees_f9 = [
         Employee(
         name = "Aaron",
         job = "Frier",
         franchise_id = new_franchise_9.id
       ),
        Employee(
         name = "Karen",
         job = "Manager",
         franchise_id = new_franchise_9.id
       ),
        Employee(
         name = "Darren",
         job = "Cashier",
         franchise_id = new_franchise_9.id
       ), 
      ]

      db.session.add_all(new_employees_f9)
      db.session.commit()

      new_employees_f10 = [
         Employee(
         name = "Paul",
         job = "Frier",
         franchise_id = new_franchise_10.id
       ),
        Employee(
         name = "Saul",
         job = "Manager",
         franchise_id = new_franchise_10.id
       ),
        Employee(
         name = "Raul",
         job = "Cashier",
         franchise_id = new_franchise_10.id
       ), 
      ]

      db.session.add_all(new_employees_f10)
      db.session.commit()