from tkinter import Tk, Button, Label, messagebox

# Cria uma instância do Tkinter
root = Tk()
root.title("Jogo da Velha")

# Variáveis globais
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
current_player = 1

# Função chamada quando um botão é clicado
def button_click(row, col):
    global current_player

    if board[row][col] == 0:
        if current_player == 1:
            board[row][col] = 1
            text = "X"
        else:
            board[row][col] = -1
            text = "O"

        buttons[row][col].config(text=text)

        if check_winner():
            messagebox.showinfo("Fim de Jogo", f"Jogador {current_player} venceu!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Fim de Jogo", "Empate!")
            reset_game()
        else:
            current_player = 2 if current_player == 1 else 1
            player_label.config(text=f"Jogador {current_player}")

# Verifica se há um vencedor
def check_winner():
    # Verifica linhas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return True

    # Verifica colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return True

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return True

    return False

# Verifica se houve empate
def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

# Reinicia o jogo
def reset_game():
    global board, current_player

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    current_player = 1
    player_label.config(text=f"Jogador {current_player}")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal")

# Cria a tela do jogador atual
player_label = Label(root, text=f"Jogador {current_player}", font=("Arial", 16))
player_label.grid(row=3, column=0, columnspan=3, pady=10)

# Cria os botões na interface gráfica
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                        command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Inicia a interface gráfica
root.mainloop()
