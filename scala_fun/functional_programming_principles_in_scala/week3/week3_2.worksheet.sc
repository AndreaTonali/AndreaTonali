/*

https://stackoverflow.com/a/9585097/5877387

Yes, all methods which are not final (static is also a bit different form the rest), 
can be overridden, unless the class itself is declared final. 
Abstract methods are only used if you do not provide any implementation in the base class.
*/

abstract class Nat:
    def isZero: Boolean
    def predecessor: Nat
    def successor: Nat
    def + (that: Nat): Nat
    def - (that: Nat): Nat
end Nat

object Zero extends Nat:
    def isZero: Boolean = true
    def predecessor: Nat = ???
    def successor: Nat = Succ(this)
    def + (that: Nat): Nat = that
    def - (that: Nat): Nat =  if that.isZero then this else ???
    override def toString = "Zero"
end Zero

class Succ(n: Nat) extends Nat:
    def isZero: Boolean = false
    def predecessor: Nat = n
    def successor: Nat = Succ(this)
    def + (that: Nat): Nat = Succ(n + that)
    def - (that: Nat): Nat = if that.isZero then this else n - that.predecessor
    override def toString = s"Succ($n)"

end Succ

val two = Succ(Succ(Zero))
val tree = Succ(Succ(Succ(Zero)))
val one = Succ(Zero)

two + one
two - one
// one - two

