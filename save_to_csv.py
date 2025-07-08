import csv

def save_to_csv(rows, attrs, filename='rentals.csv'):
    try:
        with open(filename, 'x', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(attrs)
            writer.writerows(rows)
    except FileExistsError:
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)