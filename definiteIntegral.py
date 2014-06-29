from multiprocessing import Process, Pipe

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
    i = 0
    result = 0
    while(i < array.__len__()):
        result = result + array[i]
        i = i + 1
    return result

def definedIntegral(infLimit, supLimit, precision, expoent, connection):
    i = 0
    array = []
    tmp = 0
    while(infLimit < supLimit):
        tmp = ((power(expoent, infLimit) + power(expoent, infLimit+precision))/2)*precision
        array.append(tmp)
        infLimit = infLimit + precision
        i = i + 1
    connection.send(sum(array))
    connection.close()
    
print("This software will calculate the Integral of a power function.")
infLimit = float(raw_input("Write the lower limit:"))
supLimit = float(raw_input("Write the upper limit:"))
precision= float(raw_input("Write precision:"))
expoent = int(raw_input("Write a power:"))
workersNumber = int(raw_input("Write quantity of worker processes:"))

workers = []

i = 0
while(i < workersNumber):
    parent_conn, child_conn = Pipe()	
    p = Process(target=definedIntegral, args=(infLimit+((supLimit-infLimit)/workersNumber)*i, infLimit+((supLimit-infLimit)/workersNumber)*(i+1), precision, expoent, child_conn,))
    p.start()   
    workers.append({'parent': parent_conn, 'child': child_conn, 'process': p})
    i = i + 1	

i = 0
array = []
while(i < workersNumber):
    array.append(workers[i]['parent'].recv())
    workers[i]['process'].join()
    i = i + 1

print(sum(array))
