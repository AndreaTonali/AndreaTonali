class Rational(x: Int, y: Int):
    def number = x
    def denom = y

    def add(r: Rational) =
        Rational(number * r.denom + r.number * denom,
                   denom * r.denom)
        
    def mul(r: Rational) =
        Rational(number * r.number, denom * r.denom)
    
    def neg = Rational(-number, denom)

    def sub(r: Rational) = add(r.neg)
    
    override def toString = s"$number/$denom"

end Rational

val x = Rational(1, 3)
val y = Rational(5, 7)
val z = Rational(3, 2)

x.add(y).mul(z)
x.sub(y).sub(z)


