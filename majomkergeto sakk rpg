import random
import os

WIDTH = 8
HEIGHT = 8

PLAYER = "👨"
ENEMY = "🤖"
TREASURE = "💰"
SHIELD = "🛡"
DATA = "💾"
HQ = "🏰"
EMPTY = "🟩"

player_hp = 100
player_xp = 0
player_money = 0
player_shield = 0

player_pos = [4, 4]

world = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# HQ
world[7][0] = HQ

# Kincsek
for _ in range(5):
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if world[y][x] == EMPTY:
        world[y][x] = TREASURE

# Pajzsok
for _ in range(3):
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if world[y][x] == EMPTY:
        world[y][x] = SHIELD

# Adatcsomagok
for _ in range(3):
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if world[y][x] == EMPTY:
        world[y][x] = DATA

# Hackerek
enemies = []

for _ in range(5):
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)

        if world[y][x] == EMPTY and [x, y] != player_pos:
            enemies.append([x, y])
            break


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw():
    clear()

    print("╔════════════════════════════╗")
    print("║      CYBER-BORSOD HQ       ║")
    print("╚════════════════════════════╝")

    print()

    for y in range(HEIGHT):
        row = ""

        for x in range(WIDTH):

            if [x, y] == player_pos:
                row += PLAYER + " "
            elif [x, y] in enemies:
                row += ENEMY + " "
            else:
                row += world[y][x] + " "

        print(row)

    print()
    print(f"❤️ HP: {player_hp}")
    print(f"⭐ XP: {player_xp}")
    print(f"💰 Token: {player_money}")
    print(f"🛡 Pajzs: {player_shield}")
    print()
    print("W A S D = Mozgás")
    print("Q = Kilépés")


def fight():
    global player_hp
    global player_xp

    enemy_hp = random.randint(15, 30)

    print("\n⚠ HACKER ÉSZLELVE!")

    while enemy_hp > 0 and player_hp > 0:

        print(f"\n🤖 Hacker HP: {enemy_hp}")
        print(f"❤️ Te HP: {player_hp}")

        action = input("\n[T]ámadás [M]enekülés: ").lower()

        if action == "m":
            print("🏃 Sikeres menekülés!")
            return

        damage = random.randint(8, 20)
        enemy_hp -= damage

        print(f"⚔ Sebzés: {damage}")

        if enemy_hp <= 0:
            print("🎉 Hacker legyőzve!")
            player_xp += 25
            return

        enemy_damage = random.randint(5, 15)

        if player_shield > 0:
            enemy_damage //= 2

        player_hp -= enemy_damage

        print(f"🤖 Visszatámadás: {enemy_damage}")

    if player_hp <= 0:
        print("\n💀 GAME OVER")
        quit()


while True:

    draw()

    move = input("\n👉 Lépés: ").lower()

    if move == "q":
        break

    x, y = player_pos

    if move == "w" and y > 0:
        y -= 1

    elif move == "s" and y < HEIGHT - 1:
        y += 1

    elif move == "a" and x > 0:
        x -= 1

    elif move == "d" and x < WIDTH - 1:
        x += 1

    else:
        continue

    player_pos = [x, y]

    # Ellenség
    if player_pos in enemies:
        fight()

        if player_pos in enemies:
            enemies.remove(player_pos)

    tile = world[y][x]

    if tile == TREASURE:
        gain = random.randint(10, 50)
        player_money += gain
        print(f"\n💰 Találtál {gain} tokent!")

        world[y][x] = EMPTY
        input("\nENTER...")

    elif tile == SHIELD:
        player_shield += 1

        print("\n🛡 Firewall pajzs megszerezve!")
        world[y][x] = EMPTY
        input("\nENTER...")

    elif tile == DATA:
        player_xp += 15

        print("\n💾 Adatcsomag begyűjtve!")
        world[y][x] = EMPTY
        input("\nENTER...")

    elif tile == HQ:

        draw()

        print("\n🏰 CYBER-BORSOD HQ ELÉRVE!")
        print("\n🎉 KÜLDETÉS TELJESÍTVE!")

        print(f"\n⭐ XP: {player_xp}")
        print(f"💰 Token: {player_money}")
        print(f"🛡 Pajzs: {player_shield}")

        break
