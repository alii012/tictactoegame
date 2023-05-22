# tictacto:
       a tic tac toe game that u will play aginst AI 
the player is winning, and a negative score means 
we have in tictactoe.py 8 functions lets start break all this fucntions down

1- inital_state(): as u see this function is the inital_state of the game we just EMPTY Game

2- player(board): this function take a board as  input and return which player will move next

3- action(board): this function also will take a board as input and return all of the possible action that can be taken on the board ,
and how u would now if this is a possible action or not its easy we w'll loop over all the board if its empty than we have a valid action here

4- result(board,action): it just will take the board and the action and return a new board with that action

5- winner(board): return which player has won the game 

6- termianl(board): we have a term in context of tictactoe game its called a terminal state which mean the game is over if termnial(board) true that mean games is over 

7- ultitly(board): this function is very important and i'll told u why in the next step altough this function return 1 if X wins -1 if O wins otherways 0 'Tie'


8- minimax(board): this function work by recursively exploring all possible moves and their outcomes,based on who wins or loses the game.
The scores are assigned from the perspective of the player whose turn it is at that point in the game,
so a positive score means that the player is winning, and a negative score means that the player is losing.
