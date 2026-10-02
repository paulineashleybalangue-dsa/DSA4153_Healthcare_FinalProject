# DSA4153_Healthcare_FinalProject

Formatting-only cleanup of original PSA tables. All original years, separate professions, national totals, and geographic detail retained. No sums, ratios, year filtering, or imputation performed. Multirow headers flattened; year added to each practitioner row from the original year heading. Blank spacing and repeated page headings removed. Footnote flags retained in headers or population note columns; see `Source_notes.csv` and original workbook. Missing population markers retained as supplied. Blank footnote cells are not missing population observations. CSV contains no styles, merged cells, or multiple tabs.

Run: `python src/inspect_data.py`