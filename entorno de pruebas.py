def f(n):
    s=str(n)
    if len(s) ==1:
        return s
    return s[-1] + f(int(s[:-1]))
print(f(15538895))