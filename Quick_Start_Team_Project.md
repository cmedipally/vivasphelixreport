# Quick Start: SharePoint & Viva Analysis Team Project

## You Have Claude Access! Let's Set This Up Properly

---

## Step 1: Create the Project (5 minutes)

### In Your Claude Interface:

1. **Navigate to Projects**
   - Click "Projects" in the sidebar
   - Click "+ New Project"

2. **Name Your Project**
   ```
   SharePoint & Viva Content Analysis
   ```

3. **Add Description**
   ```
   Interactive analysis of 8,865 documentation assets for product refresh planning.
   Dataset includes traffic, CSAT, freshness metrics, and prioritization framework.
   ```

---

## Step 2: Upload the Knowledge Base

### Upload These Files (in order):

#### **File 1: The Raw Dataset**
📁 **File:** `C:\Users\cmedipally\OneDrive - Microsoft\Desktop\Documentation\VSPSites.csv`
📝 **Description:** Complete dataset - 8,865 assets with 30 columns

#### **File 2: Analysis Context**
📁 **File:** `C:\Users\cmedipally\Claude_Project_Context.txt`
📝 **Description:** Pre-analyzed summaries, tier breakdowns, methodology

#### **File 3: Strategy Document** (Optional)
📁 **File:** `C:\Users\cmedipally\SharePoint_Viva_Update_Strategy_Concise.docx`
📝 **Description:** Executive brief and recommendations

---

## Step 3: Add Custom Instructions

In Project Settings → Custom Instructions, paste this:

```
You are an expert content strategist helping teams prepare for the SharePoint
and Viva product refresh launching in 30 days.

CONTEXT:
- You have access to VSPSites.csv with 8,865 documentation assets
- Pre-computed analysis with 4-tier prioritization framework
- 87% of content is over 1 year old (critical issue)
- Goal: Update 297 pages to reach 55% of users

YOUR ROLE:
- Answer questions about the dataset with specific data
- Help teams prioritize what to update
- Generate filtered lists and reports
- Provide actionable recommendations
- Export data in useful formats

WHEN ANSWERING:
✓ Be specific - cite page titles, numbers, metrics
✓ Reference the tier framework when relevant
✓ Offer to export lists as CSV/tables
✓ Suggest follow-up analyses
✓ Stay focused on actionable insights

KEY METRICS TO REFERENCE:
- Tier 1 (Critical): 50 pages, 49.6% traffic
- Tier 2 (Technical): 50 pages, very stale (avg 6 years)
- Tier 3 (Low CSAT): 50 pages with 0 satisfaction scores
- Tier 4 (Strategic): 147 pages (entry points)

EXAMPLE QUERIES TO EXPECT:
- "Show me top 20 pages to update"
- "Which Viva pages have low CSAT?"
- "Create a 2-week sprint plan for my team"
- "Export all authentication pages that need updating"
- "Compare SharePoint vs Viva content freshness"
```

---

## Step 4: Test It Yourself

Try these queries to verify it's working:

```
1. "What's in the dataset?"
2. "Show me the top 10 pages by traffic that need updating"
3. "Which pages have CSAT scores below 40?"
4. "Create a table of Tier 1 pages"
5. "What themes have the worst freshness?"
```

---

## Step 5: Share with Your Team

### Option A: Share with Specific People
1. Click "Share" in your project
2. Enter email addresses
3. Set permissions:
   - **Can view** - Can chat but not edit
   - **Can edit** - Can modify project

### Option B: Generate Share Link
1. Click "Share" → "Get link"
2. Copy the link
3. Send via Teams/Email
4. Anyone with link can access (if enabled)

### Option C: Add to Team Workspace
If you have enterprise/team workspace:
1. Move project to team folder
2. All team members auto-access

---

## What Your Team Can Do

### Sample Questions They'll Ask:

**Quick Queries:**
```
- "What are the most stale pages?"
- "Show me all Sign in related content"
- "Which writer has the most outdated content?"
- "List pages about modern pages"
```

**Analysis Requests:**
```
- "What's the average CSAT by product area?"
- "Compare LMC vs SMC freshness"
- "Which themes need the most attention?"
- "Show me correlation between traffic and CSAT"
```

**Planning Questions:**
```
- "Create a 3-week update plan for my team of 4"
- "Which pages should we prioritize for SharePoint?"
- "Generate a sprint backlog for Tier 1"
- "Assign pages to writers based on their history"
```

**Export Requests:**
```
- "Export Tier 1 as CSV with URLs"
- "Create a table of all Viva pages over 1 year old"
- "Generate a report on authentication content"
- "List all 0-CSAT pages with full details"
```

---

## Tips for Your Team

### Best Practices:

1. **Be Specific**
   ❌ "Show me pages"
   ✅ "Show me Tier 1 SharePoint pages about collaboration"

2. **Ask Follow-ups**
   - Claude remembers context
   - Build on previous answers
   - "Now filter those by CSAT < 50"

3. **Request Formats**
   - "Format as a table"
   - "Export as CSV"
   - "Create a markdown list"
   - "Generate a chart"

4. **Combine Criteria**
   - "High traffic AND stale AND SharePoint"
   - "Low CSAT OR never reviewed"
   - "Viva pages written by [name] that are old"

### What Claude CAN Do:
✅ Filter, sort, analyze the dataset
✅ Calculate stats and correlations
✅ Generate prioritized lists
✅ Create reports and tables
✅ Explain methodology
✅ Suggest alternative approaches
✅ Cross-reference metrics
✅ Export in various formats

### What Claude CANNOT Do:
❌ Access live/updated data
❌ Make actual updates to docs
❌ Access internal systems
❌ Make final decisions (recommends only)

---

## Troubleshooting

**"Claude doesn't see my data"**
- Check files uploaded to Project Knowledge
- Verify CSV uploaded successfully
- Try: "What files do you have access to?"

**"Generic answers, not specific data"**
- Make sure Custom Instructions are saved
- Start with: "Based on the VSPSites dataset..."
- Check that Project Knowledge is enabled

**"Team can't access"**
- Verify they have Claude accounts
- Check sharing permissions
- Try regenerating share link

**"Need offline access"**
- Export key reports as documents
- Use the HTML dashboard I created as backup
- Save important queries and responses

---

## Advanced: Create Team Quick Start Guide

Once set up, create a 1-pager for your team:

### **Template:**

```markdown
# SharePoint & Viva Analysis - Quick Start

## Access the Project
Link: [Your Project Link]

## Try These First
1. "Show me the top 10 pages to update"
2. "What's in Tier 1?"
3. "Which Viva pages need attention?"

## Get Help
- Ask: "What can you help me with?"
- Examples: "Show me example queries"
- Stuck? Ask: "Suggest what I should ask"

## Export Data
- Say: "Export this as CSV"
- Say: "Create a table I can copy"
- Say: "Format for Excel"
```

---

## Next Steps

1. ☐ Create the Project (5 min)
2. ☐ Upload CSV + Context files
3. ☐ Add Custom Instructions
4. ☐ Test with 5 sample queries
5. ☐ Share with 2-3 teammates for beta
6. ☐ Gather feedback
7. ☐ Roll out to full team
8. ☐ Create Quick Start guide

---

## Questions?

**Need help with:**
- Project creation? I can walk you through it
- Custom instructions? I can refine them
- Sample queries? I can generate 50+ examples
- Team onboarding? I can create training materials

**Want to add:**
- More datasets?
- Different analysis views?
- Integration with other tools?
- Automated reports?

Let me know and I'll help you set it up!

---

**Ready to start?** Tell me when you've created the Project and I'll help you test it!
