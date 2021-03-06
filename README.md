## Python project of a time series data analysis and forecasting web app 

<br>

>### **What is this project?**
>   
>A time series data analysis and forecasting containerized web application written in Python and presented in a dashboard format

<br>

>### **What Python libraries are used in this project?**
> - dash
> - dash_core_components
> - dash_html_components
> - pandas
> - plotly
> - statsmodels

<br>

>### **What mathematical tools are used in this project?**
> - Hodrick-Prescott filter
> - Error trend seasonality decomposition
> - Simple moving average
> - Exponentially weighted moving average

<br>

>### **How to run this project?**
>#### 1) Install Docker
>Open the Ubuntu terminal and run the following commands:
>
>     sudo apt update
>     sudo apt install apt-transport-https ca-certificates curl software-properties-common
>     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
>     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
>     sudo apt update
>     sudo apt install docker-ce
>#### 2) Build Docker image
>Open the Ubuntu terminal in the Python project folder and run the following commands:
>
>     sudo docker build --tag image .
>#### 3) Run Docker image
>After building the Docker image, run the following commands:
>
>     sudo docker run -it -v ${pwd}/src:/src -p 80:80 --rm image

<br>

>### **Project screenshot**
>
>![screenshot](https://github.com/EduardoMatosRodrigues/TimeSeriesDataAnalysisAndForecastingWebApp/raw/master/src/screenshots/screenshot-v1.00.png)