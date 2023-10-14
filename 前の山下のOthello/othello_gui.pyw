import PySimpleGUI as sg
import numpy as np

from othello import Othello

class Othellogui(Othello):
  GRID_LEN = 65
  RADIUS = int(GRID_LEN * 0.35)
  sg.theme('black')


  def __init__(self):
    super().__init__()
    self.copy_board = [[None for _ in range(Othello.LEN)] for _ in range(Othello.LEN)]
    self.window = self.create_window()


  def create_window(self):
    left_frame = sg.Frame(
      title = '',
      layout = [
        [sg.T('', k='END_T')],
        [sg.T('', k='NUM_T')]
      ],
      pad = (0, 0),
      border_width = 0
    )

    right_frame = sg.Frame(
      title = '',
      layout = [
        [sg.B('continue', auto_size_button=True, k='CONTINUE_B', visible=False)],
        [sg.T('', k='SUB_T')]
      ],
      pad = (0, 0),
      border_width = 0,
      expand_x = True,
      element_justification = 'center'
    )

    layout = [
      [sg.T('【先攻:黒色のターン】', k='TURN_T')],
      [sg.G(
        canvas_size = (Othellogui.GRID_LEN * Othello.LEN, Othellogui.GRID_LEN * Othello.LEN),
        graph_bottom_left = (0, 0),
        graph_top_right = (Othellogui.GRID_LEN * Othello.LEN, Othellogui.GRID_LEN * Othello.LEN),
        background_color = '#000000',
        enable_events = True,
        k = 'BOARD_G'
      )],
      [left_frame, right_frame]
    ]

    return sg.Window('TETRIS', layout, font='メイリオ', use_default_focus=False)


  def create_figure(self, graph):
    LEN = Othellogui.GRID_LEN

    self.figure = [[dict() for _ in range(Othello.LEN + 1)] for _ in range(Othello.LEN + 1)]
    for y in range(Othello.LEN + 1):
      for x in range(Othello.LEN + 1):
        top_left = LEN * x, LEN * (y + 1)  # x, y
        bottom_right = LEN * (x + 1), LEN * y
        center_location = int(LEN * (x + 0.5)), int(LEN * (y + 0.5))

        self.figure[Othello.LEN - y - 1][x][-2] = graph.draw_rectangle(  # 置くことができる
          top_left = top_left,
          bottom_right = bottom_right,
          fill_color = '#FFFF00',
          line_color = '#000000',
          line_width = 1
        )

        self.figure[Othello.LEN - y - 1][x][0] = graph.draw_rectangle(  # 空白
          top_left = top_left,
          bottom_right = bottom_right,
          fill_color = '#008000',
          line_color = '#000000',
          line_width = 1
        )

        self.figure[Othello.LEN - y - 1][x][1] = graph.draw_circle(  # 黒
          center_location = center_location,
          radius = Othellogui.RADIUS,
          fill_color = '#000000',
          line_width = 1
        )

        self.figure[Othello.LEN - y - 1][x][2] = graph.draw_circle(  # 白
          center_location = center_location,
          radius = Othellogui.RADIUS,
          fill_color = '#FFFFFF',
          line_width = 1
        )


  def display(self, graph):
    for y, line in enumerate(self.board[1:Othello.LEN + 1]):
      for x, pixel in enumerate(line[1:Othello.LEN + 1]):
        if pixel == self.copy_board[y][x]:
          continue
        elif pixel != Othello.CAN:
          graph.bring_figure_to_front(self.figure[y][x][Othello.AIR])
        graph.bring_figure_to_front(self.figure[y][x][pixel])
        self.copy_board[y][x] = pixel


  def judge_all(self):
    if not self.can_put_all():
      self.display(self.window['BOARD_G'])
      self.turn, self.enemy = self.enemy, self.turn
      if not self.can_put_all():
        if np.any(self.board == Othello.AIR):
          self.window['SUB_T'].update('*どちらも置くことができません')
        return True
      else:
        if np.any(self.board == Othello.AIR):
          self.window['SUB_T'].update(
            '*後攻:白色は置くことができません' if self.turn % 2 else '*先攻:黒色は置くことができません'
          )
        return False
    else:
      self.window['SUB_T'].update('')
      return False


  def play(self):
    timeout = 0
    while True:
      event, value = self.window.read(timeout)
      if event == sg.WIN_CLOSED:
        break

      elif event == 'BOARD_G':
        x, y = value['BOARD_G']
        x //= Othellogui.GRID_LEN
        y //= Othellogui.GRID_LEN

        if self.board[Othello.LEN - y][x + 1] != Othello.CAN:
          continue
        self.put(x + 1, Othello.LEN - y)
        self.turn, self.enemy = self.enemy, self.turn
        end_game = self.judge_all()
        self.display(self.window['BOARD_G'])
        self.window['TURN_T'].update(
          '【先攻:黒色のターン】' if self.turn % 2 else '【後攻:白色のターン】'
        )

        if end_game:
          black = np.count_nonzero(self.board == Othello.BLACK)
          white = np.count_nonzero(self.board == Othello.WHITE)
          if black > white:
            self.window['END_T'].update('先攻:黒色の勝利！')
          elif black < white:
            self.window['END_T'].update('後攻:白色の勝利！')
          else:
            self.window['END_T'].update('引き分け')

          self.window['NUM_T'].update(f'(黒色:{black}個, 白色:{white}個)')
          self.window['TURN_T'].update('【Game Set】')

          self.window['CONTINUE_B'].update(visible=True)

      elif event == 'CONTINUE_B':
        self.window['CONTINUE_B'].update(visible=False)
        super().__init__()
        self.copy_board = [[None for _ in range(Othello.LEN)] for _ in range(Othello.LEN)]
        self.window['TURN_T'].update('【先攻:黒色のターン】')
        self.window['SUB_T'].update('')
        self.window['END_T'].update('')
        self.window['NUM_T'].update('')
        self.judge_all()
        self.display(self.window['BOARD_G'])

      elif event == '__TIMEOUT__':
        self.create_figure(self.window['BOARD_G'])
        self.judge_all()
        self.display(self.window['BOARD_G'])
        timeout = None

    self.window.close()


def main():
  othello = Othellogui()
  othello.play()


if __name__ == '__main__':
  main()