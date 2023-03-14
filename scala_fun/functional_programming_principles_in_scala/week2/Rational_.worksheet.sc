class Rational(x: Int, y: Int):
    require(y > 0, s"denominator must be positive, was $x/$y")
    def this(x: Int) = this(x, 1)

    private def gcd(a: Int, b: Int): Int =
        if b == 0 then a else gcd(b, a % b)

    def numer = x 
    def denom = y

    def add(r: Rational) = 
        Rational(numer * r.denom + r.numer * denom,
                   denom * r.denom)
    
    def mul(r: Rational) =
        Rational(numer * r.numer, denom * r.denom)
    
    def neg = Rational(-numer, denom)

    def sub(r: Rational) = add(r.neg)

    def less(that: Rational): Boolean = 
        this.numer * that.denom < that.numer * this.denom

    def max(that: Rational): Rational =
        if this.less(that) then that else this
    
    override def toString = s"${numer/gcd(x.abs, y)}/${denom/gcd(x.abs, y)}"
end Rational // The end marker is follwoed by the name that's defined in the defintion that ends at the this point. It must align with the opening keyword (class in this case).

/* 

End markers are also allowed for other constructs.

def sqrt(x: Double): Double =
    ...
end sqrt

If the end markert terminates a conrtol expression such as if, the beginning keyword is repeated.

if x >= 0 then
    ...
else
    ...
end if

*/ 

val x = Rational(1, 3)
val y = Rational(5, 7)
val z = Rational(3, 2)

x.add(y).mul(z)
x.sub(y).sub(z)

Rational(1, 2).less(Rational(2, 3))

