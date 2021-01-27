#Roblox API Python Wrapper
#by JohnMackYouTube05
import requests #Literally the backbone to this program, apart from api.roblox.com
import json
import warnings
import os
import getpass

global cookie
cookie = {'.ROBLOSECURITY': "your cookie here"}
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
    def searchUsers(keyword, limit=None):
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
        r = requests.get(url, cookies=cookie)
        j = json.loads(r.text)
        return j
class Groups:
    def getGroupInfo(groupId):
        """Gets group details for the specified group ID."""
        url = f"https://groups.roblox.com/v1/groups/{groupId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
class Catalog:
    def Categories():
        """Returns all possible categories."""
        cat = {
    	    "Featured": 0,
    	    "All": 1,
    	    "Collectibles": 2,
    	    "Clothing": 3,
    	    "BodyParts": 4,
    	    "Gear": 5,
    	    "Models": 6,
    	    "Plugins": 7,
	        "Decals": 8,
    	    "Audio": 9,
    	    "Meshes": 10,
	        "Accessories": 11,
	        "AvatarAnimations": 12,
	        "CommunityCreations": 13,
	        "Video": 14,
	        "Recommended": 15
        }
        return cat
    def Subcategories():
        """Returns all possible subcategories."""
        subcat = {
    	"Featured": 0,
    	"All": 1,
    	"Collectibles": 2,
    	"Clothing": 3,
    	"BodyParts": 4,
    	"Gear": 5,
    	"Models": 6,
    	"Plugins": 7,
    	"Decals": 8,
    	"Hats": 9,
    	"Faces": 10,
    	"Packages": 11,
    	"Shirts": 12,
    	"Tshirts": 13,
    	"Pants": 14,
    	"Heads": 15,
    	"Audio": 16,
    	"RobloxCreated": 17,
    	"Meshes": 18,
    	"Accessories": 19,
    	"HairAccessories": 20,
    	"FaceAccessories": 21,
    	"NeckAccessories": 22,
    	"ShoulderAccessories": 23,
    	"FrontAccessories": 24,
    	"BackAccessories": 25,
    	"WaistAccessories": 26,
    	"AvatarAnimations": 27,
    	"ClimbAnimations": 28,
    	"FallAnimations": 30,
    	"IdleAnimations": 31,
	    "JumpAnimations": 32,
	    "RunAnimations": 33,
    	"SwimAnimations": 34,
    	"WalkAnimations": 35,
    	"AnimationPackage": 36,
    	"Bundles": 37,
    	"AnimationBundles": 38,
	    "EmoteAnimations": 39,
	    "CommunityCreations": 40,
	    "Video": 41,
	    "Recommended": 51
    }
        return subcat

    def listExclusiveItems(appStore):
        """Returns all exclusive items for 1 of 4 app stores; Xbox, Amazon, Google Play or iOS."""
        appStores = ('Xbox', 'Amazon', 'iOS', 'Google Play')
        if appStore not in appStores:
            Exception(f"No valid app store was provided. Valid choices are {appStores}.")
        else:
            url = f"https://catalog.roblox.com/v1/exclusive-items/{appStore}/bundles"
            r = requests.get(url)
            j = json.loads(r.text)
            return j['data']
    def showOwnedBundles(userId):
        """Returns a list of all bundles owned by a specified ID. The user MUST have a public inventory or this function won't work."""
        url = f"https://catalog.roblox.com/v1/users/{userId}/bundles?limit=100&sortOrder=Asc"
        r = requests.get(url)
        j = json.loads(r.text)
        return j['data']
    def showUserInventory(userId, assetType):
        """Returns the user inventory from the specified user ID. Player MUST have a public inventory for this to work."""
        validTypes = {'Image', 'TShirt', 'Audio', 'Mesh', 'Lua', 'Hat', 'Place','Model','Shirt','Pants','Decal','Head','Face', 'Gear', 'Badge', 'Animation', 'Torso', 'RightArm', 'LeftArm', 'LeftLeg', 'RightLeg', 'Package', 'GamePass', 'Plugin','MeshPart','HairAccessory', 'FaceAccesory', 'NeckAccessory', 'ShoulderAccessory', 'FrontAccessory', 'BackAccessory', 'WaistAccessory', 'ClimbAnimation', 'DeathAnimation', 'FallAnimation', 'IdleAnimation', 'JumpAnimation', 'RunAnimation', 'SwimAnimation', 'WalkAnimation', 'PoseAnimation', 'EarAccessory', 'EyeAccessory', 'EmoteAnimation', 'Video'}
        if assetType not in validTypes:
            Exception(f"You have entered an invalid asset type to show inventory for. Currently, the valid asset types are: {validTypes}")
            return
        else:
            url = f"https://inventory.roblox.com/v2/users/{userId}/inventory?assetTypes={assetType}&limit=100&sortOrder=Desc"
            r = requests.get(url)
            j = json.loads(r.text)
            return j['data']






        
        
        
        
                
                    
                
            
            
        
        
        
        
        
        
