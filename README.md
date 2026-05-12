# Lead Generator Scraper

A Python-based lead generation scraper built using Playwright, MySQL, and asynchronous scraping workflows.

---

# Features

* Scrape business lead URLs from search queries
* Extract detailed business information
* Store scraped data directly into MySQL
* Export data into Excel files
* Bulk query generation support
* Modular scraping workflow

---

# Project Setup

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd lead_generator
```

---

## 2. Create Python Environment

### Using venv

```bash
python -m venv venv
source venv/bin/activate
```

### Using uv

```bash
uv venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or with uv:

```bash
uv pip install -r requirements.txt
```

---

## 4. Install Playwright Browsers

```bash
playwright install
```

This will install:

* Chromium
* Firefox
* WebKit

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
host_db=localhost
user_db=root
pass_db=your_password
db_name=your_database
```

---

# Database Setup

## Option 1 — Import Existing Schema

Use the provided `schema.sql` file.

```bash
mysql -u root -p your_database < schema.sql
```

---

## Option 2 — Create Tables Using Python

A file named:

```text
create_schema.py
```

is included in the project.

It contains functions for automatically creating database tables.

Run:

```bash
python create_schema.py
```

If you encounter any issues with schema creation, please verify the functions inside the file manually.

---

# Scraper Workflow

The scraper works in two stages.

## Step 1 — Generate Lead URLs

Run:

```text
get_lead_url.py
```

Main functions:

* `custom_run_scrapper()`
* `function_run_scrapper()`

Example query:

```text
restaurants in UK
```

This stage collects lead/business URLs.

---

## Step 2 — Extract Business Data

Run:

```text
get_main_main_data.py
```

Main function:

* `main()`

This stage:

* visits collected URLs
* extracts business information
* stores data into the database

---

# Data Flow Understanding

If you want to understand the complete internal workflow and data pipeline, check:

```text
custome_buitl_data.ipynb
```

This notebook demonstrates:

* query generation
* scraping flow
* database insertion
* data transformation

---

# Excel Export

To export scraped data into Excel format, use:

```text
data_in_excle_finished.py
```

Additional advanced export workflows are available inside:

```text
custome_buitl_data.ipynb
```

---

# Bulk Query Generation

For generating bulk scraping queries, use the notebooks available inside:

```text
jupyter_notebook/
```

---

# Database Schema

The database schema is available in:

```text
schema.sql
```

This file contains:

* table structure
* constraints
* foreign keys
* indexes

---

# Technologies Used

* Python
* Playwright
* MySQL
* asyncio
* pandas
* dotenv

---

# Notes

* Ensure MySQL server is running before starting the scraper.
* Use valid proxies and delays if scraping at scale.
* Some websites may block automated traffic depending on region and request frequency.

---
