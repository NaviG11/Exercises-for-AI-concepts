from colored import Fore, Back, Style
import csv
import math

class DataSet:
    def __init__(self, data):
        self.data = data
        self.columns = self.extract_columns()
        self.percentile = 0.25  # Porcentaje para calcular los cuartiles y percentiles

    def extract_columns(self):
        columns = {}
        for col_index in range(len(self.data[0])):
            column_data = [row[col_index] for row in self.data]
            columns[col_index] = column_data
        return columns

    def column_mean(self, col_index):
        column_data = self.columns[col_index]
        return sum(column_data) / len(column_data)

    def column_median(self, col_index):
        column_data = sorted(self.columns[col_index])
        n = len(column_data)
        if n % 2 == 0:
            return (column_data[n // 2 - 1] + column_data[n // 2]) / 2
        else:
            return column_data[n // 2]

    def column_min(self, col_index):
        column_data = self.columns[col_index]
        return min(column_data)

    def column_max(self, col_index):
        column_data = self.columns[col_index]
        return max(column_data)

    def column_sum(self, col_index):
        column_data = self.columns[col_index]
        return sum(column_data)

    def column_std_dev(self, col_index):
        column_data = self.columns[col_index]
        mean = self.column_mean(col_index)
        variance = sum((x - mean) ** 2 for x in column_data) / len(column_data)
        return math.sqrt(variance)

    def set_percentile(self, percentile):
        self.percentile = percentile

    def column_percentile(self, col_index):
        column_data = sorted(self.columns[col_index])
        index = int(len(column_data) * self.percentile)
        return column_data[index]

    def column_quartiles(self, col_index):
        column_data = sorted(self.columns[col_index])
        n = len(column_data)
        q1_index = int(n * 0.25)
        q2_index = int(n * 0.5)
        q3_index = int(n * 0.75)
        return column_data[q1_index], column_data[q2_index], column_data[q3_index]

# Definir la dirección del archivo CSV
DIRECCTION = "../../data/StressLevelDataset.csv"

# Función para cargar los datos desde el archivo CSV
def load_data_from_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Omitir la primera fila (encabezados)
        for row in csv_reader:
            data.append([float(val) for val in row])
    return data

# Cargar los datos desde el archivo CSV
data = load_data_from_csv(DIRECCTION)

# Ejemplo de uso
dataset = DataSet(data)
#print("Number of columns:", len(dataset.columns))
column = int(input("Enter the column index: "))
print("Mean of column 0:", dataset.column_mean(column))
print("Median of column 0:", dataset.column_median(column))
print("Minimum value of column 0:", dataset.column_min(column))
print("Maximum value of column 0:", dataset.column_max(column))
print("Sum of column 0:", dataset.column_sum(column))
print("Standard deviation of column 0:", dataset.column_std_dev(column))
# Establecer el percentil al 80%
dataset.set_percentile(0.80)
print("80th percentile of column 0:", dataset.column_percentile(column))
# Calcular cuartiles de la columna 0
q1, q2, q3 = dataset.column_quartiles(column)
print("Q1 of column 0:", q1)
print("Q2 (median) of column 0:", q2)
print("Q3 of column 0:", q3)