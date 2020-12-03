def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1

    else:
        if month < 12:
            return year, month + 1, 1
        # , 1

        else:
            return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True

    if year1 == year2:
        if month1 < month2:
            return True

        if month1 == month2:
            return day1 < day2

    return False


def isLeapYear(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def daysInMonth(year, month):
    if month == 1:
        return 31

    elif month == 2:

        if isLeapYear(year):
            return 29

        return 28

    elif month == 3:
        return 31

    elif month == 4:
        return 30

    elif month == 5:
        return 31

    elif month == 6:
        return 30

    elif month == 7:
        return 31

    elif month == 8:
        return 31

    elif month == 9:
        return 30

    elif month == 10:
        return 31

    elif month == 11:
        return 30

    elif month == 12:
        return 31


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    # assert (days > 0), "invalid input"
    return days


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    # 36524
    # 36523
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
