# =====================================================
#              LOGIC GATES USING PYTHON
# =====================================================

# AND Gate
def AND_gate(a, b):
    return a & b


# OR Gate
def OR_gate(a, b):
    return a | b


# NOT Gate
def NOT_gate(a):
    return 1 - a


# NAND Gate
def NAND_gate(a, b):
    return 1 - (a & b)


# NOR Gate
def NOR_gate(a, b):
    return 1 - (a | b)


# XOR Gate
def XOR_gate(a, b):
    return a ^ b


# XNOR Gate
def XNOR_gate(a, b):
    return 1 - (a ^ b)


# -----------------------------------------------------
# Display Truth Table
# -----------------------------------------------------

print("=" * 70)
print("                 LOGIC GATES")
print("=" * 70)

print("\nTruth Table")
print("-" * 70)

print("A  B  AND  OR  NAND  NOR  XOR  XNOR")
print("-" * 70)

for a in [0, 1]:
    for b in [0, 1]:

        and_result = AND_gate(a, b)
        or_result = OR_gate(a, b)
        nand_result = NAND_gate(a, b)
        nor_result = NOR_gate(a, b)
        xor_result = XOR_gate(a, b)
        xnor_result = XNOR_gate(a, b)

        print(
            a,
            b,
            "   ",
            and_result,
            "   ",
            or_result,
            "   ",
            nand_result,
            "    ",
            nor_result,
            "   ",
            xor_result,
            "    ",
            xnor_result
        )


# -----------------------------------------------------
# NOT Gate Truth Table
# -----------------------------------------------------

print("\n")
print("=" * 40)
print("             NOT GATE")
print("=" * 40)

print("A    NOT A")
print("-" * 20)

for a in [0, 1]:

    print(
        a,
        "     ",
        NOT_gate(a)
    )


# -----------------------------------------------------
# User Input
# -----------------------------------------------------

print("\n")
print("=" * 50)
print("       LOGIC GATE CALCULATOR")
print("=" * 50)

a = int(input("Enter first input A (0 or 1): "))
b = int(input("Enter second input B (0 or 1): "))


# Check whether input is valid
if a not in [0, 1] or b not in [0, 1]:

    print("\nInvalid input!")
    print("Please enter only 0 or 1.")

else:

    print("\nInput A =", a)
    print("Input B =", b)

    print("\nGate Outputs")
    print("-" * 40)

    print("AND  =", AND_gate(a, b))
    print("OR   =", OR_gate(a, b))
    print("NAND =", NAND_gate(a, b))
    print("NOR  =", NOR_gate(a, b))
    print("XOR  =", XOR_gate(a, b))
    print("XNOR =", XNOR_gate(a, b))

    print("\nNOT Operations")
    print("-" * 40)

    print("NOT A =", NOT_gate(a))
    print("NOT B =", NOT_gate(b))


# -----------------------------------------------------
# Boolean Expression Examples
# -----------------------------------------------------

print("\n")
print("=" * 50)
print("       BOOLEAN LOGIC EXPRESSIONS")
print("=" * 50)

if a in [0, 1] and b in [0, 1]:

    expression1 = AND_gate(a, b)

    expression2 = OR_gate(a, b)

    expression3 = NOT_gate(a)

    expression4 = NOT_gate(b)

    print("A AND B =", expression1)
    print("A OR B  =", expression2)
    print("NOT A   =", expression3)
    print("NOT B   =", expression4)


# -----------------------------------------------------
# Final Message
# -----------------------------------------------------

print("\n")
print("=" * 50)
print("       LOGIC GATE SIMULATION COMPLETED")
print("=" * 50)

print("\nGates simulated:")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. NAND")
print("5. NOR")
print("6. XOR")
print("7. XNOR")

print("\n0 = LOW / FALSE")
print("1 = HIGH / TRUE")

print("\nEnd of Program.")
