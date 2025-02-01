import csv
import re

# Regex to match lines starting with a date in MM/DD format, followed by some text, and ending with an amount.
# Pattern explanation:
# ^(\d{2}/\d{2})  -> Capture the date at start of line: e.g. "10/20"
# \s+(.*?)         -> Some spaces, then capture everything (non-greedy) until the next pattern
# (\-?\$?\d[\d,]*\.\d{2})$ -> Capture the amount at the end of the line, which could be negative or positive, 
#                             possibly with a comma, and possibly a '$' sign. If the '$' is not always present, 
#                             we can relax that requirement.
#
# If the lines don't have a '$' symbol explicitly, just remove \$ from the pattern.
#
# Adjusting for the provided data (which doesn't seem to consistently have a $ sign, but shows negative amounts):
# Let's just match a negative or positive number at the end with optional commas.
# pattern = re.compile(r'^(\d{2}/\d{2})\s+(.*\s)(-?\d[\d,]*\.\d{2})$', re.MULTILINE)

# with open()
# matches = pattern.findall(text)

# # We'll clean up the description: remove trailing spaces.
# transactions = []
# for match in matches:
#     date, description, amount = match
#     description = description.strip()
    
#     # Remove commas from amount if you want a pure numeric format, or just leave them.
#     # Convert amount like "-4,806.90" to -4806.90 (if needed).
#     amount = amount.replace(',', '')
    
#     transactions.append((date, description, amount))

# # Write out to CSV
# with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Date', 'Description', 'Amount'])
#     writer.writerows(transactions)

# print("CSV conversion completed. Check output.csv.")


# import csv
# import re

def convert_markdown_to_csv(input_file: str, output_file: str) -> None:
    # Read the entire Markdown file into a string
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Regex pattern explanation:
    # ^(\d{2}/\d{2})      - Capture a date in MM/DD format at the start of a line
    # \s+                 - One or more spaces
    # (.*?)               - Non-greedy capture of the description
    # \s+                 - One or more spaces
    # (-?\d[\d,]*\.\d{2}) - Capture the amount at the end of the line (negative or positive, 
    #                      possibly with commas), with two decimals
    # $                   - End of line
    pattern = re.compile(r'^(\d{2}/\d{2})\s+(.*?)\s+(-?\d[\d,]*\.\d{2})$', re.MULTILINE)

    matches = pattern.findall(text)

    transactions = []
    for match in matches:
        date, description, amount = match
        description = description.strip()
        # Remove any commas from the amount for a cleaner numeric value
        amount = amount.replace(',', '')
        transactions.append((date, description, amount))

    # Write the extracted data to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Description', 'Amount'])
        writer.writerows(transactions)

    print(f"CSV conversion completed. Check {output_file}.")


# Example usage:
convert_markdown_to_csv('output.md', 'output.csv')
