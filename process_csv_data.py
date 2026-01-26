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

def should_include_page(row):
    """
    Filter pages based on team requirements:
    - Viva: Only pages with Product Area = "Viva Connections"
    - SharePoint: Only pages related to Home, Homesite, News, or Start
    """
    product = row.get('Product', '').strip()
    product_area = row.get('Product Area', '').strip()
    title = row.get('TopicTitle', '').strip().lower()

    # For Viva product: only include Viva Connections
    if product == 'Viva':
        return product_area == 'Viva Connections'

    # For SharePoint product: only include Home/Homesite/News/Start pages
    if product == 'SharePoint':
        # Check for SharePoint News pages
        if 'news' in title:
            return True

        # Check for SharePoint Start page (excluding "get started" pages)
        if 'start' in title and 'started' not in title:
            return True

        # Check for SharePoint Home/Homesite pages
        if 'home' in title or 'homesite' in title:
            return True

        return False

    # Exclude all other products
    return False

def determine_category(row):
    """
    Categorize pages into 3 main segments:
    - Viva Connections
    - SharePoint Start
    - SharePoint News
    """
    product = row.get('Product', '').strip()
    title = row.get('TopicTitle', '').strip().lower()

    if product == 'Viva':
        return 'Viva Connections'
    elif 'news' in title:
        return 'SharePoint News'
    elif 'start' in title and 'started' not in title:
        return 'SharePoint Start'
    elif 'home' in title or 'homesite' in title:
        return 'SharePoint Home'
    else:
        return 'Other'

# Read CSV file
csv_file = r'C:\Users\cmedipally\OneDrive - Microsoft\Desktop\Documentation\VSPSites.csv'
output_file = r'C:\Users\cmedipally\vivasphelixreport\all_pages_data.js'

pages = []
rank = 1

print("Reading CSV file...")
total_rows = 0
filtered_out = 0
zero_impressions = 0

with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            total_rows += 1

            # Apply product/area filtering first
            if not should_include_page(row):
                filtered_out += 1
                continue

            impressions = parse_impressions(row.get('Impressions', '0'))

            # Skip pages with 0 impressions
            if impressions == 0:
                zero_impressions += 1
                continue

            page = {
                'rank': rank,
                'title': row.get('TopicTitle', '').strip(),
                'url': row.get('url', '').strip(),
                'impressions': impressions,
                'age': parse_days_since_review(row.get('DaysSinceReview', '')),
                'csat': parse_csat(row.get('Content SAT', '')),
                'product': row.get('Product', '').strip(),
                'theme': determine_theme(row),
                'category': determine_category(row)
            }

            pages.append(page)
            rank += 1

        except Exception as e:
            print(f"Error processing row {rank}: {e}")
            continue

print(f"\nFiltering Summary:")
print(f"  Total rows in CSV: {total_rows}")
print(f"  Filtered out (not Viva Connections or SP Home/News/Start): {filtered_out}")
print(f"  Excluded (zero impressions): {zero_impressions}")
print(f"  Included in dataset: {len(pages)}")

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
