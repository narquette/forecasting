# Forecasting (Streamlit, fbprophet)
A [streamlit](https://www.streamlit.io/) application that uses Facebook's timeseries module [fbprophet](https://facebook.github.io/prophet/docs/quick_start.html#python-api) to forecast various healthcare care executive key performance indicators (KPI's) such as average length of stay, etc.

# Pre-requisites

Option 1 - WSL (Windows Sub-Linux)

1. Enable [WSL](https://winaero.com/blog/enable-wsl-windows-10-fall-creators-update/) in windows 
2. Install Ubuntu App from Windows Store
3. Create Login and sudo password for Linux

Option 2 - Docker Desktop

1. Install [docker desktop - windows](https://docs.docker.com/docker-for-windows/install/)

# Getting Started (WSL)

1. Open Windows Sub Linux (Ubuntu App)

2. Run the following command

```sh
git clone https://github.com/narquette/forecasting
```

3. Change install script to executable and run install file

```sh
cd ~/forecasting
chmod +x prereq_install.sh
./prereq_install.sh
conda activate forecast
```

4. Run stream list application

```sh
  streamlit run code/app.py
```
5. Copy url and paste into the browser

# Getting Started (Docker)

1. Ensure Docker Desktop is running
2. Pull docker image
```cmd
   docker pull narquette/forecasting
```
3. Start up docker image
```cmd
  docker run -it --rm -p 8501:8501 narquette/forecasting 
```
4. Run Streamlit app
```sh
  streamlit run app.py
```
5. [Launch App](http://127.0.0.1:8501) or copy url into browser (http://127.0.0.1:8501)
6. Enter password - kpi2020
7. Interact with side bars (change kpi or facility)

# Folder Overview

Code 
- Where all the application code lives

Data
- Data needed to run the application

