# definition of the database
myems_historical_db = {
    'user': 'root',
    'password': 'MyPassword',
    'host': '192.168.0.1',
    'database': 'myems_historical_db',
}

# indicates how long analog values and digital values will be kept in database
# the longer days the more memory and disc space needed.
live_in_days = 365
# note: By default, energy values in historical db will never be deleted automatically.

# indicates if the program is in debug mode
is_debug = False
