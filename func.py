'''self made functions
labList
vLookupLine
'''

def labList():
    """Making Long Uppercase Alphabets List
    A~Z, AA~ZZを順番に並べたリストを作る関数
    主にExcelで複数列のリストを扱うときに使う"""
    
    ab_list = []
    dab_list = []
    lab_list = []

    for i in range(65,91):
        ab_list.append(chr(i))

    for j in range(26):
        for k in range(26):
            dab_list.append(ab_list[j] + ab_list[k])

    '''dab_listの中身チェック用
    path = 'list/dablist.txt'

    with open(path, mode='w', encoding='utf-8') as f:
        for d in dab_list:
            f.write('%s\n' % d)
    '''

    lab_list = ab_list + dab_list

    '''lab_listの中身チェック用
    path = 'list/lablist.txt'

    with open(path, mode='w', encoding='utf-8') as f:
        for d in lab_list:
            f.write('%s\n' % d)
    '''
    return lab_list

def vLookupLine(start_cell, value, area, return_column):
    '''条件付きVLOOKUP関数の数式を作る
    
    基本構文
    IF(ISNUMBER(開始セル)*1, IFERROR(VLOOKUP(TEXT(開始セル, "@"),範囲,戻り値列,FALSE), 0), 0)

    開始セルに数値が入っていた場合、検索範囲から、開始セルの値を検索し、戻り値列の値を返す。
    '''
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

    s = ''.join(s_list)
    
    return s