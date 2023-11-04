def is_leap_year(year):
    return True if year % 4 == 0 and year % 100 != 0 else year % 400 == 0

    # if year % 4 == 0 and year % 100 != 0:
    #     return True
    # elif year % 400 == 0:
    #     return True
    # return False

print(is_leap_year(2020))