try:
    print(5 / 0)
    break
except:
    print("Sorry, something went wrong")
except (ValueError, ZeroDivisionError) :
    print("Too Bad...")