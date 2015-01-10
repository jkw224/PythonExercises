def gas_master():
    gas = input("Crap-ton-O-Conversions! How many gallons-o-gas you gonna convert??")
    floaty_gas = float_converter(gas)

    print("Aight! The numbers of gallons of gas you gave me: {} \n Behold the magic!!".format(floaty_gas))
    print("{} gallons is the equivalent of {}".format(float_gas, gas_liters))
    print("{} gallons of gasoline produces {} barrels of oil").format(floaty_gas, barrels)
    print("{} gallons of gasoline produces {} pounds of CO2. Wow!")
    print("{} gallons of gasoline is energy equivalent to {} gallons of ethanol")
    print("")

def float_converter(gasolina):
    if gasolina.isdigit():
       new_float = float(gasolina)
    else:
        print("Please enter a number")

    return new_float


def conversions():



gas_master()