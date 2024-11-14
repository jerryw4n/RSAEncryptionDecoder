# RSA Decryption Script

This Python script performs RSA decryption by calculating the private key `d` from the public key components and decrypting a series of ciphertext blocks to reveal the original plaintext message. The script works by factoring the modulus `n` to obtain the prime factors `p` and `q`, computing Euler's Totient function, and using the modular inverse of the public exponent `e` to find the private key `d`.

# RSA Decryption Script Breakdown

# 1. Given Values
n := The modulus used in the public key.
e := The public exponent used in the encryption process.
ciphertextBlocks := The encrypted blocks of the message.

# 2. Functions

# getFactor(n)
# A function that uses the Floyd's cycle-finding algorithm to factor the modulus n into its prime factors p and q.
getFactor: 
	@echo "Factorizing n into p and q using Floyd's cycle-finding algorithm."

# gcd(a, b)
# A function to compute the greatest common divisor of two numbers, used by getFactor().
gcd:
	@echo "Computing GCD of two numbers, used in getFactor."

# computeTotient(p, q)
# Computes Euler’s Totient function φ(n), where φ(n) = (p - 1) * (q - 1).
computeTotient:
	@echo "Computing Euler’s Totient function φ(n) = (p - 1) * (q - 1)."

# computePrivate(e, phi_n)
# Computes the private key d using the modular inverse of e modulo φ(n).
computePrivate:
	@echo "Computing private key d using the modular inverse of e modulo φ(n)."

# decryptBlock(c, d, n)
# Decrypts a ciphertext block c using the formula m = c^d mod n.
decryptBlock:
	@echo "Decrypting a ciphertext block c using the formula m = c^d mod n."

# toText(m)
# Converts the decrypted integer m (interpreted in base-26) back into a readable string of characters.
toText:
	@echo "Converting decrypted integer m to a readable string."

# 3. Main Execution Flow

# Factor n
factorN:
	@echo "Factorizing n into p and q."

# Compute Totient φ(n)
computeTotientN:
	@echo "Calculating Euler’s Totient function φ(n) using p and q."

# Compute Private Key d
computePrivateKey:
	@echo "Calculating private key d using modular inverse of e modulo φ(n)."

# Decrypt Ciphertext
decryptCiphertext:
	@echo "Decrypting ciphertext blocks c using d and n, and converting to text."
