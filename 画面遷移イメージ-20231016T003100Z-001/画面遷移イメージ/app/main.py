from Controller.title.con_title import *
from Controller.title.cui_title import * 
from Controller.game.con_game import *
from Controller.log.con_log import *
from Controller.setting.con_setting import *


# 関数入り辞書を定義
UI = {
	'title'  : con_title,
	'game'   : con_game,
	'log'    : con_log,
	'setting': con_setting,
	}

# 初期値はtitleでタイトル画面からゲームが始まることを意味する
flag = 'title'
# この中でゲームが完結する
while True:
	if flag == 'exit':
		break
	flag = UI[flag]()