class SerialGenerator:
    """Machine to create unique incrementing serial numbers

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        """Create a serial number generator starting from a provided input num"""
        self.start = self.current = start

    def __repr__(self):
        return f"Series starting with {self.start}. Current number is {self.current}."

    def generate(self):
        """Returns the next number in the sequence that begins with the start value"""
        self.current+=1
        return self.current - 1

    def reset(self):
        """Resets the generator to the original start value"""
        self.current = self.start





