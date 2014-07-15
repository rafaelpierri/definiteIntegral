Definite Integral
=================

This tool will numerically estimate the definite integral of a power function, like:

<math xmlns="http://www.w3.org/1998/Math/MathML">
    <msubsup>
        <mo>&int;</mo>
        <mi>a</mi>
        <mi>b</mi>
    </msubsup>
    <msup>
        <mi>x</mi>
        <mi>y</mi>
    </msup>
    <mo>d<mi>x</mi></mo>
</math>

Provide it with the desired exponent _y_, and have fun!

You can also provide some non-default inferior and superior bounds (_a_ and _b_, respectivelly), and precision (i.e. the estimated result should not be further to the actual result than this value). You can also run this program with several processes (see below).

## Usage

```text
usage: main.py [-h] [-a LOWER] [-b UPPER] [-p PRECISION] [-f FORK] expression

Calculates the definite integral of a power function.

positional arguments:
  exponent              Power function's exponent.

optional arguments:
  -h, --help            show this help message and exit
  -a LOWER, --lower LOWER
                        Lower integration bound (default: 0.0).
  -b UPPER, --upper UPPER
                        Upper integration bound (defualt: 1.0).
  -p PRECISION, --precision PRECISION
                        Calculation precision (default: 1e-4).
  -f FORK, --fork FORK  Number of worker processes.
```


