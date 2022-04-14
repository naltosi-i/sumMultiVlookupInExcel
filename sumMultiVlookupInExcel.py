import os
from datetime import datetime
import func

s = 'test'

''' 基本構文
IF(ISNUMBER(開始セル)*1, IFERROR(VLOOKUP(TEXT(開始セル, "@"),検索範囲,戻り値列,FALSE), 0), 0) + …

開始セルに数値が入っていた場合、検索範囲から、開始セルの値を検索し、戻り値列の値を返す。
次に隣の列の数値を検索し、戻り値列の値を加える。
以下目的の列まで同様の処理を行う。
'''

start_column = 'G' # 開始セルの列を文字列で入力
start_row = '10' # 開始セルの行を文字列で入力
start_cell = start_column + start_row
columns = 36 # VLOOKUPしたい列の数
value = True # 検索範囲の対象が文字列の場合「True」、数値のままなら「False」
sheet = 'レポート4!' # 検索範囲の存在するシートを記入。末尾に「!」
search_start = '$' + 'G' # 検索範囲の開始列
search_end = '$' + 'V' # 検索範囲の末尾列
area = sheet + search_start + ':' + search_end
return_column = '16' # 戻り値列（検索範囲の開始列を1とする）

now = datetime.now()
str_now = f'{now:%Y-%m-%d_%H%M%S}'

lab_list = func.labList()
# 自作モジュールの実行検証用
'''
path = 'list/lablist.txt'

with open(path, mode='w', encoding='utf-8') as f:
    for d in lab_list:
        f.write('%s\n' % d)
'''
# 検証ここまで


s = func.vLookupLine(start_cell, value, area, return_column)

s.append(' +\n')

s = '=' + s.rstrip(' +\n')

log_path = 'log/' + str_now + '.txt'
with open(log_path, mode='w', encoding='utf-8') as f: # output text file
    f.write(s)

print("End")

#this programm is End