# Singleton Pattern Implementation
class Singleton:
    # Define Private variable
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    # Instance 1
    s = Singleton()
    print(s)

    # Instance 2
    q = Singleton.getInstance()
    print(q)

    # Instance 3
    r = Singleton.getInstance()
    print(r)

    if s == q:
        print('Both are Same Object')
    else:
        print('Different Object!!!!')
