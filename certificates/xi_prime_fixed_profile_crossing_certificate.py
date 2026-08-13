#!/usr/bin/env python3
"""Exact-rational crossing certificate for ONE fixed positive xi-prime window profile.

This is intentionally simpler than the Fredholm-optimality certificate.  It proves
for the explicit degree-16 even polynomial V below that

  c_{lambda_lo}(V) < 1/2 < c_{lambda_hi}(V),

where
  lambda_lo = 0.51331975984768,
  lambda_hi = 0.51331975984769.

All theorem comparisons use fractions.Fraction only.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
from math import comb, factorial

LAST = 14
LO = Fraction(51331975984768, 10**14)
HI = Fraction(51331975984769, 10**14)
HALF = Fraction(1, 2)

# x=2s, V(s)=sum_j V[j] x^(2j)
V = (
    Fraction(971155550317656951337483,10**24),
    Fraction(15089410059120446578381,10**24),
    Fraction(-10570820974057940961828,10**24),
    Fraction(-135437250208184551147,10**24),
    Fraction(-988112801997344913,10**24),
    Fraction(-18990426030083130,10**24),
    Fraction(-255720379351603,10**24),
    Fraction(-2563664956391,10**24),
    Fraction(-23009470972,10**24),
)

def d1(m):
    return Fraction(2*4**m*factorial(m-1), factorial(2*m))

def int_power(k):
    return Fraction(0) if k % 2 else Fraction(2, k+1)

def ordered_half(p,q,n):
    total=Fraction(0)
    common=int_power(p+q+n+1)
    for k in range(n+1):
        cc=Fraction(comb(n,k)*((-1)**k),q+k+1)
        boundary=((-1)**(q+k+1))*int_power(p+n-k)
        total += cc*(common-boundary)
    return total

def moment(i,j,n):
    return (ordered_half(2*i,2*j,n)+ordered_half(2*j,2*i,n))/(4*2**n)

def mass(c):
    return sum(c[i]*Fraction(1,2*i+1) for i in range(len(c)))

def energy0(c):
    return sum(c[i]*c[j]*Fraction(1,2*(i+j)+1)
               for i in range(len(c)) for j in range(len(c)))

def qmoment(c,n):
    return sum(c[i]*c[j]*moment(i,j,n)
               for i in range(len(c)) for j in range(len(c)))

def kernel_terms(lam):
    # lambda D1(lambda r) = lambda^2 r - 4 lambda^3 r^2
    #                         + sum d_m lambda^(2m+2) r^(2m+1)
    return [(1,lam**2),(2,-4*lam**3)] + [
        (2*m+1,d1(m)*lam**(2*m+2)) for m in range(1,LAST+1)
    ]

def qform_trunc(c,lam):
    ans=energy0(c)
    for n,aa in kernel_terms(lam):
        ans += aa*qmoment(c,n)
    return ans

def tail_pointwise(lam):
    # Positive omitted series tail, uniformly for 0<=r<=1.
    first=LAST+1
    ratio=Fraction(2*first,(first+1)*(2*first+1))*lam**2
    return d1(first)*lam**(2*first+2)/(1-ratio)

def positive_lower(c):
    # |x|<=1: negative monomials are bounded below by their coefficients;
    # positive nonconstant monomials may be discarded.
    return c[0] + sum(a for a in c[1:] if a < 0)

def c_upper(c,lam):
    # The omitted D1 tail is positive and c>=0, so the full denominator
    # is >= its m<=LAST truncation.
    b=mass(c)
    den=qform_trunc(c,lam)
    assert den > 0
    return lam*b*b/den

def c_lower(c,lam):
    # Tail contribution <= tail_pointwise * (int c)^2 because c>=0.
    b=mass(c)
    den=qform_trunc(c,lam)+tail_pointwise(lam)*b*b
    return lam*b*b/den

def dec(x,digits=70):
    getcontext().prec=digits
    return Decimal(x.numerator)/Decimal(x.denominator)

def main():
    pmin=positive_lower(V)
    assert pmin>0
    upper_lo=c_upper(V,LO)
    lower_hi=c_lower(V,HI)
    assert upper_lo < HALF
    assert lower_hi > HALF
    print('Exact-rational fixed-profile crossing certificate passed.')
    print('V(s) is strictly positive; certified lower bound =', dec(pmin,50))
    print('lambda_lo =', dec(LO,30))
    print('c_lambda_lo(V) <=', dec(upper_lo,70))
    print('1/2 - upper =', dec(HALF-upper_lo,50))
    print('lambda_hi =', dec(HI,30))
    print('c_lambda_hi(V) >=', dec(lower_hi,70))
    print('lower - 1/2 =', dec(lower_hi-HALF,50))
    print('Therefore continuity of lambda -> c_lambda(V) gives a fixed-profile crossing')
    print('0.51331975984768 < lambda_V < 0.51331975984769.')

if __name__ == '__main__':
    main()
