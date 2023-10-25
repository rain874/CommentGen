# CommentGen
CommentGen is a small python script that generates comment flags with a number via the cmd. 

# Requimes 
  - pip install win32api 
  - pip install win32clipboard
  - pip install terminaltables

# Description:
The python script generates a comment and a number and copies them to the clipboard. At the same time. 
About a config.ini a counter, projektid and developerid, specified. 

  Usage: set the counter and IDs over the config.ini
  
  exit = 0

  - TD = # ToDo: 037-231023-000001-7001

  - BD = # BugDoc: 037-231023-000004-7001

  - DC = # DocCOM: 037-231023-000005-7001   

it can be set in the IDE pyCharm colors for TODO. 

I call the script via a BATCH, the path must be adjusted accordingly.  


  1. Download 
  2. unpack into the desired directory
  3. Adjust path in the BATCH. 
  4. Adjust projektid, developerid config.ini. If necessary, adjust counter. 
  5. pyCharm - > Settings - Editor -> Create TODO.  

