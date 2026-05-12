<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lead Generator Scraper</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      background: #f7f7f7;
      color: #222;
    }
    .container {
      max-width: 900px;
      margin: 40px auto;
      background: #fff;
      padding: 32px;
      border-radius: 12px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    }
    h1, h2, h3 {
      color: #111;
    }
    h1 {
      margin-top: 0;
      font-size: 2rem;
    }
    h2 {
      margin-top: 28px;
      border-bottom: 1px solid #e5e5e5;
      padding-bottom: 8px;
    }
    code, pre {
      background: #f3f3f3;
      border-radius: 6px;
      padding: 2px 6px;
      font-family: Consolas, monospace;
    }
    pre {
      padding: 16px;
      overflow-x: auto;
    }
    ul {
      margin-top: 8px;
    }
    .note {
      background: #fff8db;
      border-left: 4px solid #f0c419;
      padding: 12px 16px;
      border-radius: 6px;
      margin-top: 12px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Lead Generator Scraper</h1>
    <p>
      A Python-based lead generation scraper built using Playwright, MySQL,
      and asynchronous scraping workflows.
    </p>

    <h2>Features</h2>
    <ul>
      <li>Scrape business lead URLs from search queries</li>
      <li>Extract detailed business information</li>
      <li>Store scraped data directly into MySQL</li>
      <li>Export data into Excel files</li>
      <li>Bulk query generation support</li>
      <li>Modular scraping workflow</li>
    </ul>

    <h2>Project Setup</h2>
    <h3>1. Clone the Repository</h3>
    <pre><code>git clone &lt;your-repository-url&gt;
cd lead_generator</code></pre>

    <h3>2. Create Python Environment</h3>
    <p>Using venv:</p>
    <pre><code>python -m venv venv
source venv/bin/activate</code></pre>

    <p>Using uv:</p>
    <pre><code>uv venv
source .venv/bin/activate</code></pre>

    <h3>3. Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <p>or with uv:</p>
    <pre><code>uv pip install -r requirements.txt</code></pre>

    <h3>4. Install Playwright Browsers</h3>
    <pre><code>playwright install</code></pre>

    <p>This will install Chromium, Firefox, and WebKit.</p>

    <h2>Environment Variables</h2>
    <p>Create a <code>.env</code> file in the project root:</p>
    <pre><code>host_db=localhost
user_db=root
pass_db=your_password
db_name=your_database</code></pre>

    <h2>Database Setup</h2>
    <h3>Option 1 — Import Existing Schema</h3>
    <pre><code>mysql -u root -p your_database &lt; schema.sql</code></pre>

    <h3>Option 2 — Create Tables Using Python</h3>
    <p>
      A file named <code>create_schema.py</code> is included in the project.
      It contains functions for automatically creating database tables.
    </p>
    <pre><code>python create_schema.py</code></pre>

    <div class="note">
      If you encounter any issues with schema creation, verify the functions inside the file manually.
    </div>

    <h2>Scraper Workflow</h2>
    <h3>Step 1 — Generate Lead URLs</h3>
    <p>Run <code>get_lead_url.py</code>.</p>
    <p>Main functions:</p>
    <ul>
      <li><code>custom_run_scrapper()</code></li>
      <li><code>function_run_scrapper()</code></li>
    </ul>
    <p>Example query: <code>restaurants in UK</code></p>
    <p>This stage collects lead/business URLs.</p>

    <h3>Step 2 — Extract Business Data</h3>
    <p>Run <code>get_main_main_data.py</code>.</p>
    <p>Main function:</p>
    <ul>
      <li><code>main()</code></li>
    </ul>
    <p>This stage visits collected URLs, extracts business information, and stores data into the database.</p>

    <h2>Data Flow Understanding</h2>
    <p>
      To understand the complete internal workflow and data pipeline, check
      <code>custome_buitl_data.ipynb</code>.
    </p>

    <h2>Excel Export</h2>
    <p>
      To export scraped data into Excel format, use
      <code>data_in_excle_finished.py</code>.
    </p>

    <h2>Bulk Query Generation</h2>
    <p>
      For generating bulk scraping queries, use the notebooks available inside
      <code>jupyter_notebook/</code>.
    </p>

    <h2>Database Schema</h2>
    <p>The database schema is available in <code>schema.sql</code>.</p>
    <p>This file contains table structure, constraints, foreign keys, and indexes.</p>

    <h2>Technologies Used</h2>
    <ul>
      <li>Python</li>
      <li>Playwright</li>
      <li>MySQL</li>
      <li>asyncio</li>
      <li>pandas</li>
      <li>dotenv</li>
    </ul>

    <h2>Notes</h2>
    <ul>
      <li>Ensure MySQL server is running before starting the scraper.</li>
      <li>Use valid proxies and delays if scraping at scale.</li>
      <li>Some websites may block automated traffic depending on region and request frequency.</li>
    </ul>
  </div>
</body>
</html>