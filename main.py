from definiteIntegral import definedIntegral

if __name__ == '__main__':
    print("This software will calculate the Integral of a power function.")
    infLimit = float(raw_input("Write the lower limit:"))
    supLimit = float(raw_input("Write the upper limit:"))
    precision= float(raw_input("Write precision:"))
    expoent = int(raw_input("Write a power:"))

    print(definedIntegral(infLimit, supLimit, precision, expoent))

