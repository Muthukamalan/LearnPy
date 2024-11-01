from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Constants
DOWNLOAD_PATH = os.path.expanduser('~/Downloads')  # Adjust as needed
AMAZON_URL = "https://www.amazon.com"

def create_chrome_driver(**context):
    """Create and configure Chrome WebDriver"""
    try:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Configure download settings
        prefs = {
            "download.default_directory": DOWNLOAD_PATH,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        # Initialize driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)
        
        # Store driver in XCom for next task
        context['task_instance'].xcom_push(key='webdriver', value=driver)
        return "Driver created successfully"
        
    except Exception as e:
        print(f"Error creating driver: {str(e)}")
        raise

def navigate_to_amazon(**context):
    """Navigate to Amazon using the created driver"""
    try:
        # Get driver from previous task
        driver = context['task_instance'].xcom_pull(task_ids='create_driver', key='webdriver')
        
        if not driver:
            raise ValueError("No WebDriver found in XCom")
            
        # Navigate to Amazon
        driver.get(AMAZON_URL)
        
        # Verify we're on Amazon (basic check)
        assert "Amazon" in driver.title, "Failed to navigate to Amazon"
        
        return f"Successfully navigated to {AMAZON_URL}"
        
    except Exception as e:
        print(f"Error navigating to Amazon: {str(e)}")
        raise
    finally:
        if driver:
            driver.quit()

# DAG definition
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'amazon_driver_test',
    default_args=default_args,
    description='Test DAG for creating WebDriver and navigating to Amazon',
    schedule_interval=None,  # Manual trigger only
    catchup=False
) as dag:

    create_driver = PythonOperator(
        task_id='create_driver',
        python_callable=create_chrome_driver,
        provide_context=True,
    )

    goto_amazon = PythonOperator(
        task_id='navigate_to_amazon',
        python_callable=navigate_to_amazon,
        provide_context=True,
    )

    # Set task dependencies
    create_driver >> goto_amazon
