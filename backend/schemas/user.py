# from .base import Base


# class User(Base):
#     id: int
#     admin: bool
#     username: str
#     email: str
#     firstName: str
#     lastName: str
#     resetPassword: bool
#     loginAttempts: int
#     maxLoginAttempts: int


# class Token(Base):
#     access_token: str
#     token_type: str
#     user: User


# class TokenData(Base):
#     username: str | None = None
#     scopes: list[str] = []


# class NewUser(Base):
#     username: str
#     firstName: str
#     lastName: str
#     password: str
#     email: str