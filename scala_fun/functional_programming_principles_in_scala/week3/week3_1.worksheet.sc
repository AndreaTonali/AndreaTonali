
// type IntSet = scala.collection.immutable.Set[Int]

abstract class IntSet:
    def incl(x: Int): IntSet
    def containes(x: Int): Boolean
    def union(s: IntSet): IntSet

object IntSet:
  def apply(): IntSet = Empty
  def apply(x: Int): IntSet = Empty.incl(x)
  def apply(x: Int, y: Int): IntSet = Empty.incl(x).incl(y)

object Empty extends IntSet:
    def containes(x: Int): Boolean = false
    def incl(x: Int): IntSet = NonEmpty(x, Empty, Empty)
    def union(s: IntSet): IntSet = s

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet:

    def containes(x: Int): Boolean =
        if x < elem then left.containes(x)
        else if x > elem then right.containes(x)
        else true
    
    def incl(x:Int): IntSet =
        if x < elem then NonEmpty(elem, left.incl(x), right)
        else if x > elem then NonEmpty(elem, left, right.incl(x))
        else this
    
    def union(s: IntSet): IntSet =
        left.union(right).union(s).incl(elem)

end NonEmpty


val a = IntSet.apply()
val b = IntSet.apply(1)
IntSet.apply(1,2)

NonEmpty(1, a, b)

//Type Parameters example 

def listOfDuplicates[A](x: A, length: Int): List[A] = {
  if (length < 1)
    Nil
  else
    x :: listOfDuplicates(x, length - 1)
}
println(listOfDuplicates[Int](3, 4))  // List(3, 3, 3, 3)
println(listOfDuplicates("La", 8))  // List(La, La, La, La, La, La, La, La)



def nth[T](xs: List[T], n: Int): T = {
    if xs.isEmpty then throw IndexOutOfBoundsException()
    else if n == 0 then xs.head
    else nth(xs.tail, n - 1)
}

print(nth(List("a", "b", "c"), 2)) // c
print(nth(List(1, 2, 3), 2)) // 3
// print(nth(List(1, 2), 2)) // IndexOutOfBoundsException

// Defining HashCode

object Main extends App {

// string hashcode  
  val result = "Hello".hashCode()
  println(result)

// integer hashcode  
  val result1 = 123.hashCode()
  println(result1)
}

