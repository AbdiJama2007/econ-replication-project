#Project name: Building a research profile through an econ paper replication
###Author: Abdikhaliq Jama Mohamed
###Start date: 2025-09-15
###Last update: 2025-09-15
###Objective: To replicate Nathan Nunn's 2008 paper "The Long-Term Effects of Africa's Slave Trades" published in The Quarterly Journal of Economics
###This replication emphazises the core concepts of Nunn's research, employing spatial and statistical analysis
###This replication is part of a broader initiative to enhance my research profile in economics through practical application of econometric techniques
###Date Files: the project utilizes ESRI Shapefiles for spatial data analysis and Stata data file (slave_trade_QJE.dta) for statistical analysis
###Python analysis: Using libraries like Pandas and NumPy, the project replicates key ideas of Nunn's work. Detailed comments are included to explain each step of the analysis
# check git and python
git --version
python3 --version    # or `python --version` on Windows if python maps to Python 3
# remove the wrong placeholder remote
git remote remove origin

# add the correct remote (your real repo)
git remote add origin https://github.com/AbdiJama2007/econ-replication-project.git

# set your branch name to main (safe even if it's already main)
git branch -M main

# push your code to GitHub
git push -u origin main
