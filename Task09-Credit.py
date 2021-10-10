def annuitentny_platezh(i, n, s):
    # Вычисдяем по формуле из задачи
    # i - процент
    # n - количество лет
    # s - сумма кредита
    k =  i * (1 + i) ** n / ((1 + i) ** n - 1)
    a = k * s
    return a  # размер аннуитентного платежа


def calc_body_credit(a, s, i):
    return a - (s * i)


def viplachennye_percent(s, i):
    return s * i


s = float(input("Введите сумму кредита: "))
n = float(input("На сколько лет выдан? "))
i = float(input("Сколько процентов годовых? "))

i /= 100
a = annuitentny_platezh(i, n, s)

period = 0
vp = 0  # выплаченные проценты
body = 0 # тело кредита

while period <= n:
    period += 1
    s -= vp
    vp = viplachennye_percent(s, i)
    body = calc_body_credit(a, s, i)

    print("\nПериод:", period)
    print("Остаток долга на начало периода:", s)
    print("Выплачено процентов:", vp)
    print("Выплачено тела кредита:", body)

