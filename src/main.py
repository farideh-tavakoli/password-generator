from abc import ABC, abstractclassmethod
import random
import string
import nltk


nltk.download('words')


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractclassmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password.
        """
        pass


class  RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generates a random password.
    """
    def __init__(self, length: int = 8, include_number: bool = False, include_symbols: bool = False):
        self.lenght = length
        self.characters = string.ascii_letters
        if include_number:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """
        Generate a password from specified characters.
        """
        return ''.join([random.choice(self.characters) for _ in range(self.lenght)])


class MemorablePasswordGenerator(PasswordGenerator):
    """Class to generates a memorable password."""
    def __init__(
        self,
        number_of_words: int = 4,
        seperator: str = '-',
        capitalize: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.seperator = seperator
        self.capitalize = capitalize

    def generate(self) -> str:
        """
        Generate a password from a list of vocabulary words.
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

        return self.seperator.join(password_words)


class PinGenerator(PasswordGenerator):
    """Class to generetae a pin code."""
    def __init__(self, length: int = 8):
        self.length = length

    def generate(self) -> str:
        """Generates a pin code."""
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    

#if __name__ == '__main__':
#    p_obj = RandomPasswordGenerator()
#    print(p_obj.generate())