# =================================================
#           ライブラリインポート
# =================================================
import PySimpleGUI as gui

# =================================================
#           変数定義
# =================================================
TEXT_YOURNAME = 'xxxxxxxxxx'

# =================================================
#           関数定義
# =================================================
def func_button_ok(name):
   window['ket_tex_name'].update(name)
   pass

# =================================================
#           ウィンドウレイアウト
# =================================================
layout = [
   [gui.Text('名前：'), gui.InputText(default_text='', key='key_box_name')],
   [gui.Button('OK', key='key_button_ok')],
   [gui.Text('')],
   [gui.Text('あなたの名前は'), gui.Text(TEXT_YOURNAME, key='ket_tex_name')]
]

# =================================================
#           ウィンドウ処理
# =================================================
# ウィンドウオブジェクトの作成
window = gui.Window('PySimpleGUI', layout, size=(400, 200))

# イベントのループ
while True:
   # イベントの読み込み
   event, values = window.read()
   # ウィンドウの×ボタンが押されれば終了
   if event == gui.WIN_CLOSED:
       break
   # ボタン操作時のアクション
   elif event == 'key_button_ok':
       # 関数呼び出し, 引数はテキストボックス入力データ
       func_button_ok(values['key_box_name'])

# ウィンドウ終了処理
window.close()
