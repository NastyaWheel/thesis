# Research Project: Research and Modeling of Accident Frequency and Severity on Toll Highways in Russia

This repository contains materials, scripts, and interim results for my thesis titled **"Research and Modeling of Accident Frequency and Severity on Toll Highways in Russia
"** The goal of the study is to explore accident patterns on toll and free roads across Russia, focusing on their frequency and severity.

## Project Description
This project investigates the impact of road type (toll vs free) on the frequency and severity of traffic accidents on rural roads in Russia. The study combines classical econometric methods with modern machine learning approaches to explore key factors influencing road safety and to build predictive models.

### Hypotheses

1.1 The average number of accidents per month is lower on toll roads than on free roads.

1.2 The factors influencing the number of accidents differ between toll and free roads.

2.1 The probability of a more severe accident outcome is lower on toll roads than on free roads.

2.2 The factors influencing accident severity differ between toll and free roads.


## Repository Structure

```text
├── gibdd_parser/               # Directory containing XML parsing logic
│  ├── parser.py                # Script for extracting XML files from the traffic statistics portal
│  └── settings.py              # Configuration file with parameters such as request URLs, headers, and regions

├── example_data_cards.pdf       # Human-readable example of raw accident data
├── example_data_cards.xml       # Sample raw XML data for one region and month
├── reading_XML_files.ipynb      # Script to transform and aggregate XML data into a single CSV file
├── getting_started_with_the_data.ipynb  # Script for initial data cleaning, preprocessing, and feature engineering

├── .gitignore                   # Git ignored files
├── README.md                    # Project documentation
└── thesis_concept_overview.pptx # Concept presentation for the project
```

## Current Status
The project is still in progress. Data extraction, initial preprocessing, and feature engineering have been completed, but further work is required, particularly to create the **key binary variable** identifying whether a road is toll-based.


## Workflow Overview  
### 1. **Data Extraction**  
Accident data from **January 2015 to March 2025** were collected from the [stat.gibdd.ru](http://stat.gibdd.ru) website using `gibdd_parser/`. Example data for one month and one region can be found in `example_data_cards.pdf` (human-readable format) and `example_data_cards.xml` (raw XML format).  

**Output:** raw XML files stored monthly for each region (e.g., `ДТП_1_2015_01.xml`).  


### 2. **Data Aggregation**  
The XML files were combined and transformed into a single CSV file (~1.5 million observations) using `reading_XML_files.ipynb`:
  - extracts relevant information, such as location, accident type, weather conditions, and participant attributes  
  - converts participant-level data to accident-level data  
  - ereation of new features based on existing accident attributes

**Output:** raw CSV file (single dataset for all accidents)


### 3. **Data Preprocessing**  
Initial preprocessing and feature engineering were performed using `getting_started_with_the_data.ipynb`:  
  - preprocessing data  
  - filling the gaps
  - analyzing and removing non-informative features
  - renaming columns (for better readability)

**Output:** processed CSV file (single dataset for all accidents)


## Next Steps  


### 4. **Data Processing**
Creating two datasets were constructed based on raw traffic accident data in Russia:

1. Panel Dataset
- Unit of observation: road section × month
- Purpose: analysis of accident frequency

2. Accident-level Dataset
- Unit of observation: individual accident
- Purpose: analysis of accident severity
- Adding a binary variable `is_toll` indicating the road type


### 5. Hypotheses Testing
Methods applied:
- Panel Regression with Fixed Effects
- Negative Binomial Regression (in case of overdispersion)
- Multinomial Logit Model (for accident severity analysis)
- Machine Learning models: Random Forest, Gradient Boosting
- SHAP analysis for feature importance
- Evaluation metrics: MAE/MSE for frequency models, Accuracy/F1-score for severity models


### 6. Analyzing "hot spots"
- Identifing high-accident locations ("hot spots") using the DBSCAN algorithm based on accident coordinates
- Negative sampling: generating observations without accidents for modeling accident probability
- Training separate machine learning models for toll and free road "hot spots"
- SHAP analysis to identify the most important factors influencing accident probability
- Comparison of accident risk factors between toll and free road sections with high accident concentration
- Separate clustering for toll and free roads