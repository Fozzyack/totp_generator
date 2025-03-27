import pyotp
import base64



def main():

    email = input("provide email: ")
    SECRET_TOKEN = input("provide secret: ")

    email_token = email + SECRET_TOKEN
    
    encoded = base64.b32encode(email_token.encode()).decode("utf-8")
    totp = pyotp.TOTP(encoded, digits=10, digest="sha512")
    totp_password = totp.now()


    auth_dec = f"{email}:{totp_password}"
    auth_enc = base64.b64encode(auth_dec.encode()).decode("utf-8")

    print(totp_password)
    print(auth_dec)
    print(auth_enc)
    
    

if __name__ == "__main__":
    main()
