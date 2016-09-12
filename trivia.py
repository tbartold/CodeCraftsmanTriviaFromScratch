
class Game:

    def has_categories(self):
        return True

    def __init__(self):
        self.default_question_file = 'questions.txt'
        self.category = ({})

    def readFile(self, *args):
        # no args -> default file
        with open(self.default_question_file, 'r') as file:
            for line in file:
                words = line.strip("\n").split(",")
                if not words[0] in self.category.keys():
                    self.category[words[0]] = []
                #print self.category
                self.category[words[0]].append(words[1])
        return len(self.category) > 0
