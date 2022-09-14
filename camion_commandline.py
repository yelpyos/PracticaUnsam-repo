
import csv
import sys

def costo_camion(nombre_archivo):
    total_cost = 0.0
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                quantity = int(row[1])
                price = float(row[2])
                total_cost += quantity * price
            except ValueError:
                print('Bad row', row)
    return total_cost

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('costo total:', costo)
