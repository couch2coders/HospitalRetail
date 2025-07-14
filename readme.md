
<!-- Header Image -->
<p align="center">
  <img src=".\img\touchpoint_logo.png" alt="Project Header" style="width:40%; max-width:400px;">
</p>

# 🏥 Hospital Cafeteria Retail 

This case study provides a holistic recommendation of TouchPoint Health Services food cafeteria. 

I provide analysis for the following business aspects:

- Data Prep
- NLP Data Model
- Analysis
  - Customer & Site Profile
  - Food Assortment
  - Healthy Incentive Pricing
  - Future Recommendations 

# 📖 Table of Contents

- [📊 Data Prep](#data-prep)
- [NLP Data Model](#nlp-data-model)
- [Analysis](#analysis)
- [Tableau](#tableau)

  
# 📊 Data Prep

### Google BigQuery (GBQ)
Utilized [GBQ]([https://example.com](https://console.cloud.google.com/bigquery?hl=en&inv=1&invt=Ab2rzQ&project=zeta-matrix-337222&ws=!1m0)) as data warehouse & primary data prep tool

**Keywords** used: *SELECT/FROM/WHERE/GROUPBY/JOIN/HAVING*
<br>
**Functions** used: *TRIM/UPPER/SUM/DISTINCT/EXTRACT/OVER/DENSE_RANK*

#### Wrangling
-  Input from CSV
-  Normalize column names
-  Normalize column elements (TRIM/UPPER)

#### Analytic Prep
-  Use WINDOW FUNCTIONS to calculate running totals & rankings
-  Identified low velocity items identifying items that have less than 10 different sales day within past 6 months
  -  Must have at least 2 separate months of data (remove new items from scrub)


# 🙊 NLP Data Model

Purpose of model is to identify item type category & healthy/unhealthy without having a pretrained dataset
<br>
<br>
I use Facebooks BART Zero-Shot-Classification due to its ease of use, accuracy, and ability to categorize without needing a trained dataset
<br>
<br>
**NOTE:** BART package has several package conflicts requiring a new envirnoment to be created for this project
<br>
<br>

<div align="center">

<table style="width:100%; table-layout:fixed; border-collapse:collapse;">
  <tr>
    <th style="width:33%; text-align:left; font-weight:600; border:none; background:none;">Packages Needed</th>
    <th style="width:33%; text-align:left; font-weight:600; border:none; background:none;">Food Labels</th>
    <th style="width:33%; text-align:left; font-weight:600; border:none; background:none;">Healthiness</th>
  </tr>
  <tr><td>Pandas</td><td>Beverage</td><td>Healthy</td></tr>
  <tr><td>Pipeline/Transformers</td><td>Meat</td><td>Unhealthy</td></tr>
  <tr><td>Re</td><td>Dairy</td><td></td></tr>
  <tr><td>tqdm</td><td>Side</td><td></td></tr>
  <tr><td>Counter/Collections</td><td>Fruit</td><td></td></tr>
  <tr><td>Torch</td><td>Dessert</td><td></td></tr>
  <tr><td>Numpy</td><td>Snack</td><td></td></tr>
  <tr><td></td><td>Healthy</td><td></td></tr>
</table>

</div>


Labels were selected based on types of food categories without being too specific (ex: only include meat versus chicken/pork/fish)
<br>
<br>
Several iterations were used with different labels to tune model. Different combinations included only using Beverage/Food since that was the primary focus of the analysis (bev/food have different margins)
<br>
<br>
Including 'Vegetables' did not improve the model as certain items that would fit 'Meat' and 'Vegetables' (Chicken Vegetable Stir Fry) would flip between the two, when we would want Meat to trump Vegetables as a category 
<br>
<br>
Only using Bev/Food did not yield desired results as many drinks would be listed as food instead of drinks (based on top 50 categories)
<br>
<br>
# 📈 Analysis

Full Analysis can be found [here](https://github.com/couch2coders/HospitalRetail/tree/main/Viz)

# 🖥️ Tableau

Tableau published dashboards can be viewed [here](https://public.tableau.com/app/profile/candice.filar/viz/Hospital_Retail_CaseStudy/RevenueSpreadbyItem)
