# ==============================================================================
# FÁJL NÉV: 129_cyber_amoba_matrix.py
# SORSZÁM: 125 -> UTÓD: 129
#
# LEÍRÁS ÉS FELADAT:
# Nagyvállalati 10x10-es Amőba (Gomoku Core) és Mátrix-Logikai Játékmodul.
# Tisztán a terminálban fut, külső grafikus könyvtárak nélkül. Egy 10x10-es 
# kétdimenziós tömböt kezel. Tartalmaz egy beépített, heurisztikus mini-AI 
# ellenfelet, amely figyeli a játékos lépéseit és védekezési mintákat aktivál.
# A győzelemhez 5 egymás melletti jel (X vagy O) szükséges vízszintesen, 
# függőlegesen vagy átlósan.
# ==============================================================================

import os
import random
import time

class CyberAmobaMatrix:
    def __init__(self):
        self.size = 10
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.player_sign = "X"
        self.ai_sign = "O"

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========================================================")
        print("         CYBER-BORSOD ADAT-MÁTRIX -> 10x10 AMŐBA        ")
        print("=========================================================")
        # Oszlop fejléc
        print("    " + "   ".join([str(i) for i in range(self.size)]))
        print("  +" + "---+" * self.size)
        for r_idx, row in enumerate(self.board):
            print(f"{r_idx} | " + " | ".join(row) + " |")
            print("  +" + "---+" * self.size)
        print("=========================================================")

    def check_line(self, r, c, dr, dc, sign):
        """Ellenőrzi, hogy van-e 5 egymás melletti jel az adott irányban."""
        count = 0
        for i in range(5):
            nr, nc = r + i * dr, c + i * dc
            if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == sign:
                count += 1
            else:
                break
        return count == 5

    def check_winner(self, sign):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for r in range(self.size):
            for c in range(self.size):
                for dr, dc in directions:
                    if self.check_line(r, c, dr, dc, sign):
                        return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def ai_smart_move(self):
        """Heurisztikus AI: Először a nyerést keresi, utána a játékos blokkolását (3-4 jelnél)."""
        # 1. Megnézi, tud-e nyerni most
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == " ":
                    self.board[r][c] = self.ai_sign
                    if self.check_winner(self.ai_sign):
                        return
                    self.board[r][c] = " "

        # 2. Megnézi, kell-e blokkolni a játékost (X)
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == " ":
                    self.board[r][c] = self.player_sign
                    if self.check_winner(self.player_sign):
                        self.board[r][c] = self.ai_sign
                        return
                    self.board[r][c] = " "

        # 3. Ha nincs közvetlen veszély, rak a közép közelébe véletlenszerűen
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == " "]
        if empty_cells:
            # Preferáljuk a belső 6x6-os magot a jobb taktika érdekében
            center_cells = [(r, c) for r, c in empty_cells if 2 <= r <= 7 and 2 <= c <= 7]
            target = random.choice(center_cells) if center_cells else random.choice(empty_cells)
            self.board[target[0]][target[1]] = self.ai_sign

    def play_game(self):
        while True:
            self.print_board()
            # Játékos lépés bekérése és validálása
            try:
                move = input("Adja meg a koordinátákat (sor oszlop, pl: 4 5): ")
                row, col = map(int, move.split())
                if not (0 <= row < self.size and 0 <= col < self.size) or self.board[row][col] != " ":
                    print("❌ Hiba: Érvénytelen vagy már foglalt mező!")
                    time.sleep(1)
                    continue
            except ValueError:
                print("❌ Hiba: Két számot adj meg szóközzel elválasztva!")
                time.sleep(1)
                continue

            # Játékos lépése
            self.board[row][col] = self.player_sign
            if self.check_winner(self.player_sign):
                self.print_board()
                print("🏆 SZÉP MUNKA, TÁBORNOK! GYŐZTÉL A GÉP ELLEN! 🏆")
                break

            if self.is_full():
                self.print_board()
                print("🤝 Döntetlen! A mátrix megtelt.")
                break

            # AI lépése
            print("[*] AI gondolkodik a lépésen...")
            time.sleep(0.4)
            self.ai_smart_move()
            
            if self.check_winner(self.ai_sign):
                self.print_board()
                print("🤖 A kiber-AI győzött! A rendszert optimalizálni kell.")
                break

if __name__ == "__main__":
    game = CyberAmobaMatrix()
    game.play_game()
