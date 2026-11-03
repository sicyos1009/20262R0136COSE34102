def gcd(first: int, second: int) -> int:
    while second != 0:
        remainder = first % second
        first = second
        second = remainder
    return first


if __name__ == "__main__":
    first = int(input())
    second = int(input())
    answer = gcd(first, second)
    print("gcd:", answer)
