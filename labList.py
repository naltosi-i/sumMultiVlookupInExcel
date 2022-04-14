def labList():
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

if __name__== '__main__':
    labList()