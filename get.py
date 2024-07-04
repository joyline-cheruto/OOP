class Staff:
   ...
def main():
    staff = get_staff()
    print(f"{staff.name} from {staff.department}")


def get_staff():
    staff = Staff()
    staff.name = input("Enter name: ")
    staff.department = input("Enter department: ")
    return staff


if __name__ == "__main__":
    main()
