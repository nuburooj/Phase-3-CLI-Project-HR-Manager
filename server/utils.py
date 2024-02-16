from config import db
from models import Franchise, Employee
from pick import pick
from datetime import datetime
from rich import print

def get_all_franchises():
    return db.session.query(Franchise).all()


def search_franchise_by_id(id):
    return db.session.get(Franchise, id)


def search_employee_by_id(id):
    return db.session.get(Employee, id)


def get_all_employees():
    return db.session.query(Employee).all()


def change_employee_job(employee):
    req_type = "What job is this Employee gonna be working?"
    new_job, index = pick(["Manager", "Frier", "Cashier"], req_type)
    employee.job = new_job
    db.session.commit()


def add_employee_to_franchise(franchise):
    employee_names = [employee.name for employee in db.session.query(Employee).all()]
    prompt = "Which employee is gonna be working at this franchise?"
    employee_name, index = pick(employee_names, prompt)
    employee = db.session.query(Employee).filter(Employee.name == employee_name).first()
    req_type = "What job is this Employee gonna be working?"
    job, index = pick(["Manager", "Frier", "Cashier"], req_type)
    date_string = input("Enter date and time to sign employment contract in the format YYYY-MM-DD HH:MM:SS: ")
    date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    employee = Employee(
        name=employee_name,
        franchise_id=franchise.id,
        job=job,
        hiring_date=date,
       
    )
    print("[italic yellow]Employee has been hired![/]")

    db.session.add(employee)
    db.session.commit()


def fire_employee_from_franchise(employee):
    db.session.delete(employee)
    db.session.commit()
    