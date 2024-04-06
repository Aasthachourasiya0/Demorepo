# if/else/elif




# Match Case
day = 2
match(day):
    case 1:
        print("Sun")
    case 2:
        print("Mon")
    case 3:
        print("Tue")
    case 4:
        print("Wed")
    case 5:
        print("Thurs")
    case 6:
        print("Fri")
    case 7:
        print("Sat")
    case _:
        print("No days Assigned")




# 12 - Season
       
# Nov - Dec - Jan -Feb : Winter Season
# Mar - Apr - May - Jun : Summer Season
# Jul - Aug - Sept - Oct : Rainy Season
       
month = input("Enter the month : (jan)")


match(month):
    case "jan":
        print("winter Season")
    case "feb":
        print("winter Season")
    case "mar":
        print("Summer Season")
    case "apr":
        print("Summer Season")
    case "may":
        print("Summer Season")
    case "jun":
        print("Summer Season")
    case "jul":
        print("Rainy Season")
    case "aug":
        print("Rainy Season")
    case "sept":
        print("Rainy Season")
    case "oct":
        print("Rainy Season")
    case "nov":
        print("winter Season")
    case "dec":
        print("winter Season")
    case _:
        print("Invalid month")
