import os
from wordnik import swagger, WordsApi

# Setting up api
apiUrl = 'http://api.wordnik.com/v4'
apiKey = os.environ.get("API_KEY")
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordsApi.WordsApi(client)

MAX_ERRORS = 6
HANGMAN_PICTURES = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

class Picture:
    """
    A class used to represent a Hangman Figure

    ...

    Attributes
    ----------
    image : str
        A formatted string to print out the hangman figure

    Methods
    -------
    update_image(num_errors)
        Updates the hangman figure to the next image
    draw_image()
        Prints out the current hangman figure
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Picture object.

        Parameters
        ----------
        image : str
            The hangman figure at the beginning of the game
        """

        self.image = HANGMAN_PICTURES[0]

    def update_image(self, num_errors: int) -> None:
        """Updates the hangman figure based on the number of errors the user has made.

        Parameters
        ----------
        num_errors : int
            The number of errors the user has made
        """
        
        self.image = HANGMAN_PICTURES[num_errors]

    def draw_image(self) -> None:
        print(self.image)

class Word:
    """
    A class used to represent a Word

    ...

    Attributes
    ----------
    word : str
        A random word returned by the Wordnik API
    display: [str]
        A formatted string which replaces each letter of the word with '_'
    guesses: [str]
        A str array holding the letters guessed by the user
    num_guess: int
        The number of guesses made by the user
    num_errors: int
        The number of errors made by the user

    Methods
    -------
    __get_random_word()
        Updates the hangman figure to the next image
    get_word()
        Prints out the current hangman figure
    get_display()
        Return the current display of the word to user
    get_num_guess()
        Return the number of guesses the user has made
    get_guesses()
        Return the list attribute locations holding the letters the user has guessed
    get_num_errors()
        Return the attribute num_errors 
    add_num_guess()
        Increase attribute num_guess by 1
    add_num_errors()
        Increase attribute num_errors by 1
    add_guess_letter()
        Append letter to attribute list guesses
    show_word()
        Prints the word object to stdout as a string
    get_word_indices(guess)
        Gets the indices where guess exists in word
    update_display(indices, letter)
        Updates display attribute by replacing '_' with letter at given indices
    check_guess(guess)
        Checks whether the guess made exists in word or is an error
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Word object.

        Parameters
        ----------
        word : str
            The word being guessed
        display : [str]
            Formatted display with '_' as placeholder for letter in word
        guesses : [str]
            The letters the user has already guessed
        num_guess : int
            The number of guesses the user has made
        num_errors : int
            The number of errors the user has made
        """

        self.word = self.__get_random_word()
        self.display = ['_ ' for letter in self.word]
        self.guesses = []
        self.num_guess = 0
        self.num_errors = 0

    def __get_random_word(self) -> str:
        word = wordApi.getRandomWord(maxLength=8)
        return word.word

    def get_word(self) -> str:
        return self.word
    
    def get_display(self) -> list[str]:
        return self.display

    def get_num_guess(self) -> int:
        return self.num_guess
    
    def get_guesses(self) -> list[str]:
        return self.guesses

    def get_num_errors(self) -> int:
        return self.num_errors
    
    def add_num_guess(self) -> None:
        self.num_guess += 1
    
    def add_num_errors(self) -> None:
        self.num_errors += 1
    
    def add_guess_letter(self, letter: str) -> None:
        self.guesses.append(letter)

    def show_word(self) -> None:
        display = ' '.join(self.display)
        print(f'\nThe word is {display}')
    
    def get_word_indices(self, guess: str) -> list[int]:
        locations = []
        for i, letter in enumerate(list(self.word)):
            if letter == guess:
                locations.append(i)
        return locations
    
    def update_display(self, indices: list[int], letter: str) -> None:
        for i in indices:
            self.display[i] = letter

    def check_guess(self, guess: str) -> int:
        if guess not in self.guesses and guess in self.get_word():
            self.add_guess_letter(guess)
            self.add_num_guess()
            indices = self.get_word_indices(guess)
            self.update_display(indices, guess)
            print('\nYou got it! The letter '+guess+' is in the word!\n')
            return 0
        else:
            if guess in self.guesses:
                self.add_num_guess()
                self.add_num_errors()
                print('\nUh oh, you have already guessed the letter '+guess+'!\nA part to the stick figure will be added.\n')
            else:
                self.add_guess_letter(guess)
                self.add_num_guess()
                self.add_num_errors()
                print('\nUh oh, the letter '+guess+' is not in the word!\nA part to the stick figure will be added.')
            return -1

class Game:
    """
    A class used to represent a Hangman Game

    ...

    Attributes
    ----------
    word : Word object
        A formatted string to print out the hangman figure
    picture : Picture object
        Something here

    Methods
    -------
    print_title()
        Prints out the ASCII title to stdout
    check_for_win()
        Checks for win condition of the game
    reset()
        Gets a new Word object and Picture object and resets game
    play_again()
        Gets user input whether to play the game again to reset or not to exit game
    run()
        Runs the game awaiting user input for guess, until win condition or user exit
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the Game object.

        Parameters
        ----------
        word : Word object
            Word object
        picture : Picture object
            Picture object
        """

        self.word = Word()
        self.picture = Picture()

    def print_title(self) -> None:
        print(' _    _      _                            _         ')    
        print('| |  | |    | |                          | |        ')     
        print('| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   ')
        print('| |/\| |/ _ \ |/ __/ _ \| \'_ ` _ \ / _ \ | __/ _ \ ')
        print('\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | ')
        print(' \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  ')
                                                                                                    
        print(' _   _')                                       
        print('| | | |   ')                                        
        print('| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __     ')
        print('|  _  |/ _` | \'_ \ / _` | \'_ ` _ \ / _` | \'_ \   ') 
        print('| | | | (_| | | | | (_| | | | | | | (_| | | | |   ')
        print('\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   ')
        print('                    __/ |')                       
        print('                   |___/') 

    def check_for_win(self) -> bool:
        display = ''.join(self.word.get_display())
        if display == self.word.get_word():
            return True

    def check_for_lose(self) -> bool:
        if self.word.get_num_errors() == MAX_ERRORS:
            self.picture.update_image(self.word.get_num_errors())
            self.picture.draw_image()
            return True
    
    def reset(self) -> None:
        self.word = Word()
        self.picture = Picture()
    
    def play_again(self) -> None:
        answer = input('Want to play again? Type \'y\' to play another round, or \'n\' to exit the game.\n>>> ')
        if answer.lower() == 'y':
            self.reset()
        else:
            exit()

    def run(self) -> None:
        running = True
        self.print_title()

        while running:
            self.picture.draw_image() 
            self.word.show_word()
            guess = input('Guess a letter or type exit to leave the game\n>>> ')

            if guess == 'exit':
                print('Thanks for playing! The word was '+self.word.get_word()+'. See you soon!')
                exit()
                
            if self.word.check_guess(guess.lower()) == -1:
                self.picture.update_image(self.word.get_num_errors())
            if self.check_for_win():
                print(f'You have guessed the word {self.word.word} in {self.word.get_num_guess()} guesses!')
                self.play_again()
            elif self.check_for_lose():
                print('You have lost the game! The word was '+self.word.get_word()+'.')
                self.play_again()


if __name__ == '__main__':
    game = Game()
    game.run()