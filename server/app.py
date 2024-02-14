from config import app, migrate
from rich import print
from models import db


def welcome_screen():
  print("[yellow]Hello! Welcome to [/yellow][bold cyan]HR Manager[/bold cyan]")

def display_main_menu():
  print("[bold green]Main Menu[/]")
  print("1. Show all Franchises")
  print("2. Add a Franchise")
  print("3. Exit")

def get_main_choice():
  return input("What's it gonna be?")


if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    

    welcome_screen()
    while True:
      display_main_menu()
      choice = get_main_choice()
      print(choice)
      if choice == "1":
        print("display all franchises")
      elif choice == "2":
        print("add franchise feature coming soon")
      else: 
          break
    # remove pass and write your cli logic
