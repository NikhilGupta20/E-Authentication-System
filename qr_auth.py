import qrcode
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Function to choose a URL for QR code generation
def choose_url():
    print("Choose an option for QR code generation:")
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

# Function to generate a QR code
def generate_login_qr():
    # Get the user's choice for URL
    qr_data = choose_url()

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill="black", back_color="white")
    return qr_img

# Function to show the QR code in a Tkinter window
def show_qr_in_window():
    root = Tk()
    root.title("QR Code Login")

    # Generate the QR code
    qr_img = generate_login_qr()

    # Convert the image for Tkinter compatibility
    qr_img_tk = ImageTk.PhotoImage(qr_img)

    # Display the QR code in the Tkinter window
    label = Label(root, image=qr_img_tk)
    label.image = qr_img_tk  # Keep a reference to avoid garbage collection
    label.pack()

    # Set a timer to close the window after 60 seconds
    root.after(60000, root.quit)  # Close after 60 seconds

    # Display the window
    root.mainloop()

if __name__ == "__main__":
    # Show the QR code in a Tkinter window
    show_qr_in_window()
