# Facade Pattern  using Computer Example

# Processing Unit Class
class ProcessingUnit:
    '''Subsystem #1'''

    def process(self):
        print("Processing...")


# Display Unit Class
class DisplayUnit:
    '''Subsystem #2'''

    def display(self):
        print("Displaying...")


# Memory Class
class Memory:
    '''Subsystem #3'''

    def ioOperation(self):
        print("Reading and writing to memory...")


# Facade Class Implementation
class Computer:
    '''Facade'''

    def __init__(self):
        self.processingUnit = ProcessingUnit()
        self.displayUnit = DisplayUnit()
        self.memory = Memory()

    def bootUp(self):
        self.processingUnit.process()
        self.memory.ioOperation()
        self.displayUnit.display()


if __name__ == "__main__":
    computer = Computer()
    computer.bootUp()
