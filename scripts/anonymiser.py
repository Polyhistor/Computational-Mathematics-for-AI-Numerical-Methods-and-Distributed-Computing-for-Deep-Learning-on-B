import csv
import os
from typing import List, Dict

def read_disputed_items(csv_file: str) -> List[Dict]:
    disputed_items = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not all(row.get(reviewer, '').lower() == 'yes' for reviewer in ['Marcellin', 'Pouya', 'Brian', 'Arnaud', 'Stones']):
                    disputed_items.append({
                        'title': row.get('Name', 'Unknown Title'),
                        'summary': "Disagreement on relevance to numerical methods and/or big data applications for deep learning."
                    })
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return disputed_items

def generate_google_forms_csv(disputed_items: List[Dict], output_file: str):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Question Type', 'Option 1', 'Option 2'])
        for item in disputed_items:
            writer.writerow([f"{item['title']}\n{item['summary']}\nDo you think this paper should be included?", 'Multiple Choice', 'Include', 'Exclude'])
            writer.writerow([f"Reasoning for your decision on: {item['title']}", 'Paragraph', '', ''])

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    csv_file = os.path.join(project_root, 'CSVs', 'Controversial Papers-Grid view.csv')
    
    disputed_items = read_disputed_items(csv_file)
    if not disputed_items:
        print("No disputed items found or there was an error reading the file.")
        return

    output_file = os.path.join(project_root, 'google_forms_questions.csv')
    generate_google_forms_csv(disputed_items, output_file)
    print(f"Google Forms CSV generated: {output_file}")

if __name__ == "__main__":
    main()