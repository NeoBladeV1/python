months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

days_p_mth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_wd = [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 2]

a = input("Enter month number: ")
b = int(a) - 1

if 0 <= b < 12:
    month_n = months[b]
    total_d = days_p_mth[b]
    current_wd = start_wd[b]

    print()
    print(f"        {month_n} 2026")
    print()
    print(" Mo  Tu  We  Th  Fr  Sa  Su ")

    # blank space for the start of week
    row = ''
    for i in range(current_wd):
        for j in range(4):
            row += " "

    for day in range(1, total_d + 1):
        if day < 10:
            row += f"  {day} "
        else:
            row += f" {day} "

        current_wd += 1

        if current_wd % 7 == 0:
            print(row)
            row = ""

    if current_wd % 7 != 0:
        while current_wd % 7 != 0:
            for j in range(4):
                row += " "
            current_wd += 1
        print(row)
    print()
else:
    print('Invalid month number! please check ur brain for extra brain cells and write a number between 1 and 12')
    print('🤣🤣🤣🤣🤣🤣🤣🤣😂😂😂😂😂😂')