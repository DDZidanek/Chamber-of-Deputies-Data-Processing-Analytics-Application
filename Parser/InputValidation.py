from datetime import datetime

def is_valid_date(date_text):
    try:
        datetime.strptime(date_text, '%d.%m.%Y')
        return True
    except ValueError:
        return False
    
def is_valid_datetime(datetime_text):
    try:
        datetime.strptime(datetime_text, '%Y-%m-%d %H')
        return True
    except ValueError:
        return False
    
def is_valid_datetime_Year_to_Minute(datetime_text):
    try:
        datetime.strptime(datetime_text, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False
    
def is_valid_datetime_Hour_to_Minute(datetime_text):
    try:
        time = datetime.strptime(datetime_text, '%H:%M')
        return time.strftime('%H:%M')
    except ValueError:
        return None
def is_valid_datetime_fraction(datetime_text):
    try:
        datetime.strptime(datetime_text, '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False
def date_format(date_text):
    date_obj = datetime.strptime(date_text, "%d.%m.%Y")
    iso_format_date = date_obj.strftime("%Y-%m-%d")
    return iso_format_date

def datetime_format(datetime_text):
    datetime_obj = datetime.strptime(datetime_text, "%Y-%m-%d %H:%M")
    return datetime_obj

def datetime_format_Y_H(datetime_text):
    datetime_obj = datetime.strptime(datetime_text, "%Y-%m-%d %H")
    return datetime_obj

def convert_to_sqlite_datetime(datetime_text):
    try:
        dt_obj = datetime.strptime(datetime_text, '%Y-%m-%d %H:%M:%S.%f')
        
        sqlite_format = dt_obj.strftime('%Y-%m-%d %H:%M:%S.%f')[:23]
        return sqlite_format
    except ValueError:
        return None
def is_valid_id(value):
    if (not value.isdigit() or (not value)):
        return False
    else:
        return True
    
def is_valid_int(value):
    if (not value.isdigit() or (not value)):
        return None
    else:
        return value

def is_valid_char(value):
    if (value == "" or value == " "):
        return None
    else:
        return value