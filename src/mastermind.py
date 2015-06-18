'''
Classes for playing a game of mastermind.  Create a new game object
and then game.play_game()

'''


from random import randint

class Code:
    
    def __init__(self, num_pegs = 4, code = None):
        self.num_pegs = num_pegs
        if code is not None:
            self.code = code
        else:
            rand_list = [chr(randint(65, 65 + num_pegs - 1)) for i in range(num_pegs)]
            self.code = ''.join(rand_list)

    
class Guess:
    """
    Used in Game class
    """

    def __init__(self, guess, code):
        self.guess = guess
        self.code = code
        self.evaluate()
        
    def evaluate(self):

        self.black = 0
        self.white = 0
        code_list = [i for i in self.code]
        guess_list = [i for i in self.guess]
    
        # find blacks
        for i in range(len(self.guess)):
            if guess_list[i] == code_list[i]:
                self.black += 1
                guess_list[i] = "*"
                code_list[i] = "*"
    
        # find whites
        for letter in guess_list:
            if letter != "*":
                try:
                    ix = code_list.index(letter)
                except:
                    ix = -1
                if ix >= 0:
                    self.white += 1
                    code_list[ix] = "*"

class Game:

    """
    Initialist a Game object and run method play_game()
    """
    def __init__(self, turns = 10, pegs = 4, show_code=False):
        self.turns = turns
        self.turns_remaining = turns
        self.pegs = pegs
        self.show_code = show_code
        self.code = Code(num_pegs = 4)

    def print_intro(self):
        print "This is a game of mastermind.\n"
        print "There are {} pegs and {} turns\n".format(self.pegs, self.turns)

    def print_prompt(self):
        print "You have {} guesses left. ".format(self.turns_remaining)
        print "Take a guess.\n"
        self.turns_remaining -= 1
        
    def get_guess(self):
        
        get_input = True
        while(get_input):
            if self.show_code:
                print "[Code is {}]".format(self.code.code)
            user_guess = raw_input("Make a guess with {} letters: ".format(self.pegs))
            if len(user_guess) == self.pegs:
                get_input = False
            else:
                print "You need {} letters.\n".format(self.pegs)
        
            self.guess = Guess(user_guess, self.code.code)
    
    def play_game(self):
        player_won = False
        self.print_intro()        
        for turn in range(self.turns):
            self.print_prompt()
            
            self.get_guess()
            
            if self.guess.guess == self.code.code:
                player_won = True
                break
                
            else:
                self.give_feedback()
                

        if player_won:
            print "You won!\n\n"
        else:
            print "Sorry, you lost.\n\n"
            

    def give_feedback(self):
        
        print "{} blacks {} whites".format(self.guess.black, self.guess.white)
        
