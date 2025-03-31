# Trae Downloader

This script installs the Trae.ai IDE for you without you needing to visit the site.

Clone the Repository
git clone https://github.com/101409/trae-downloader.git
cd trae-downloader

Running Without a Virtual Environment
  Ensure Python (3.6+) is installed and then install dependencies globally:
  pip install requests colorama

Run the script:
  python download_trae.py

Running Within a Virtual Environment
For Windows
  python -m venv venv
  venv\Scripts\activate

  pip install requests colorama
  python download_trae.py

For macOS/Linux
  python3 -m venv venv
  source venv/bin/activate

  pip install requests colorama
  python download_trae.py
