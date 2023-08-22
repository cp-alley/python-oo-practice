from random import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """A word finder for a provided file."""
        self.path = path
        self.word_list = []
        # call method to print num of words read
        self.read_file()
        self.print_count()

    def __repr__(self):
        return f"A word finder for the file at {self.path}"

    def read_file(self):
        """Reads the provided file and notes how many words were read. Called upon
        initialization of an intance."""
        file = open(self.path, "r")
        for line in file:
            self.word_list.append(line.strip('\n'))

    def print_count(self):
        """Print the number of words read"""
        print(f"{len(self.word_list)} words read")

    def random_word(self):
        """Returns a random wors from the words the finder read from the provided
        file."""
        ran_num = int(random() * len(self.word_list))
        print(ran_num)
        return self.word_list[ran_num]

class SpecialWordFinder(WordFinder):
    """Finds words from files that include comments and blank lines"""
    super().read_file()

    def read_file(self):
        self.word_list = [word for word in self.word_list if not word == ""]
        self.word_list = [word for word in self.word_list if not word[0] == "#"]