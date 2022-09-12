"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        #reads the dictionary and returns num of words read
        dictionary = open(path)
        self.words = self.parse(dictionary)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary):
        #parses through file and returns a list of words
        return [w.strip() for w in dictionary]

    def random(self):
        #selects a random word from the list
        return random.choice(self.words)

class SpecialWordFinder:
    def parse(self, dictionary):
        #parses through the dictionary list and ignores blanks/comments
        return [w.strip for w in dictionary
            if w.strip() and not w.startswith("#")]

