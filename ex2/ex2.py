def gas_master():

    gas = input("           ######################\n"
                "           Crap-Ton-O-Conversions!\n"
                "           ######################\n\n"

                "Type a number representing gallons of gas you want to convert: ")

    # eval(gas)
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    # Third Rendition of Loop
    # ~~~~~~~~~~~~~~~~~~~~~~~~
    while True:
        try:
            eval(gas)
        except NameError:
            gas = input("Must enter a number: ")
            continue
        else:
            break

    floaty_gas = float(gas)
    print("returned with: " + str(floaty_gas))
    print(type(floaty_gas))

    gas_liters = floaty_gas * 3.7854  # 1 gallon = 3.7854 liters
    barrels = floaty_gas / 42.0  # 1 barrel requires 42 gallons of gas
    co2 = floaty_gas * 20.0  # 1 gallon gas produces 20 pounds CO2
    ethanol_btu_equiv = floaty_gas * 115000.0/75700.0  # gas = 115000 BTU, ethanol = 75700 BTU (British Thermal Units)
    us_dollars = floaty_gas * 1.97  # $1.97 is current price of gas!! (5yrs ago is was over $4.00 !

    print("Aight! The numbers of gallons of gas you gave: {} \n Behold the magic!!\n".format(floaty_gas))
    print("{} gallons is the equivalent of {} liters".format(floaty_gas, round(gas_liters)))
    print("{} gallons of gasoline produces {} barrels of oil".format(floaty_gas, barrels))
    print("{} gallons of gasoline produces {} pounds of CO2. Wow!".format(floaty_gas, co2))
    print("{} gallons of gasoline is energy equivalent to {} gallons of ethanol".format(floaty_gas, ethanol_btu_equiv))
    print("{} gallons of gasoline requires {} US dollars".format(floaty_gas, us_dollars))


gas_master()


# ~~~~~~~~~~~~~~~~~~
# First Rendition
# ~~~~~~~~~~~~~~~~~~
#     print(gassy)
#     print(type(gassy))
#
#     while True:
#         try:
#             float(eval(gassy))
#             print("What is going on??")
#             print(type(gassy))
#             break
#         except ValueError:
#             gassy = eval(input("Sorry pal, need ta enter a number: "))
#             print("NameError: Gassy")
#             print("NameError: Type" + gassy)
#             string_checker(gassy)
#             continue
#         except NameError:
#             gassy = eval(input("Sorry pal, need ta enter a number: "))
#             print("NameError: Gassy")
#             print("NameError: Type" + gassy)
#             string_checker(gassy)
#             continue
#         else:
#                 break
#
#         print("Made it out!!")
#         return float(gassy)

# ~~~~~~~~~~~~~~~~~~
# Second Rendition
# ~~~~~~~~~~~~~~~~~~
# def string_checker(gassy):
#     gasper = eval(gassy)
#     print("Eval gassy: " + str(gasper))
#     while True:
#         if float(gasper):
#             floaty_gas = gasper
#             break
#         elif int(gasper):
#             floaty_gas = float(gasper)
#             break
#         else:
#             gasper = input("Gonna have ta enter a number: ")
#             continue
#
#     return floaty_gas