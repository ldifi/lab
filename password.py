p = input()
p_low = False
p_up = False
p_sim = False
p_ch = False
for char in p:
    if char.isnumeric():
        p_ch = True
    if char.islower():
        p_low = True
    if char.isupper():
        p_up = True
    if char in '&?@*^%!.,№:;':
        p_sim = True

if p_low and p_up and p_sim and p_ch is True:
    print("Надежный пароль")
elif p_low is False:
    print("Добавьте буквы нижнего регистра")
elif p_up is False:
    print("Добавьте буквы верхнего регистра")
elif p_ch is False:
    print("Добавьте цифры")
elif p_sim is False:
    print("Добавьте специальные символы")
else:
    print("Вы не ввели пароль!")