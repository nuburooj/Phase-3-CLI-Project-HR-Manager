from config import app, migrate
from rich import print
from models import db
from utils import get_all_franchises, search_franchise_by_id, get_all_employees, add_employee_to_franchise, fire_employee_from_franchise, search_employee_by_id, change_employee_job

def welcome_screen():
  print("""[yellow]
 ____  ____ _______      ____    ____      _      ____  _____      _       ______ ________ _______     
|_   ||   _|_   __ \    |_   \  /   _|    / \    |_   \|_   _|    / \    .' ___  |_   __  |_   __ \    
  | |__| |   | |__) |     |   \/   |     / _ \     |   \ | |     / _ \  / .'   \_| | |_ \_| | |__) |   
  |  __  |   |  __ /      | |\  /| |    / ___ \    | |\ \| |    / ___ \ | |   ____ |  _| _  |  __ /    
 _| |  | |_ _| |  \ \_   _| |_\/_| |_ _/ /   \ \_ _| |_\   |_ _/ /   \ \\ `.___]  _| |__/ |_| |  \ \_  
|____||____|____| |___| |_____||_____|____| |____|_____|\____|____| |____`._____.|________|____| |___|[/]                                                                                                              
""")


def display_main_menu():
  print("[bold green]Main Menu[/]")
  print("1. [bold]Show all Franchises[/]")
  print("2. [bold]Add a Franchise[/]")
  print("3. [bold red]Exit[/]")


def get_main_choice():
  return input("What's it gonna be? ")


def display_all_franchises():
  franchises = get_all_franchises()
  for franchise in franchises:
    print(f"{franchise.id} | [yellow]Location:[/] [bold cyan]{franchise.branch_name}[/] |")
  print("[bold green]What do you wanna do?[/]")
  print("1. [bold]See more about a franchise[/]")
  print("2. [bold]Return to Main Menu[/]")
  choice = input()
  if choice == "1":
    choose_franchise_by_id()
  else:
    return 
  

def choose_franchise_by_id():
  search_id = input("Enter the id of the franchise you'd like to know more about: ")
  franchise = search_franchise_by_id(search_id)
  print(f"{franchise.id} | [yellow]Location:[/] [bold cyan]{franchise.branch_name}[/] | [yellow]Franchise no.[/] {franchise.franchise_no} | [yellow]Inaugurated:[/] {franchise.date_opened} |")
  display_franchise_submenu(franchise)


def display_franchise_submenu(franchise):
  print("[bold yellow]What would you like to do?[/]")
  print("1. [bold]See a Franchise's Employees[/]")
  print("2. [bold]Add an Employee to a Franchise[/]")
  print("3. [bold green]Main menu[/]")
  choice = input()
  handle_franchise_choice(choice, franchise)


def handle_franchise_choice(choice, franchise):
  if choice == "1":
    show_franchise_employees(franchise)
  elif choice == "2":
    add_employee_to_franchise(franchise)
  else:
    return


def show_franchise_employees(franchise):
  employees = get_all_employees()
  for employee in employees:
    if franchise.id == employee.franchise_id:
      print(f"{employee.id} | [yellow]Name:[/] [bold cyan]{employee.name}[/] | [yellow]Job:[/] [bold cyan]{employee.job}[/] | [yellow]Hired on:[/] {employee.hiring_date} | [yellow]Franchise ID:[/] {employee.franchise_id} |" )
  choose_employee_by_id()


def choose_employee_by_id():
    search_id = input("Enter the id of the Employee for options: ")
    employee = search_employee_by_id(search_id)
    display_employee_submenu(employee)


def display_employee_submenu(employee):
    print("1. [bold red]Fire[/] employee")
    print("2. [bold yellow]Update[/] employee job")
    print("3. [bold green]Main Menue[/]")
    choice = input()
    handle_employee_choice(choice, employee)

    
def handle_employee_choice(choice, employee):
  if choice == "1":
    fire_employee_from_franchise(employee)
    print("[italic yellow]Employee has been let go.[/]")
  elif choice == "2":
    change_employee_job(employee)
    print("[italic yellow]Employee just got promoted or demoted. (it's all about perspective)[/]")
  else:
    return
  

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    

    welcome_screen()
    while True:
      display_main_menu()
      choice = get_main_choice()
      print(choice)
      if choice == "1":
        display_all_franchises()
      elif choice == "2":
        print("add franchise feature coming soon")
      else: 
          break
    # remove pass and write your cli logic
