import pandas as pd
import pywhatkit as kit
import time
import re

# File Configuration
excel_file = 'excel.xlsx' 
df = pd.read_excel(excel_file)

group_link = "https://chat.whatsapp.com/"

def format_phone(phone):
    # Strip all non-numeric characters (spaces, parentheses, dashes)
    clean_phone = re.sub(r'\D', '', str(phone))
    
    # Normalization logic for regional phone formats
    if clean_phone.startswith('05'):
        return '+90' + clean_phone[1:]
    elif clean_phone.startswith('5'):
        return '+90' + clean_phone
    elif clean_phone.startswith('90'):
        return '+' + clean_phone
    return None

# Main automation loop
for index, row in df.iterrows():
    raw_phone = row['Phone'] 
    formatted_phone = format_phone(raw_phone)
    name = row['Name'] 

    if formatted_phone:
        try:
            print(f"Status: Sending message to {name} ({formatted_phone})")
            
            # Execute instant messaging protocol
            # wait_time=15, tab_close=True, close_time=2
            kit.sendwhatmsg_instantly(
                formatted_phone, 
                f"Hello, {group_link}", 
                15, 
                True, 
                2
            )
            
            # Mandatory cooling period to maintain system stealth
            time.sleep(20) 
            
        except Exception as e:
            print(f"System Error ({name}): {e}")
