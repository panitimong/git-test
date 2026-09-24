msg = "Hello World"

print(msg)

def add(x1, x2):
    res = x1 + x2
    return res

def main():
    num1 = 2
    num2 = 3

    total = add(num1, num2)

    print(f"Sum = {total}")

if __name__ == "__main__":
    main()