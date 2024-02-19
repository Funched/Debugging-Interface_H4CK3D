import csv

def copy_column(input_file, output_file, column_name):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as csv_in:
            reader = csv.DictReader(csv_in)
            if column_name not in reader.fieldnames:
                print(f"Column '{column_name}' not found in the input CSV file.")
                return
            
            with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
                writer = csv.DictWriter(csv_out, fieldnames=[column_name])
                writer.writeheader()

                for row in reader:
                    writer.writerow({column_name: row[column_name]})
                
        print(f"Column '{column_name}' copied from '{input_file}' to '{output_file}' successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these values with your file names and column name
input_csv_file = 'Square-to-HEX.csv'
output_csv_file = 'output.csv'
target_column_name = 'data'

copy_column(input_csv_file, output_csv_file, target_column_name)
