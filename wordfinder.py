from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """A word finder for a provided file."""
        self.path = path
        self.word_list = self.read_file()
        # call method to print num of words read
        self.print_count()

    def __repr__(self):
        return f"A word finder for the file at {self.path}"

    def read_file(self):
        #DONE: return a list and set word_list equal to that val in init
        """Reads the provided file and notes how many words were read. Called upon
        initialization of an intance."""
        file = open(self.path, "r")
        new_list = [line.strip() for line in file]
        return new_list


    def print_count(self):
        """Print the number of words read"""
        print(f"{len(self.word_list)} words read")

    def random_word(self):
        """Returns a random wors from the words the finder read from the provided
        file."""
        #DONE: use random's choice function, import choice instead
        return choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """Finds words from files that include comments and blank lines"""

    def read_file(self):
        """An updated read_file method that strips out comments and empty lines"""
        #DONE: use word.startswith()
        return [word for word in super().read_file()
                          if not word == "" and not word.startswith("#") ]