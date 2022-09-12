"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start=0):
        #init method/constructor

        self.start = self.current = start

    def __repr__(self):
        #displays the current numbers
        return f"<SerialGenerator start = {self.start} current = {self.current}>"

    def generate(self):
        #generates a new increment by 1
        self.current += 1
        return self.current - 1

    def reset(self):
        #resets number back to starting number
        self.current = self.start

