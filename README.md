Definite Integral
=================

This tool numerically estimates the definite integral of a function. The integral must have at most one variable, and is bound between two (numerically) real values. Its value will be estimated by the [trapezoidal rule][trapezoidal-rule], using almost regular spacing given by _p_.

[trapezoidal-rule]: http://en.wikipedia.org/wiki/Trapezoidal_rule

You can provide some non-default inferior and superior bounds (_a_ and _b_, respectivelly), and "precision" (currently, the width of the trapezoid slices).

## Usage

```text
usage: main.py [-h] [-a LOWER] [-b UPPER] [-p PRECISION] [-f FORK] expression

Estimates the definite integral of a single-variable function.

positional arguments:
  expression            Single-variable expression.

optional arguments:
  -h, --help            show this help message and exit
  -a LOWER, --lower LOWER
                        Lower integration bound (default: 0.0).
  -b UPPER, --upper UPPER
                        Upper integration bound (defualt: 1.0).
  -p PRECISION, --precision PRECISION
                        Estimation precision (default: 1e-4).
  -f FORK, --fork FORK  Number of worker processes.
```


