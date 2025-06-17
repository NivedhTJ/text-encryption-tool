# Import the base64 module for encoding/decoding
import base64


# Function to encode a string into Base64
def base64_encode(text):
    encoded_bytes = base64.b64encode(
        text.encode()
    )  # Convert string to bytes and encode
    encoded_string = encoded_bytes.decode()  # Convert encoded bytes back to string
    return encoded_string


# Function to decode a Base64-encoded string
def base64_decode(text):
    decoded_bytes = base64.b64decode(
        text.encode()
    )  # Convert Base64 string to bytes and decode
    decoded_string = decoded_bytes.decode()  # Convert decoded bytes back to string
    return decoded_string


# Function to encrypt text using Caesar cipher with a given shift
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_base = ord("A")
            else:
                shift_base = ord("a")
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted


# Caesar decryption is just encryption with negative shift
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# CLI Menu
def main():
    while True:
        print("\nSimple Encryption Tool")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. Base64 Encode")
        print("4. Base64 Decode")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value (e.g. 3): "))
            print("Encrypted:", caesar_encrypt(text, shift))

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value used during encryption: "))
            print("Decrypted:", caesar_decrypt(text, shift))

        elif choice == "3":
            text = input("Enter text to encode: ")
            print("Base64 Encoded:", base64_encode(text))

        elif choice == "4":
            text = input("Enter Base64 encoded text: ")
            print("Decoded:", base64_decode(text))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
