
start_column = 'G'
start_row = '10'
columns = 10
cnt = 0


column_list = []
ab_list = []


for i in range(65,91):
    ab_list.append(chr(i))

ab_cnt = 0

while cnt < columns:
    while ab_cnt < 26:
        for i in ab_list:
            column_list.append(ab_list[i])
    cnt += 1


print(column_list)