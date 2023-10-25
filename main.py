import streamlit as st
from interface import *




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
                autoextract=st.button('Click to Auto extraction',key='autoextract')
                if autoextract != None:
                    result=automated_extraction()
                st.table(result)

        with col2:
            with st.container():
                st.header('Extracted Text')
                if image_file !=None:    
                    result1=text_extractor(image_file)
                    st.write(result1)
                st.divider()
            with st.container():
                st.header('Auto Extracted Text')
                if result!=None:
                    st.write(result)
                st.divider()

                
        with col3:
            with st.container():
                st.header('Upload To Database')
                st.divider()
                st.header('Contacts in Database')
                x=st.button("Click to upload to Database",key='x')
                if x!=None:    
                    with st.spinner(text="loading..."):
                        st.write("loaded to db")
                        st.success('Done!',icon="✅")












if __name__=='__main__':
    run()