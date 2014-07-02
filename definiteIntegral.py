from math import floor
from multiprocessing import Pool

def defined_integral(exponent, lower=0.0, upper=1.0, precision=0.0001):
    n = int(floor(float(upper - lower) / precision))
    x = tuple(lower + i * precision for i in range(n))
    y = map(lambda x: x ** exponent, x)
    a = map(lambda y0, y1: (y0 + y1) * precision / 2.0, y[:-1], y[1:])
    last = (y[-1] + upper ** exponent) * (upper - x[-1]) / 2.0
    return sum(a) + last 

def _defined_integral_task(args):
    'Expands arguments received from Pool to our API.'
    return defined_integral(*args)

def mp_defined_integral(exponent, lower=0.0, upper=1.0, precision=0.0001, workers=4):
    'Numerically calculates a defined integral using several processes.'

    if workers == 1:
        return defined_integral(exponent, lower, upper, precision)

    # split by equal width x-range
    width = float(upper - lower) / workers
    tasks = tuple(lower + i * width for i in range(workers)) + (upper,)
    tasks = tuple((exponent, a, b, precision) 
                  for (a, b) in zip(tasks[:-1], tasks[1:]))

    # run all tasks and aggregate results
    pool = Pool(processes=workers)
    return sum(pool.map(_defined_integral_task, tasks))

