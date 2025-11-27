price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки: {"{:.2f}".format(base)} ₽')
print(f'НДС: {"{:.2f}".format(vat_amount)} ₽')
print(f'Итого к оплате: {"{:.2f}".format(total)} ₽')
