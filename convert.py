import csv

def hex_with_0x_to_ascii(input_file, output_file, hex_column_name, txt_output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as csv_in:
            reader = csv.DictReader(csv_in)
            if hex_column_name not in reader.fieldnames:
                print(f"Column '{hex_column_name}' not found in the input CSV file.")
                return
            
            with open(output_file, 'w', newline='', encoding='utf-8') as csv_out, open(txt_output_file, 'w', encoding='utf-8') as txt_out:
                writer_csv = csv.DictWriter(csv_out, fieldnames=[hex_column_name, 'ASCII'])
                writer_csv.writeheader()

                ascii_string = ''  # To store concatenated ASCII characters

                for row in reader:
                    hex_data_with_0x = row[hex_column_name]
                    hex_data = int(hex_data_with_0x, 16)
                    ascii_data = chr(hex_data)
                    writer_csv.writerow({hex_column_name: hex_data_with_0x, 'ASCII': ascii_data})
                    
                    # Concatenate ASCII characters
                    ascii_string += ascii_data

                # Write the concatenated ASCII string to the txt file
                txt_out.write(ascii_string)
                
        print(f"Hex data in '{hex_column_name}' converted to a single ASCII string and exported to '{output_file}'. ASCII data also exported to '{txt_output_file}' successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these values with your file names and column name
input_csv_file = 'output.csv'
output_csv_file = 'ascii_output.csv'
hex_column_name = 'data'
output_txt_file = 'ascii_output.txt'

hex_with_0x_to_ascii(input_csv_file, output_csv_file, hex_column_name, output_txt_file)
