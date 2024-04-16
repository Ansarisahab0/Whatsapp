import requests
import json


print('''
                              .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        _
     /\                        (_)
    /  \   _ __  ___  __ _ _ __ _
   / /\ \ | '_ \/ __|/ _` | '__| |
  / ____ \| | | \__ \ (_| | |  | |
 /_/    \_\_| |_|___/\__,_|_|  |_|


Author   : Hacker Ansari
Github : https://github.com/hacker_ansari_07
instagram : https://instagram.com/hacker_ansari_07
Thank you for using this tool

def send_otp(phone_number):
    url = "https://api.whatsapp.com/v1/users/login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "phone_number": phone_number,
        "method": "sms"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def verify_otp(phone_number, otp):
    url = "https://api.whatsapp.com/v1/users/login/verify"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "phone_number": phone_number,
        "otp": otp
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

phone_number = input("Enter your phone number: ")
otp = input("Enter the OTP: ")

send_otp_response = send_otp(phone_number)
if send_otp_response["status"] == "success":
    verify_otp_response = verify_otp(phone_number, otp)
    if verify_otp_response["status"] == "success":
        print("OTP verification successful!")
    else:
        print("OTP verification failed. Please try again.")
else:
    print("OTP sending failed. Please try again.")
