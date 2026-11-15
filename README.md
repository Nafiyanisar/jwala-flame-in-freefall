# Flame in Freefall: Combustion Investigation Explorer

**Team Jwala** - NASA Space Apps Challenge 2026 (Kochi, India)
**Challenge:** Flame in Freefall: SI-Powered Fire Safety Insights from Microgravity Combustion Data

## What it is
A small interactive explorer (Streamlit) for NASA microgravity combustion investigations listed in
NASA's Physical Sciences Informatics (PSI) repository. For each investigation you can see its type,
objective, approach, flight platform, DOI and license, plus the sample-table rows that were copied
from the PSI page. It helps a researcher quickly see what was tested and where to look for data.

## What it is NOT
- It does not analyse the experiments' measurement files. It catalogues what each investigation
  set out to do and what it tested.
- It is not a validated or certified fire-safety tool.
- No machine-learning or language model runs inside the app.

## Run it
```
pip install -r requirements.txt
streamlit run app.py
```

## Data
Investigation text was copied by hand from the PSI pages (psi.nasa.gov) and shortened where marked
"condensed". Sample-table values are shown exactly as displayed on PSI, including entries that look
like typos (for example "037 mm" in PSI-99).

| ID | Investigation | DOI (as shown on PSI) |
|----|---------------|-----------------------|
| PSI-21 | ACME CLD Flame | 10.60555/23e1-9950 |
| PSI-98 | SAFFIRE-I | 10.60555/0t15-1z43 |
| PSI-99 | SAFFIRE-II | 10.60555/2chp-m469 |
| PSI-100 | SAFFIRE-III | 10.60555/040q-4h36 |
| PSI-117 | Cool flame CFD study (ground investigation) | - |
| PSI-159 | ACME CFI-G (cool flames with gases) | - |

Source: NASA Physical Sciences Informatics, https://psi.nasa.gov. Pages show license CC0-1.0.

## SI (AI) disclosure
- **Code (`app.py`) and this README were written with help from Claude (Anthropic)** and reviewed
  by the team member.
- The project idea, the choice of challenge and data, and all copying of PSI content were done by
  the team member. Claude helped turn screenshots the team member supplied into CSV rows.
- No images, audio or video were generated with SI.

## Limitations and future work
- Only six investigations and a few sample rows are included.
- Future: load the real measurement files, add comparisons across test conditions, and add a clearly
  labelled language-model summary of related NASA papers.
