class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        self.file = open(file)
        self.words = self.fetch_words()
        print(self.words)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<WordFinder>"

    def fetch_words(self):
        return [line.strip() for line in self.file]
        # for line in self.file:
        #     self.words.append(line.strip())
        # return self.words
        # print(f"{len(self.words)} words read")

    def random(self):
        from random import choice
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)
        print("hello", self.words)
        self.words = self.fetch_special_words()

    def __repr__(self):
        return f"<SpecialWordFinder>"

    def fetch_special_words(self):
            print("fetchspecialwords")
            # for word in self.words:
            #     print(word)
            #     if word.startswith("#") or word == '':
            #         self.words.remove(word)
            # print("fetch special words", self.words)

            return [word for word in self.words if word != '' and not word.startswith("#")]

        # for line in self.file:
        #     if line.startswith("#") or line == "":
        #         pass
        #     super().fetch_words

            # for word in self.words:
            #     if not word.startswith("#") or word != "":
            #         self.new_list.append(word)
            # print(self.new_list)
