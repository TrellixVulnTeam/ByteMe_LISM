# ByteMe, Unified Event Sharing Platform

Please don't forget to write README.md files for others to understand..


## Tasks

* UI
* Server
* DB


## Things to be careful in the repo!!

* Do not include build files in the repo, please change .gitignore so that it will ignore the whole folder or file
* When changing one part, please make sure no one else will get effected, if it is crucial let them know
* When working on parts where intersect with other works, please try to specify in the Trello's description field



## How to use the server
### Installation
1. Install django   
`pip install django==1.11`    

2. Install djano rest framework   
`pip install djangorestframework`   
`pip install markdown`    
`pip install django-filter`   

3. Install httpie - for test API    
`pip install --upgrade httpie`    
> You can also use curl to test it    
-----   

### Running
1. cd server/byteme   
run `python manage.py runserver`    

##### View Admin website
1. use browser, url: http://127.0.0.1:8000/admin/   
> account:  admin   
> password: password@   

##### Test the API

1. Browse API:
- Name: http://127.0.0.1:8000/api/v1/event/browse?type=   
- Method: GET   
- Description: Browse the events by user or all events    
- Parameters: type(String/required) value: attending or created or all          
- Example: http://127.0.0.1:8000/api/v1/event/browse?type=all                   
- Response:     
```
{
    "Events": [
        {
            "abstract": "Test",
            "attendant": [
                "Wuharlem",
                "User1"
            ],
            "creater": "Wuharlem",
            "details": "details",
            "identifier": "6207788a-3530-40da-be59-8bc41124c750",
            "place": "KAIST",
            "req": "non",
            "speaker": "Zombie",
            "tags": [
                "AI  9.87",
                "ML  10.00",
                "SE  0.87"
            ],
            "time": "2018-11-03 03:01:00+00:00",
            "title": "test"
        },
        {
            "abstract": "BlaBla",
            "attendant": [],
            "creater": "Wuharlem",
            "details": "Blabla",
            "identifier": "ec8ba317-2c50-4298-a2d3-086b47541758",
            "place": "Kaist",
            "req": "non",
            "speaker": "Zombie",
            "tags": [],
            "time": "2018-11-03 03:01:00.914138+00:00",
            "title": "Zombies"
        }
    ],
    "Response": "List_events"
}
```        


2. Add Event API:
- Name: http://127.0.0.1:8000/api/v1/event/add
- Method: POST
- Description: Request to add the event
- Request json interface:  
```
{    
    "Request": "Add_event",     
    "User": {   
        "email": "user1@gmail.com",      
        "pw_hash": "XXA83jd3kljsdf",    
        "ip": "143.248.143.29"  
    },      
    "speaker":{     
        "name": "Zombie"   
    },      
    "Event": {      
        "abstract": "BlaBla",       
        "place": "Kaist",       
        "time": "2018-11-03 03:01:00.914138+00:00",         
        "title": "Zombies",         
        "details": "Blabla",
        "poster_image": "imageimage" 
    }       
}     
```
- Response json interface:   
HTTP/1.0 202 Accepted  
```
{       
    "Events": {     
        "id": "51dca183-1dd7-4342-ae22-a10efe1d9d3f",       
        "status": "wait",       
        "title": "Zombies"      
    },      
    "Response": "Add_Event"     
}           
```
HTTP/1.0 400 Bad Request                
```
{       
    "Response": "Add_Event",        
    "status": "please check the response json"      
}       
```

3. Delete Event:       
- Name: http://127.0.0.1:8000/api/v1/event/delete/<event_id>
- Method: DELETE
- Description: Delete request to add/mod/del the event
- Parameters: event_id(UUID/required)       
- Example: http://127.0.0.1:8000/api/v1/event/delete/aa6634c6-b10c-4339-b2c4-3e4baf49880e               
- Response json interface:     
HTTP/1.0 202 Accepted  
```
{
    "Response":"Delete_event",
    "Event":{
        "id":"aa6634c6-b10c-4339-b2c4-3e4baf49880e",
        "title":"Superman",
        "status":"processing"}
    }
}
```

4. Modify Event:       
- Name: http://127.0.0.1:8000/api/v1/event/modify/<event_id>
- Method: DELETE
- Description: Delete request to add/mod/del the event
- Parameters: event_id(UUID/required)       
- Example: http://127.0.0.1:8000/api/v1/event/modify/aa6634c6-b10c-4339-b2c4-3e4baf49880e       
- Request json interface:  
```
{
    "Request": "Modify_event",
    "User": {   
        "email": "user1@gmail.com",      
        "pw_hash": "XXA83jd3kljsdf",    
        "ip": "143.248.143.29"  
    },   
    "Event": {
        "abstract": "Superman is the best",
        "place": "Kaist",
        "time": "2018-11-03 03:01:00.914138+00:00",         
        "title": "Superman",         
        "details": "Blabla",
        "poster_image": "imageimage",
    }
}   
```             
- Response json interface:     
HTTP/1.0 202 Accepted        
```
{
    "Response":"Modify_Event",
    "Events":{
        "abstract":"Superman is the best",
        "place":"Kaist",
        "time":"2018-11-03 03:01:00.914138+00:00",
        "title":"Superman",
        "details":"Blabla",
        "poster_image":"imageimage"
    },
    "status":"processing"
}
```

5. Approve Event request:       
- Name: http://127.0.0.1:8000/api/v1/event/request/approvel/<event_id>
- Method: POST
- Description: Request to delete the event      
- Parameters: event_id(UUID/required)  *need to use form to pass!!
- Example: http://127.0.0.1:8000/api/v1/event/request/approvel/aa6634c6-b10c-4339-b2c4-3e4baf49880e               
- Response json interface:        
```
HTTP/1.0 205 Reset Content  
{       
    "Response": "Delete_event",        
    "Event": {      
        "id": aa6634c6-b10c-4339-b2c4-3e4baf49880e,      
        "title": "Zombies",     
        "status": "wait"             
    }                   
}           
```


-----
### Model
If you change the code in the model, you need to run:   
`python manage.py makemigrations`   
`python manage.py migrate`    
    
this is for modifying the table in sqlite   
