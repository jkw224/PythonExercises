# Two questions:
# 1) Where does "none" come from in output of type test?
# 2) How to exit try/except loop in main() if I enter a string (e.g. "r")


def main():
    mph = input("Please enter a speed in miles per hour!: ")

    test = type_test(mph)
    print(test)

    print("\nSPEED CONVERSIONS!...")

    # Catch if user_input == string
    while True:
        try:
            float(mph)
        except ValueError:
            user_input = input("Naughty naughty, gotta enter a number: ")
            mph = user_input
            continue
        else:
            break


    # Calls to conversion functions
    floaty_mph = float(mph)
    barleycorn_per_day = barleycorn_day(floaty_mph)
    furlong_per_fortnight = furlong_fortnight(floaty_mph)
    percentage_of_mach1 = mach1(floaty_mph)
    percentage_speed_of_light = speed_of_light(floaty_mph)

    # Output
    print("Origin speed in mph is: {}".format(floaty_mph))
    print("Converted to barleycorn/day is: {}".format(barleycorn_per_day))
    print("Converted to furlongs/fortnight is: {}".format(furlong_per_fortnight))
    print("Converted to percent speed of Mach1: {}%".format(percentage_of_mach1))
    print("Converted to the percentage of the speed of light is: {}%".format(percentage_speed_of_light))


def type_test(mph_input):
    try:
        mph = eval(mph_input)
    except NameError:
        message = print("Test passed\n  eval(mph) of type string == NameError (in try/except loop)")
    else:
        message = print("Test passed\n  eval(mph) type:" + str(type(mph)))

    return str(message)


def barleycorn_day(mph):
    # Barleycorn/day Variables
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    input_miles = mph
    hour = 1.0
    _24hours = 24.0
    day = 1.0
    _1609meters = 1609.34
    mile = 1.0
    _117barleycorns = 117.647
    meter = 1.0

    # Barleycorn/day Conversion
    # | 117 barleycorns/ |  x  | 1609 meters/ |  x  | input_miles/ |  x  | 24hours/ |  =  barleycorns/
    # |   1 meter        |     |    1 mile    |     | 1 hour       |     | 1 day    |     day
    barleycorn_per_day = (_117barleycorns/meter) * (_1609meters/mile) * (input_miles/hour) * (_24hours/day)

    return barleycorn_per_day


def furlong_fortnight(mph):
    # Furlong/fortnight Variables
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    input_miles = mph
    furlong = 1.0
    _220yards = 220.0
    _1760yards = 1760.0
    _336hours = 336.0
    fortnight = 1.0
    mile = 1.0
    hour = 1.0

    # Furlong/fortnight Conversion
    # | 1 furlong/ |  x  | 1760 yards/ |  x  | input_miles/ |  x  | 336 hours/  |  =  furlong/
    # | 220 yards  |     | 1 mile      |     | 1 hour       |     | 1 fortnight |     fortnight
    furlong_per_fortnight = (furlong/_220yards) * (_1760yards/mile) * (input_miles/hour) * (_336hours/fortnight)

    return furlong_per_fortnight


def mach1(mph):
    # Mach number Variables
    # ~~~~~~~~~~~~~~~~~~~~~~
    input_miles = mph
    _5280feet = 5280.0
    _3600seconds = 3600.0
    _mach1 = 1300.0/1.0 # 1300ft per 1second
    mile = 1.0
    hour = 1.0

    # Mach number Conversion
    # | 5280 feet/ |  x  | input_miles/ |  x  | 1 hour/      |  =  feet/    divided   1300ft/  (% speed of Mach1)
    # | 1 mile     |     | 1 hour       |     | 3600 seconds |     second     by      1 second
    feet_per_second = (_5280feet/mile) * (input_miles/hour) * (hour/_3600seconds)
    mach1_speed = feet_per_second / _mach1
    percentage_of_mach1 = mach1_speed * 100

    return percentage_of_mach1


def speed_of_light(mph):
    # Speed of light Variables
    # ~~~~~~~~~~~~~~~~~~~~~~~~~
    input_miles = mph
    _1609meters = 1609.34
    mile = 1.0
    _3600seconds = 3600.0
    hour = 1.0
    sol = 299792458.0  # speed of light = 299,792,458 meters per second


    # Speed of light Conversion
    # | 1609 meters/ |  x  | input_miles/ |  x  | 1 hour/      |  =  feet/    divided   1300ft/  (% speed of Mach1)
    # | 1 mile       |     | 1 hour       |     | 3600 seconds |     second     by      1 second
    feet_per_second = (_1609meters/mile) * (input_miles/hour) * (hour/_3600seconds)
    percentage_of_speed_of_light = (feet_per_second / sol) * 100

    return percentage_of_speed_of_light


main()