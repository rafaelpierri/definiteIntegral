# Full syntax

```text
EXPRESSION := ADDSUB
ADDSUB := ADDSUB ('+' | '-') MULDIV | MULDIV
MULDIV := MULDIV ('*' | '/') POWER | POWER
POWER := UNARY '^' POWER | UNARY
UNARY := ('+' | '-') PAR_EXPR | PAR_EXPR
PAR_EXPR := '(' ADDSUB ')' | CONSTANT | VARIABLE
CONSTANT := number
VARIABLE := name
```

```text
EXPRESSION := ADDSUB
ADDSUB := MULDIV (('+' | '-') MULDIV)*
MULDIV := POWER (('*' | '/') POWER)*
POWER := UNARY ('^' UNARY)*
UNARY := ('+' | '-')? PAR_EXPR
PAR_EXPR := '(' ADDSUB ')' | CONSTANT | VARIABLE
CONSTANT := number
VARIABLE := name
```

# Syntax Analysis: First Token

## 1st pass

```text
first(EXPRESSION) = first(ADDSUB)
first(ADDSUB) = first(MULDIV)
first(MULDIV) = first(POWER)
first(POWER) = first(UNARY)
first(UNARY) = '+', '-', first(PAR_EXPR)
first(PAR_EXPR) = '(', first(CONSTANT), first(VARIABLE)
first(CONSTANT) = number
first(VARIABLE) = name
```

## Final pass

```text
first(EXPRESSION) = '+', '-', '(', number, name
first(ADDSUB) = '+', '-', '(', number, name
first(MULDIV) = '+', '-', '(', number, name
first(POWER) = '+', '-', '(', number, name
first(UNARY) = '+', '-', '(', number, name
first(PAR_EXPR) = '(', number, name
first(CONSTANT) = number
first(VARIABLE) = name
```

# Syntax Analysis: Follow Token

## 1st pass

```text
follow(EXPRESSION) = <end>
follow(ADDSUB) = '+', '-', ')', follow(EXPRESSION)
follow(MULDIV) = '*', '/', follow(ADDSUB)
follow(POWER) = follow(MULDIV)
follow(UNARY) = '^', follow(POWER)
follow(PAR_EXPR) = follow(UNARY)
follow(CONSTANT) = follow(PAR_EXPR)
follow(VARIABLE) = follow(PAR_EXPR)
```

## Final pass

```text
follow(EXPRESSION) = <end>
follow(ADDSUB) = '+', '-', ')', <end>
follow(MULDIV) = '*', '/', '+', '-', ')', <end>
follow(POWER) = '*', '/', '+', '-', ')', <end>
follow(UNARY) = '^', '*', '/', '+', '-', ')', <end>
follow(PAR_EXPR) = '^', '*', '/', '+', '-', ')', <end>
follow(CONSTANT) = '^', '*', '/', '+', '-', ')', <end>
follow(VARIABLE) = '^', '*', '/', '+', '-', ')', <end>
```

