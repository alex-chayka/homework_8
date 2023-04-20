from datetime import datetime, timedelta
from collections import defaultdict
import calendar


def get_next_week_start_date(d: datetime.date):
    difference_dates = 7 - d.weekday()
    return d + timedelta(days=difference_dates)


def parse_birthday(text: str):
    try:
        bd = datetime.strptime(text, "%d, %m, %Y")
        return bd.replace(year=datetime.now().year).date()
    except ValueError as e:
        return None


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    # today = datetime(2023, 4, 26).date()
    today = datetime.now().date()

    next_week_start_date = get_next_week_start_date(today)

    start_interval = next_week_start_date - timedelta(days=2)
    end_interval = next_week_start_date + timedelta(days=4)

    birthdays_users = []
    for user in users:
        bd_user = parse_birthday(user["birthday"])
        if bd_user is not None:
            if start_interval <= bd_user <= end_interval:
                birthdays_users.append(user)
        else:
            print(
                "The date {} is not valid (user: {})".format(
                    user["birthday"], user["name"]
                )
            )

    for user in birthdays_users:
        current_bd = parse_birthday(user["birthday"])
        if current_bd.weekday() in (5, 6):
            # birthdays["Monday"].append(user["name"])
            birthdays[0].append(user["name"])
        else:
            # birthdays[current_bd.strftime("%A")].append(user["name"])
            birthdays[current_bd.weekday()].append(user["name"])

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Aleksandr", "birthday": "25, 4, 2000"},
        {"name": "Anna", "birthday": "26, 4, 1985"},
        {"name": "Mark", "birthday": "25, 4, 1990"},
        {"name": "Yulia", "birthday": "27, 4, 1992"},
        {"name": "Oleg", "birthday": "29, 4, 1981"},
        {"name": "Halyna", "birthday": "22, 04, 1982"},
        {"name": "Mykola", "birthday": "23, 4, 1983"},
        {"name": "Aleksei", "birthday": "24, 4, 1986"},
        {"name": "Larysa", "birthday": "28, 4, 1987"},
        {"name": "Maksim", "birthday": "31, 4, 2005"},
    ]

    result_dict = get_birthdays_per_week(users)

    print(result_dict)

    for k, v in sorted(result_dict.items()):
        print("{}: {}".format(calendar.day_name[k], ", ".join(v)))
