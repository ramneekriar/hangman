# 👾 Hangman

## Description
A simple command line hangman game implemented in Python using object oriented programming and Wordnik's random-word API.

## Getting Started

To run the project locally, you can get a free Wordnik api key by signing up at <https://developer.wordnik.com/>

1. Clone this repo `git clone https://github.com/rkriar/hangman.git`
3. Create a file at the root of the project named .env
4. Create a variable inside the .env file with the following name: `API_KEY=<YOUR_API_KEY>` where you replace `<YOUR_API_KEY>` by the api key received from Wordnik
5. Run `python3 hangman.py` to play

## Game Play
```
 _    _      _                            _         
| |  | |    | |                          | |        
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
 _   _
| | | |   
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __     
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   
| | | | (_| | | | | (_| | | | | | | (_| | | | |   
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   
                    __/ |
                   |___/
  +---+
  |   |
      |
      |
      |
      |
=========

The word is _  _  _  _  _  _  _  _ 
Guess a letter or type exit to leave the game
>>> 
```
