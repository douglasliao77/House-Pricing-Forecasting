import os
import json
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# -------------------------------
# CONFIG
# -------------------------------
WAIT_TIME = 10
BASE_FOLDER = os.path.join(os.getcwd(), "data")
os.makedirs(BASE_FOLDER, exist_ok=True)

# Load steps from JSON
with open("pages.json", "r", encoding="utf-8") as f:
    PAGES = json.load(f)

# Map tabs to canvas selectors
CANVAS_MAP = {
    "prisutveckling": ".chartjs--br-48m-prisutveckling",
    "rum": ".chartjs--br-48m-rum"
}

# -------------------------------
# SETUP SELENIUM BASE OPTIONS
# -------------------------------
# Initialize driver with default options
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set default download directory
prefs = {
    "download.default_directory": BASE_FOLDER,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# -------------------------------
# PROCESS EACH PAGE
# -------------------------------
for page in PAGES:
    url = page["url"]
    folder_name = page["folder"]
    tab = page.get("tab", None)
    step = page.get("selector", None)
    filename = page.get("filename", None)  # Get the custom filename
    folder_path = os.path.join(BASE_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    print(f"\nProcessing: {url}")
    driver.get(url)

    driver.execute_cdp_cmd("Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": folder_path
    })

    if tab and tab in CANVAS_MAP:
        selectors = [CANVAS_MAP[tab]]

        for selector in selectors:
            try:
                canvas = WebDriverWait(driver, WAIT_TIME).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )

                labels = json.loads(canvas.get_attribute("data-labels"))
                series = json.loads(canvas.get_attribute("data-series"))

                # Combine all series into one DataFrame
                data = {"Datum": labels}
                if tab == "rum":
                    for idx, s in enumerate(series):
                        if idx == 4:
                            data[f"{idx+1}:or+"] = s
                        else:
                            data[f"{idx+1}:or"] = s
                else:
                    data[f"pris"] = series[0]  # Fixed: should be series[0] instead of s

                df = pd.DataFrame(data)

                # Generate filename - use custom filename if provided, otherwise default
                if filename:
                    chart_filename = f"{filename}.csv"
                else:
                    chart_name = tab if tab else selector.replace(".chartjs--", "")
                    chart_filename = f"{chart_name}.csv"
                
                file_path = os.path.join(folder_path, chart_filename)
                df.to_csv(file_path, index=False)
                print(f"Saved file: {file_path}")
                time.sleep(5) 
            except Exception as e:
                print(f"Error with selector {selector}: {e}")

    elif step:
        try:
            print(f"Waiting for button: {step}")
            btn = WebDriverWait(driver, WAIT_TIME).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, step))
            )
            print(f"Found element, clicking via JS: {step}")
            driver.execute_script("arguments[0].click();", btn)
            print(f"Clicked successfully: {step}")
            
            # If this is a download button and we have a filename, wait for download and rename
            if filename:
                # Wait for download to complete
                time.sleep(5)  # Adjust based on typical download time
                
                # Get the most recently downloaded file
                files = os.listdir(folder_path)
                files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
                files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
                
                if files:
                    latest_file = files[0]
                    old_path = os.path.join(folder_path, latest_file)
                    new_path = os.path.join(folder_path, f"{filename}.xlsx")
                    
                    # Rename the file
                    if os.path.exists(old_path):
                        os.rename(old_path, new_path)
                        print(f"Renamed {latest_file} to {filename}.xlsx")
            
            time.sleep(5)
        except Exception as e:
            print(f"Error clicking button for {step}: {e}")

driver.quit()
print("\nDone! All data extracted.")