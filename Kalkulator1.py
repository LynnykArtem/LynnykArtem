
input_value1=int(input("Введите первое число:"))
input_value2=int(input("Введите второе число:"))
operator=input("Что делаем?(+,-,*,/):")
if input_value2==0:
    print("Деление на ноль!!!")
elif operator == "+":
    result = input_value1 + input_value2
    print("Результат:" + str(result))
elif operator=="-":
    result=input_value1-input_value2
    print("Результат:" + str(result))
elif operator=="*":
    result=input_value1*input_value2
    print("Результат:" + str(result))
elif operator=="/":
    result=input_value1/input_value2
    print("Результат:" + str(result))
else:
    print("Выбрана неверная операция!")



