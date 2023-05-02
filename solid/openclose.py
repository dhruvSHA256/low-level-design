from abc import ABCMeta, abstractmethod


class _HashingType:
    pass


class _PasswordHasher:
    def __init__(self, password: str, hashingType: _HashingType):
        self.password = password
        self.hashingType = hashingType

    def hashPassword(self):
        if self.hashingType == "base64":
            # hash password with bas64
            pass
        elif self.hashingType == "sha256":
            # hash password with sha256
            pass
        elif self.hashingType == "md5":
            # hash password with md5
            pass


class IHashingType(metaclass=ABCMeta):
    @abstractmethod
    def hashPassword(self, password: str):
        pass


class Base64Hashing(IHashingType):
    def hashPassword(self, password: str):
        # hash password with bas64
        pass


class Md5Hashing(IHashingType):
    def hashPassword(self, password: str):
        # hash password with md5
        pass


class SHA256Hashing(IHashingType):
    def hashPassword(self, password: str):
        # hash password with sha256
        pass


class PasswordHasher:
    def __init__(self, password: str, hashingType: IHashingType):
        self.password = password
        self.hashingType = hashingType

    def hashPassword(self):
        self.hashingType.hashPassword(self.password)
