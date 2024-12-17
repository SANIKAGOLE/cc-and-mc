# Define shared parameters
shared_prime = 23  # Replace with a large prime number
shared_base = 5    # Replace with a primitive root modulo shared_prime

# Alice's private key
alice_secret = 6

# Bob's private key
bob_secret = 15

# Alice Sends Bob A = g^a mod p
A = (shared_base**alice_secret) % shared_prime
print(f"Alice Sends Bob A = {A}")

# Bob Sends Alice B = g^b mod p
B = (shared_base**bob_secret) % shared_prime
print(f"Bob Sends Alice B = {B}")

# Alice Computes Shared Secret: s = B^a mod p
alice_shared_secret = (B**alice_secret) % shared_prime
print(f"Alice Shared Secret: {alice_shared_secret}")

# Bob Computes Shared Secret: s = A^b mod p
bob_shared_secret = (A**bob_secret) % shared_prime
print(f"Bob Shared Secret: {bob_shared_secret}")
