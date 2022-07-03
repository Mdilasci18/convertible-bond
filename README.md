# Convertible Bond Research

This repository includes all the code and analysis of convertible bond project.

## Brief Introductions of each file
 - This project work mainly contains 8 jupyter notebooks. 
1. [Data Processing.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Data%20Processing.ipynb): Works of data pre-processing and data cleaning. Reorgnizing data into easy-to-use data structure.
2. [Sina Finance.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/SinaFinance.ipynb): Web crawler to collect convert price and interest rate from sina finance website.
3. [Pricing Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/PricingModel.ipynb): Implementation of convertible bond pricing model.
4. [Run Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Run%20Model.ipynb): Monte Carlo simulation on dataset.
5. [Data Analysis.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Data%20Analysis.ipynb): Integrated works of data analysis, data visulization and factors design.
6. [ML Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/ML%20Model.ipynb): Implementation of machine learning algorithms to improve the performance of overnight strategy.
7. [Backtest.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Backtest.ipynb): Backtesting framework designed for convertible bond and stock trading.
8. [Strategy.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Strategy.ipynb): Integrated works of strategy implementation, performance statistics and visualization.

Detailed introductions can be found at the beginning of each notebook.

 - [backtest_config.py](https://github.com/rookieyifan/convertible-bond/blob/main/backtest_config.py): config file including backtest setting parameters.

## Usage Instructions
### Data Path
+ input raw data path: `export/scratch/for_yifan/`
+ output data path: `export/scratch/for_yifan/research/`

Note: input and output data path are explicitly set at the beginning of each notebook(if needed). 

### Data Exploration & Strategy Design Purpose 
If you have access to the input and output path above and just want to run the research code (data analysis and strategy backtesting part), you can play with [Data Analysis.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Data%20Analysis.ipynb), [ML Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/ML%20Model.ipynb) and  [Strategy.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Strategy.ipynb), where I finished most of my research work.

If new data need to be added, please refer to the next instruction.

### Data Generation Purpose
If you want to generate new output data(when new input data is added/have no access to the output path), please follow the instructions below. Please make sure all the **input files** exist in your **input raw data path** before you run the code for each step and you can expect that the **output files** will be generated in your **output data path**.

+ [Data Processing.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Data%20Processing.ipynb)
    + input files: `data`, `stock_data` and `index_data`
    + output files: `cbond_info.csv`, `cbond_price.csv`, `bond_data.pkl`, `stock_data.pkl`, `stock_data_raw.pkl`, etc
    + instructions: No modifications required. 
    + expected running time: less than 5 mins.

+ [Sina Finance.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/SinaFinance.ipynb)
    + input files: `cbond_info.csv`
    + output files: `sina_cvprice.csv`, `sina_rate.csv`
    + instructions: No modifications required.
    + expected running time: around 10 mins, depends on Internet stability and sleep time(default 1s) for each bond.
    
+ [Run Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Run%20Model.ipynb)
    + input files: `cbond_info.csv`, `cbond_price.csv`, `sina_rate.csv`, `cbond_data.pkl`, `stock_data.pkl`
    + output files: `model_para.pkl`, `model_hidden_vol.pkl`, `model_V3`
    + instructions: If new data is added, please set ``read==False`` in this notebook(3 places) thus the code will generate and rewrite `model_para.pkl`, `model_hidden_vol.pkl` and `model_V3` . 
    + expected running time: 3 mins for `model_para.pkl`, less than 10 mins for `model_hidden_vol.pkl`, **more than 1 day** for `model_V3`.
+ [Data Analysis.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Data%20Analysis.ipynb)
    + input files: `cbond_info.csv`, `cbond_price.csv`, `stock_price.csv`, `'model_V3'`
    + output files: `neg_premium.csv`, `ovnt_arb.csv`, `ml_model_data.csv`, `pricing.csv`
    + instructions: No modifications required. Please feel free to do further research based on the notebook.
    + expected running time: less than 3 mins.
+ [ML Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/ML%20Model.ipynb)
    + input files: `ml_model_data.csv`
    + output files: `ovnt_ml.csv`
    + instructions: No modifications required. Please feel free to do further research based on the notebook.
    + expected running time: 10 mins.
+ [Strategy.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Strategy.ipynb)
    + input files: `neg_premium.csv`, `ovnt_arb.csv`, `ovnt_ml.csv`, `pricing.csv`
    + instructions: No modifications required. Please feel free to do further research based on the notebook.
    + expected running time: 10 mins.

### Package-like Notebook
No need to run or modify these two notebooks unless further development required.
+ [Pricing Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/PricingModel.ipynb): Implementation of convertible bond pricing model API. Only imported and used in [Run Model.ipynb]([http://gitlab.intern.dtl/yifan/convertible-bond/blob/master/Run%20Model.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Run%20Model.ipynb)
+ [Backtest.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Backtest.ipynb): Backtest framework. Only imported and used in [Strategy.ipynb](https://github.com/rookieyifan/convertible-bond/blob/main/Strategy.ipynb)
    +  input files: `cbond_info.csv`, `cbond_price.csv`, `cbond_data.pkl`, `stock_data.pkl`, `stock_data_raw.pkl`
