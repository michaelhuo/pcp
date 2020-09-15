class T:
    def A(self):
        print(B())

    def B(self):
        return "hello"


if __name__ == "__main__":
    T().A()