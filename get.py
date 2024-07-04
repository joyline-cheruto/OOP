class Staff:
    def __init__(self, name, department):
        self.name = ""
        self.department = ""


def main():
    staff = get_staff()
    print(f"{staff.name} from {staff.department}")


def get_staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    staff = Staff(name, department)
    return staff


if __name__ == "__main__":
    main()
