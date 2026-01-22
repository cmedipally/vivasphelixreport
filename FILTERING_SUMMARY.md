# Data Filtering Summary

## Overview
Updated the dashboard to show only the pages requested by your team:
- **Viva Product**: Pages with Product Area = "Viva Connections"
- **SharePoint Product**: Pages related to Home, Homesite, News, and Start

## Results

### Before Filtering
- Total pages: 8,865 documentation assets
- All SharePoint and Viva products included

### After Filtering
- **Total pages: 174 priority pages**
- **Total traffic: 3.69M impressions**

### Breakdown by Category

#### Viva Connections
- 34 pages identified with Product Area = "Viva Connections"
- Top page: "Overview: Viva Connections" (70.7K views)

#### SharePoint News
- 49 pages with "news" in title
- Top page: "Create and share news on your SharePoint sites" (1.1M views)

#### SharePoint Start Page
- 72 pages with "start" in title (excluding "get started" pages)
- Top pages:
  - "Discover content with the SharePoint start page" (567K views)
  - "Viewing SharePoint start page with Microsoft Graph turned off" (552K views)

#### SharePoint Home/Homesite
- 20 pages with "home" or "homesite" in title
- Top page: "Use a different page for your SharePoint site home page" (57K views)

## Traffic Distribution

The filtered dataset has highly concentrated traffic:

| Phase | Pages | Traffic Coverage | Page Range |
|-------|-------|-----------------|------------|
| Phase 1 | 6 pages | 70% | 1-6 |
| Phase 2 | 19 pages | 89% | 7-25 |
| Phase 3 | 25 pages | 97% | 26-50 |
| Phase 4 | 89 pages | 99.9% | 51-139 |
| Phase 5 | 35 pages | 100% | 140-174 |

## Key Insights

1. **Top 6 pages cover 70% of traffic** - These are your absolute highest priority
2. **Top 50 pages cover 97% of traffic** - Recommended focus area
3. **Phases 4 & 5 have minimal traffic impact** - Only pursue if you have excess resources

## Recommendation

**Focus on Phases 1-3 (top 50 pages)** to reach 97% of your target audience with optimal resource investment.

## Files Updated

1. **process_csv_data.py** - Added `should_include_page()` function with filtering logic
2. **all_pages_data.js** - Regenerated with 174 filtered pages
3. **SharePoint_Viva_Interactive_Dashboard.html** - Updated phase definitions and coverage percentages
4. **index.html** - (No changes needed, already redirects correctly)

## How to View

Your dashboard is ready at:
- **Local**: Open `SharePoint_Viva_Interactive_Dashboard.html` in a browser
- **GitHub Pages** (if enabled): https://cmedipally.github.io/vivasphelixreport/

## Next Steps

If you need to adjust the filtering criteria:
1. Edit the `should_include_page()` function in [process_csv_data.py](process_csv_data.py:46)
2. Run: `python process_csv_data.py`
3. The dashboard will automatically load the updated data
