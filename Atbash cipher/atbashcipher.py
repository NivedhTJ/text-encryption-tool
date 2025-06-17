def atbash_cipher(text):
    result = []
    for char in text:
        if char.isalpha():
            # Check if uppercase or lowercase
            if char.isupper():
                # 'A' = 65, 'Z' = 90
                result.append(chr(90 - (ord(char) - 65)))
            else:
                # 'a' = 97, 'z' = 122
                result.append(chr(122 - (ord(char) - 97)))
        else:
            # Non-alphabetic characters remain the same
            result.append(char)
    return "".join(result)


def main():

    while True:
        print("\nAtbash encryption / decryption Tool")
        print("1. Atbash Encrypt")
        print("2. Atbash Decrypt")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            text = input("Enter text to encrypt: ")
            print("Encrypted:", atbash_cipher(text))

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            print("Decrypted:", atbash_cipher(text))

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
