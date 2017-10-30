#Оператор continue используется для указания Python, что необходимо пропустить все оставшиеся команды в текущем блоке цикла и продолжить со следующей итерации цикла
while True:
    s = input('Enter smth: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('Too little')
        continue
    print('The input string is of sufficient length')
    #other actions here