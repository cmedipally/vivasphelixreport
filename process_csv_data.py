import csv
import json
import re
from datetime import datetime

def parse_impressions(value):
    """Parse impression value from string like '12,976,493' to integer"""
    if not value or value.strip() == '':
        return 0
    return int(value.replace(',', '').replace('"', ''))

def parse_days_since_review(value):
    """Parse DaysSinceReview value"""
    if not value or value.strip() == '' or value == 'N/A':
        return None
    try:
        return int(value)
    except:
        return None

def parse_csat(value):
    """Parse Content SAT value"""
    if not value or value.strip() == '':
        return None
    try:
        return int(value)
    except:
        return None

def determine_theme(row):
    """Determine theme from Theme column or Content Type"""
    theme = row.get('Theme', '').strip()
    if theme:
        return theme

    content_type = row.get('ContentType', '').strip()
    if content_type:
        return content_type

    product_area = row.get('Product Area', '').strip()
    if product_area:
        return product_area

    return 'Other'

# Read CSV file
csv_file = r'C:\Users\cmedipally\OneDrive - Microsoft\Desktop\Documentation\VSPSites.csv'
output_file = r'C:\Users\cmedipally\vivasphelixreport\all_pages_data.js'

pages = []
rank = 1

print("Reading CSV file...")
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            impressions = parse_impressions(row.get('Impressions', '0'))

            # Skip pages with 0 impressions
            if impressions == 0:
                continue

            page = {
                'rank': rank,
                'title': row.get('TopicTitle', '').strip(),
                'url': row.get('url', '').strip(),
                'impressions': impressions,
                'age': parse_days_since_review(row.get('DaysSinceReview', '')),
                'csat': parse_csat(row.get('Content SAT', '')),
                'product': row.get('Product', '').strip(),
                'theme': determine_theme(row)
            }

            pages.append(page)
            rank += 1

        except Exception as e:
            print(f"Error processing row {rank}: {e}")
            continue

# Sort by impressions descending
pages.sort(key=lambda x: x['impressions'], reverse=True)

# Reassign ranks after sorting
for i, page in enumerate(pages, 1):
    page['rank'] = i

print(f"Total pages processed: {len(pages)}")
print(f"Top 10 pages by traffic:")
for i, page in enumerate(pages[:10], 1):
    print(f"  {i}. {page['title']} - {page['impressions']:,} views")

# Generate JavaScript array
print("\nGenerating JavaScript file...")
js_output = "// Generated from VSPSites.csv - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
js_output += "// Total pages: " + str(len(pages)) + "\n\n"
js_output += "const allPagesData = " + json.dumps(pages, indent=4) + ";\n"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_output)

print(f"JavaScript file created: {output_file}")
print(f"Data contains {len(pages)} pages")
