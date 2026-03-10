import random
import smtplib
import time

OTP_TTL_SECONDS = 60
MAX_VERIFY_ATTEMPTS = 3
MAX_RESEND = 3

sender_email = "prachisharma5232@gmail.com"  # Change this to YOUR Gmail address
# TODO: Replace with a newly generated App Password from YOUR Gmail account
app_password = "qnzfpocpuugiadxv" 

# Dummy in-memory database to store registered users {email: password}
users_db = {}

def generate_otp():
    return random.randint(100000, 999999)

def send_otp(email, otp):
    message = f"""Subject: OTP Verification\n\nYour OTP is {otp}\nIt will expire in 60 seconds.\n"""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, email, message)
        server.quit()
    except Exception as e:
        print(f"Failed to send email. Check credentials or network. Error: {e}")

def verify_otp_flow(receiver_email):
    """Handles the sending, retrying, and verification of the OTP."""
    expected_otp = generate_otp()
    send_otp(receiver_email, expected_otp)
    print("OTP sent to your email.")

    start_time = time.time()
    attempts = MAX_VERIFY_ATTEMPTS
    resend_count = 0

    while attempts > 0:
        try:
            user_otp = int(input("Enter OTP: "))
        except ValueError:
            print("Invalid input. Digits only.")
            attempts -= 1
            print("Attempts left:", attempts)
            continue

        if time.time() - start_time > OTP_TTL_SECONDS:
            print("OTP expired.")
        elif user_otp == expected_otp:
            return True # Successfully verified
        else:
            attempts -= 1
            print("Wrong OTP. Attempts left:", attempts)

        # Offer resend when attempts finished or OTP expired
        if attempts == 0 or time.time() - start_time > OTP_TTL_SECONDS:
            if resend_count >= MAX_RESEND:
                print("Max resends reached.")
                return False

            choice = input("Resend OTP? (y/n): ").strip().lower()

            if choice == "y":
                expected_otp = generate_otp()
                send_otp(receiver_email, expected_otp)
                print("New OTP sent!")
                
                resend_count += 1
                attempts = MAX_VERIFY_ATTEMPTS
                start_time = time.time()
            else:
                return False
                
    return False

def main():
    print("\n--- Main Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option (1/2/3): ").strip()

    if choice == '1':
        print("\n--- Register ---")
        email = input("Enter your email: ")
        if email in users_db:
            print("User already exists. Please login instead.")
            return
        
        password = input("Create a password: ")
        print("\nVerifying your email address...")
        
        # Verify email before saving the user
        if verify_otp_flow(email):
            users_db[email] = password
            print("✅ Registration Successful! You can now login.")
        else:
            print("❌ Registration failed.")

    elif choice == '2':
        print("\n--- Login ---")
        email = input("Enter your email: ")
        if email not in users_db:
            print("Email not found. Please register first.")
            return
        
        password = input("Enter your password: ")
        if users_db[email] == password:
            print("\nPassword correct. Sending 2FA OTP to your email...")
            
            # 2FA Verification
            if verify_otp_flow(email):
                print("✅ Login Successful!")
            else:
                print("❌ Login failed due to OTP timeout/incorrect attempts.")
        else:
            print("❌ Incorrect password.")
            
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    # Runs the menu in a loop so you can Register, then Login right after
    while True:
        main()