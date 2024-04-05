# Simple-Text-Encrypt-and-Decrypt
This repository contains a simple Python script for encrypting and decrypting text using the Advanced Encryption Standard (AES) algorithm. The script allows users to input a text message, encrypt it with a user-defined key, and then decrypt it back to its original form.

Features:

Encryption: Encrypt any text message using AES encryption with a user-defined key.
Decryption: Decrypt the encrypted text back to its original form using the same key.
Key Generation: The script generates a fixed-length key based on the user's input, ensuring consistent encryption and decryption processes.
Save to File: Optionally save the encrypted or decrypted text to a text file for future reference.
Generate QR Code: Generate a QR code for the encrypted or decrypted text, providing an easy way to share or store the encrypted data.

Usage:

Run the script and choose whether to encrypt or decrypt text.
Input the text message and a private password (key) for encryption or decryption.
Optionally, save the encrypted or decrypted text to a file.
Optionally, generate a QR code for the encrypted or decrypted text for easy sharing or storage.


Dependencies:

pycryptodome: A Python library that provides cryptographic functionalities, including AES encryption and decryption.
qrcode: A Python library for generating QR codes.
Pillow (PIL Fork): A Python Imaging Library (PIL) fork, required by qrcode for generating QR codes.
Note:
This script is intended for educational purposes and may not be suitable for use in production environments without further security considerations.

Feel free to clone, modify, and use this script according to your requirements. If you have any questions or suggestions, please don't hesitate to open an issue or contribute to the repository.
