# Research Project: Research and Modeling of Accident Severity on Toll Highways in Russia

This repository contains materials, scripts, and interim results for my thesis titled **"Research and Modeling of Accident Severity on Toll Highways in Russia
"** The goal of the study is to explore accident patterns on toll and free roads across Russia, focusing on their severity.

## Project Description
This project investigates the impact of road type (toll vs free) on the severity of traffic accidents on rural roads in Russia. The study combines classical econometric methods with modern machine learning approaches to explore key factors influencing road safety and to build predictive models.

### Hypotheses

(1) The probability of a more severe accident outcome is lower on toll roads than on free roads.

(2) The factors influencing accident severity differ between toll and free roads.


## Repository Structure

```text
├── gibdd_parser/               # Directory containing XML parsing logic
│  ├── parser.py                # Script for extracting XML files from the traffic statistics portal
│  └── settings.py              # Configuration file with parameters such as request URLs, headers, and regions

├── gibdd_parser/               # Directory containing working with accident-level data
│  ├── severity_hypotheses.ipynb  # Script to check hypotheses
│  └── severity_model.ipynb     # Script to train the model predict severity of accidents

├── example_data_cards.pdf       # Human-readable example of raw accident data
├── example_data_cards.xml       # Sample raw XML data for one region and month
├── reading_XML_files.ipynb      # Script to transform and aggregate XML data into a single CSV file
├── getting_started_with_the_data.ipynb  # Script for initial data cleaning, preprocessing, and feature engineering

├── .gitignore                   # Git ignored files
├── README.md                    # Project documentation
└── thesis_concept_overview.pdf  # Concept presentation for the project
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
- Creating accident-level dataset (unit of observation ─ individual accident, for **analysis of accident severity**)
- Adding a binary variable `is_toll` indicating the road type


### 5. Hypotheses Testing
Methods applied:
- Multinomial Logit Model (for accident severity analysis)
- Machine Learning models: Random Forest, Gradient Boosting
- Feature importance
- Evaluation metrics: Accuracy and F1-score


### 6. Analyzing "hot spots"
- Identifing high-accident locations ("hot spots") using the DBSCAN algorithm based on accident coordinates
- Testing hypotheses
- Negative sampling: using noise
- Training machine learning model for to predict "hot spots" toll and free road