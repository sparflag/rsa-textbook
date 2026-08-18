#!/usr/bin/env python3
"""RSA Rookie — factor the small modulus, decrypt to the seed (fernet delivery)."""
import os, sys
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", "small-exponent")

def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    with open("/challenge/rsa.txt", "w") as f:
        f.write(f"n and e are small; factor n, recover d, RSA-decrypt c.\nrecovered seed = {CHALLENGE_KEY}\n")
    print('flag.enc is Fernet ciphertext. rsa.txt describes the textbook-RSA step.')
    print('Decrypt flag.enc with the recovered seed (Fernet).')

if __name__ == "__main__":
    main()
