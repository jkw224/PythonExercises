city_temp = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}

for key, value in city_temp.items():
    val = int(value[:-2])
    if value[-1] == ("F" or "f"):
        print("In %s it is %s degrees Fahrenheit\n\twhich is equivalent to %d degress Celsius" % (key, value[:-2], (val - 32) * 5/9))
    elif value[-1] == ("C" or "c"):
        print("In %s it is %s degrees Celsius\n\twhich is equivalent to %d degress Fahrenheit" % (key, value[:-2], (val * (9/5))+32))
    else:
        print("-1")