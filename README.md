# DSA4153_Healthcare_FinalProject

Week 8 proposal and initial data inspection for a study of public healthcare resource distribution across Philippine regions during 2020–2023.

## Data Preparation

The CSVs contain formatting-only cleanup of the original PSA tables. All source years, separate professions, national totals, geographic detail, and ownership categories are retained. No aggregation, ratios, year filtering, or imputation have been performed.

Multirow headers were flattened, year labels were added to practitioner rows, and blank spacing and repeated page headings were removed. Population note columns were removed; source notes and annotations are documented in `data/source_notes/Source_notes.csv`. Practitioner footnote flags remain in regional column headers.

Missing population markers are retained as supplied and may not be detected by the initial missing-cell check. Selection of regional totals, government hospital and bed categories, and 2020–2023 records is planned for the cleaning stage.

## Source

Philippine Statistics Authority, Philippine Statistical Yearbook:
https://psa.gov.ph/philippine-statistical-yearbook

Health tables use Department of Health data.

## Run the Initial Inspection

Install pandas:

python -m pip install pandas

From the repository root, run:

python src/inspect_data.py

The script displays sample records, shapes, column names, data types, missing-cell counts, and duplicate-row counts for all five datasets.
