# Proxy: Structural pattern

from abc import ABCMeta, abstractmethod

class AbstractCmd(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, command: str):
        pass

class RealCmd(AbstractCmd):
    def execute(self, command: str):
        print(f"{command} executed")

class ProxyCmd(AbstractCmd):
    def __init__(self, user: str):
        self.is_authorized = False
        if user=="Admin":
            self.is_authorized = True
        self.executor = RealCmd()
        self.restricted_commands = ['rm','mv']

    def execute(self, command: str):
        try:
            if any([command.strip().startswith(cmd) for cmd in self.restricted_commands]) and not self.is_authorized:
                raise Exception(f"{command} is not allowed for normal user")
            else:
                self.executor.execute(command)
        except Exception as e:
            print(e)

def main():
    admin = ProxyCmd("Admin")
    admin.execute("rm *")
    normal = ProxyCmd("Dhruv")
    normal.execute("rm *")


if __name__ == "__main__":
    main()
