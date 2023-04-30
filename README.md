# HPDS-interview-task

In this project we have created simple FastAPI app that shows the memory info including total, used and free memory of the system that the code is running on it.  
This app will store the info in a sqlite database on a repitetive manner of each one minute string the app but ommiting the first commit which means after string the app 
it will take 2 minutes to start recording, this is on perpose in order to prevent duplication in case of a fast restart of the app. the view takes an optional http request get parameter `n` which is expected to be an integer that indicates the number 
of recordes you want to obtain form the api. it will return the last `n` records orderd decending based on record datetime.

* I've used python 3.11 in the time of writing this project, but it should work for python version compatible with the 
packages listed in requirements.txt file.

### Initilization

- make sure using a new version of python3
- run `pip install -r requirements.txt` to install dependencies
- run `uvicorn web:app --reload`
- go to `127.0.0.1:8000/docs` to see the result. this is recommended to cisit this address as it contains more information
