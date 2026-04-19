from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        print ("Wrong date format use YYYY-MM-DD")
        return None

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("abcd"))