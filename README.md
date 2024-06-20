# LLM-AggregationTool

## Overview

LLM-AggregationTool is a web automation project built using Selenium IDE. This tool automates the process of reading prompts from a localhosted webpage, running the prompts through various Large Language Models (LLMs), and collecting the responses in a Google Form sheet. The responses are then stored in an Excel sheet for convenient download as a CSV file for further evaluation through Python scripts.

## Features

- **Web Automation with Selenium IDE**: Automates interaction with a localhosted webpage where prompts are uploaded.
- **Integration with Multiple LLMs**: Runs prompts through multiple LLMs, including:
  - ChatGPT
  - GeminiAI
  - Claude AI
  - Perplexity AI
  - Meta AI
  - Hugging Chat
- **Response Collection**: Collects responses from the LLMs and stores them in a Google Form sheet, which is then saved as an Excel sheet for easy CSV download.
- **Response Evaluation**: Evaluates responses using a Python script (`Response_Evaluation.ipynb`) with the following features:
  - **Analysis**: Analyzes response length, sentiment polarity, and produces word clouds.
  - **Evaluation Metrics**: Implements evaluation metrics such as BLEU, ROUGE, Cosine Similarity, Distinct-1, and Distinct-2 to assess the quality of the responses.
  - **Comparison**: Compares models' outputs with a reference ideal response and between the models themselves.

## Files

- **LLMAggTool.side**: Selenium IDE project file that contains the web automation script.
- **Response_Evaluation.ipynb**: Jupyter notebook that performs response evaluation using Python, pandas, matplotlib.pyplot, and seaborn.

## Folders

- **PDFReader**: Contains the localhost webpage code which allows you to read a PDF containing the prompts and displays it on the webpage for the Selenium IDE to read.
- **DataScraping**: Contains Selenium web automation code for scraping data from the [c40knowledgehub.org](https://www.c40knowledgehub.org/) website, specifically for 790 articles on Climate Policy.

## Demo

Check out a demo of the Selenium process [here](https://www.youtube.com/watch?v=yHAjJDH-QbA).

## Usage

### Web Automation

1. Open the `LLMAggTool.side` file in Selenium IDE.
2. Run the automation script to interact with the localhosted webpage, submit prompts to various LLMs, and collect the responses in a Google Form sheet.
3. Download the Google Form sheet responses as an Excel file.

### Localhost Webpage (PDFReader)

1. Navigate to the `PDFReader` folder.
2. Follow the instructions in the README file within the `PDFReader` folder to set up and run the localhost webpage.
3. Upload the PDF containing the prompts to the webpage.

### Data Scraping (DataScraping)

1. Navigate to the `DataScraping` folder.
2. Open the Selenium web automation code for scraping data from the c40knowledgehub.org website.
3. Run the automation script to scrape data for 790 articles on Climate Policy.

### Response Evaluation

1. Open the `Response_Evaluation.ipynb` file in Jupyter Notebook.
2. Follow the instructions in the notebook to load the collected responses.
3. Run the evaluation metrics and analysis to assess and compare the quality of the LLM responses.

## Dependencies

### Selenium IDE

- [Selenium IDE](https://www.selenium.dev/selenium-ide/) must be installed to run the web automation script.

### Python Packages

The following Python packages are required to run the `Response_Evaluation.ipynb` notebook:

- pandas
- matplotlib.pyplot
- seaborn
- nltk
- sklearn
- wordcloud

Install the required packages using pip:

```bash
pip install pandas matplotlib seaborn nltk scikit-learn wordcloud
