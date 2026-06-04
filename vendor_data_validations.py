import pandas as pd

# Read raw data
df = pd.read_csv("vendor_master_raw.csv")
print(f"Records loaded: {len(df)}")

# Valid reference values
valid_categories = ["IT", "Logistics", "Finance", "HR", "Operations", "Legal", "Marketing"]
valid_statuses   = ["Active", "Inactive", "Under Review"]
country_region   = {
    "India": "APAC", "Singapore": "APAC", "Australia": "APAC",
    "USA": "AMER", "Canada": "AMER",
    "UK": "EMEA", "Germany": "EMEA"
}

# Check if date is valid DD/MM/YYYY format
def is_invalid_date(val):
    val = str(val).strip()
    if val in ["", "nan"]: return False
    try:
        pd.to_datetime(val, dayfirst=True)
        return False
    except:
        return True

# ---------- VALIDATION ----------
duplicates      = df.duplicated(subset=["Vendor_ID"]).sum()
missing_name    = (df["Vendor_Name"].fillna("") == "").sum()
spaces_name     = df["Vendor_Name"].apply(lambda x: str(x) != str(x).strip() and str(x).strip() != "").sum()
invalid_cat     = (~df["Category"].isin(valid_categories)).sum()
invalid_status  = (~df["Status"].isin(valid_statuses)).sum()
missing_email   = (df["Contact_Email"].fillna("") == "").sum()
invalid_email   = df["Contact_Email"].apply(lambda x: "@" not in str(x) and str(x).strip() != "").sum()
missing_account = (df["Account_Code"].fillna("") == "").sum()
missing_region  = (df["Region"].fillna("") == "").sum()
region_mismatch = sum(df.apply(lambda r: str(r["Region"]) != country_region.get(r["Country"], ""), axis=1) & (df["Region"].fillna("") != ""))
missing_updated = (df["Last_Updated"].fillna("") == "").sum()
invalid_onboard = df["Onboarding_Date"].apply(is_invalid_date).sum()
invalid_updated = df["Last_Updated"].apply(is_invalid_date).sum()
missing_verified = (df["Verified_By"].fillna("") == "").sum()

print("\n--- Validation Results ---")
print(f"Duplicate Vendor IDs        : {duplicates}")
print(f"Missing Vendor Name         : {missing_name}")
print(f"Spaces in Vendor Name       : {spaces_name}")
print(f"Invalid Category            : {invalid_cat}")
print(f"Invalid Status              : {invalid_status}")
print(f"Missing Contact Email       : {missing_email}")
print(f"Invalid Email Format        : {invalid_email}")
print(f"Missing Account Code        : {missing_account}")
print(f"Missing Region              : {missing_region}")
print(f"Region Mismatch             : {region_mismatch}")
print(f"Missing Last Updated        : {missing_updated}")
print(f"Invalid Onboarding Date     : {invalid_onboard}")
print(f"Invalid Last Updated Date   : {invalid_updated}")
print(f"Missing Verified By         : {missing_verified}")

# ---------- CLEANING ----------
# Remove duplicates
df = df.drop_duplicates(subset=["Vendor_ID"], keep="first")

# Trim spaces in Vendor Name
df["Vendor_Name"] = df["Vendor_Name"].str.strip()

# Fix Category typos
cat_fixes = {
    "it": "IT", "FINANCE": "Finance", "Fianance": "Finance",
    "logistic": "Logistics", "HR Dept": "HR",
    "Opreations": "Operations"
}
df["Category"] = df["Category"].replace(cat_fixes)

# Fix Status typos
status_fixes = {
    "active": "Active", "INACTIVE": "Inactive",
    "Actve": "Active", "Inactve": "Inactive",
    "under review": "Under Review"
}
df["Status"] = df["Status"].replace(status_fixes)

# Fix Region from Country
df["Region"] = df["Country"].map(country_region)

# Fix date formats
def fix_date(val):
    try:
        return pd.to_datetime(val, dayfirst=True).strftime("%d/%m/%Y")
    except:
        return val

df["Onboarding_Date"] = df["Onboarding_Date"].apply(fix_date)
df["Last_Updated"] = df["Last_Updated"].apply(fix_date)

# Save cleaned file
df.to_csv("vendor_master_cleaned.csv", index=False)

print(f"\n--- Cleaning Complete ---")
print(f"Records after cleaning      : {len(df)}")
print(f"Saved as                    : vendor_master_cleaned.csv")
