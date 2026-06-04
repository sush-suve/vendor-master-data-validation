# Vendor Master Data Validation & Quality Management

## Project Overview
End-to-end data validation and quality management project 
replicating real enterprise data operations work on a 
1000-record Vendor Master dataset.

## Tools Used
- Microsoft Excel
- Python (Pandas)
- Jupyter Notebook

## Project Structure
| File | Description |
|---|---|
| vendor_master_raw.csv | Raw dataset with injected data quality issues |
| vendor_master_validation.xlsx | Excel workbook with full validation and cleaning |
| vendor_data_validations.py | Python script for automated validation and cleaning |
| vendor_master_cleaned.csv | Final cleaned dataset output |

## What Was Done

### Data Validation
Performed 11 validation checks across 13 columns:
- Duplicate Vendor IDs
- Missing and invalid Vendor Names
- Invalid Category and Status values
- Missing and invalid Contact Emails
- Missing Account Codes
- Region mismatches with Country
- Date format validation
- Missing Verified By records

### Data Cleaning
- Removed 50 duplicate records
- Trimmed leading and trailing spaces
- Corrected category and status typos
- Fixed region mismatches using country mapping
- Standardised date formats to DD/MM/YYYY

### Results
| Metric | Value |
|---|---|
| Total Records Received | 1000 |
| Total Issues Found | 445 |
| Issues Resolved | 192 |
| Final Clean Records | 715 |
| Data Quality Score | 75.3% |

### Excel Workbook Contents
- **Raw_Data** — Original untouched dataset
- **Validated_Data** — Working sheet with all validation checks
- **Reference_Data** — Valid values reference table
- **Issue_Log** — Issue counts and resolution summary
- **Cleaned_Data** — Final clean records only
- **Summary_Dashboard** — Visual quality report with charts

### Python Automation
The Python script automates the entire validation 
process. Run it on any new vendor CSV file:

vendor_data_validations.py vendor_master_raw.csv

Output:
- Validation results printed to console
- Cleaned file saved as vendor_master_cleaned.csv
  
## Key Learnings
- Excel COUNTIF is case insensitive — Python catches 
  case errors that Excel misses
- Region mismatches can be fixed automatically using 
  a country to region reference mapping
- One flagged row can contain multiple issues — 
  235 flagged rows contained 253 total issue instances
- Validation must be done before cleaning — 
  issues must be logged before fixing
- Master data quality directly impacts accuracy 
  of all downstream reporting
