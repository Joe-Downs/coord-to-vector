#dms_to_decimal() converts degress/minutes/seconds to decimal degrees; can return str of number to 3 places
def dms_to_decimal(degrees, minutes, seconds, is_string):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 360)
    if is_string:
        return str(round(decimal_degrees, 3))
    else:
        return decimal_degrees

vector_notation = None
#decimal_to_vector() converts two sets of decimal degress to a vector
def decimal_to_vector(north_start, west_start, north_stop, west_stop):
    global vector_notation
    y_start = north_start * (40000/360) * 3280.4
    x_start = west_start * (40000/360) * 3280.4
    y_stop = north_stop * (40000/360) * 3280.4
    x_stop = west_stop * (40000/360) * 3280.4
    y_vector = y_stop - y_start
    x_vector = x_stop - x_start
    vector_notation = str(round(x_vector)) + "î + " + str(round(y_vector)) + "ĵ"
    
#dms_to_vector() converts two sets of DMS to a vector
def dms_to_vector():
    print("Successfully converted DMS to vector!\n")

def haversine_vector():

degrees_north = None
minutes_north = None
seconds_north = None
degrees_west = None
minutes_west = None
seconds_west = None
full_dms_1 = None
full_dms_2 = None
decimal_north_start = None
decimal_west_start = None
decimal_north_stop = None
decimal_west_stop = None
full_decimal_start = None
full_decimal_stop = None

def take_dms_input(is_first):
    global degrees_north
    global minutes_north
    global seconds_north
    global degrees_west
    global minutes_west
    global seconds_west
    global full_dms_1
    global full_dms_2
    #if is_vector:
    #    print("Choose your first set of North coordinates:")
    #else:
    #    print("Choose your second set of North coordinates:")
    degrees_north = int(input("Enter degrees North: "))
    minutes_north = int(input("Enter minutes North: "))
    seconds_north = int(input("Enter seconds North: "))
    if is_first:
        full_dms_1 = str(degrees_north) + "° " + str(minutes_north) + "' " + str(seconds_north) + '" N '
    else:
        full_dms_2 = str(degrees_north) + "° " + str(minutes_north) + "' " + str(seconds_north) + '" N '
    #if is_vector:
    #    print("Choose your first set of West coordinates:")
    #else:
    #    print("Choose your second set of West coordinates:")
    degrees_west = int(input("Enter degrees West: "))
    minutes_west = int(input("Enter minutes West: "))
    seconds_west = int(input("Enter seconds West: "))
    if is_first:
        full_dms_1 += str(degrees_west) + "° " + str(minutes_west) + "' " + str(seconds_west) + '" W'
    else:
        full_dms_2 += str(degrees_west) + "° " + str(minutes_west) + "' " + str(seconds_west) + '" W'

def take_decimal_input():
    global decimal_north_start
    global decimal_west_start
    global decimal_north_stop
    global decimal_west_stop
    global full_decimal_start
    global full_decimal_end
    decimal_north_start = float(input("Enter the starting North coordinate: "))
    decimal_west_start = float(input("Enter the starting West coordinate: "))
    full_decimal_start = str(decimal_north_start) + "° N " + str(decimal_west_start) + "° W"
    decimal_north_stop = float(input("Enter the ending North coordinate: "))
    decimal_west_stop = float(input("Enter the ending West coordinate: "))
    full_decimal_stop = str(decimal_north_stop) + "°  N" + str(decimal_west_stop) + "° W"
    
def take_input(function):
    if function == "dms_to_decimal" or "dms_to_vector" :
        print()
        if function == "dms_to_decimal":
            take_dms_input(is_first = True)
            decimal_degrees_north = dms_to_decimal(degrees_north, minutes_north, seconds_north, is_string = True)
            decimal_degrees_west = dms_to_decimal(degrees_west, minutes_west, seconds_west, is_string = True)
            print(full_dms_1 + " is " + decimal_degrees_north + "° N " + decimal_degrees_west + "° W")
        elif function == "dms_to_vector":
            print("Input the first set of coordinates.")
            take_dms_input(is_first = True)
            decimal_degrees_north_1 = dms_to_decimal(degrees_north, minutes_north, seconds_north, is_string = True)
            decimal_degrees_west_1 = dms_to_decimal(degrees_west, minutes_west, seconds_west, is_string = True)
            print("Input the second set of coordinates.")
            take_dms_input()
            decimal_degrees_north_2 = dms_to_decimal(degrees_north, minutes_north, seconds_north, is_string = True)
            decimal_degrees_west_2 = dms_to_decimal(degrees_west, minutes_west, seconds_west, is_string = True)
    if function == "decimal_to_vector" or "haversine_vector":
        print()
        take_decimal_input()
        decimal_to_vector(decimal_north_start, decimal_west_start, decimal_north_stop, decimal_west_stop)
        if function == "haversine_vector":
            haversine_vector(decimal_north_start, decimal_west_start, decimal_north_stop, decimal_west_stop)
        print("Starting at " + full_decimal_start + "  and ending at " + full_decimal_stop +
              " yields the vector of: " + vector_notation)

user_choice = ()
sentinel_values = ("q", "exit", "quit", "stop")
print("#1 Deg/Min/Sec to Decimal Degrees")
print("#2 Decimal Degrees to Vector Coordinates")
print("#3 Deg/Min/Sec to Vector Coordinates")
print("#4 Decimal Degrees to Vector Coordinates using the Haversine Formula")
print()

while user_choice not in sentinel_values:
    user_choice = str.lower(str(input("Choose an option: ")))
    if user_choice == "1":
        take_input("dms_to_decimal")
    elif user_choice == "2":
        take_input("decimal_to_vector")
    elif user_choice == "3":
        take_input("dms_to_vector")
    elif user_choice == "4":
        take_input("haversine_vector")
    elif user_choice not in sentinel_values:
       print("Invalid option. Please choose again.")
