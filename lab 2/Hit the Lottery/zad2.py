money = int(input())

output = money // 100
money %= 100

output += money // 20
money %= 20

output += money // 10
money %= 10

output += money // 5
money %= 5

output += money

print(output)
