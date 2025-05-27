line = input('Введите строку: ')

if line[0] == 'a' and line[1] == 'b' and line[2] == 'c':
    result = 'www' + line[3:]
else:
    result = line + 'zzz'

print(result)