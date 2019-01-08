class Game:
    def __init__(self, player):
        self.player = player #0 == X, 1 == O
        self.enemy = int(not player)
        self.chips = [4, 4]  #chips of X and O)
        self.mode = 0 #mode=1 means BID mode
        self.board = [] #2D array representation of the board
        self.prev_bids = [] #2D array, X and O bids respectively 
    
    def update_chips(self):
        for i in range(len(self.prev_bids[0])):
            X_bid = int(self.prev_bids[0][i])
            O_bid = int(self.prev_bids[1][i])
            if(X_bid>O_bid or (X_bid == O_bid and self.chips[0]>=self.chips[1] )):
                self.chips[0] -= X_bid
                self.chips[1] += X_bid      
            else:
                self.chips[0] += O_bid
                self.chips[1] -= O_bid
    
    def get_bid(self):
        self.update_chips()
        print(self.chips)
        if(self.chips[self.player]==self.chips[self.enemy]):
            print(self.chips[self.player]//2)
        elif(self.chips[self.player]>self.chips[self.enemy]):
            print(self.chips[self.enemy])
        else:
            print(self.chips[self.player])
      
    def get_move(self):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if(val=="_"):
                    print(i, j)
                    return i, j
    def play(self):
        if(self.mode):
            self.get_bid()
        else:
            self.get_move()
        
def main():
    '''Reads inputs and creates the Game object, prints the output'''
    game = Game(input().strip()=="O")
    game.mode = input().strip()=="BID"
    game.prev_bids.append(input().strip().split())  #X bids
    game.prev_bids.append(input().strip().split())  #O bids
    for i in range(3):
        game.board.append(list(input().strip()))
        
    game.play()
        
main()