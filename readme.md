# Beautifulsoup Requests Demo
Solutions of 'Decode A Web Page' from http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
It includes a list of exercises to introduce people to Python programming language.

This repository also includes the PDF file of the exercises.

## Step to install Beautifulsoup and Requests inside virtualenv
To install Beautifulsoup and Requests with Python3 in Ubuntu,
Create a folder and open terminal in it then write the following lines one by one in terminal:
```bash
 $ virtualenv -p python3 venv
 $ source venv/bin/activate
 (venv)$ python -m pip install --upgrade pip
 (venv)$ python -m pip install --upgrade setuptools
 (venv)$ pip install requests
 (venv)$ pip install beautifulsoup4
```

## Step to run nytimes.py inside venv
```bash
 Keep the nytimes.py inside the venv folder and write the following line in terminal
 (venv)$ python venv/nytimes.py
```


## Contributing
Everyone is welcome to contribute. Feel free to submit a pull request, issue or suggestion you may find relevant.

## Reference
The original exercise was created by Michele Pratusevich ([Personal_site(http://www.mprat.org/)])
and can be found [here](http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html).
