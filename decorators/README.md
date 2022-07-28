# **The Decorators**

1. Cache decorator is presented. If the function arguments are the same, the calculation is not repeated. 
The value is taken from the cache. 
```
@decor_cache
def f_1(a, b, c):
    return a * b * c

@decor_cache
def f_2(a, b, c):
    return a * b * c

@decor_cache
def f_3(a, b, c):
    return a * b * c
```