def solve(base, sales):
    print(f"TOTAL = R$ {base + 0.15*sales:.2f}")

name = input()
base = float(input())
sales = float(input())

solve(base, sales)