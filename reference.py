print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь еще одно имя, указывающее на тот же объект!

del shoplist[0] # Я сделал первую покупку, поэтому удаляю ее из списка

print('shoplist:', shoplist)
print('mylist:', mylist)

print('Копирование при помощи полной вырезки')
mylist = shoplist[:] # Создаем копию путем полной вырезки
del mylist[0] # Удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)