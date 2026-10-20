"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day_cost = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return day_cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    credit_cost = semester_cost / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    class_cost = (credit_cost * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


def worth_it(classes_skiped, annual_cost, credits):
   class_cost2 = cost_per_class(annual_cost, credits)
   skip_cost = class_cost2 * classes_skiped
   return skip_cost

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total cost for one year: "))
    credits = int(input("Credits this semester: "))
    while True:
        # Show your menu here.
        print("The Cost of College")
        print("1 Per semester")
        print("2 Per month")
        print("3 Per day")
        print("4 Per credit")
        print("5 Per CS1430 class")
        print("6 Worth it?")
        print("Q Quit")
        choice = input("Choose an option: ")
        if choice == "Q":
            print("Thank you for running the numbers!")
            break
        elif choice == "1":
            cost_per_semester(annual_cost)
            print(f"Every semester costs ${cost_per_semester(annual_cost):.2f}.")
        elif choice == "2":
            cost_per_month(annual_cost)
            print(f"Every month costs ${cost_per_month(annual_cost):.2f}.")
        elif choice == "3":
            cost_per_day(annual_cost)
            print(f"Every class day costs ${cost_per_day(annual_cost):.2f}.")
        elif choice == "4":
            cost_per_credit(annual_cost, credits)
            print(f"Every credit costs ${cost_per_credit(annual_cost, credits):.2f}.")
        elif choice == "5":
            cost_per_class(annual_cost, credits)
            print(f"Every CS1430 class costs ${cost_per_class(annual_cost, credits):.2f}.")
        elif choice == "6":
            classes_skiped = int(input("How many classes did you skip? "))
            worth_it(classes_skiped, annual_cost, credits)
            print(f"Skipping {classes_skiped} classes cost you ${worth_it(classes_skiped, annual_cost, credits):.2f}.")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
