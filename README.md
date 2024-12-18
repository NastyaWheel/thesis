# Research Project: Analysis and Modeling of Accident Frequency and Severity on Russian Toll Roads

## Project Description
This repository contains materials, scripts, and interim results for my thesis titled **"Analysis and Modeling of Accident Frequency and Severity on Russian Toll Roads."** The goal of the study is to explore accident patterns on toll roads across Russia, focusing on their frequency and severity.

## Current Status
The project is still in progress. Data extraction, initial preprocessing, and feature engineering have been completed, but further work is required, particularly to create the **key binary variable** identifying whether a road is toll-based.

## Workflow Overview  
### 1. **Data Extraction**  
Accident data from **January 2015 to June 2024** were collected from the [stat.gibdd.ru](http://stat.gibdd.ru) website using:  
- **`parser.py`**: Script to fetch XML files for all regions and months.  
- **`settings.py`**: Configuration file for parser settings, such as regions, request headers, and storage paths.  

Example data for one month and one region can be found in:  
- **`example_data_cards.pdf`** (human-readable format).  
- **`example_data_cards.xml`** (raw XML format).  

**Output:**  
Raw XML files stored monthly for each region (e.g., `ДТП_1_2015_01.xml`).  


### 2. **Data Aggregation**  
The XML files were combined and transformed into a single CSV file (~1.5 million observations) using:  
- **`reading_XML_files.ipynb`**:  
  - Converts participant-level data to accident-level data.  
  - Extracts relevant information, such as location, accident type, weather conditions, and participant attributes.  
  - Saves the aggregated output in **`processed_data.csv`**.


### 3. **Data Preprocessing**  
Initial preprocessing and feature engineering were performed using:  
- **`getting_started_with_the_data.ipynb`**:  
  - Removal of non-informative features.  
  - Handling missing values for critical variables.  
  - Creation of new features based on existing accident attributes.  

**Key Next Step:**  
The creation of the **binary feature indicating toll road presence** remains a critical task, as this variable is central to the thesis analysis.


## Repository Structure  
- **parser.py**: Script for extracting XML files from the traffic statistics portal.  
- **settings.py**: Configuration file with parameters such as request URLs, headers, and regions.  
- **example_data_cards.pdf**: Human-readable example of raw accident data.  
- **example_data_cards.xml**: Sample raw XML data for one region and month.  
- **reading_XML_files.ipynb**: Script to transform and aggregate XML data into a single CSV file.  
- **getting_started_with_the_data.ipynb**: Script for initial data cleaning, preprocessing, and feature engineering.   


## Next Steps  

1. **Data Processing and Feature Engineering:**  
   - Use accident coordinates to create the **key binary feature**: whether the accident occurred on a toll road.  
   - Create an additional feature to determine if the accident occurred **within a populated area**.  
   - Filter the dataset to retain only accidents **outside populated areas** (as toll roads are located outside cities).  
   - Remove **non-informative features** to streamline the dataset.  

2. **Dataset Segmentation:**  
   - Build a separate dataset for **toll roads** and their **free alternatives**.  
   - Incorporate information about the **opening time** of toll roads to identify pre- and post-opening periods for analysis.

3. **Hypothesis Testing:**  
   - Test the hypothesis:  
     **"The introduction of alternative toll roads reduces the accident rate on the route."**  
   - Test the hypothesis:  
     **"The accident rate on toll roads is lower than on their free alternatives."**  

4. **Accident Forecasting:**  
   - Develop predictive models to forecast accident rates on:  
     - **Recently opened toll roads.**  
     - **Toll roads scheduled to open soon.**  

5. **Neural Network Analysis (Optional Extension):**  
   - Implement a neural network to identify **road segments** where the construction of toll roads could be effective in reducing accident rates.  

6. **Results and Insights:**  
   - Compare accident rates on toll and free roads.  
   - Visualize trends and key findings to support the hypotheses.  
   - Provide actionable recommendations for toll road placement based on accident patterns.   