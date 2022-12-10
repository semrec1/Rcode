#find square root of a number newtons method
def newton_sqrt(n,howmany):
    approx=0.5*n
    for i in range(howmany):
        betterapprox=0.5*(approx+n/approx)
        approx=betterapprox
    return approx
print(newton_sqrt(10,10))
