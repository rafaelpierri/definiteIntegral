from argparse import ArgumentParser
from multiprocessing import Process, Pipe

from definiteIntegral import definedIntegral

if __name__ == '__main__':
    argparser = ArgumentParser(description=
            'Calculates the definite integral of a power function.')
    argparser.add_argument('-a', '--lower', default=0.0, type=float,
            help='Lower integration bound (default: 0.0).')
    argparser.add_argument('-b', '--upper', default=1.0, type=float,
            help='Upper integration bound (defualt: 1.0).')
    argparser.add_argument('-p', '--precision', default=1e-4, type=float,
            help='Calculation precision (default: 1e-4).')
    argparser.add_argument('-f', '--fork', default=1, type=int, 
            help='Number of worker processes.')
    argparser.add_argument('exponent', type=float, 
            help='Power function\'s exponent.')
    args = argparser.parse_args()


    workers = []

    i = 0
    while(i < args.fork):
        parent_conn, child_conn = Pipe()
        p = Process(target=definedIntegral,
                    args=(args.lower+((args.upper-args.lower)/args.fork)*i,
                    args.lower+((args.upper-args.lower)/args.fork)*(i+1),
                    args.precision, args.exponent, child_conn,))
        p.start()
        workers.append({'parent': parent_conn, 'child': child_conn, 'process': p})
        i = i + 1

    i = 0
    array = []
    while(i < args.fork):
        array.append(workers[i]['parent'].recv())
        workers[i]['process'].join()
        i = i + 1

    print(sum(array))

