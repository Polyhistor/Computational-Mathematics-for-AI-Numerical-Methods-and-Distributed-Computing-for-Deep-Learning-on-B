import csv
import random
import string
import os
from typing import List, Dict

def generate_unique_id(length: int = 8) -> str:
    """Generate a unique ID for each reviewer."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def read_disputed_items(csv_file: str) -> List[Dict]:
    """Read disputed items from the CSV file."""
    disputed_items = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            
            # Print column names for debugging
            print("Column names in CSV:", reader.fieldnames)
            
            # Determine the correct column name for the title
            title_column = next((col for col in reader.fieldnames if 'name' in col.lower()), None)
            if not title_column:
                print("Error: Could not find a column for the paper title.")
                return []
            
            reviewer_columns = ['Marcellin', 'Pouya', 'Brian', 'Arnaud', 'Stones']
            
            for row in reader:
                if not all(row.get(reviewer, '').lower() == 'yes' for reviewer in reviewer_columns):
                    disputed_items.append({
                        'title': row[title_column],
                        'summary': f"Disagreement on relevance to numerical methods and/or big data applications for deep learning."
                    })
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    
    print(f"Number of disputed items found: {len(disputed_items)}")
    return disputed_items

def generate_survey_form(disputed_items: List[Dict]) -> str:
    """Generate the survey form content."""
    form_content = "# Anonymous Reflection Form\n\n"
    for i, item in enumerate(disputed_items, 1):
        form_content += f"## Disputed Item {i}: {item['title']}\n"
        form_content += f"Summary: {item['summary']}\n\n"
        form_content += "Your decision:\n"
        form_content += "[ ] Include  [ ] Exclude\n\n"
        form_content += "Reasoning for your decision:\n"
        form_content += "[Your explanation here]\n\n"
    return form_content

def main():
    csv_file = '../CSVs/Controversial Papers-Grid view.csv'
    disputed_items = read_disputed_items(csv_file)
    survey_content = generate_survey_form(disputed_items)
    
    # Generate a unique ID for this survey
    survey_id = generate_unique_id()
    
    # Save the survey to a file
    with open(f'survey_form_{survey_id}.md', 'w') as file:
        file.write(survey_content)
    
    print(f"Survey form generated: survey_form_{survey_id}.md")

if __name__ == "__main__":
    main()



