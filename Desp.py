from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate a random key
key = get_random_bytes(8)  # DES key is 8 bytes

# Initialize the DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Get the plaintext from the user
plaintext = input("Enter plaintext: ")
plaintext_bytes = plaintext.encode('utf-8')

# Pad the plaintext to a multiple of 8 bytes
padded_plaintext = pad(plaintext_bytes, DES.block_size)

# Encrypt the padded plaintext
ciphertext = cipher.encrypt(padded_plaintext)

# Print the ciphertext in hexadecimal format
print(f"Ciphertext: {ciphertext.hex()}")

# Decrypt the ciphertext
decrypted_padded_plaintext = cipher.decrypt(ciphertext)

# Remove the padding from the decrypted plaintext
decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size)

# Print the decrypted plaintext
print(f"Decrypted Plaintext: {decrypted_plaintext.decode()}")
