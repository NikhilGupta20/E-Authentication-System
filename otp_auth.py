from datetime import datetime, timedelta
from twilio.rest import Client
import webbrowser

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC5329f9c47dfa4be553ce996325a4a1b3'
TWILIO_AUTH_TOKEN = '72d6f66055f29e031d04accd8ec1fd94'
SERVICE_SID = 'VA1d0eb19ebea8eb867f2f3302f0f026e5'  # Replace with your Twilio Verify Service SID

# Function to choose a URL after successful authentication
def choose_url():
    print("Choose an option to open after successful authentication:")
    print("1. GitHub")
    print("2. LinkedIn")
    
    while True:
        choice = input("Enter your choice (1/2): ")
        if choice == "1":
            return "https://github.com/NikhilGupta20"
        elif choice == "2":
            return "https://www.linkedin.com/in/nikhillguptaa/"
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Function to send OTP via Twilio Verify Service
def send_otp_sms(phone_number):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        verification = client.verify.v2.services(SERVICE_SID).verifications.create(
            to=phone_number, channel='sms'
        )
        print(f"Sent OTP via SMS: {verification.sid}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Function to verify OTP using Twilio Verify Service
def verify_otp(phone_number, entered_otp):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        verification_check = client.verify.v2.services(SERVICE_SID).verification_checks.create(
            to=phone_number, code=entered_otp
        )
        if verification_check.status == "approved":
            selected_url = choose_url()
            webbrowser.open(selected_url)
            return "OTP verified"
        else:
            return "Incorrect OTP"
    except Exception as e:
        return f"Error verifying OTP: {e}"

# Main function to handle OTP authentication
def otp_authentication():
    phone_number = input("Enter your phone number (with country code, e.g., +1 for US): ")
    email = input("Enter your email address (optional, press Enter to skip): ")

    print("OTP has been sent to your phone number.")
    send_otp_sms(phone_number)

    try:
        entered_otp = input("Enter OTP received: ")
        verification_result = verify_otp(phone_number, entered_otp)
        print(verification_result)
    except ValueError:
        print("Invalid OTP format. Please enter numbers only.")

if __name__ == "__main__":
    otp_authentication()
