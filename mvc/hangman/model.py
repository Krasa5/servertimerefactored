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

        if self.check_guesses_left() == 0:
            game_over = True

        won = self.check_word_guess(guess)
        if won:
            game_over = True
        return game_over, won

    def get_number_of_guesses_left(self):
        return len(self.guesses)

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
