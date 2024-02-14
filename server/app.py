from config import app, migrate
from rich import print
from models import db
from utils import get_all_franchises, search_franchise_by_id

def welcome_screen():
  print("[yellow]Hello! Welcome to [/yellow][bold cyan]HR Manager[/bold cyan]")

def display_main_menu():
  print("[bold green]Main Menu[/]")
  print("1. Show all Franchises")
  print("2. Add a Franchise")
  print("3. Exit")

def get_main_choice():
  return input("What's it gonna be?")

def display_all_franchises():
  franchises = get_all_franchises()
  for franchise in franchises:
    print(f"{franchise.id} | {franchise.branch_name} |")
  print("[bold green]What do you wanna do?[/]")
  print("1. See more about a franchise")
  print("2. Return to Main Menu")
  choice = input()
  if choice == "1":
    choose_franchise_by_id()
  else:
    return 
  
def choose_franchise_by_id():
  search_id = input("Enter the id of the franchise you'd like to know more about: ")
  franchise = search_franchise_by_id(search_id)
  print(f"{franchise.id} | {franchise.branch_name} | {franchise.franchise_no} | {franchise.date_opened} |")
  display_franchise_submenu(franchise)

def display_franchise_submenu(franchise):
  print("[bold green]What would you like to do?[/]")
  print("1. See a Franchise's Employees")
  print("2. Add an Employee to a Franchise")
  print("3. Exit")
  choice = input()




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
