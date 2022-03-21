## Gait Analysis

To get started, 

1. clone the repository
2. cd into the root folder of your repository
3. create a folder called `ignoredFiles`

```
mkdir ignoredFiles
```

4. create a virtual environment (if you use venv, do the following; otherwise look up which library you want to use instead to create a virtual environment on your local machine)

```
python3 -m venv venv
```

5. activate your virtual environment (if you use venv, do the following; otherwise look up which library you want to use instead to create a virtual environment on your local machine)

```
source venv/bin/activate
```

6. now that your virtual environment is activated, install the packages from `requirements.txt`

```
pip3 install -r requirements.txt
```

7. now that all dependencies are installed, you can start the streamlit application

```
streamlit run app.py
```

8. check out [streamlit.io](https://streamlit.io/), it is an amazing library

