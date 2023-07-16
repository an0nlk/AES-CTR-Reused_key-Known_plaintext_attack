from pwn import xor
from Crypto.Util.Padding import pad


def decrypt(ciphertext, keystream):
    return xor(ciphertext, keystream)

def main():
    # Known plaintexts-ciphertext pair
    known_plaintext = 'This is a test message!'
    known_ciphertext = bytes.fromhex("31958ec9da67c3514d90a68a377f2cce2b8a801449427a18e7ec4b036c144d99")

    #add padding to the plaintext
    known_plaintext = pad(known_plaintext.encode(), 16)#replace 16 with padding value

    #cipher text that need to decrpt
    ciphertext = bytes.fromhex("31958ec9da67c35158d8b7cf21656fd1378987104a0736749d96236d003c4692")

    # Recover the keystream by XORing the known plaintext with the corresponding ciphertext
    keystream = xor(known_ciphertext, known_plaintext)
    # Use the recovered keystream to decrypt the encrypted text
    decrypted_cipher = decrypt(ciphertext, keystream)

    print(f"{decrypted_cipher=}")

if __name__ == "__main__":
    main()
