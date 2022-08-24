from datetime import datetime


class AppConstants:
    STARTYEAR = 2022
    STARTMONTH = 'JUNE'
    CURRENTMONTH = datetime.now().month
    CURRENTYEAR = int(datetime.now().strftime("%Y"))

