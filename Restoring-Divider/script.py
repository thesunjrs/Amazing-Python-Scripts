def main():
    A = ""
    Q = int(input("Enter the Dividend => "))
    M = int(input("Enter the Divisor => "))
    Q = bin(Q).replace("0b", "")
    M = bin(M).replace("0b", "")
    size = 0
    """
    This part makes the initialisation of required for the Restoring Division to occur.
    Which includes:
    1) Setting an extra to M compared to A
    2) Filling up A with zeroes
    3) Setting the size
    """
    if len(M) == len(Q):
        M = f"0{M}"
    elif len(Q) > len(M):
        how = len(Q) - len(M)
        for _ in range(how):
            M = f"0{M}"
    else:
        how = len(M) - len(Q)
        for _ in range(how - 1):
            Q = f"0{Q}"
    for _ in range(len(M)):
        A = f"0{A}"
    size = len(M)
    """
    The Calculation and Line by Line Display begins from here
    """
    A = f"0{A}"
    M = f"0{M}"
    M2 = twos_complement(M)
    print("Solution=>")
    print("A=", A)
    print("Q=", Q)
    print("M=", M)
    print("M2=", M2)
    printer = "A\t\tQ\t\tSize\t\tSteps"
    print(printer)
    # Printing the Initialisation step
    printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tInitialization"
    print(printer)
    """
    The division will be taking place until the size of the Divisor becomes zero
    """
    for _ in range(size, 0, -1):
        """
        Left Shift Operation
        """
        A = A[1:] + Q[0]
        Q = Q[1:]
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tLeft Shift"
        print(printer)
        """
        Subtraction
        """
        A = add(A, M2)
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tSubtraction"
        print(printer)
        """
        Bit Checking and AAddition if required
        """
        if A[0] == '0':
            Q = f"{Q}1"
        else:
            Q = f"{Q}0"
            A = add(A, M)
        printer = A + "\t\t" + Q + "\t\t" + str(size) + "\t\tBit Checking"
        print(printer)
        """
        Decreasing Size
        """
        size -= 1
        printer = A + "\t\t" + Q + "\t\t" + str(size)
        print(printer)


def twos_complement(n):
    a = ""
    c = ""
    """
    Performing 1's Complement by changing all zeroes to one
    """
    for i in range(len(n)):
        a = f"{a}0" if n[i] == '1' else f"{a}1"
    """
    Performing 2's complement by adding 1 to the 1's complement
    """
    d = ""
    for _ in range(len(a) - 1):
        d = f"{d}0"
    d = f"{d}1"
    c = add(a, d)
    return c


def add(x, y):
    """
    Binary Adddition bing carried out
    """
    carry = ""
    result = ""
    carry = "0"
    for i in range(len(x) - 1, -1, -1):
        a = carry[0]
        b = x[i]
        c = y[i]

        if a == b and b == c and c == '0':
            result = f"0{result}"
            carry = "0"
        elif a == b and b == c and c == '1':
            result = f"1{result}"
            carry = "1"
        elif a == '1' and b == c and c == '0':
            result = f"1{result}"
            carry = "0"
        elif a == '0' and b == '1' and c == '0':
            result = f"1{result}"
            carry = "0"
        elif a == '0' and b == '0' and c == '1':
            result = f"1{result}"
            carry = "0"
        elif a == '0' and b == '1' and c == '1':
            result = f"0{result}"
            carry = "1"
        elif a == '1' and b == '0' and c == '1':
            result = f"0{result}"
            carry = "1"
        elif a == '1' and b == '1' and c == '0':
            result = f"0{result}"
            carry = '1'
    return result


main()
