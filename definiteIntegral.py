from multiprocessing import Pool

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

def definedIntegral(infLimit, supLimit, precision, expoent):
    i = 0
    array = []
    tmp = 0
    while(infLimit < supLimit):
        tmp = ((power(expoent, infLimit) + power(expoent, infLimit+precision))/2)*precision
        array.append(tmp)
        infLimit = infLimit + precision
        i = i + 1
    return sum(array)

def _defined_integral_task(args):
    'Expands arguments received from Pool to our API.'
    return definedIntegral(*args)

def mp_defined_integral(exponent, lower=0, upper=1, precision=0.001, workers=1):
    'Numerically calculates a defined integral using several processes.'
    if workers == 1:
        return definedIntegral(lower, upper, precision, exponent)

    # split by equal width x-range
    width = float(upper - lower) / workers
    tasks = tuple(lower + i * width for i in range(workers)) + (upper,)
    tasks = tuple((a, b, precision, exponent) 
                  for (a, b) in zip(tasks[:-1], tasks[1:]))

    # run all tasks and aggregate results
    pool = Pool(processes=workers)
    return sum(pool.map(_defined_integral_task, tasks))

