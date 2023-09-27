
from datetime import datetime
def ts(given_date):

    print(given_date.timestamp())
    return given_date
initial_date = datetime.strptime('11:15 16-09-2023',
                       '%H:%M %d-%m-%Y')
ts(initial_date)