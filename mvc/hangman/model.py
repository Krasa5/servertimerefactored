class Hangman:
    word = ""
    progress_word = ""
    guesses = list()
    max_guesses = int

    def __init__(self, word):
        self.word = word
        self.guesses = list()

    def is_game_over(self, guess):
        game_over = False
        won = False
        guesses_left = self.check_guesses_left()
        # print(f"Guesses left: {guesses_left}")

        if guesses_left == 0:
            game_over = True

        won = self.check_word_guess(guess)
        if won:
            game_over = True
        return game_over, won

    def get_number_of_guesses_left(self):
        list1 = self.guesses
        theword = self.word.lower()

        matching = [s for s in list1 if s in theword]  # total correct guesses
        correct_guesses = len(matching)  # correct
        total_guesses = len(list1)

        # for every correct guess we want to deduct it from the amount of wrong guesses.
        # if the user has the right answer the number of guesses won't be reduced
        return total_guesses - correct_guesses

    def check_guesses_left(self):
        self.max_guesses = len(self.word)
        if self.get_number_of_guesses_left() >= self.max_guesses:
            return 0
        return self.max_guesses - self.get_number_of_guesses_left()

    def check_word_guess(self, word):
        if self.word.lower() == word.lower():
            return True
        return False

    def guess(self, character):
        character = character.lower()

        self.progress_word = ""
        for c in self.word.lower():
            if character == c or c in self.guesses:
                self.progress_word += c
            else:
                self.progress_word += "\_."

        self.guesses.append(character)
