#dms_to_decimal() converts degress/minutes/seconds to decimal degrees; can return str of number to 3 places
def dms_to_decimal(degrees, minutes, seconds, is_string):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 360)
    if is_string:
        return str(round(decimal_degrees, 3))
    else:
        return decimal_degrees
    #print("Successfully converted DMS to decimal!\n")
    
#decimal_to_vector() converts two sets of decimal degress to a vector
def decimal_to_vector():
    print("Successfully converted decimal to vector!\n")

#dms_to_vector() converts two sets of DMS to a vector
def dms_to_vector():
    print("Successfully converted DMS to vector!\n")

degrees_north = None
minutes_north = None
seconds_north = None
degrees_west = None
minutes_west = None
seconds_west = None
full_dms_1 = None
full_dms_2 = None
    
def take_dms_input(is_first):
    global degrees_north
    global minutes_north
    global seconds_north
    global degrees_west
    global minutes_west
    global seconds_west
    global full_dms_1
    global full_dms_2
    degrees_north = int(input("Enter degrees North: "))
    minutes_north = int(input("Enter minutes North: "))
    seconds_north = int(input("Enter seconds North: "))
    #direction = str.upper(str(input("(N)orth or (W)est? ")))
    if is_first:
        full_dms_1 = str(degrees_north) + "° " + str(minutes_north) + "' " + str(seconds_north) + '" N '
    else:
        full_dms_2 = str(degrees_north) + "° " + str(minutes_north) + "' " + str(seconds_north) + '" N '
    degrees_west = int(input("Enter degrees West: "))
    minutes_west = int(input("Enter minutes West: "))
    seconds_west = int(input("Enter seconds West: "))
    if is_first:
        full_dms_1 += str(degrees_west) + "° " + str(minutes_west) + "' " + str(seconds_west) + '" W'
    else:
        full_dms_2 += str(degrees_west) + "° " + str(minutes_west) + "' " + str(seconds_west) + '" W'

def take_input(function):
    if function == "dms_to_decimal" or "dms_to_vector" :
        print()
        if function == "dms_to_decimal":
            take_dms_input(is_first = True)
            decimal_degrees_north = dms_to_decimal(degrees_north, minutes_north, seconds_north, is_string = True)
            decimal_degrees_west = dms_to_decimal(degrees_west, minutes_west, seconds_west, is_string = True)
            print(full_dms_1 + " is " + decimal_degrees_north + "° N " + decimal_degrees_west + "° W")

#Menu allows user 3 options:
#1 Deg/min/sec to decimal deg
#2 Convert decimal deg to vector
#3 Convert deg/min/sec to vector
#4 Quit

user_choice = ()
sentinel_values = ("q", "exit", "quit", "stop")
print("#1 Deg/Min/Sec to Decimal Degrees")
print("#2 Decimal Degrees to Vector Coordinates")
print("#3 Deg/Min/Sec to Vector Coordinates")
print()

while user_choice not in sentinel_values:
    user_choice = str.lower(str(input("Choose an option: ")))
    if user_choice == "1":
        take_input("dms_to_decimal")
    elif user_choice == "2":
        take_input("decimal_to_vector")
    elif user_choice == "3":
        take_input("dms_to_vector")
    elif user_choice not in sentinel_values:
       print("Invalid option. Please choose again.")
