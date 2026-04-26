# Convert a month name to a number of days. with if else and match case

month_inp=input("Enter a month name: ").capitalize()
if month_inp in ['January','February','March','May','July','August','October','December','April','June','September','November']:
    match month_inp:
        case 'January'|'March'|'May'|'July'|'August'|'October'|'December':
            print(f"{month_inp} has 31 days")
        case 'February':
            print(f"{month_inp} has 28 days")
        case 'April'|'June'|'September'|'November':
            print(f"{month_inp} has 30 days")
else:
    print(f"{month_inp} is wrong input. Enter full month name such as January,Februrary,.....,etc")

