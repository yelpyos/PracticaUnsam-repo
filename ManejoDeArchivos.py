with open('camion.csv', 'rt') as f:
    data = f.read()

print(data)

with open('camion.csv', 'rt') as f:
    for line in f:
        print(line, end='')


