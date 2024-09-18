import csv

# Input and output file names
input_file = "test.txt"
output_file = "output.csv"

# Headers from the image
headers = ["Name", "Author", "Year", "Publication Name", "DOI", "Publication Year", "Publication Type", "Database", "Todo"]

# Open input file and create output CSV file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    # Read input file and write data to CSV
    current_entry = {}
    for line in infile:
        line = line.strip()
        if line.startswith("%T"):
            if current_entry:
                writer.writerow(current_entry)
                current_entry = {}
            current_entry["Name"] = line[3:].strip()
        elif line.startswith("%A"):
            if "Author" not in current_entry:
                current_entry["Author"] = line[3:].strip()
            else:
                current_entry["Author"] += "; " + line[3:].strip()
        elif line.startswith("%D"):
            current_entry["Year"] = line[3:].strip()
            current_entry["Publication Year"] = line[3:].strip()
        elif line.startswith("%B"):
            current_entry["Publication Name"] = line[3:].strip()
        elif line.startswith("%U"):
            current_entry["DOI"] = line[3:].strip()

        current_entry["Database"] = "Aisel"
    # Write the last entry
    if current_entry:
        writer.writerow(current_entry)

print(f"CSV file '{output_file}' has been created with the specified headers.")