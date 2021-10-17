# Github Repository Finder - with sample dataset

## Introduction
This notebook gives information about the function used to fetch Github repositories based on a keyword and a determined timeframe starting from the day of fetching.

## Running instruction

### Requirements:
1. Generate your own Github Token: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2. Save your token as an enviroment variable, remember to name the variable as 'GITHUBTOKEN': [Configuring Environment Variables](https://tilburgsciencehub.com/building-blocks/store-and-document-your-data/store-data/environment-variables/) 
3. Make sure you have installed the following packages in python: requests, math, datetime, dateutil, csv, pandas, json, os, time. Installation instruction can be found at [Python website](https://www.python.org/) 

## Function structure:
GRF collects data by operating 4 separate steps accquired via 4 functions: find_repo, export_repo_list; save_column; save_dt. The working of these functions is illustrated in the following diagram:


![Fig1 GitHub Repository Finder components](docs/Function_documentation/fig1-grf-component-diagram.png "GitHub Repository Finder components")

## Sample dataset:
A sample dataset was obtained by using the following command:
```
grf("python", 3, 8)
```
+ Detailed datasheet can be found here: [Datasheet for GRF sample dataset](docs/Datasheet_for_GitHub_Repository_Finder_Sample_Dataset.pdf)
+ Below is a preview of the final dataset:


```python
import pandas as pd
pd.read_csv("data/dt.csv", delimiter= ";",nrows=10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>url</th>
      <th>language</th>
      <th>created</th>
      <th>stars</th>
      <th>watch</th>
      <th>forks</th>
      <th>readme</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>416977797</td>
      <td>AI_Project</td>
      <td>https://github.com/pbl4team/AI_Project</td>
      <td>Python</td>
      <td>2021-10-14T03:37:01Z</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>Project AI Systeam - Computer Vision with pyth...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>416995331</td>
      <td>python</td>
      <td>https://github.com/Cam0411/python</td>
      <td>Python</td>
      <td>2021-10-14T05:06:00Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>python</td>
    </tr>
    <tr>
      <th>2</th>
      <td>416908634</td>
      <td>Python</td>
      <td>https://github.com/psplendid61/Python</td>
      <td>NaN</td>
      <td>2021-10-13T21:53:43Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>416963376</td>
      <td>python</td>
      <td>https://github.com/iAMSe/python</td>
      <td>NaN</td>
      <td>2021-10-14T02:28:55Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>python</td>
    </tr>
    <tr>
      <th>4</th>
      <td>416996896</td>
      <td>python</td>
      <td>https://github.com/rakeshk67/python</td>
      <td>NaN</td>
      <td>2021-10-14T05:13:42Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>python</td>
    </tr>
    <tr>
      <th>5</th>
      <td>416961346</td>
      <td>python</td>
      <td>https://github.com/colddie/python</td>
      <td>NaN</td>
      <td>2021-10-14T02:19:55Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>416990435</td>
      <td>Python</td>
      <td>https://github.com/mahdidahmani/Python</td>
      <td>Python</td>
      <td>2021-10-14T04:41:11Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>416952467</td>
      <td>python</td>
      <td>https://github.com/grace-th3/python</td>
      <td>Python</td>
      <td>2021-10-14T01:38:42Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>416928589</td>
      <td>Python</td>
      <td>https://github.com/Cheung-man/Python</td>
      <td>NaN</td>
      <td>2021-10-13T23:36:27Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>416935834</td>
      <td>python</td>
      <td>https://github.com/mygithuang/python</td>
      <td>NaN</td>
      <td>2021-10-14T00:15:25Z</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>python mygithuang</td>
    </tr>
  </tbody>
</table>
</div>



***

# Function source code:

Source code and detailed function documentation are available at: [GRF Source code](https://github.com/thtbui/github-repository-finder/tree/main/src) 
