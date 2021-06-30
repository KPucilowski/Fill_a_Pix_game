import tkinter as tk
import random
N = 10
M = 10
black_count = 80
checkTab = [[0 for j in range(M)] for i in range(N)]
neightbours = [[0 for j in range(M)] for i in range(N)]
global game_table
game_table = [[0 for j in range(M)] for i in range(N)]

def initWindow():
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Fill a Pix')

    return root







def initUpPanel(root):
    infoLabel = tk.Label(root)
    infoLabel.config(text = "Check result")
    restartButton = tk.Button(root)
    checkButton = tk.Button(root)
    checkButton.config(text="Check result")
    restartButton.config(text="Restart")
    infoLabel.grid(row=0, column=0, columnspan=3)
    restartButton.grid(row = 0,column = 3, columnspan = 3)
    checkButton.grid(row = 0,column = 6,columnspan = 3)
    checkButton.bind('<Button-1>',lambda event:checkWin(infoLabel))
    up_panel = [infoLabel,restartButton,checkButton]
    return up_panel

def initBoard(root,up_panel,game_table,neightbours):
    for i in range(N):
        for j in range(M):
            checkTab[i][j]=0
    buttons = [tk.Button(root) for i in range(N*M)]
    neightbours = initGameBoard(game_table)
    for i in range(N):
        for j in range(M):
            buttons[i*M + j].config(height = 3, width = 7)
            buttons[i*M + j].grid(row = i + 1, column = j)
            buttons[i*M + j].config(text = neightbours[i][j])
            buttons[i * M + j].bind('<Button-1>',lambda event, button = buttons[i*M + j]: leftClick(button,i,j,buttons))
            buttons[i*M + j].bind('<Button-3>',lambda event, button = buttons[i*M + j]: rightClick(button,i,j,buttons))

    return buttons
def rightClick(button,i,j,buttons):
    button.config(bg = "white")
    id = buttons.index(button)
    checkTab[id // M][id % M]=0
    pass
def leftClick(button,i,j,buttons):
    button.config(bg="blue")
    id = buttons.index(button)
    checkTab[id // M][id % M] = 'b'
    pass

def checkWin(infoLabel):
    if(game_table==checkTab):
        infoLabel.config(text="You win")
        msg = tk.Message(root, text="You win")

    else:
        infoLabel.config(text="You lose")
        msg = tk.Message(root, text="You lose")


def findNeightbours(tab,x,y):
    neightbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            if y + 1 >= 0 and y+1 < N:
                if x + j >= 0 and x + j < M:
                    neightbours.append((x + j, y + i))

    return neightbours

def initGameBoard(game_table):
    for i in range(N):
        for j in range(M):
            game_table[i][j]=0
    b_count = black_count
    tableX = [[0 for j in range(M)] for i in range(N)]
    neightboursX = [[0 for j in range(M)] for i in range(N)]
    while b_count :
        x = random.randint(0,M-1)
        y = random.randint(0,N-1)
        if tableX[x][y]==0:
            tableX[x][y] = 'b'
            b_count -= 1
            game_table[x][y] = 'b'

    for i in range(N):
        for j in range(M):
            b_count = 0
            if i > 0 and i +1 < N:
                if j > 0 and j +1 < M:
                    for k in range(3):
                        for x in range(3):
                            if tableX[i+k-1][j+x-1]=='b':
                                b_count += 1
                    neightboursX[i][j] = b_count
            if i == 0 and j == 0:
                for k in range(2):
                    for x in range(2):
                        if tableX[k][x]== 'b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif i == N-1 and j == M-1:
                for k in range(2):
                    for x in range(2):
                        if tableX[i-k][j-x]== 'b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif i == 0 and j == M - 1:
                for k in range(2):
                    for x in range(2):
                        if tableX[i+k][j-x]== 'b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif i == N-1 and j == 0:
                for k in range(2):
                    for x in range(2):
                        if tableX[i-k][j+x]== 'b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif i == 0:
                for k in range(2):
                    for x in range(3):
                        if tableX[i+k][j-1+x]=='b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif i == N-1:
                for k in range(2):
                    for x in range(3):
                        if tableX[i + k-1][j - 1 + x] == 'b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif j == 0:
                for k in range(3):
                    for x in range(2):
                        if tableX[i+k-1][j+x]=='b':
                            b_count += 1
                neightboursX[i][j] = b_count
            elif j == N-1:
                for k in range(3):
                    for x in range(2):
                        if tableX[i+k-1][j+x-1]=='b':
                            b_count += 1
                neightboursX[i][j] = b_count
    return neightboursX

def restartGame(root,up_panel,buttons,game_table,neightbours):

    buttons = initBoard(root, up_panel,game_table,neightbours)






if __name__ == '__main__':
    root = initWindow()
    up_panel = initUpPanel(root)
    buttons = initBoard(root,up_panel,game_table,neightbours)
    up_panel[1].bind(
        "<Button-1>", lambda event: restartGame(root,up_panel,buttons,game_table,neightbours)
    )
    root.mainloop()