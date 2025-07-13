
<!-- Header Image -->
<p align="center">
  <img src=".\img\touchpoint_logo.png" alt="Project Header" style="width:20%; max-width:400px;">
</p>

# 💡 Hospital Cafeteria Retail 

This case study provides a holistic recommendation of TouchPoint Health Services food cafeteria. 

I provide analysis for the following business aspects:

- Data Prep
- NLP Data Model
- Analysis
  - Customer & Site Profile
  - Food Assortment
  - Healthy Incentive Pricing
  - Future Recommendations 

## 📖 Table of Contents

- [Data Prep](#data-prep)
- [NLP Data Model](#nlp-data-model)
- [Analysis](#analysis)
- [Tableau](#tableau)

  
# Data Prep

### Google BigQuery (GBQ)
Utilized GBQ as data warehouse & primary data prep tool

**Keywords** used: SELECT/FROM/WHERE/GROUPBY/JOIN/HAVING
<br>
**Functions** used: TRIM/UPPER/SUM/DISTINCT/EXTRACT/OVER/DENSE_RANK

#### Wrangling
-  Input from CSV
-  Normalize column names
-  Normalize column elements
  - TRIM/UPPER

#### Analytic Prep
-  Use WINDOW FUNCTIONS to calculate running totals & rankings
-  Identified low velocity items identifying items that have less than 10 different sales day within past 6 months
-  Must have at least 2 separate months of data (remove new items from scrub)
-  

# NLP Data Model


# Analysis


# Tableau
