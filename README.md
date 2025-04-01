# Trae Downloader

This script installs the Trae.ai IDE for you without you needing to visit the site.

---

## Installation  

### 1️. Clone the Repository  

```sh
git clone https://github.com/101409/trae-downloader.git
cd trae-downloader
```

### 2️. Run Without a Virtual Environment
Ensure Python 3.6+ is installed. Then install dependencies:
```sh
pip install requests colorama
```
Run the script:
```sh
python trae.py
```

### 3. Running in a Virtual Environment
Windows
```sh
python -m venv venv
.\venv\Scripts\activate
pip install requests colorama
python trae.py
```

MacOS
```sh
python3 -m venv venv
source venv/bin/activate
pip install requests colorama
python trae.py
```

## Notes
The script automatically selects the correct version for your system
If the download fails, check your internet connection or try running the script again
