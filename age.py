driving = input('請問你有沒有開過車?: ')
age = input('請問你年紀為?: ')
if driving == '有':
    if int(age) >= 18:
        print('你通過測驗了。')
    else:
        print('未滿18歲不能開車!!!')
elif driving == '沒有':
    if int(age) >= 18:
        print('考不到駕照嗎? 加油!')
    else:
        print('滿18歲就可以考駕照了。')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有, 請確認!')