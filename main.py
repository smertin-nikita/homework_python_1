import datetime

from application.salary import calculate_salary
from application.db.people import get_employees


def print_datetime():
    print(datetime.date.today())

if __name__ == '__main__':
    print_datetime()
    calculate_salary()
    get_employees()

