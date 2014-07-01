from multiprocessing import Pool

def defined_integral(exponent, lower=0.0, upper=1.0, precision=0.001):
    area = 0
    while(lower < upper):
        area += ((lower ** exponent + (lower + precision) ** exponent)) * precision / 2
        lower = lower + precision
    return area

def _defined_integral_task(args):
    'Expands arguments received from Pool to our API.'
    return defined_integral(*args)

def mp_defined_integral(exponent, lower=0.0, upper=1.0, precision=0.001, workers=1):
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

