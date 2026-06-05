# Chamber of Deputies Data Processing & Analytics Application

A Python-based data processing tool and Django web application designed to ingest, clean, and analyze historical public datasets from the Chamber of Deputies of the Parliament of the Czech Republic.

## Key Features

*   **Local Data Parsing & Cleaning:** Custom Python scripts to parse raw `UNL` data files, handle character encoding (`windows-1250`), reformat date strings to ISO 8601, and resolve historical relational database schema discrepancies.
*   **Django Backend:** Built on the **Django framework** utilizing its Object-Relational Mapping (ORM) to handle localized database queries and structure public dataset entities.
*   **Advanced Analytics:** Implemented **K-means** and **hierarchical clustering** models to analyze party/deputy voting patterns and determine political alignments.
*   **Interactive UI:** Web dashboard featuring **Plotly.js** for interactive data visualization and **jQuery DataTables** for filtering, sorting, and exporting datasets directly into CSV or Excel formats.

## Tech Stack

*   **Backend:** Python 3, Django Framework, SQLite3
*   **Data Science:** Scikit-learn, Plotly, Pandas
*   **Frontend:** Bootstrap, HTML5/CSS3, JavaScript, jQuery DataTables
