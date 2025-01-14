import os
import sys
import subprocess

# Function to run face authentication
def run_face_authentication():
    face_auth_path = r"C:\Users\nikhi\OneDrive\Documents\Program\Minor\face_auth.py"
    subprocess.run([sys.executable, face_auth_path])

# Function to run OTP authentication
def run_otp_authentication():
    otp_auth_path = r"C:\Users\nikhi\OneDrive\Documents\Program\Minor\otp_auth.py"
    subprocess.run([sys.executable, otp_auth_path])

# Function to run QR code authentication
def run_qr_authentication():
    qr_auth_path = r"C:\Users\nikhi\OneDrive\Documents\Program\Minor\qr_auth.py"
    subprocess.run([sys.executable, qr_auth_path])

def main():
    while True:
        print("Select the authentication method:")
        print("1. Face Authentication")
        print("2. OTP Authentication")
        print("3. QR Code Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_face_authentication()
        elif choice == "2":
            run_otp_authentication()
        elif choice == "3":
            run_qr_authentication()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
