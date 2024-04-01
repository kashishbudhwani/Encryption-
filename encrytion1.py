from cryptography.fernet import Fernet
key=Fernet.generate_key()
msg = "Welcome to channel".encode()
f_obj = Fernet(key)
encryted_msg = f_obj.encrypt(msg)
print(encryted_msg)

decryted_msg = f_obj.decrypt(encryted_msg)
print(decryted_msg)
