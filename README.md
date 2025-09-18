# Econ Replication Project

## Overview
This project is part of academic activities that I will be undertaking in the course of the next six months to build a research profile for the intention to position myself a predoc role.
In it, I aim to replicate the research conducted by Nathan Nunn. The provided data files have been sourced from his website and include shape files and data tables necessary for the analysis. The analyses were performed using Python, focusing on reproducing the main ideas presented in Nunn's work.
The analyses were perfomed using python, focusing on reproducing the main ideas represented in Nunn's work. 

## What Question Does the Paper Tries to Answer? 
Did Africa’s exposure to the slave trades (1400–1900) cause lower levels of economic development today?
To put it in layman's language, the author, Nathan Nunn, tries to establish the correlation problem/casuality issue of economic development and slave trade in Africa in the time between 1400 up to 1900. 

## How He Frames it: 
Correlation Problem: We can observe that countries with higher slave exports tend to be poorer today. But is this just coincidence, or is it really casual?
Casuality Issue: Maybe poorer regions were more vulnerable to slave raids (reverse casuality), or maybe georgraph, or even other factors can explain?
## Approach:
1. The author collects historical data on slave exports (Atlantic, Indian Ocean, Red Sea, Trans-Saharan).
2. He measures today’s development (GDP per capita, institutions, etc.).
3. He runs OLS regressions of income today on slave exports.
4. To address reverse causality, he uses instrumental variables (IV) → distance from slave trade ports as an instrument for slave exports (arguing geography predicts exposure to slave trade but not today’s GDP directly).
5. He shows the negative relationship remains strong even after controls and with IV.

## Main Findings
1. The slave trades had a large, long-term negative impact on Africa’s development.
2. The places in Africa where the most people were taken during the slave trade are the ones that are the poorest today, compared to other places that were less affected.

## Data Files
The data files uploaded to this repository include:
- borders_tribes.dbf
- borders_tribes.prj
- borders_tribes.sbn
- borders_tribes.sbx
- borders_tribes.shp
- borders_tribes.shp.xml
- borders_tribes.shx
- slave_trade_QJE.dta

## Shape Files:
These ESRI Shapefiles contain geographical information, such as boundaries, polygons, and other spatial data, necessary for spatial analysis.
They delineate the geographical regions under study, providing a framework for spatial analysis.
#def: an ESRI Shapefile is a simple, nontopological format for storing the geometric location and attribute information of geographic features.

## Data Tables:
The main data table is in Stata formata (.dta).
This dataset includes the target variable, representing the primary outcome or the phenomena of interest, along with corresponding independent variables. 
These independent variables encompass endogenous, exogenous, and instrumental variables, which play distinct roles in the analysis.

## Python Analysis:
The analysis was carried out using python.
Python libraries such as Pandas, NumPy, Matplotlib, and others were used to replicate the main ideas presented in Nathan Nunn's work.
