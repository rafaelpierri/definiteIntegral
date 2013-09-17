def power(expoent, base):
    i = 0
    result = 0
    while (i < expoent):
            if(result==0):
                result = base
            else:
                result = result * base
            i = i + 1
    return result

def sum(array):
    i = 1
    result = 0
    while(i < array.__len__()):
        result = result + array[i]
        i = i + 1
    return result

def definedIntegral(infLimit, supLimit, precision, expoent):
    i = 0
    array = []
    tmp = 0
    while(infLimit < supLimit):
        tmp = ((power(expoent, infLimit) + power(expoent, infLimit+precision))/2)*precision
        array.append(tmp)
        #array.insert(i, tmp) 
        infLimit = infLimit + precision
        i = i + 1
    return sum(array)
    
print("This software will calculate the Integral of a power function.")
infLimit = float(raw_input("Write the lower limit:"))
supLimit = float(raw_input("Write the upper limit:"))
precision= float(raw_input("Write precision:"))
expoent = int(raw_input("Write a power:"))

print(definedIntegral(infLimit, supLimit, precision, expoent))