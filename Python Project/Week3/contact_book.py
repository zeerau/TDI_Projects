import re
from prettytable import PrettyTable

employees = []
empIDs = set()
phone_numbers = set()
emails = set()

def is_unique(empID, phone_number, email):
    if empID in empIDs:
        print(f'Employee with employee number {empID} already exists.')
        return False
    if phone_number in phone_numbers:
        print(f'Phone number {phone_number} is already assigned to another employee.')
        return False
    if email in emails:
        print(f'Email {email} is already in use.')
        return False
    return True

def is_valid_name(name):
    return name.isalpha()

def is_valid_phone_number(phone_number):
    return phone_number.isdigit()

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)

def add_employee(empID, first_name, last_name, phone_number, email, address):
    if not is_unique(empID, phone_number, email):
        return
    if not is_valid_name(first_name):
        print('First name should contain only alphabetic characters.')
        return
    if not is_valid_name(last_name):
        print('Last name should contain only alphabetic characters.')
        return
    if not is_valid_phone_number(phone_number):
        print('Phone number should contain only numeric characters.')
        return
    if not is_valid_email(email):
        print('Invalid email format.')
        return

    new_employee = {
        'empID': empID,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    employees.append(new_employee)
    empIDs.add(empID)
    phone_numbers.add(phone_number)
    emails.add(email)
    print(f'Employee {first_name} {last_name} added successfully.')

def print_all_employees():
    table = PrettyTable()
    table.field_names = ["Employee ID", "First Name", "Last Name", "Phone Number", "Email", "Address"]
    for emp in employees:
        table.add_row([emp['empID'], emp['first_name'], emp['last_name'], emp['phone_number'], emp['email'], emp['address']])
    print(table)

# Example usage
add_employee('001', 'John', 'Doe', '1234567890', 'john.doe@example.com', '123 Main St')
add_employee('002', 'Jane', 'Smith', '0987654321', 'jane.smith@example.com', '456 Elm St')
add_employee('001', 'Alice', 'Johnson', '1112223333', 'alice.johnson@example.com', '789 Oak St')  # Duplicate empID
add_employee('003', 'Bob', 'Brown', '1234567890', 'bob.brown@example.com', '101 Pine St')  # Duplicate phone number
add_employee('004', 'Charlie', 'Davis', '4445556666', 'john.doe@example.com', '202 Maple St')  # Duplicate email

print_all_employees()

