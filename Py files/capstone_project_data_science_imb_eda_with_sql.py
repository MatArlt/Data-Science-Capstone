# -*- coding: utf-8 -*-
"""Capstone project - Data Science IMB - EDA with SQL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HE2Md1Erg4gS1pMjkbiPFYORWM33lLfW
"""

!pip install sqlalchemy==1.3.9

!pip install ipython-sql
!pip install ipython-sql prettytable

# Commented out IPython magic to ensure Python compatibility.
# %load_ext sql

import csv, sqlite3
import prettytable
prettytable.DEFAULT = 'DEFAULT'

con = sqlite3.connect("my_data1.db")
cur = con.cursor()

!pip install -q pandas

# Commented out IPython magic to ensure Python compatibility.
# %sql sqlite:///my_data1.db

import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")

# Commented out IPython magic to ensure Python compatibility.
#DROP THE TABLE IF EXISTS

# %sql DROP TABLE IF EXISTS SPACEXTABLE;

# Commented out IPython magic to ensure Python compatibility.
# %sql create table SPACEXTABLE as select * from SPACEXTBL where Date is not null

# Commented out IPython magic to ensure Python compatibility.
# %sql PRAGMA table_info('SPACEXTABLE')

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT DISTINCT(Launch_Site) FROM SPACEXTABLE

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT * FROM SPACEXTABLE WHERE Launch_Site LIKE 'CCA%' LIMIT 5

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT SUM(PAYLOAD_MASS__KG_) AS 'Total payload mass carried by boosters launched by NASA (CRS)' FROM SPACEXTABLE WHERE Customer LIKE '%NASA%'

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT AVG(PAYLOAD_MASS__KG_) AS 'Average payload mass carried by booster version F9 v1.1' FROM SPACEXTABLE WHERE Booster_Version LIKE '%F9 v1.1%'

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT MIN(Date) AS 'Date of first succesful landing outcome in ground pad' FROM SPACEXTABLE WHERE Landing_Outcome LIKE '%Success (ground pad)%'

# Commented out IPython magic to ensure Python compatibility.
#List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# %sql SELECT Booster_Version FROM SPACEXTABLE WHERE Landing_Outcome = 'Success (drone ship)' AND PAYLOAD_MASS__KG_ BETWEEN 4000 AND 6000

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT Mission_Outcome, COUNT(*) AS 'Total' FROM SPACEXTABLE GROUP BY Mission_Outcome

# Commented out IPython magic to ensure Python compatibility.
# List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# %sql SELECT Booster_Version FROM SPACEXTABLE WHERE PAYLOAD_MASS__KG_ = (SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXTABLE)

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT DISTINCT(Landing_Outcome) FROM SPACEXTABLE

#List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
#Note: SQLLite does not support monthnames. So you need to use substr(Date, 6,2) as month to get the months and substr(Date,0,5)='2015' for year.

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT substr(Date, 6, 2) AS Month,Booster_Version,Launch_Site,Landing_Outcome FROM SPACEXTABLE WHERE substr(Date, 1, 4) = '2015' AND Landing_Outcome = 'Failure (drone ship)'

# Commented out IPython magic to ensure Python compatibility.
# Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order.
# %sql SELECT Landing_Outcome, COUNT(Landing_Outcome) AS COUNT FROM SPACEXTABLE WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY Landing_Outcome ORDER BY COUNT(Landing_Outcome) DESC

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT DISTINCT(launch_site) FROM SPACEXTABLE

# Commented out IPython magic to ensure Python compatibility.
# %sql SELECT DISTINCT(Mission_Outcome) FROM SPACEXTABLE