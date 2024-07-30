import csv
import faker

def generate_csv(file_name, num_rows):
    fake = faker.Faker()
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        
        for _ in range(num_rows):
            first_name = fake.first_name()
            last_name = fake.last_name()
            address = fake.address().replace('\n', ', ')
            date_of_birth = fake.date_of_birth()
            writer.writerow([first_name, last_name, address, date_of_birth])

if __name__ == "__main__":
    generate_csv('data/sample_data.csv', 1000) 
