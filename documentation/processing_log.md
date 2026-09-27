# Processing and Quality Assurance Log

## 1. Data Acquisition
*   **Source:** ILOSTAT Data Explorer (https://ilostat.ilo.org/data/)
*   **Retrieval Date:** September 26, 2026
*   **Original Formats:** `.xlsx` (Excel)
*   **Files Downloaded:** 
    *   `Labour_force_Participation.xlsx`
    *   `Unemployment Rate.xlsx`
    *   `Employment_to_Population.xlsx`
    *   `Informal Employment Rate.xlsx`

## 2. Scope & Filtering Decisions
*   **Geographic Filtering:** The dataset was filtered against a hardcoded list of 47 sovereign Sub-Saharan African countries based on the World Bank classification. Regional aggregates (e.g., "Sub-Saharan Africa") were explicitly removed to ensure only country-level data remained.
*   **Temporal Filtering (Reference Year):** Initial extraction attempts for the year 2023 yielded data for only 17 Sub-Saharan African countries. To meet the assignment's strict requirement of at least 20 countries for a cross-sectional dataset, the reference year was shifted to **2022**, which successfully provided coverage for 21 countries.

## 3. Data Cleaning and Reshaping (via Python)
*   Filtered all four raw datasets to `Year == 2022`.
*   Filtered all four raw datasets to include only the 47 Sub-Saharan African nations.
*   Retained necessary disaggregation columns (`sex.label` and `classif1.label`), standardizing names to `Sex` and `Age_Group`.
*   Handled structural differences: The Informal Employment dataset lacked an age classification column, so the Python script was designed to dynamically include `Age_Group` only if present.
*   Merged the four filtered datasets into a single longitudinal dataframe using `pd.concat()`.
*   **Missing Data Treatment:** Empty values in the `obs_status.label` (Observation Status) column were explicitly filled with the string `"Observed"` to clearly distinguish them from ILOSTAT's `"Estimated"` or `"Modelled"` flags.

## 4. Software Used
*   Python 3
