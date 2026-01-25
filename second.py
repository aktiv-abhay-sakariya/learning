from abc import ABC, abstractmethod
from datetime import datetime


def menu(title, menus):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(menus)
            print(f"\n{'=' * 10} {title} {'=' * 10}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_choice(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                try:
                    choice = int(input("Select No : "))
                    if 1 <= choice <= limit:
                        return func(*args, choice, **kwargs)
                    print(f"Enter number between 1 and {limit}")
                except ValueError:
                    print("Enter valid number")
        return wrapper
    return decorator

def check_string(msg):
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Input cannot be empty")

def check_age(msg):
    while True:
        try:
            age = int(input(msg))
            if 1 <= age <= 120:
                return age
            print("Age must be between 1 and 120")
        except ValueError:
            print("Enter valid age")


def check_mobile(msg):
    while True:
        mob_num = input(msg).strip()
        if mob_num.isdigit() and len(mob_num) == 10:
            return mob_num
        print("Mobile must be exactly 10 digits")

def check_gender(msg):
    while True:
        gender = input(msg).strip().lower()
        if gender in ("m", "f"):
            return "Male" if gender == "m" else "Female"
        print("Enter M or F")


# ------------------ ABSTRACTION ------------------

class Person(ABC):
    def __init__(self):
        self.name = check_string("Enter name : ")
        self.age = check_age("Enter age : ")
        self.gender = check_gender("Enter gender (M/F): ")
        self.mobile = check_mobile("Enter mobile number : ")

    def display_basic(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Mobile : {self.mobile}")

    @abstractmethod
    def display(self):
        pass


# ------------------ DOCTOR ------------------

class Doctor(Person):
    def __init__(self, doctor_id):
        self.doctor_id = doctor_id
        super().__init__()
        self.specialization = check_string("Enter specialization : ")

    def display(self):
        print("-" * 40)
        print(f"Doctor ID : {self.doctor_id}")
        self.display_basic()
        print(f"Specialization : {self.specialization}")


# ------------------ MEDICAL RECORD ------------------

class MedicalRecord:
    def __init__(self, diagnosis, treatment, date):
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.date = date

    def display(self):
        print(f"\nDiagnosis : {self.diagnosis}")
        print(f"Treatment : {self.treatment}")
        print(f"Date      : {self.date}")


# ------------------ PATIENT ------------------

class Patient(Person):
    def __init__(self, patient_id):
        self.patient_id = patient_id
        super().__init__()
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def display(self):
        print("-" * 40)
        print(f"Patient ID : {self.patient_id}")
        self.display_basic()


# ------------------ HMS ------------------

class HospitalManagementSystem:

    def __init__(self):
        self.doctors = {}
        self.patients = {}
        while True:
            self.main_menu()

    @menu("HOSPITAL MANAGEMENT SYSTEM", "\n1.Add \n2.View \n3.Update \n4.Delete \n5.Search \n6.Exit")
    @validate_choice(6)
    def main_menu(self, choice):
        if choice == 1:
            self.add_menu()
        elif choice == 2:
            self.view_menu()
        elif choice == 3:
            self.update_menu()
        elif choice == 4:
            self.delete_menu()
        elif choice == 5:
            self.search_by_mobile()
        else:
            print("Program terminated")
            exit()

    # ---------- ADD ----------

    @menu("ADD MENU", "\n1.Add Doctor \n2.Add Patient \n3.Add Medical Record")
    @validate_choice(3)
    def add_menu(self, choice):
        if choice == 1:
            did = check_string("Enter doctor id : ")
            self.doctors.setdefault(did, Doctor(did))
        elif choice == 2:
            pid = check_string("Enter patient id : ")
            self.patients.setdefault(pid, Patient(pid))
        else:
            pid = check_string("Enter patient id : ")
            if pid not in self.patients:
                print("Patient not found")
                return
            diagnosis = check_string("Enter diagnosis : ")
            treatment = check_string("Enter treatment : ")
            while True:
                try:
                    date = check_string("Enter date (YYYY-MM-DD) : ")
                    if datetime.strptime(date, "%Y-%m-%d").date() <= datetime.today().date():
                        break
                    print("Future date not allowed")
                except ValueError:
                    print("Invalid date format")
            self.patients[pid].add_record(MedicalRecord(diagnosis, treatment, date))
            print("Medical record added")

    # ---------- VIEW ----------

    @menu("VIEW MENU", "\n1.View Doctor \n2.View Patient \n3.View Medical Record")
    @validate_choice(3)
    def view_menu(self, choice):
        if choice == 1:
            for d in self.doctors.values():
                d.display()
        elif choice == 2:
            for p in self.patients.values():
                p.display()
        else:
            pid = check_string("Enter patient id : ")
            patient = self.patients.get(pid)
            if not patient:
                print("Patient not found")
                return
            for r in patient.records:
                r.display()

    # ---------- UPDATE ----------

    @menu("UPDATE MENU", "\n1.Update Doctor \n2.Update Patient")
    @validate_choice(2)
    def update_menu(self, choice):
        data = self.doctors if choice == 1 else self.patients
        key = check_string("Enter id : ")
        if key in data:
            data[key] = type(data[key])(key)
            print("Updated successfully")
        else:
            print("Record not found")

    # ---------- DELETE ----------

    @menu("DELETE MENU", "\n1.Delete Doctor \n2.Delete Patient")
    @validate_choice(2)
    def delete_menu(self, choice):
        data = self.doctors if choice == 1 else self.patients
        key = check_string("Enter id : ")
        if data.pop(key, None):
            print("Deleted successfully")
        else:
            print("Record not found")

    # ---------- SEARCH ----------

    def search_by_mobile(self):
        mobile = check_mobile("Enter mobile : ")
        for p in self.patients.values():
            if p.mobile == mobile:
                p.display()
                for r in p.records:
                    r.display()
                return
        print("Patient not found")


if __name__ == "__main__":
    KD = HospitalManagementSystem()
