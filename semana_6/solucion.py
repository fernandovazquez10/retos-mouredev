
valores: list = ['✂️', '📄', '🗿', '🦎', '🖖']

resultados =  [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]

pts_player_1 = 0
pts_player_2 = 0

for resultado in resultados:
    player_1, player_2 = resultado
    vencibles: list = []
    index_player_1 = valores.index(player_1)
    if index_player_1 == 5:
        vencibles.append(valores[0])
    else:
        vencibles.append(valores[index_player_1 + 1])
    if index_player_1 < 2:
        index_player_1 += 6
    vencibles.append(valores[index_player_1 - 2])
    if player_2 in vencibles:
        pts_player_1 += 1
    else:
        pts_player_2 += 1

if pts_player_1 > pts_player_2:
    print("Player 1")
elif pts_player_1 < pts_player_2:
    print("Player 2")
else:
    print("Tie")
    