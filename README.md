# RSA Rookie (`rsa-textbook`)

**Category:** cryptography · **Difficulty:** medium · **Points:** 300

You're given an RSA public key with a tiny modulus and a small exponent. Factor n, recover the private key, and decrypt the ciphertext to reveal the seed that decrypts your flag blob.

## Run it

```bash
docker build -t sparflag/rsa-textbook .
# `deca-ai start rsa-textbook` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit rsa-textbook 'sparflag{...}'
```

## Hints

- A small modulus is factorable — try it.
- With p and q you can compute phi(n) and the private exponent d.
- Decrypt the given RSA ciphertext to get the Fernet seed.
