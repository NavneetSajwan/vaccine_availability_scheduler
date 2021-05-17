# vaccine_availability_scheduler
With Indian vaccine drive turning into a hackathon for coders, people are trying to get their hands on the coveted vaccine by tapping into the cowin public api.


This repo contains a python script that takes pincode and email of subscribers and notifies them of vaccine vailability. Api calls are made every 5 minutes.

In order to successfully run this script.

- Clone the directory and cd into it.

- Create an environment and install from requirements.txt

- Create a .env file and keep the sender's email and password in it securely.

- Also, enter your pincode in the .env file.

- run the script `vaccine.py` in the terminal

As soon as the vaccines become available, the `receivers` will get the mail.
