class _PasswordHasher:
    def hashAndSavePassword(self, password: str):
        self.hashPassword(password)
        self.savePassword(password)

    def hashPassword(self, password: str):
        print(f"haashing {password}")

    def savePassword(self, password: str):
        print(f"saving {password}")


class PasswordHasher:
    def hashPassword(self, password: str):
        print(f"hashing {password}")


class PasswordStorage:
    def savePassword(self, passwordHash: str):
        print(f"saving {passwordHash}")
