from sympy import mod_inverse

# Function to get user input for n, e, and ciphertext blocks
def get_input():
    n = int(input("Enter the modulus n: "))
    e = int(input("Enter the public exponent e: "))
    
    ciphertext_blocks = []
    num_blocks = int(input("Enter the number of ciphertext blocks: "))
    for i in range(num_blocks):
        ciphertext_block = int(input(f"Enter ciphertext block {i+1}: "))
        ciphertext_blocks.append(ciphertext_block)
    
    return n, e, ciphertext_blocks

# Factor n to find p and q
def getFactor(n):
    a = 2
    b = 2
    while True:
        # a steps once, b steps twice in the sequence
        a = (a * a + 1) % n
        b = (b * b + 1) % n
        b = (b * b + 1) % n
        # Get the difference between a and b
        diff = a - b
        if diff < 0:
            diff += n
        # Give this a shot!
        factor = gcd(n, diff)
        # Found a factor
        if factor > 1 and factor < n:
            return factor
        # Test failed
        elif factor == n:
            return -1

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Compute Euler’s Totient Function φ(n) = (p - 1) * (q - 1)
def computeTotient(p, q):
    return (p - 1) * (q - 1)

# Calculate private key d, where d ≡ e^(-1) (mod φ(n))
def computePrivate(e, phi_n):
    return mod_inverse(e, phi_n)

# Decrypt each ciphertext block with c^d mod n
def decryptBlock(c, d, n):
    return pow(c, d, n)

# Convert decrypted integer to text (base-26 to characters)
def toText(m):
    text = ""
    while m > 0:
        m, remainder = divmod(m, 26)
        text = chr(remainder + ord('a')) + text
    return text

# Main execution flow
n, e, ciphertextBlocks = get_input()

# Run each function to get p, q, and phi for private key
p = getFactor(n)
print("p =", p)

q = n // p
print("q =", q)

phi = computeTotient(p, q)
print("phi =", phi)

d = computePrivate(e, phi)
print("d =", d)

# Decrypt each ciphertext block and convert to text
plaintext_message = ""
for c in ciphertextBlocks:
    m = decryptBlock(c, d, n)
    plaintext_message += toText(m)

# Output plaintext message
print("Decrypted Message:", plaintext_message)
