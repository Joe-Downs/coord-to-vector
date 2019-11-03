#dms_to_decimal() converts degress/minutes/seconds to decimal degrees
def dms_to_decimal():
    print("Successfully converted DMS to decimal!\n")
    
#decimal_to_vector() converts two sets of decimal degress to a vector
def decimal_to_vector():
    print("Successfully converted decimal to vector!\n")

#dms_to_vector() converts two sets of DMS to a vector
def dms_to_vector():
    print("Successfully converted DMS to vector!\n")

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
        dms_to_decimal()
    elif user_choice == "2":
        decimal_to_vector()
    elif user_choice == "3":
        dms_to_vector()
    elif user_choice not in sentinel_values:
       print("Invalid option. Please choose again.")
