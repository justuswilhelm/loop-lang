# LOOP language interpreter
An interpreter for the LOOP language written in Python.

## Sample
```
x1 := 1;
x2 := 20;
x0 := x1 + 0;
LOOP x2 DO
   x0 := x0 + 1;
END
x0;
```

will output

```
21
```
