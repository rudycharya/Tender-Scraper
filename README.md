*CPWD eTender Data Extractor*

A Python script to automate the extraction of tender data from the CPWD eTender portal. Collects details for the first 20 tenders and saves them in a CSV file.

*Features:*

Automated Navigation: Uses Selenium to interact with the website and handle dropdowns.

Alert Handling: Manages alerts related to the CPWD Signer application.

CSV Export: Saves tender details to tenders.csv for easy analysis.

*Project Notes:*

*Script Overview:*
This Python script automates the extraction of tender data from the CPWD eTender portal. It navigates the website, interacts with dropdown menus, and collects the required tender details for the first 20 entries.

*Dependencies:*
The script requires Python packages selenium and pandas, which are listed in the requirements.txt file.

*Chromedriver:*
The project includes chromedriver.exe, which is necessary for Selenium to interact with the Chrome browser.

*CPWD Signer:*
The website requires the CPWD Signer application to be installed and running on the local machine for full functionality. The script includes logic to handle any alerts related to the CPWD Signer.

*Data Extraction:*
The script extracts the following fields for each tender: NIT/RFP Number, Name of Work, Estimated Cost, EMD Amount, Bid Submission Closing Date & Time, and Bid Opening Date & Time.
The extracted data is saved in a CSV file (tenders.csv).

*Steps for Execution:*

Install required Python packages using pip install -r requirements.txt.

Place chromedriver.exe in the project folder.

*Run the script using Python:* python tender_scraper.py.

*Required Software*
Python 3
Google Chrome (or another Chromium-based browser)

*Installation*
Clone this repository:

bash
git clone https://github.com/yourusername/cpwd-tender-scraper.git
cd cpwd-tender-scraper
Install required Python packages:

bash
pip install -r requirements.txt
Download chromedriver.exe:

Download the appropriate version of chromedriver.exe for your Chrome browser from here.

Place chromedriver.exe in the project folder.

Install CPWD Signer (optional, but recommended):

Download and install the CPWD Signer application from the CPWD eTender portal.

Run it as administrator for full functionality.

Usage
Run the script:

bash
python tender_scraper.py
Output:

The script will extract tender data and save it to tenders.csv in the project folder.

Notes
The script handles website alerts related to CPWD Signer.

Ensure chromedriver.exe is in the project folder.

The CPWD website may require manual login or digital certificate for certain features.
