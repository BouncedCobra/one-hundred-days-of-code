def convert():
    print("Write the number of years to convert")
    years=input()
    if (int(years)<0):
        print("Only positive numbers")
        convert()
    else:
        days = int(years) * 365
        print(f"The number of days is {days}")
convert()