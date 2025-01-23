from cryptography.fernet import Fernet




def encrypt_password() :
   pasword = input("Introduce your password:   ")
   password_bytes = pasword.encode()


   key = Fernet.generate_key()
   cipher_suite = Fernet(key)


   encrypted_password = cipher_suite.encrypt(password_bytes)
   print("Your encripted password is  : ", encrypted_password.decode() )
encrypt_password()
