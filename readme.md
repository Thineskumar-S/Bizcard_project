# BizCard Data Extraction and AWS Database Integration

## Project Overview 🚀

**Title**: BizCard Data Extraction and AWS Database Integration

**Language Detected**: English

This project leverages the power of Easy OCR to extract text data from business cards, focusing on English characters, numerals, and various fonts. The extracted data is then cleaned, transformed, and loaded into an AWS RDS MySQL server.

## Project Flow 🔄

### E - Extraction
- Users can upload their business card images directly.
- The Easy OCR model predicts and extracts text from the uploaded images.
- Users have the option to click the "Load" button to save the extracted text into the cloud-hosted SQL server.

### T - Transformation
- Extracted text data is processed by cleaning and transforming it into the desired format using regular expressions (regex).

### L - Load
- Transformed data is loaded into the AWS RDS MySQL server for ease of access and future use.

## Two Options for Users 🤝

### Option 1: Manual Extraction
1. User uploads the image.
2. The model predicts and extracts text.
3. User clicks the "Load" button to save the text into the cloud-hosted SQL server.

### Option 2: Auto Extraction with Sample Images
1. User selects auto-extraction with sample images.
2. The system extracts text from a set of 5 sample images.
3. Extracted data from these images is displayed in a table to the user.
4. User can choose to click the "Auto Extract & Upload" button to load the data into the SQL database.

## Challenges Faced 🤨

1. **Accuracy of Easy OCR**:
   - The Easy OCR model may not always extract text as accurately as it appears in the image. Preprocessing and transformation using regex are necessary to improve data quality.

2. **Generalized Regex Patterns**:
   - Crafting generalized regex patterns to handle variations in text output from the Easy OCR is a complex challenge. The extracted text can vary from field to field and image to image.

## Caveats ⚠️

This BizCard data extraction relies on a set of sample images and their generalized patterns. The accuracy and reliability of the extraction process depend on the quality and diversity of these sample images.

**Note**: For the best results, ensure that the uploaded images are clear and well-lit. The accuracy of text extraction may vary based on the quality of the source images.

👉 Explore the world of BizCard Data Extraction and Database Integration! 🌐📊📄