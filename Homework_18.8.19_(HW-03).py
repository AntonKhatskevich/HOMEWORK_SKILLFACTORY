amount = 0
tickets = int(input("Введите количество билетов: "))
for age in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        amount += 0
    elif 18 <= age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Конференция для Вас бесплатная!")
else:
    print("Кол-во билетов:", tickets, "шт.")
if tickets > 3:
    discount = amount / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате с учетом скидки:", "%.2f" % (amount - discount), "руб.")
if tickets < 4:
    Nodiscount = amount
    print("К оплате:", "%.2f" % Nodiscount, "руб.")
