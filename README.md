# Curated Sub-Saharan Africa Labour Market Cross-Section (2022)

**Description:** A curated, cross-sectional dataset detailing labour market conditions across Sub-Saharan African countries for the reference year 2022. It integrates four key indicators: Labour Force Participation, Unemployment Rate, Employment-to-Population Ratio, and Informal Employment Rate.
**Purpose:** This dataset provides a harmonized foundation for analyzing and comparing cross-sectional workforce participation, employment vulnerability, and economic engagement across Sub-Saharan Africa, suitable for socio-economic modeling and policy research.

## Group 2 Members & Roles
* **Ernest Mawufermo Adansi** (Index: SE/DMD/25/0005 | GitHub: KOFI-ADANSI) – Project Manager & Discovery Metadata
* **Justice Jerry Johnson** (Index: SE/DMD/25/0006 | GitHub: ekyereshoot) – Data Engineer (Scripting & Pipeline)
* **Gozey Courage** (Index: SE/DMD/25/0007 | GitHub: Courage2292) – Variable Analyst (Codebook Generation)
* **Eric Ndorbokone Bawa** (Index: SE/DMD/25/0008 | GitHub: Ebawa14) – DDI Metadata Curator

## Data
*   **Original Data Provider:** International Labour Organization (ILOSTAT)
*   **Source Links:** [ILOSTAT Data Explorer](https://ilostat.ilo.org/data/)
*   **Date of Retrieval:** September 26, 2026
*   **Original Filenames:** `Labour_force_Participation.xlsx`, `Unemployment Rate.xlsx`, `Employment_to_Population.xlsx`, `Informal Employment Rate.xlsx`

## Coverage
*   **Geographic Scope:** Sub-Saharan Africa (World Bank classification).
*   **Country List:** Data covers 21 sovereign nations in Sub-Saharan Africa for the selected reference year. Regional aggregates were excluded.
*   **Temporal Scope:** Cross-sectional (Reference Year: 2022). 2022 was selected because 2023 lacked the required minimum 20-country coverage.
*   **Unit of Observation:** Country-Indicator-Demographic Group.
*   **Indicators Included:** Labour force participation rate, Unemployment rate, Employment-to-population ratio, Informal employment rate.

## Repository Structure
*   `data/raw/`: Contains the unmodified original `.xlsx` downloads from ILOSTAT.
*   `data/processed/`: Contains the final merged and filtered cross-sectional dataset (`curated_dataset.csv`).
*   `code/`: Contains the Python script (`data_preparation.py`) used to filter, merge, and clean the data.
*   `documentation/`: Contains the variable-level `codebook.csv` and `processing_log.md`.
*   `metadata/`: Contains the `dublin-core.jsonld` and `ddi-codebook.xml` files.

## Methodology Summary
Raw global indicator files were downloaded from ILOSTAT. Using Python and pandas, the files were strictly filtered to the year 2022 and isolated to Sub-Saharan African countries. Disaggregations for Sex and Age Group were preserved. Missing flags in the observation status column were explicitly labeled as "Observed" to differentiate them from modeled estimates.

## Licensing & Citation
*   **Licensing:** This repository's structure and code are provided under the MIT License. The source data is subject to ILO open access policies.
*   **Suggested Citation:** Adansi, E. M., Johnson, J. J., Gozey, C., & Bawa, E. N. (2026). Curated Sub-Saharan Africa Labour Market Cross-Section. Version 1.0. University of Cape Coast. University of Cape Coast. Repository: [https://github.com/EBawa14/msc-data-curation-labour-market-group-2]
