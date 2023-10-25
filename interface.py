from PIL import Image
import easyocr as ocr
import re
import numpy as np
import os



# calling ocr neural network for english language
reader=ocr.Reader(['en'])

# extraction of the phone_number 
def phone_pattern(phone_number):
    if '-' in phone_number:
        if data['Phone']==None:
            data['Phone']=phone_number
        else:
            first_no=data['Phone']
            data['Phone']=f'{first_no} & {phone_number}'
# address extraction
def address_pattern(string):
    pattern=r'\d{1,}\s[a-zA-Z]+'
    end_pattern=r'\d{4,}'
    matched=re.search(pattern,string,re.IGNORECASE)
    end_matched=re.search(end_pattern,string)
    if matched!=None:
        start=matched.start()
        end=end_matched.end()
        data['Address']=string[start:end]
#webiste extraction
def website(string):
    finding_web_pattern=r'www[.\s]'
    mathced_pattern=re.search(finding_web_pattern,string,re.IGNORECASE)
    if mathced_pattern!=None:    
        matched_web_pattern=mathced_pattern.group(0)
        matched_web_pattern=matched_web_pattern.lower()
        if matched_web_pattern=='www ':
            web_pattern=r'www[\s,.][a-z0-9]+?[.]\w{2,7}'
            matched=re.search(web_pattern,string,re.IGNORECASE)
            web=matched.group(0)
            updated_web=re.sub(r'WWW\s','WWW.',web)
            data['Website']=updated_web
            
        elif matched_web_pattern == 'www.':
            web_pattern=r'www[\s,.].+?$'
            matched=re.search(web_pattern,string,re.IGNORECASE)
            web=matched.group(0)
            updated_web=re.sub(r'com','.com',web)
            data['Website']=updated_web
#email extraction        
def email(string):
    email_pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
    matched=re.search(email_pattern,string,re.IGNORECASE)
    if matched!=None: 
        email=matched.group(0)
        data['Email']=email
        
#calling the entire extraction functions in one for modular approach.
def extract(img_path):
    img=Image.open(img_path)
    img_array=np.array(img) 
    result = reader.readtext(img_array, detail = 0)
    result1= reader.readtext(img_array, detail = 0,paragraph=True)
    data['Name']=result[0]
    data['Role']=result[1]
    data['Company_Name']=result1[-1]
    for res in result:
        phone_pattern(res)
        email(res)
    for res in result1:
        website(res)
        address_pattern(res)  
    return data

# to full automation we do like this.
def automated_extraction():

    """
    to do this automation we need to put all the images in the data folder. 

     """
    to_folder=r'data'
    os.chdir(to_folder)
    current_folder=os.getcwd()
    files=os.listdir()
    file_paths=[]
    for file in files:
        file_path=os.path.join(current_folder,file)
        file_paths.append(file_path)

    biz_cards_details=[]
    for img_path in file_paths:
        data={'Name':None,'Phone':None, 'Email': None,"Role":None,"Website":None,"Address":None,'Company_Name':None}
        extracted_data=extract(img_path)
        biz_cards_details.append(extracted_data)

# for image upload by user.

def text_extractor(image_file):
    data={'Name':None,'Phone':None, 'Email': None,"Role":None,"Website":None,"Address":None,'Company_Name':None }
    img=Image.open(image_file)
    img_array=np.array(img) 
    result = reader.readtext(img_array, detail = 0)
    result1= reader.readtext(img_array, detail = 0,paragraph=True)
    data['Name']=result[0]
    data['Role']=result[1]
    data['Company_Name']=result1[-1]
    for res in result:
        phone_pattern(res)
        email(res)
    for res in result1:
        website(res)
        address_pattern(res)  
    return data


    


