def annu_pay_in_year(i, n, s):  # расчет размера ануитентного платежа в год
    # i - проценты
    # n - время
    # s - сумма кредита
    a = s * i * (1 + i) ** n / (1 + i) ** n - 1
    return a  # размер аннуитентного платежа


def payed_percent_in_year(i, s):    # рассчет процентов за один год
    pay_percent = s * i / 100
    return pay_percent


def pay_on_credit_in_year(a, i):    # расчет выплаты по кредиту
    p_in_year = a - i
    return p_in_year


ostatok = float(input("Введите сумму кредита: "))
time_n = float(input("На сколько лет выдан? "))
percent_i = float(input("Сколько процентов годовых? "))

period = 0
percent_sum = 0
body_credit = 0
a_pay = 0
n = time_n

while period <= n:
    period += 1
    if n == 3:
        n += 2
        i += 2

    print("Период:", time_n)
    a_pay = annu_pay_in_year(percent_i, time_n, ostatok)
    print("Остаток долга на начало периода:", ostatok)
    ostatok -= pay_on_credit_in_year(a_pay, percent_i)
    percent_sum += payed_percent_in_year( percent_i, ostatok)
    print("Выплачено процентов:", percent_sum)
    body_credit += pay_on_credit_in_year(a_pay, percent_i)
    print("Выплачено тела кредита:", body_credit)
