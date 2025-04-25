from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordManager:
    @staticmethod
    def hash_password(password: str) -> str:
        if not password or not isinstance(password, str):
            raise ValueError("Password Must Be A Non-Empty String.")

        return password_context.hash(password)
