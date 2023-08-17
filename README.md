# DataOpsExercise

--------------------------------------------------------
NB: The source files were inconsistent with inputs, 2016 - 2018 ("last 3 years starting from 2018" as stipulated in no 2 instruction)
do not contain values. However, I have run with 1996 - 1998 data per month (no data per day) instead since they presented way richer data to work with.

------------------------
ETL and preprocessing
----------------------

In Jupyter notebook, [ETL](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/ETL.ipynb):
- Station Inventory file is imported
- Station ID for Toronto is gotten from  Station Inventory file
- Station ID is used as input in script to download Weather data for Toronto

-------------------------------------------------------------
Download source files: Creation and execution of shell script
-------------------------------------------------------------
History of Git Bash commands run:

- wget
- cd Desktop/
- vi download.sh
- sh download.sh

- [download.sh](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/download.sh) contains wget command scripting to download file
- [Weather data](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/en_climate_monthly_ON_6158350_1840-2006_P1M.csv) downloaded

------------------------
ETL and preprocessing
----------------------

- In ETL, weather data is cleaned, pre-processed into years [1996](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/weather_1996.csv), [1997](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/weather_1997.csv), [1998](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/weather_1998.csv), and [merged](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/weather_all.csv) i.e 4 files 
- Other questions are also explored



--------------------------------------
Creation of S3 bucket using Terraform
--------------------------------------

- Launch Red Hat EC2 instance (Terraform server)
- Install Terraform
- Create user (terraform)
- Attach role with S3 Full access instead of access/secret keys (best pratice)
- Create [s3bucket.tf](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/s3bucket.tf) file with AWS provider and s3 resources
- terraform init
- terraform apply --auto-approve

- Upload 4 csv files to s3 bucket


-----------------------------------------------
create python environment and requirements file
-----------------------------------------------

- python -m venv env
- pip install pandas
- pip freeze > requirements.txt
- [requirements](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/requirements.txt) file created

- questions are answered in executable format
- year (1996 - 1998) should be entered as input variable from the command line as follows:

- python <pythonfile> <year>


--------------------
Push files to GitHub
--------------------
 
- git init
- git status
- vi .gitignore
- git add .
- git status
- git commit -m 'First commit'
- git remote add origin https://github.com/gregoryoffodum/DataOpsExercise.git
- git push origin master

-----------------------------
Containerization and Packaging
-----------------------------
- Create Ubuntu server (Docker)
- sudo apt update -y
- sudo apt install docker.io
- sudo usermod -aG docker ubuntu

- docker version
- docker info

Clone repo
-----------
- git clone https://github.com/gregoryoffodum/DataOpsExercise.git
- ls -la
- cd DataOpsExercise/
- chmod -R 755 DataOpsExercise/
- cd -

Create Docker file
------------------
- vi Dockerfile
- [Dockerfile](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/Dockerfile) created

Execution instructions
-------------------------------
- [question1](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/question1.py) and [question2](https://github.com/gregoryoffodum/DataOpsExercise/blob/master/question2.py) are python executables.
- year is input: 1996, 1997 or 1998
  
Build image and run question1
-------------------------------
- docker build -t question1 .
- docker run question1 <year>

Build image and run question2
-------------------------------
- docker build -t question1 .
- docker run question1 <year>

