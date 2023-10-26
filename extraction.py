import re
import os
from ocr_model_output import *
 

# extraction of the phone_number 
def phone_pattern(phone_number,data):
    if '-' in phone_number:
        if data['Phone']==None:
            data['Phone']=phone_number
        else:
            first_no=data['Phone']
            data['Phone']=f'{first_no} & {phone_number}'
# address extraction
def address_pattern(string,data):
    pattern=r'\d{1,}\s[a-zA-Z]+'
    end_pattern=r'\d{4,}'
    matched=re.search(pattern,string,re.IGNORECASE)
    end_matched=re.search(end_pattern,string)
    if matched!=None:
        start=matched.start()
        end=end_matched.end()
        data['Address']=string[start:end]
#webiste extraction
def website(string,data):
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
def email(string,data):
    email_pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
    matched=re.search(email_pattern,string,re.IGNORECASE)
    if matched!=None: 
        email=matched.group(0)
        data['Email']=email
        
#calling the entire extraction functions in one for modular approach.
def extracted_data(img_path,data):
    result, result1=extract_text(img_path)
    data['Name']=result[0]
    data['Role']=result[1]
    data['Company_Name']=result1[-1]
    for res in result:
        phone_pattern(res,data)
        email(res,data)
    for res in result1:
        website(res,data)
        address_pattern(res,data)  
    return data

# to full automation we do like this.
def automated_extraction():

    """
    to do this automation we need to put all the images in the data folder. 

     """
    to_folder=r'\Bizcard project\data'
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
        res_extracted_data=extracted_data(img_path,data)
        biz_cards_details.append(res_extracted_data)
    return biz_cards_details

# for image upload by user.

def text_extractor(image_file):
    data={'Name':None,'Phone':None, 'Email': None,"Role":None,"Website":None,"Address":None,'Company_Name':None }
    result, result1=extract_text(image_file)
    data['Name']=result[0]
    data['Role']=result[1]
    data['Company_Name']=result1[-1]
    for res in result:
        phone_pattern(res,data)
        email(res,data)
    for res in result1:
        website(res,data)
        address_pattern(res,data)  
    return data


    


