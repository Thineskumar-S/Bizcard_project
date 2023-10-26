import streamlit as st
from extraction import *
from sql_engine import *



def run():
    st.set_page_config(page_title="Biz Card",page_icon=':newspaper:',layout='wide')
    st.title(":rainbow[Biz Card OCR Extraction]")
    with st.container():
            
        col1,col2,col3=st.columns(3)
        with col1:
            with st.container():
                st.header('Upload the Image')
                st.divider()
                st.write('')
                image_file=st.file_uploader('click to upload the card')
            with st.container():
                st.header('Auto extraction of text from sample images')
                autoextract=st.button('Click to Auto extract',key='autoextract')
                if autoextract != None:
                    auto_extracted_result=automated_extraction()
                

        with col2:
            st.header('Extracted Text')
            with st.container():
                st.header('Extracted Text for manually uploaded image')
                if image_file !=None:    
                    extracted_result=text_extractor(image_file)
                    st.table(extracted_result)
                st.divider()
            with st.container():
                st.header('Auto Extracted Text')
                if auto_extracted_result!=None:
                    st.table(auto_extracted_result)
                st.divider()

                
        with col3:
            
            st.header('Upload To Database')
            with st.container():
                button1=st.button('Click to upload the extracted text from Manually uploaded picture')
                if button1!=None:
                    one_img_extracted_data(extracted_result)
                    with st.spinner(text="loading..."):
                            load(auto_extracted_result)
                    st.success('Done!',icon="✅")
                st.divider()
            
            with st.container():
                    
                    st.subheader('Auto extracted text upload')
                    button2=st.button("Click to upload to Database",key='x')
                    if button2!=None:    
                        with st.spinner(text="loading..."):
                            load(auto_extracted_result)
                        st.success('Done!',icon="✅")




if __name__=='__main__':
    run()