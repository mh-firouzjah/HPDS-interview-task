# HPDS-interview-task

In this project we have created simple FastAPI app that shows the memory info including total, used and free memory of the system that the code is running on it.  
This app will store the info in a sqlite database on a repitetive manner of each one minute string the app but ommiting the first commit which means after string the app 
it will take 2 minutes to start recording, this is on perpose in order to prevent duplication in case of a fast restart of the app.  
