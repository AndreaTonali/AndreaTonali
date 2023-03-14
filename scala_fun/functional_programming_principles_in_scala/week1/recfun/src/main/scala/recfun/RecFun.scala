package recfun

import scala.collection.mutable.ListBuffer

object RecFun extends RecFunInterface:

  def main(args: Array[String]): Unit =
    println("Pascal's Triangle")
    for row <- 0 to 10 do
      for col <- 0 to row do
        print(s"${pascal(col, row)} ")
      println()

  /**
   * Exercise 1
   *     1
   *    1 1
   *   1 2 1
   *  1 3 3 1
   * 1 4 6 4 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0 || c == r) 1
    else pascal(c - 1, r - 1) + pascal(c, r - 1)
  }

  /**
   * Exercise 2
   * Write a recursive function which verifies the balancing of parentheses in a string,
   * which we represent as a List[Char] not a String.
   * For example, the function should return true for the following strings:
   *  - (if (zero? x) max (/ 1 x))
   *  - I told him (that it's not (yet) done). (But he wasn't listening)
   * The function should return false for the following strings:
   *  - :-)
   *  - ())(
   */
  def balance(chars: List[Char]): Boolean = {
    def f(chars: List[Char], numOpens: Int): Boolean = {
      if (chars.isEmpty) {
        numOpens == 0
      } else {
        val h = chars.head
        val n =
          if (h == '(') numOpens + 1
          else if (h == ')') numOpens - 1
          else numOpens
        if (n >= 0) f(chars.tail, n)
        else false
      }
    }
    f(chars, 0)
  }

  /**
   * Exercise 3
   * Write a recursive function that counts how many different ways you
   * can make change for an amount, given a list of coin denominations.
   * For example, there are 3 ways to give change for 4
   * if you have coins with denomiation 1 and 2: 1+1+1+1, 1+1+2, 2+2.
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    def f(lastMaxCoin: List[(Int, Int)], count: Int): Int = {
      if (lastMaxCoin.isEmpty) {
        count
      } else {
        val b = ListBuffer[(Int, Int)]()
        var newCount = count
        for ((lastMaxCoin, total) <- lastMaxCoin) {
          if (total < money) {
            for (c <- coins) {
              if (c >= lastMaxCoin) {
                val e = (c, total + c)
                b += e
              }
            }
          } else if (total == money) {
            newCount += 1
          }
        }

        f(b.toList, newCount)
      }
    }

    val b = coins.map { c => (c, c) }
    f(b, 0)
  }

