year = 1000
match year%400:
    case 0:
        print("Leap year")
    case other:
        match year%4==0 and year%100!=0:
            case True:
               print("Leap Year")
            case other:
                print("Not Leap Year")

        
