from argparse import ArgumentParser

from definiteIntegral import mp_defined_integral


class PowerFunction(object):
    '''
    Calculates a power function. Functions defined using context variables
    cannot be pickled by the multiprocessing API for inter-process 
    communication. On the other hand, objects (like instances of this class) 
    and functions without context variables (like the ones used in the unit 
    tests) can be pickled.
    '''

    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, x):
        return x ** self.exponent


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

    print mp_defined_integral(PowerFunction(args.exponent), 
            args.lower, args.upper, args.precision, args.fork)

