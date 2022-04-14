import os
from datetime import datetime
from labList import labList

now = datetime.now()
str_now = f'{now:%Y-%m-%d_%H%M%S}'

lab_list = labList()
s = 'test'

''' 基本構文
IF(ISNUMBER(開始セル)*1, IFERROR(VLOOKUP(TEXT(開始セル, "@"),範囲,戻り値列,FALSE), 0), 0) + …

開始セルに数値が入っていた場合、検索範囲から、開始セルの値を検索し、
'''

start_column = 'G' # 開始セルの列を文字列で入力
start_row = '10' # 開始セルの行を文字列で入力
start_cell = start_column + start_row
value = True # 検索範囲の対象が文字列の場合「True」、数値のままなら「False」
sheet = 'レポート4!' # 検索範囲の存在するシートを記入。末尾に「!」
search_start = '$' + 'G' # 検索範囲の開始列
search_end = '$' + 'V' # 検索範囲の末尾列
area = sheet + search_start + ':' + search_end
return_column = '16' # 戻り値列（検索範囲の開始列を1とする）

s_list = []

s_list.append('IF(ISNUMBER(')
s_list.append(start_cell)

# 以下で文字列の変換が必要か判定
if value:
    s_list.append(')*1, IFERROR(VLOOKUP(TEXT(')
else:
    s_list.append(')*1, IFERROR(VLOOKUP(')
s_list.append(start_cell)
if value:
    s_list.append(', "@"),')
else:
    s_list.append(',')
# 判定ここまで

s_list.append(area)
s_list.append(',')
s_list.append(return_column)
s_list.append(',FALSE), 0), 0)')
s_list.append(' +\n')


s = ''.join(s_list)


log_path = 'log/' + str_now + '.txt'
with open(log_path, mode='w', encoding='utf-8') as f: # output text file
    f.write(s)

print("End")

#this programm is End