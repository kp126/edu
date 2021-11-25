from sys import argv

name, output_in_hours, rate_per_hour, bonus = argv

print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print('\nФормула расчета: (выработка в часах * ставка в час) + премия\n')

print((float(output_in_hours) * float(rate_per_hour)) + float(bonus))
