
a + b ^? c ?^ d  less a ==> b | c

/*

Precedence Rules
The precedence of an operator is determined by its first character.
The following table lists the characters in increasing order of priority

precedence:

    (all letters)
 ^  |
 |  ^
 |  &
 |  < >
 |  = !
 |  :
 |  + -
 |  * / %
    (all other special characters)

*/

((a + b) ^? (c ?^ d)) less((a ==> b) | c)