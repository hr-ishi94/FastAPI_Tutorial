from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ['bcrypt'],deprecated = "auto")

def hash_pwd(password:str):
    new_pwd = pwd_context.hash(password)
    return new_pwd

def hash_verify(plain_password, encrypted_password):
    return pwd_context.verify(plain_password,encrypted_password)