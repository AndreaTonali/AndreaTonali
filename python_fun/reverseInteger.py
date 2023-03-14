

def reverse(m: int):
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    :param m: int
    :rtype: int
    """
    y = -2147483648  # -2**31
    z = 2147483647  # 2**31 -1
    x = 0
    n = m
    if m < 0:
        n *= -1
    while n > 0:
        x *= 10
        x += n % 10
        n /= 10
    if y < x > z:
        return 0
    if m < 0:
        return "-" + "x"
    else:
        return x
