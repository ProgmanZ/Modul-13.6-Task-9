def annuitentny_platezh(i, n, s):
    # Вычисдяем по формуле из задачи
    # i - процент
    # n - количество лет
    # s - сумма кредита
    k = i * (1 + i) ** n / ((1 + i) ** n - 1)
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

period = 1
vp = 0  # выплаченные проценты
body = 0 # тело кредита
count = 1
flag = True

while count <= n:
    vp = viplachennye_percent(s, i)
    body = calc_body_credit(a, s, i)

    print("\nПериод:", period)
    print("Остаток долга на начало периода:", s)
    print("Выплачено процентов:", vp)
    print("Выплачено тела кредита:", body)

    s -= body

    if period == 3 and flag:
        print("\nОстаток долга:",s)
        print("\n ====================\n")
        n_2 = float(input("На сколько лет продляется договор? "))
        i_2 = float(input("Увеличение ставки до: "))
        n += n_2 - period
        i = i_2 / 100
        a = annuitentny_platezh(i, n, s)
        period = 0
        flag = False

    count += 1
    period += 1


