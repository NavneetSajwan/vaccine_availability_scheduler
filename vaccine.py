import requests
import smtplib
import datetime 
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv('sender_email')
SENDER_PASSWORD = os.getenv('sender_password')


url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like


def check_availability():
    availability = False
    PINCODE = os.getenv('pincode')
    current_time = datetime.datetime.now() 
    today = current_time.day
    today, month, year = current_time.day, current_time.month, current_time.year
    for day in range(today,today+8):
        # print(day)
        print(current_time)
        if availability==True:
            break


        date  = f"{day}-{month}-{year}"
        params = {'pincode':PINCODE, 'date':date}
        result = requests.get(url, params = params, headers = headers).json()

        for hospital_dict in result['sessions']:
            # print(hospital_dict['name'])
            print(hospital_dict['min_age_limit'])
            age = hospital_dict['min_age_limit']
            dose1 = hospital_dict['available_capacity_dose1']
            if age <45 and dose1>0:
                availability = True 
                break
        print(availability)

    receivers = ["navneetsinghsajwan@gmail.com",]

    if availability==True:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL, SENDER_PASSWORD)
        receivers = ["navneetsinghsajwan@gmail.com","imankitsajwan@gmail.com"]
        s.sendmail(SENDER_EMAIL, receivers, "Vaccine Available")
        s.quit()

def test():
    print("Hello!")

if __name__ == "__main__":
    schedule.every(5).minutes.do(check_availability)
    # schedule.every(5).seconds.do(test)
    while True:

        # Checks whether a scheduled task
        # is pending to run or nots
        schedule.run_pending()
        time.sleep(1)

