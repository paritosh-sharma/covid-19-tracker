def get_choice():
    print("welcome to the covid tracker")
    print("enter 0 to get the list of locations")
    print("enter 1 to get the latest covid data for a select country")
    print("enter 2 to get covid data for a select country on a select date")
    print("enter 3 to get covid data diffference for a select country between two dates")
    print("enter 4 to exit the program")
    return("enter your choice : ")
def location_list(a):
    for x in a:
        print(x,"\n")