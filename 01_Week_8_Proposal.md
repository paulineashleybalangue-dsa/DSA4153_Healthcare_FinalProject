**UNEQUAL CARE: A REGIONAL ANALYSIS OF PUBLIC HEALTHCARE INFRASTRUCTURE AND GOVERNMENT MEDICAL PERSONNEL DISTRIBUTION IN THE PHILIPPINES FROM 2020 TO 2023**

**Week 8 Check-in 1—Proposal and Programming Plan**  
**Study Group:** Group 6 | Section: 2DSA2  
**Members:** Alano, Balangue, Cubol, Espiritu, Fernandez, & Tilo

**Repository URL:** [https\://github.com/paulineashleybalangue-dsa/DSA4153\_Healthcare\_FinalProject.git](https://github.com/paulineashleybalangue-dsa/DSA4153_Healthcare_FinalProject.git)   
**Current Commit Identifier:**  b12061a4fb3ab112ad2454085681fb8fc2638d6b

**PROBLEM:**  
The COVID-19 pandemic highlighted the importance of adequate public healthcare resources in the Philippines during 2020–2023. Differences in the distribution of government medical practitioners, the number of government hospitals and their authorized beds, and barangay health stations may contribute to unequal healthcare availability across regions. This study will examine these regional differences and identify areas with relatively low resource availability, considering population size where suitable data are available.

**TARGET AUDIENCE:**  
Philippine healthcare policymakers, including DOH, and public health NGOs concerned with equitable regional resource distribution.

**QUESTIONS:**

1. How does the availability of government medical practitioners per capita vary across different Philippine regions from 2020 to 2023?  
2. Which regions have relatively low availability across government medical practitioners, authorized beds in government hospitals, and government hospitals?  
3. How do health infrastructure capacities differ between highly urbanized centers (such as the National Capital Region) and rural or remote provinces?

The proposed datasets are Tables 1.1, 9.14, 9.17, 9.18, and 9.19 of the Philippine Statistical Yearbook published by the Philippine Statistics Authority. The health tables contain data from the Department of Health. Original tables and accompanying source notes are available through the PSA Philippine Statistical Yearbook ([https\://psa.gov.ph/philippine-statistical-yearbook](https://psa.gov.ph/philippine-statistical-yearbook)).

**Table 1\. Proposed Datasets, Sources, Coverage, and Integration Keys**

| Dataset or table  | Provider / original data source | Source coverage | Relevant fields | Likely integration keys |
| ----- | ----- | ----- | ----- | ----- |
| **Table 1.1 — Population, Land Area, and Density by Region and Province** | PSA; Census of Population and Housing/population census data | Census years 2000, 2007, 2010, 2015, 2020, and 2024; includes national, regional, provincial, and city records | Region name, population by census year, land area, population density | Standardized **region \+ year**, after selecting regional totals and reshaping year columns |
| **Table 9.14 — Number of Government Medical Practitioners by Region** | DOH, Field Health Services Information System; published by PSA | 2013–2023; regional counts of doctors, dentists, nurses, and midwives | Year, profession, regional counts, Philippine total | **Region \+ year** for cross-table integration; **profession** additionally identifies practitioner records |
| **Table 9.17 — Authorized Hospital Bed Capacity by Type and Region** | DOH, Health Facilities and Services Regulatory Bureau; published by PSA | 2020–2024; government, private, and total authorized beds by region | Region, year, ownership category, authorized bed count | **Region \+ year \+ ownership** when matching with hospital counts |
| **Table 9.18 — Number of Regulated Hospitals by Type and Region** | DOH, Health Facilities and Services Regulatory Bureau; published by PSA | 2020–2024; government, private, and total hospitals by region | Region, year, ownership category, hospital count | **Region \+ year \+ ownership** when matching with bed capacity |
| **Table 9.19 — Number of Barangay Health Stations by Region** | DOH, Field Health Services Information System; published by PSA | 2006–2023; regional counts and Philippine totals | Year, region, barangay health station count | **Region \+ year** |

### **Table 1** summarizes the five proposed datasets, their providers, coverage, relevant variables, and planned integration keys. Only government hospital and bed-capacity figures will be used in the analysis.

### **Usage conditions.** The PSA website states that its content is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0), unless otherwise stated.	

### **Integration plan and coverage considerations.** Regional names will be standardized, and year columns will be reshaped as needed for integration. National totals will be kept separate from regional observations; population records will be restricted to regional totals. Ownership categories and professions will remain identifiable to prevent duplicated counts during joins.

### **Table 2\. Planned Program Components and Responsibilities**

| Component | Primary Scope | Primary Programmer | Primary Reviewer |
| ----- | ----- | ----- | ----- |
| **Inspections (inspections.py)** | Profile raw sample files, inspect column types, generate null/duplicate audits. | **Balangue**  | **Alano** |
| **Acquisition (acquisition.py)** | Import raw CSV tables from DOH and PSA sources, enforce required fields, and log raw data snapshots. | **Balangue** | **Alano** |
| **Cleaning (cleaning.py)** | Select regional totals and relevant fields for the 2020–2023 study period, remove unnecessary records and columns, and standardize region names and labels. Identify and flag missing-value markers without automatically replacing them, while preserving footnotes and source annotations separately for reference. | **Alano** | **Cubol** |
| **Validation (validation.py)** | Check required columns, non-negative counts, numeric types, verify file schema integrity, valid years, and complete integration keys; flag coverage differences. | **Cubol** | **Balangue** |
| **Integration (integration.py)** | Reshape tables as needed and merge using region and year, adding ownership where applicable; check duplicate keys and unmatched records. Handle the population baseline explicitly. | **Tilo** | **Espiritu** |
| **Analysis (analysis.py)** | Summarize regional resource counts, calculate population-adjusted measures with a documented denominator, and identify regions with relatively low resource availability using a defined criterion. | **Espiritu** | **Tilo** |
| **Visualization (viz.py)** | Produce regional comparison charts, resource heatmaps, and trends for 2020–2023. | **Cubol** | **Fernandez** |
| **Testing (test\_workflow.py)** | Test missing markers, invalid counts, duplicate keys, unmatched regions, and zero-denominator handling. | **Fernandez** | **Cubol** |
| **Execution & Performance (main.py)** | Run the workflow in order using documented input paths and save reproducible summaries and charts. | **Fernandez** | **Balangue**  |

**Table 2** outlines the planned programming tasks and identifies the primary programmer and reviewer responsible for each component.  
**Table 3\. Likely Risks and Feasible Fallbacks**

| Area | Risk | Feasible Fallback |
| :---- | :---- | :---- |
| **Access** | Website Crashes or Internet Loss | Download a raw copy of the data as CSV files and save them directly into the project folder. If the live website goes down, the code will automatically switch to reading these saved offline files.  |
| **Mismatched Keys** | Misalignment within the healthcare tables.  | We will filter the dataset to keep regional totals only (preventing double-counting) and use a custom mapping dictionary to match geographic coverage across tables before merging. |
| **Missing Information** | Missing annual population data | If no other sources are found to fill in the missing data, we will use the official 2020 Census population as a fixed, steady baseline for all calculations between 2020 and 2023, rather than attempting to guess the missing years. |
| **Privacy** | Data misrepresentation and ethical handling | The team will analyze and display all data strictly at the broad regional level, avoiding any focus on individual clinics, hospitals, or medical practitioners.  |
| **Scope** | Facility count ≠ accessibility | Present hospital/facility counts as availability indicators, not direct measures of accessibility or healthcare quality.  |
| **Schedule** | Possible delays due to exams or other school work.  | The team will use clearly labeled synthetic test data so everyone can code at the same time. This way, no one has to sit around waiting for another person to finish their step before they can start working on their own part. We can also meet up or hold meetings when we have onsite classes to make sure everyone is on track. |

**Table 3** identifies potential challenges involving data access, integration, missing information, privacy, scope, and schedule, together with practical fallback measures.  
**Table 4\. Week-by-Week Work Plan**

| Week | Planned Activities | Expected Output |
| :---: | ----- | ----- |
| **8** | Present the proposal and initial inspection; record instructor feedback, action owners, and follow-up dates. | Proposal, inspection code, and feedback log |
| **9** | Address required revisions and confirm questions, public-only scope, population denominator, and comparison criteria. | Revised proposal and agreed analysis plan |
| **10** | Preserve source files and notes; select regional totals, government categories, and 2020–2023 records. | Selected datasets and source documentation |
| **11** | Standardize region labels, convert numeric text, flag missing markers, and check reporting coverage. | Cleaned datasets and quality report |
| **12** | Reshape and integrate tables; verify duplicate keys, unmatched records, and population-baseline handling. | Integrated regional dataset |
| **13** | Calculate regional summaries and documented population-adjusted measures; identify relatively low resource availability. | Preliminary analytical results |
| **14** | Create comparison charts, resource heatmaps, and trends; review labels and interpretations. | Draft visualizations |
| **15** | Test calculations, joins, missing-value handling, and reproducibility; resolve reviewer findings. | Tested workflow and updated results |
| **16** | Complete the report, README, limitations, and contribution records; rehearse the presentation. | Draft final submission and presentation |
| **17** | Run final checks, confirm repository access and submission commit, and submit according to Canvas instructions. | Final deliverables and repository snapshot |

**Table 4** outlines the planned activities and expected outputs through Week 17\. Implementation will follow the programming techniques covered in class.

**INITIAL DATA INSPECTION**  
	Initial inspection code and sample data are included in the accompanying ZIP. All five datasets loaded successfully, and the code displayed sample records, shapes, columns, data types, missing-cell counts, and duplicate-row counts. No duplicate rows were detected. Population fields contain text missing-value markers requiring cleaning; regional selection and standardization to 2020–2023 remain planned. Population and practitioner counts will support workforce comparisons, while government hospital and authorized bed counts will support infrastructure comparisons.

**QUESTIONS FOR INSTRUCTOR FEEDBACK**

1. Is using the 2020 population as a fixed baseline acceptable for resource comparisons during 2020–2023, or should population-adjusted analysis be limited to 2020?  
2. What criterion should we use to identify regions with relatively low resource availability?  
3. Are comparisons between NCR and other Philippine regions appropriate for our regional datasets?  
4. Should barangay health station counts be included in the main analysis or used as supporting context?

