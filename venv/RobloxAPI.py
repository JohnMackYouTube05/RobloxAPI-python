#Roblox API Python Wrapper
#by JohnMackYT
import requests #Literally the backbone to this program, apart from api.roblox.com
import json
import warnings
import os
import getpass
def AuthAPI(cookie):
    """STORES YOUR COOKIE IN A FILE LOCALLY ON YOUR PC TO USE WITH THE API. THIS COOKIE ONLY GOES TO ROBLOX, AND YOUR COMPUTER'S HARD DRIVE. NOWHERE ELSE."""
    os.mkdir(rf"C:\Users\{getpass.getuser()}\AppData\Roaming\RobloxAPI")
    try:
        # Create  Directory  MyDirectory 
        os.mkdir(rf"C:\Users\{getpass.getuser()}\AppData\Roaming\RobloxAPI")
        #print if directory created successfully...
        print("Directory Created") 
    except FileExistsError:
        ##print if directory already exists...
        print("Cookie Stored")
    else:
        """hwee"""
    with open(rf"C:\Users\{getpass.getuser()}\AppData\Roaming\RobloxAPI\cookies.txt", 'a') as cookies:
        c = "{'.ROBLO_SECURITY': " + cookie + "}"
        cookies.write(c)
        cookies.close()

def readCookie():
    with open(rf"C:\Users\{getpass.getuser()}\AppData\Roaming\RobloxAPI\cookies.txt", 'r') as cookies:
        c = cookies.read()
        cookies.close()
        return c
class Users:
    """all functions for the user API"""
    def getUserStatus(UserId):
        """Gets the status string for the inputted user ID."""
        url = f"https://users.roblox.com/v1/users/{UserId}/status"
        resp = requests.get(url)
        js = json.loads(resp.text)
        statusString = str(js)[12:len(str(js))-2]
        return statusString
    def getUsernameHistory(UserId):
        """Gets the username history of the inputted user ID, and returns a dictionary object containing said history."""
        url = f"https://users.roblox.com/v1/users/{UserId}/username-history"
        r = requests.get(url)
        j = json.loads(r.text)
        data = j['data']
        return data
    def getUserInfo(UserId):
        """Gets detailed user information by the inputted ID."""
        url = f"https://users.roblox.com/v1/users/{UserId}"
        r = requests.get(url)
        j = json.loads(r.text)
        displayName = j['displayName']
        name = j['name']
        uid = j['id']
        isBanned = j['isBanned']
        joinDate = j['created']
        description = j['description']
        return displayName,name,uid,isBanned,joinDate,description
    def searchUsers(keyword, limit):
        """Searches for users by keyword. Limit variable can be 10, 25, 50, or 100, representing how many users this function can give back, if there is enough to fill that many usernames."""
        url = f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit={limit}"
        acceptableLimits = (10, 25, 50, 100)
        if limit in acceptableLimits:
            r = requests.get(url)
            j = json.loads(r.text)
            data = j['data']
            return data
        else:
            if limit == None:
                warnings.warn('You did not specify a limit. The default limit is 100, and other valid limits are 10, 25, and 50.')
                limit = 100
                r = requests.get(url)
                j = json.loads(r.text)
                data = j['data']
                return data
            else:
                e = Exception("You have entered an invalid limit, please enter a limit of 10, 25, 50, or 100. If you don't enter a limit at all however, the default is 100.")
        return
    def getUserByUsername(username, excludeBannedUsers=None):
        """Gets the user info for the specified username. Default for excluding banned users is false."""
        if excludeBannedUsers == None:
            excludeBannedUsers = False
        url = "https://users.roblox.com/v1/usernames/users"
        js = {
	"usernames": [
		f"{username}"
                
	],
	"excludeBannedUsers": excludeBannedUsers
        }
        r = requests.post(url, json=js)
        j = json.loads(r.text)
        data = j['data']
        return data

class Games:
    def getGameInfo(placeId):
        """Retrieves info about a game with the inputted place ID."""
        url = f"https://games.roblox.com/v1/games/multiget-place-details?placeIds={placeId}"
        cookies = readCookie()
        r = requests.get(url, cookies=cookies)
        j = json.loads(r.text)
        return jc
        
        
        
        
        
                
                    
                
            
            
        
        
        
        
        
        
