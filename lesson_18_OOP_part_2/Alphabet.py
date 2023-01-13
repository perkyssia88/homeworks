class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__(lang="En", letters="qwertyuioplkjhgfdsazxcvbnm")
        self.__letters_num = len(self.letters)

    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return "sample text in English"


al = EngAlphabet()
print(al.letters)
print(al.letters_num())
print(al.is_en_letter("f"))
print(al.is_en_letter("щ"))
print(EngAlphabet.example())