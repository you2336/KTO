import title_con
import game_con
import log_con
import setting_con

# 関数入り辞書を定義
UI = {
	'title'  : title_con.display,
	'game'   : game_con.display,
	'log'    : log_con.display,
	'setting': setting_con.display,
	}

# 初期値はtitleでタイトル画面からゲームが始まることを意味する
flag = 'title'
# この中でゲームが完結する
while True:
	if flag == 'exit':
		break
	flag = UI[flag]()