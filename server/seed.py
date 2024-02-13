from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():

      print("Clearning out tables")

      Franchise.query.delete()
      Employee.query.delete()

      print("Seeding Franchise table...")

      new_franchise = Franchise(
         branch_name = "Downtown Baltimore",
         franchise_no = 1
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Inner Harbor",
         franchise_no = 2
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Catonsville",
         franchise_no = 3
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Elicott City",
         franchise_no = 4
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Columbia",
         franchise_no = 5
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "College Park",
         franchise_no = 6
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Laurel",
         franchise_no = 7
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Bethesda",
         franchise_no = 8
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Rockville",
         franchise_no = 9
      )

      db.session.add(new_franchise)
      db.session.commit()

      new_franchise = Franchise(
         branch_name = "Silver Springs",
         franchise_no = 10
      )

      db.session.add(new_franchise)
      db.session.commit()
    
    
    
    
    


    
    
    
    
    

