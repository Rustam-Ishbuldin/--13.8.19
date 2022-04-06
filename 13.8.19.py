number_tickets = int(input("Введите необходимое количество билетов:"))
price_tickets = 0
for i in range(number_tickets):
    age = int(input("Введите возраст посетителя, для которого преобретается билет:"))
    i += 1
    if age < 18:
        print("Лицам до 18 лет билет Бесплатно!")
    elif 18 <= age < 25:
        price_tickets += 990
        print("Стоимость билета 990 рублей")
    else:
        price_tickets += 1390
        print("Стоимость билета 1390 рублей")
if number_tickets > 3:
    price_tickets = price_tickets*0.9
    print("При копупке свыше 3-х билетов предоставляется скидка 10%:", price_tickets)
else:
    print("Общая сумма к оплате составляет:", price_tickets)