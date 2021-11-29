# photos

### 26th Nov. 2021

## Author  
  
[Elizabeth Gikonyo]
  
# Description  
This is a photo gallery web application that showcases incredible pictures. Users can view photos uploaded by the website admin. Users can also view photos based on the location, by clicking on the listed locations in the navbar dropdown as well as by category. They can also copy the link to a photo to paste.
  
##  Live Link  
 
  
## Screenshots 

###### ADMIN page
 
 ###### HOME results
 
 ###### SEARCH Details 
 
 
## User Story  
  
* View different photos from the galllery 
* Click a single image to expand it and view the details of that photo  
* Search for images by different categories.   
* Copy a link to the photo.  
* Filter photos based on the location.  
  

  
## Setup and Installation  
  
## Clone the repository:  
 
## Navigate into the folder and install requirements  

## Install and activate Virtual  
  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations photos
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bug


## License

### MIT LICENCE

Copyright (c) 2021 lizgi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
