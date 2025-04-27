# Research Project: Research and Modeling of Accident Frequency and Severity on Toll Highways in Russia

This repository contains materials, scripts, and interim results for my thesis titled **«Research and Modeling of Accident Frequency and Severity on Toll Highways in Russia»** The goal of the study is to explore accident patterns on toll and free roads across Russia, focusing on their frequency and severity.

## Project Description
This project investigates the impact of road type (toll vs free) on the frequency and severity of traffic accidents on rural roads in Russia. The study combines classical econometric methods with modern machine learning approaches to explore key factors influencing road safety and to build predictive models.

### Hypotheses

(1.1) The average number of accidents per month is lower on toll roads than on free roads.

(1.2) The factors influencing the number of accidents differ between toll and free roads.

(2.1) The probability of a more severe accident outcome is lower on toll roads than on free roads.

(2.2) The factors influencing accident severity differ between toll and free roads.

## Data Description
**~1.5 million observations** of road traffic accidents from **January 2015 to March 2025** collected from [stat.gibdd.ru](http://stat.gibdd.ru) website. 


## Repository Structure

```text
├── gibdd_parser/                # Directory containing XML parsing logic
│  ├── parser.py                 # Script for extracting XML files from the traffic statistics portal
│  └── settings.py               # Configuration file with parameters such as request URLs, headers, and regions

├── severity/                    # Directory containing working with accident-level data
│  ├── severity_hypotheses.ipynb # Script to check hypotheses
│  └── severity_model.ipynb      # Script to train the model predict severity of accidents

├── frequency/                   # Directory containing working with panel data

├── creating_final_dataset.ipynb # Constructe two datasets with different observations
├── example_data_cards.pdf       # Human-readable example of raw accident data
├── example_data_cards.xml       # Sample raw XML data for one region and month
├── reading_XML_files.ipynb      # Script to transform and aggregate XML data into a single CSV file
├── getting_started_with_the_data.ipynb  # Script for initial data cleaning, preprocessing, and feature engineering

├── .gitignore                   # Git ignored files
├── README.md                    # Project documentation
├── thesis_concept_overview.pdf  # Concept presentation for the project
└── variables_description.md     # Description of project features
```


## Workflow Overview 
### 1.1. **Data Extraction**  
Collecte accident data from the website using `gibdd_parser/`. Example data for one month and one region can be found in `example_data_cards.pdf` (human-readable format) and `example_data_cards.xml` (raw XML format).

**Output:** raw XML files stored monthly for each region (e.g., `ДТП_<REGION_NUMBER>_YYYY_MM.xml`).


### 1.2. **Data Aggregation**  
Using `reading_XML_files.ipynb`:
  - extract relevant information, such as location, accident type, weather conditions, and participant attributes  
  - convert participant-level data to accident-level data
  - create of new features based on existing accident attributes
  - combine and transforme data into a single DataFrame with ~1.5 million observations

**Output:** raw CSV file (single dataset for all accidents)


### 1.3. **Data Preprocessing**  
Using `getting_started_with_the_data.ipynb`:  
  - remove or filling the gaps with ML algorithms
  - process caregorical features
  - remove unnecessary features and creating the new ones

**Output:** processed CSV file (single dataset for all accidents)


### 1.4. **Data Processing**
Using `creating_final_dataset.ipynb` code constructe:
  1. accident-level dataset (unit of observation ─ individual accident, for **analysis of accident severity**)
  2. panel dataset (unit of observation ─ road section × month, for **analysis of accident frequency**)
    - with negative sampling and feature aggregation
and add a binary variable `is_toll` indicating the road type

**Output:** ACCIDENT_LEVEL_DATA.csv, PANEL_DATA.csv


### 2. **Work with accident-level data**
Work in `severity/`.

#### Tasks:
  1. Check hypotheses (2.1) and (2.2)
  2. Identify «hot spots» and check hypotheses (2.1) and (2.2) again
  3. Train a model to predict «hot spots»

#### Methods applied:
  - Multinomial Logit (MNL) Model
  - undersampling, class weighting
  - VIF (Variance Inflation Factor), correlation matrix
  - feature importance, PCA, UMAP
  - DBSCAN, Random Forest, Gradient Boosting, Neural Network
  - GridSearchCV
  - evaluation metrics: Accuracy and F1-score

#### Results:
  - Hypotheses (2.1) and (2.2) confirmed for both full sample and «hot spots»
  - Model predicting «hot spots» achieved **0.85** accuracy and **0.80** F1-score on random obs


### 3. **Work with panel data** (currently in progress)
Work in `frequency/`.

#### Tasks:
  1. Check hypotheses (1.1) and (1.2)
  2. Check hypotheses (1.1) and (1.2) for «hot spots»
  3. Train a model to predict the probability of an accident

#### Methods planned to apply:
  - Panel Regression with Fixed Effects
  - Negative Binomial Regression (in case of overdispersion)
  - undersampling, class weighting
  - VIF (Variance Inflation Factor), correlation matrix
  - feature importance
  - Random Forest, Gradient Boosting
  - GridSearchCV
  - evaluation metrics: MAE and MSE

#### Results (Expected):
  - Hypotheses (1.1) and (1.2) confirmed
  - Model predicting probability achieved over **0.80** MSE