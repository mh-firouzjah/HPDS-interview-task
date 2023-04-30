# HPDS-interview-task

In this project we have created simple FastAPI app that shows the memory info including total memory, used memory and free memory of the system on which the code is running.  
This program stores data in a sqlite database by interval of 1-minute starting the app but ommiting the first commit which means after string the app it will take 2 minutes to start recording, this is on perpose in order to prevent duplication in case of a fast restart of the app. the view takes an optional http request get parameter `n` which is expected to be an integer that indicates the number of recordes you want to obtain form the api. it will returns the last `n` records sorted by `created` field in descending order.

* I've used python 3.11 in the time of writing this project, but it should work for python version compatible with the 
packages listed in requirements.txt file.

### Initilization

- make sure using a new version of python3
- run `pip install -r requirements.txt` to install dependencies
- run `uvicorn web:app --reload`
- go to `127.0.0.1:8000/docs` to see the result. this is recommended to cisit this address as it contains more information
