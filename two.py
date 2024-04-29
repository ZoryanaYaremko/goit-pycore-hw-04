#  Завдання 1
def total_salary(path):
    total_sum = 0
    developer_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 2:  # перевірка, чи є два значення в рядку
                    try:
                        salary = int(data[1])
                        total_sum += salary
                        developer_count += 1
                    except ValueError:
                        print(f"Warning: Incorrect salary value in line '{line.strip()}'. Skipping.")
                else:
                    print(f"Warning: Incorrect data format in line '{line.strip()}'. Skipping.")

        if developer_count > 0:
            average_salary = total_sum / developer_count
        else:
            average_salary = 0

        return total_sum, average_salary

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Завдання 2
def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:  # перевірка, чи є три значення в рядку
                    cat_dict = {
                        "id": data[0],
                        "name": data[1],
                        "age": int(data[2])  # перетворюємо вік на ціле число
                    }
                    cats_list.append(cat_dict)
                else:
                    print(f"Warning: Incorrect data format in line '{line.strip()}'. Skipping.")

        return cats_list

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Завдання 3
import sys
import os
from pathlib import Path
from colorama import Fore, Style

def list_directory_contents(directory_path, indent=""):
    try:
        directory = Path(directory_path)
        if not directory.is_dir():
            print(f"{indent}Invalid directory path: {directory_path}")
            return

        print(f"{indent}Contents of directory: {directory}")

        for item in directory.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}Directory: {item.name}{Style.RESET_ALL}")
                list_directory_contents(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}File: {item.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        return

    directory_path = sys.argv[1]
    list_directory_contents(directory_path)

if __name__ == "__main__":
    main()

# Завдання 4
def parse_input(input_str):
    parts = input_str.strip().split()
    command = parts[0].lower()
    arguments = parts[1:]
    return command, arguments

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added with phone number '{phone}'.")

def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Phone number for contact '{name}' changed to '{new_phone}'.")
    else:
        print(f"Contact '{name}' not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(f"Phone number for contact '{name}': {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = {}

    while True:
        user_input = input("Enter command (add, change, show, exit): ")
        command, arguments = parse_input(user_input)

        if command == "exit" or command == "close":
            print("Exiting the program.")
            break
        elif command == "add" and len(arguments) == 2:
            add_contact(contacts, arguments[0], arguments[1])
        elif command == "change" and len(arguments) == 2:
            change_contact(contacts, arguments[0], arguments[1])
        elif command == "show" and len(arguments) == 1:
            show_phone(contacts, arguments[0])
        else:
            print("Invalid command or arguments. Please try again.")

if __name__ == "__main__":
    main()