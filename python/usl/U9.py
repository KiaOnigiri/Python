day = int(input('Day - '))
month = int(input('Month - '))
year = int(input('Year - '))
if day > 31 and month == 1 or day > 31 and month in [3,5,7,8,10,12] or day > 30 and month in [4, 6, 9, 11] or day > 28 and month == 2 or year > 2021 or month > 12 or 1 > day or 1 > month or 1 > year:
    print('False')
else:
    print('True')
7
