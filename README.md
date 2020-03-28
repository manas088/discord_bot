#discord_bot

Discord bot implementation    

This is hosted on AWS Server using Supervisor as a service  
**Supported Commands-**  
**#google search_word**- This will google "search_word" and in return will provide 5 links  
**#recent search_word**- This will return all the recent searches matching the search_word  
**Steps to Run**    
-Download the Repo  
-Make virtualenv using python 3.6  
-Install requirements.txt  
-Install postgres  
-create database and table (table name "search_history" column- id,search_word,user_name) in postgres  
-overwrite GOOGLE_API_TOKEN,DISCCORD_BOT_TOKEN,DATABASE_NAME in constants.py  
-Run app.py  

