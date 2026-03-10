start = int(input())
end = int(input())

TOKEN_TUPLE = tuple(range(start, end + 1))

EVEN_TUPLE = tuple(x for x in TOKEN_TUPLE if x % 2 == 0)
ODD_TUPLE = tuple(x for x in TOKEN_TUPLE if x % 2 != 0)

REVERSED_EVEN = EVEN_TUPLE[::-1]
REVERSED_ODD = ODD_TUPLE[::-1]

EVEN_LIST = list(REVERSED_EVEN)
ODD_LIST = list(REVERSED_ODD)

print(f"Tokens from {start} to {end}")
print("EVEN_TUPLE:", EVEN_TUPLE)
print("ODD_TUPLE:", ODD_TUPLE)
print("Reversed EVEN_TUPLE:", REVERSED_EVEN)
print("Reversed ODD_TUPLE:", REVERSED_ODD)
print("List from Reversed EVEN_TUPLE:", EVEN_LIST)
print("List from Reversed ODD_TUPLE:", ODD_LIST)