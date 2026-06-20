
def encrypt(message, shift):
    """Encrypt a message using Caesar Cipher"""
    result = ""
    for char in message:
        if char.isalpha():  # Only shift letters
            # Check if uppercase or lowercase
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # Keep spaces, numbers, symbols as-is
    return result


def decrypt(message, shift):
    """Decrypt a message using Caesar Cipher"""
    return encrypt(message, -shift)  # Decryption = reverse shift


def main():
    print("=" * 45)
    print("        CAESAR CIPHER PROGRAM")
    print("=" * 45)

    while True:
        print("\nWhat do you want to do?")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (e.g. 3): "))
            encrypted = encrypt(message, shift)
            print(f"\n✅ Original Message : {message}")
            print(f"🔒 Encrypted Message: {encrypted}")

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value used during encryption: "))
            decrypted = decrypt(message, shift)
            print(f"\n✅ Encrypted Message : {message}")
            print(f"🔓 Decrypted Message : {decrypted}")

        elif choice == "3":
            print("\nGoodbye! Good luck with your internship! 🎉")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
