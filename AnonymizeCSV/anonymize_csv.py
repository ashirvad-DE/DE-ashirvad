import csv
import hashlib

def hash_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def anonymize_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            row['first_name'] = hash_value(row['first_name'])
            row['last_name'] = hash_value(row['last_name'])
            row['address'] = hash_value(row['address'])
            writer.writerow(row)

if __name__ == "__main__":
    anonymize_csv('data/sample_data.csv', 'data/anonymized_data.csv')
