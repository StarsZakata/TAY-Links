#Импорт библиотек
import matplotlib.pyplot as plt
import control.matlab as cmatlab
import control as control
#Оформляем в цикл, для удобства
start="yes"
def pereda(Kch,Kzn,Tch,Tzn):
    num = [Tch, Kch]
    den = [Tzn, Kzn]
    w = cmatlab.tf([Tch, Kch], [Tzn, Kzn])
    k = cmatlab.tf([Tch/2, Kch*2],[Tzn/2, Kzn])
    return w,k
while start=="yes":
#Начало программы
  print("----Внимание!----")
  print("Ввод передаточной функции до первого порядка!")
  print("Какую передаточную функцию вы хотите ввести? \n 1-Безинерционное звено \n 2-Апериадическое звено \n 3-Интегрирующее звено \n 4-Идеально дифференцирующее звено \n 5-Реально дифференцирующее звено")
  zveno = input("Введите номер звена: ")
#Узнаем вид передаточной функции и её запись
  if zveno == "1":
     print("----Ввод выглядит следующим образом----")
     print(" Kch \n ------ \n 1")
     Kch = float(input('Введите значение свободного члена числителя Kch= '))
     Kzn = 1
     Tch = 0
     Tzn = 0
     w,k=pereda(Kch,Kzn,Tch,Tzn)
     print("----Вы ввели следующую передаточную функцию----")
     print(w,k)
  elif zveno == "2":
      print("----Ввод выглядит следующим образом----")
      print("   Kch \n ------ \n Tzn p + 1")
      Kch = float(input('Введите значение свободного члена числителя Kch= '))
      Kzn = 1
      Tch = 0
      Tzn = float(input('Введите значение постоянной времени знаменателя Tzn= '))
      w, k = pereda(Kch, Kzn, Tch, Tzn)
      print("----Вы ввели следующую передаточную функцию----")
      print(w, k)
  elif zveno == "3":
      print("----Ввод выглядит следующим образом----")
      print(" 1 \n --- \n Tzn p ")
      Kch = 1
      Kzn = 0
      Tch = 0
      Tzn = float(input('Введите значение постоянной времени числителя Tzn= '))
      w, k = pereda(Kch, Kzn, Tch, Tzn)
      k = cmatlab.tf([Tch/2, Kch],[Tzn/2, Kzn])
      print("----Вы ввели следующую передаточную функцию----")
      print(w, k)
  elif zveno == "4":
      print("----Ввод выглядит следующим образом----")
      print(" Tch p ")
      Kch = 0
      Kzn = 1
      Tch = float(input('Введите значение постоянной времени числителя Kch=Tch= '))
      print("---------------------")
      Tzn = 0.000001
      print("Постоянная времени имеет такой вид, т.к. по условию ")
      print("ПОРЯДОК ПОЛИНОМА ЧИСЛИТЕЛЯ НЕ ДОЛЖЕН ПРЕВЫШАТЬ ПОРЯДОК ПОЛИНОМА ЗНАМЕНАТЕЛЯ")
      w, k = pereda(Kch, Kzn, Tch, Tzn)
      k = cmatlab.tf([Tch*2, Kch], [Tzn, Kzn])
      print("----Вы ввели следующую передаточную функцию----")
      print(w,k)
  elif zveno == "5":
      print("----Ввод выглядит следующим образом----")
      print("    Kch p \n ------ \n Tzn p + 1")
      Kch = 0
      Kzn = 1
      Tch = float(input('Введите значение постоянной времени знаменателя Kch=Tch= '))
      Tzn = float(input('Введите значение постоянной времени знаменателя Tzn= '))
      w, k = pereda(Kch, Kzn, Tch, Tzn)
      k = cmatlab.tf([Tch * 2, Kch], [Tzn/2, Kzn])
      print("----Вы ввели следующую передаточную функцию----")
      print(w, k)
  while True:
   fun=input("Получить графики(yes/no) \n ")
#Построение графиков
   if fun=="yes":
       TimeLine = []
       for i in range(0, 200,10):
         TimeLine.append(i)
# Построение переходной характеристики
       plt.figure(figsize=(9, 5))
       plt.subplot(1, 2, 1)
       y, x = cmatlab.step(w,TimeLine)
       plt.plot(x, y)
       y, x = cmatlab.step(k, TimeLine)
       plt.plot(x, y)
       plt.title('Переходная характеристика ')
       plt.ylabel('Амплитуда', fontsize=10, color='black' )
       plt.xlabel('Время(сек)', fontsize=8, color='black')
       plt.grid(axis='x', color='0.95')
       plt.legend(['K && T', 'K*2 && T/2'], fontsize=8, shadow=True)
# Построение импульсной характеристики
       plt.subplot(1, 2, 2)
       y, x = cmatlab.impulse(w,TimeLine)
       plt.plot(x, y)
       y, x = cmatlab.impulse(k, TimeLine)
       plt.plot(x, y)
       plt.title('Импульсная характеристика', )
       plt.xlabel('Время(сек)', fontsize=8, color='black')
       plt.grid(axis='x', color='0.95')
       plt.legend(['K && T', 'K*2 && T/2'])
# Вывод переходной и импульсной характеристики
       plt.figure(2, figsize=[9, 5])
# Построение АЧХ и ФЧХ
       mag, phase, omega = cmatlab.bode(w, dB=False)
       mag, phase, omega = cmatlab.bode(k, dB=False)
       plt.legend(['K && T', 'K*2 && T/2'])
       plt.show()
       print("Графики получены")
   elif fun=="no":
       print("------------------------------------------")
       print("Вы отказались в получении графика")
       print("------------------------------------------")
       break
  print("Вернуться к повторному вводу данных передаточной функции?(yes/no)")
  start= input('Итог= ')
#Закрываем программу
if start=="no":
    print("Работа программы завершена")

