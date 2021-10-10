def annu_pay(i, n, s):
    # Вычисдяем по формуле из задачи
    k = i * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    a = k * s
    return a  # размер аннуитентного платежа


def calc_pay(i, n, s):
    # Вычисляем разность аннуитентный алатеж - проценты
    payd_percent = s * i  # выплаченные проценты
    pay_credit = annu_pay(i, n, s) - payd_percent
    return pay_credit

def calc_body(s, percent_credit):
    return s - percent_credit

s = float(input("Введите сумму кредита: "))
n = float(input("На сколько лет выдан? "))
i = float(input("Сколько процентов годовых? "))


# paid interests - выплаченные проценты
# body_credit - тело кредита
# anuit_pay - аннуитентный платеж

percent_credit = calc_pay(i, n, s)
body_credit = s -

period = 0
summa_credit = 0
while period <= n:
    period += 1
    summa_credit = s - summa_credit
    print("Период:", n)
    print("Остаток долга на начало периода:")
    print("Выплачено процентов:")
    print("Выплачено тела кредита:")
