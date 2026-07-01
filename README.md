# Financial Data Extraction Pipeline (Day 68)

## Overview
This module automates the extraction of structured financial tables from web sources using Python. It bypasses manual data entry by fetching HTML documents, isolating specific data tables, and converting them into clean, analysis-ready Pandas DataFrames, ultimately exporting to Excel.

## Technologies Used
*   **Python 3.x**
*   **Requests:** For handling HTTP GET requests and network communication.
*   **BeautifulSoup (bs4):** For parsing raw HTML and traversing the DOM tree.
*   **Pandas:** For automated HTML-to-DataFrame conversion (`read_html`) and data cleaning.

## Pipeline Architecture
1.  **Fetch:** Initiates a secure HTTP request with standardized User-Agent headers.
2.  **Parse:** Converts the HTML response into a navigable BeautifulSoup object.
3.  **Target:** Locates the specific `<table>` element via DOM identifiers (ID/Class).
4.  **Process:** Ingests the HTML table into Pandas, filters necessary columns (e.g., Symbol, Sector), and standardizes naming conventions.
5.  **Output:** Generates a formatted `.xlsx` file ready for downstream financial modeling.

## Usage
Ensure dependencies are installed:
```bash
pip install requests beautifulsoup4 pandas lxml openpyxl
