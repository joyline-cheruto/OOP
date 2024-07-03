def main():
    staff = get_staff()
    if staff[0] == "KIM":
        staff[1] = "FINANCE"
    print(f"{staff[0]} from {staff[1]}")


def get_staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    return [name, department]


if __name__ == "__main__":
    main()
