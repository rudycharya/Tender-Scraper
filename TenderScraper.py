from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

url = 'https://etender.cpwd.gov.in/'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    print("Opening the website...")
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.dismiss()
        print("Alert dismissed")
    except:
        print("No alert present")


    all_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='dLinksDuration'][contains(text(),'All')]"))
    )
    all_btn.click()

    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    select_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "awardedDataTable_length"))
    )
    select = Select(select_elem)
    select.select_by_visible_text("20")

    time.sleep(3)

    tender_rows = driver.find_elements(By.XPATH, "//table[@id='awardedDataTable']/tbody/tr")
    print(f"Found {len(tender_rows)} tenders.")

    tenders_data = []
    for i, row in enumerate(tender_rows[:20]):
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 8:
            nit_rfp_no = cols[1].text.strip()
            name_of_work = cols[2].text.strip()
            estimated_cost = cols[4].text.strip()
            emd_amount = cols[5].text.strip()
            bid_submission_end_date = cols[6].text.strip()
            bid_open_date = cols[7].text.strip()

            tenders_data.append({
                'NIT/RFP NO': nit_rfp_no,
                'Name of Work / Subwork / Packages': name_of_work,
                'Estimated Cost': estimated_cost,
                'EMD Amount': emd_amount,
                'Bid Submission Closing Date & Time': bid_submission_end_date,
                'Bid Opening Date & Time': bid_open_date
            })

    print("Converting to DataFrame & renaming columns")
    df = pd.DataFrame(tenders_data)
    csv_cols = {
        "NIT/RFP NO": "ref_no",
        "Name of Work / Subwork / Packages": "title",
        "Estimated Cost": "tender_value",
        "EMD Amount": "emd",
        "Bid Submission Closing Date & Time": "bid_submission_end_date",
        "Bid Opening Date & Time": "bid_open_date"
    }
    df.rename(columns=csv_cols, inplace=True)
    print("File is being saved as tenders.csv")
    df.to_csv('tenders.csv', index=False)
    print("File saved as tenders.csv.")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
