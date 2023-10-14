from os import system
from time import sleep
from itertools import count, product

import numpy as np

class Othello:
  LEN = 8
  CAN, WALL, AIR, BLACK, WHITE = list(range(-2, 3))
  PIECE = ['・', '●', '○', '＊', '']  # 0, 1, 2, -2, -1


  def __init__(self):
    self.board = np.array(
      [[Othello.WALL if {i, j} & {0, Othello.LEN + 1} else Othello.AIR for i in range(Othello.LEN + 2)] for j in range(Othello.LEN + 2)]
    )
    first_pos = Othello.LEN // 2
    for i, j in product({first_pos, first_pos + 1}, repeat=2):
      self.board[i][j] = Othello.WHITE if i == j else Othello.BLACK
    self.turn = Othello.BLACK
    self.enemy = self.turn % 2 + 1


  def display(self):
    system('cls')

    print(Othello.PIECE[self.turn], end='')
    for i in range(Othello.LEN):
      print(chr(ord('Ａ') + i), end='')
    print()

    for i, line in enumerate(self.board[1:Othello.LEN + 1]):
      print(chr(ord('①') + i), end='')
      for pixel in line:
        print(Othello.PIECE[pixel], end='')
      print()


  def input_point(self):
    print('【先攻:黒色のターン】' if self.turn % 2 else '【後攻:白色のターン】')
    while True:
      try:
        point = input('英語数字の順で入力してください:').translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
        x = ord(point[0].lower()) - ord('a') + 1
        y = int(point[1:])
        if self.board[y][x] == Othello.CAN:
          return x, y

      except:
        pass


  def put(self, x, y):
    for move_y, move_x, times in self.can_put(x, y):
      for time in range(times + 1):
        self.board[y + move_y * time][x + move_x * time] = self.turn


  def can_put(self, x, y):
    if not(0 < x <= Othello.LEN and 0 < y <= Othello.LEN):
      return False
    if self.board[y][x] not in {Othello.CAN, Othello.AIR}:
      return False

    result = []
    enemy_filter = np.array(
      [[None if i == j == 1 else self.enemy for i in range(3)] for j in range(3)]
    )
    for move_y, line in enumerate(self.board[y - 1:y + 2, x - 1: x + 2] == enemy_filter, -1):
      for move_x, is_enemy in enumerate(line, -1):
        if is_enemy:
          for times in count(2):
            if self.board[y + move_y * times][x + move_x * times] == self.turn:
              result += [[move_y, move_x, times - 1]]
            if self.board[y + move_y * times][x + move_x * times] not in {self.enemy, Othello.CAN}:
              break

    return result


  def can_put_all(self):
    result = False
    for y, x in product(range(1, Othello.LEN + 1), repeat=2):
      if self.board[y][x] == Othello.CAN:
        self.board[y][x] = Othello.AIR
      if self.can_put(x, y):
        self.board[y][x] = Othello.CAN
        result = True

    return result


  def play(self):
    while True:
      if not self.can_put_all():
        self.display()
        print('先攻:黒色' if self.turn % 2 else '後攻:白色', 'は置く場所がありません')
        sleep(2)
        self.turn, self.enemy = self.enemy, self.turn
        if not self.can_put_all():
          print('先攻:黒色' if self.turn % 2 else '後攻:白色', 'も置く場所がありません')
          sleep(2)
          break
      self.display()
      x, y = self.input_point()
      self.put(x, y)
      self.turn, self.enemy = self.enemy, self.turn

    black = np.count_nonzero(self.board == Othello.BLACK)
    white = np.count_nonzero(self.board == Othello.WHITE)
    if black > white:
      print('先攻:黒色の勝利！')
    elif black < white:
      print('後攻:白色の勝利！')
    else:
      print('引き分け')
    print(f'(黒色:{black}個, 白色:{white}個)')
    system('pause')


  def start(self):
    self.play()


def main():
  system('color f0')
  while True:
    othello = Othello()
    othello.start()


if __name__ == '__main__':
  main()