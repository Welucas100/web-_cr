#리스트

date = ['5.15', '5.16', '5.17', '5.18']
temp = ['20', '22', '21', '22']
status = ['맑음', '흐림', '맑음', '흐림']

#5.15
print(f'{date[0]} {status[0]} {temp[0]}C')
print(f'{date[1]} {status[1]} {temp[1]}C')
print(f'{date[2]} {status[2]} {temp[2]}C')
print('-' * 30)

#for문 사용하기
for idx in range(3):
    print(f'{date[idx]} {status[idx]} {temp[idx]}C')
print('-' * 30)

#for, enumerate 사용하기
for idx, one in enumerate(date):
    print(f'idx: {idx}, one: {one}, 기온: {temp[idx]}, 상태: {status[idx]}')
