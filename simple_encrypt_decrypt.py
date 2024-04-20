from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import qrcode

def generate_iv_from_key(key):
    iv = hashlib.sha256(key).digest()[:16]
    return iv

def generate_private_key(private_pass):
    private_key = (private_pass * 256).encode()
    return private_key

def encrypt_text(plaintext, private_key):
    private_key_16 = private_key[:16]
    iv = generate_iv_from_key(private_key)
    cipher = AES.new(private_key_16, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext

def decrypt_text(ciphertext, private_key):
    private_key_16 = private_key[:16]
    iv = generate_iv_from_key(private_key)
    cipher = AES.new(private_key_16, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text.decode()

def save_to_file(text, filename):
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text saved to {filename}")
    except IOError:
        print(f"Error: Failed to save text to {filename}")

def create_qr_code(text, filename):
    try:
        qr = qrcode.make(text)
        qr.save(filename)
        print(f"QR code saved to {filename}")
    except IOError:
        print(f"Error: Failed to save QR code to {filename}")

def main():
    while True:
        choice = input("Do you want to Encrypt or Decrypt (e/d)? ")

        if choice.lower() == 'e':
            print("Enter the text to Encrypt (Type '/done' on a new line to finish or '/clear' to clear all text):")
            plaintext_lines = []
            while True:
                line = input()
                if line.strip() == '/clear':
                    plaintext_lines.clear()
                    print("All text is cleared, type the text again:")
                    continue
                if line.strip() == '/done':
                    if not plaintext_lines:
                        print("Error: No input provided.")
                        return
                    break
                plaintext_lines.append(line)

            plaintext = '\n'.join(plaintext_lines)

            private_pass = input("Enter your Private Password: ")
            if not private_pass:
                print("Please Must Enter Password.")
                return

            private_key = generate_private_key(private_pass)
            ciphertext = encrypt_text(plaintext, private_key)
            print("Encrypted text:", ciphertext.hex())

            save_option = input("Do you want to Save the encrypted text file: (y/n) ")
            if save_option.lower() == 'y':
                filename = input("Enter the Filename: ")
                save_to_file(ciphertext.hex(), filename + '_encrypted.txt')

            qr_option = input("Do you want to create a QR code: (y/n) ")
            if qr_option.lower() == 'y':
                qr_filename = input("Enter the Filename: ")
                create_qr_code(ciphertext.hex(), qr_filename + '_encrypted.png')

            print("Encrypt done.")

        elif choice.lower() == 'd':
            try:
                ciphertext = bytes.fromhex(input("Enter the Encrypted text: "))
                private_pass = input("Enter your private password: ")
                private_key = generate_private_key(private_pass)
                decrypted_text = decrypt_text(ciphertext, private_key)
                print("Decrypted text:", decrypted_text)

                save_option = input("Do you want to Save the Decrypted text file: (y/n) ")
                if save_option.lower() == 'y':
                    filename = input("Enter the Filename: ")
                    save_to_file(decrypted_text, filename + '_decrypted.txt')

                qr_option = input("Do you want to create a QR code: (y/n) ")
                if qr_option.lower() == 'y':
                    qr_filename = input("Enter the Filename: ")
                    create_qr_code(decrypted_text, qr_filename + '_decrypted.png')

                print("Decrypt done.")

            except ValueError:
                print("Invalid hexadecimal format for ciphertext.")

        elif choice.lower() == 'e':
            break

        else:
            print("Invalid choice. Please enter 'e' for encryption, 'd' for decryption, or 'c' for clearing input.")

        continue_option = input("Do you want to continue again? (y/n) ")
        if continue_option.lower() != 'y':
            break

if __name__ == "__main__":
    main()
