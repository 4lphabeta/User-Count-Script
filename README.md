# User-Count-Script
A Python script that cuts user count times down from 1-2 hours to 3 minutes tops. The script checks all user folders for the last modified date of the VorCfg user file to see when it was last used. Users with a VorCfg modified date of over 6 months are deemed inactive users.
The output is as a CSV spreadsheet which should be double checked and sent to accounts.


The file should be placed inside the Vortex Master folder if available.
Make sure to change the file paths on line #3 and #5 as indicated in the file to match the server.

IMPORTANT: When editing the file path, you MUST note the structure used and inclue the relevant FORWARD SLASHES (not backslash) and ASTERISK. Python uses forward slashes to denote file path, the opposite to what Windows uses. If the server does not have a user counts folder, one needs to be created.


When the script runs it will create a 'date.csv' file, this can be ignored as it is used to get accurate system dates as some servers did not function correctly with direct date pulls from the system time.

The script will be complete when the batch file shows: =================DONE=================
