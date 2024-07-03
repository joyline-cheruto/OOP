
def employee():
    name = get_name()
    department = get_department()
    print(f"{name} from {department}")


def get_name():
    return input("Enter name: ")


def get_department():
    return input("Enter department: ")


if __name__ == "__main__":
    employee()
=======
def main():
    staff = get_staff()
    if staff[0] == "KIM":
        staff[1] = "FINANCE"
    print(f"{staff[0]} from {staff[1]}")


def get_staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    return (name, department)


if __name__ == "__main__":
    main()

