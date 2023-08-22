from random import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """A word finder for a provided file."""
        self.path = path
        self.word_list = []
        # call method to print num of words read
        self.read_file()

    def __repr__(self):
        return f"A word finder for the file at {self.path}"

    def read_file(self):
        """Reads the provided file and notes how many words were read. Called upon
        initialization of an intance."""
        file = open(self.path, "r")
        count = 0
        for line in file:
            count+=1
            self.word_list.append(line.strip('\n'))
        print(f"{count} words read")

    def random(self):
        """Returns a random wors from the words the finder read from the provided
        file."""
        ran_num = int(random.random() * len(self.word_list))
        return self.word_list[ran_num]

