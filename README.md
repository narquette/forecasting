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

3. Change install script to executable and run install file (you may be prompted to enter the sudo password for installing java)

```sh
cd ~/forecasting
chmod +x prereq_install.sh
./prereq_install.sh
conda activate forecasting
```

4. Run stream list application

```sh
  streamlit run app.py
```

# Getting Started (Docker)

1. Ensure Docker Desktop is running
2. Pull docker image
```cmd
   docker pull narquette/claims
```
3. Start up docker image
```cmd
  docker run -it --rm -p 8888:8888 narquette/claims 
```
4. Run Jupyter Notebook
```sh
  ./run_notebook.sh
```
5. Copy and paste url with tokens into browser
6. Navigate to Code / Claims EDA.ipynb
7. Run all cells

# Folder Overview


