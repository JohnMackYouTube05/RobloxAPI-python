#Roblox API Python Wrapper
#by JohnMackYouTube05
import requests #Literally the backbone to this program, apart from api.roblox.com
import json
import warnings
import os
import getpass
from PIL import Image
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
    def getGameProductInfo(universeId):
        url = f"https://games.roblox.com/v1/games/games-product-info?universeIds={universeId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j['data']
    def getVotes(universeId):
        url = f"https://games.roblox.com/v1/games/1700523381/{universeId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
    def searchGamesByKeyword(keyword):
        url = "https://games.roblox.com/v1/games/list?model.keyword={keyword}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j['games']


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
class Badges:
    def getBadgeInfo(badgeId):
        """Gets badge information for the specified badge ID."""
        url = f"https://badges.roblox.com/v1/badges/{badgeId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
    def updateBadgeInfo(badgeId, name, description, badgeEnabled):
        """Sets badge information to the specified parameters. You must be the creator of the badge to modify, or else you won't be able to modify it."""
        parameters = {
	    "name": name,
	    "description": description,
	    "enabled": badgeEnabled
        }
        url = f"https://badges.roblox.com/v1/badges/{badgeId}"
        r = requests.patch(url, params=parameters, cookies=cookie)
        j = json.loads(r.text)
        return j
    def getBadgesByGame(universeId, limit=None):
        url = f"https://badges.roblox.com/v1/universes/{universeId}/badges?limit={limit}&sortOrder=Asc"
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
    def getBadgesFromUser(userId, limit=None):
        """Returns a set amount of badges that the specified user has been awarded."""
        url = f"https://badges.roblox.com/v1/users/{userId}/badges?limit={limit}&sortOrder=Desc"
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
    def getBadgeAwardedTime(userId, badgeId):
        """Returns the time that the specified badge ID was awarded to the specified user ID."""
        url = f"https://badges.roblox.com/v1/users/{userId}/badges/awarded-dates?badgeIds={badgeId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j['data']
class Legacy:
    def getRobux():
        """Returns the Robux balance for the currently authenticated user."""
        url = "https://api.roblox.com/my/balance"
        r = requests.get(url, cookies=cookie)
        j = json.loads(r.text)
        return j
    def userOwnsAsset(userId, assetId):
        """Gets whether the specified user owns the specified asset, and returns True or False."""
        url = f"https://api.roblox.com/ownership/hasasset?assetId={assetId}&userId={userId}"
        r = requests.get(url)
        if r.text == 'true':
            return True
        else:
            return False
    def getAssetInfo(assetId):
        """Gets asset info for specified ID. User must have permissions to manage the asset or function won't work."""
        url = f"https://api.roblox.com/assets/{assetId}/versions"
        r = requests.get(url, cookies=cookie)
        j = json.loads(r.text)
        return j
    def getGroups(userId):
        """Get a user's joined groups"""
        url = f"http://api.roblox.com/users/{userId}/groups"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
    def getDeviceInfo():
        """Gets the device info of the current device"""
        url = "https://api.roblox.com/reference/deviceinfo"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
class Develop:
    def getPluginInfo(pluginId):
        """Gets the information of the specified plugin ID."""
        url = f"https://develop.roblox.com/v1/plugins?pluginIds={pluginId}"
        r = requests.get(url)
        j = json.loads(r.text)
        return j['data']
    def getUniverses(limit=None):
        """Gets universes that the logged in user has made."""
        url = f"https://develop.roblox.com/v1/user/universes?limit={limit}&sortOrder=Desc"
        if limit in (10, 25, 50):
            r = requests.get(url, cookies=cookie)
            j = json.loads(r.text)
            return j
        else:
            limit = 50
            r = requests.get(url, cookies=cookie)
            j = json.loads(r.text)
            return j
    def getRobloxBadges(userId):
        """Get ROBLOX-created badges the specified user has earned, such as the Bricksmith badge."""
        url = f"https://accountinformation.roblox.com/v1/users/{userId}/roblox-badges"
        r = requests.get(url)
        j = json.loads(r.text)
        return j
    def universePayoutHistory(universeId, startDate, endDate):
        """Gets payout history of the specified universe ID. You must have edit permissions on the universe for this function to work properly."""
        url = f"https://engagementpayouts.roblox.com/v1/universe-payout-history?endDate={endDate}&startDate={startDate}&universeId={universeId}"
        r = requests.get(url, cookies=cookie)
        j = json.loads(r.text)
        return j
class Thumbnails:
    def downloadAssetThumbnail(assetId, size, isCircular=None):
        "Downloads the thumbnail for the specified asset."
        url = f"https://thumbnails.roblox.com/v1/assets?assetIds={assetId}&format=Png&isCircular={isCircular}&size={size}"
        if isCircular == None:
            isCircular = False #Default
        validSizes = ('30x30', '42x42', '50x50', '60x62', '75x75', '110x110', '140x140', '150x150', '160x100', '160x600', '250x250', '256x144','300x250','304x166','384x216','396x216','420x420','480x270','512x512','576x324','700x700','728x90','768x432')
        if size in validSizes:
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            filename = imageUrl.split("/")[-1]
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f'Error: Image could not be retrieved; request returned code {r.status_code}')
                return
        else:
            print(f"Please enter a valid size. Valid sizes are {validSizes}")
            return
    def downloadBadgeIcon(badgeId, isCircular=None):
        "Downloads badge icon for the set badge ID."
        if isCircular == None:
            isCircular = False
        url = f"https://thumbnails.roblox.com/v1/badges/icons?badgeIds={badgeId}&format=Png&isCircular={isCircular}&size=150x150"
        r = requests.get(url)
        j = json.loads(r.text)
        imageUrl = j['data']['imageUrl']
        r = requests.get(imageUrl)
        filename = imageUrl.split("/")[-1]
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print(f'Image successfully downloaded: {filename}')
            i = Image.open(filename, mode='r')
            i.show()
            return i
        else:
            warnings.warn(f'Error: Image could not be retrieved; request returned code {r.status_code}')
            return f"Error Code {r.status_code}"
    def downloadGamePassIcon(gamePassId, isCircular=None):
        "Downloads icon for the specified game pass ID."
        if isCircular == None:
            isCircular = False
        url = f"https://thumbnails.roblox.com/v1/game-passes?format=Png&gamePassIds={gamePassId}&isCircular={isCircular}&size=150x150"
        r = requests.get(url)
        j = json.loads(r.text)
        imageUrl = j['data']['imageUrl']
        r = requests.get(imageUrl)
        filename = imageUrl.split("/")[-1]
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            print(f'Image successfully downloaded: {filename}')
            i = Image.open(filename, mode='r')
            i.show()
            return i
        else:
            warnings.warn(f'Error: Image could not be retrieved; request returned code {r.status_code}')
            return f"Error Code {r.status_code}"
    def downloadGameIcon(placeId, size, isCircular=None):
        "Downloads the icon for the specific place ID."
        validSizes = ('50x50','128x128','150x150','256x256','512x512')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/places/gameicons?format=Png&isCircular={isCircular}&placeIds={placeId}&size={size}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return
    def downloadGameThumbnails(universeId, size):
        """Downloads all thumbnails for a specific universe ID."""
        validSizes = ('256x144', '384x216','480x270','576x324','768x432')
        if size in validSizes:
            url = f"https://thumbnails.roblox.com/v1/games/multiget/thumbnails?format=Png&isCircular=true&size={size}&universeIds={universeId}"
            print("Getting thumbnail data...")
            r = requests.get(url)
            j = json.loads(r.text)
            print("Thumbnail data received.")
            thumbs = j['data']['thumbnails']
            numThumbs = len(thumbs)
            thumbnailCounter = 0
            for thumbnail in thumbs:
                thumbnailCounter += 1
                print(f"Downloading thumbnail {thumbnailCounter} of {numThumbs}...")
                imageUrl = thumbnail['imageUrl']
                r = requests.get(imageUrl)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename, 'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                    print(f'Image successfully downloaded: {filename}')
                    i = Image.open(filename, mode='r')
                    i.show()
                    return i
                else:
                    warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                    return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter a valid size: {validSizes}")
            return
    def downloadGroupIcon(groupId, size):
        validSizes = ('150x150','420x420')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/groups/icons?format=Png&groupIds={groupId}&isCircular=false&size={size}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return
    def downloadAvatarBust(userId, size, isCircular=None):
        """Downloads the avatar bust for the specified user ID."""
        validSizes = ('50x50', '60x60', '75x75')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/users/avatar-bust?format=Png&isCircular={isCircular}&size={size}&userIds={userId}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return
    def downloadAvatarHeadshot(userId, size, isCircular=None):
        validSizes = ('48x48', '50x50', '60x60', '75x75', '110x110', '150x150', '180x180', '352x352', '420x420', '720x720')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?format=Png&isCircular={isCircular}&size={size}&userIds={userId}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return
    def downloadAvatarFullBody(userId, size, isCircular=None):
        """Downloads the full body shot of the specified user ID's avatar."""
        validSizes = ('30x30', '48x48', '50x50', '60x60', '75x75', '100x100', '110x110', '140x140', '150x150', '150x200', '180x180', '250x250', '352x352', '420x420', '720x720')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/users/avatar?format=Png&isCircular={isCircular}&size={size}&userIds={userId}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return
    def downloadOutfitPreview(outfitId, size, isCircular=None):
        """Downloads the avatar bust for the specified user ID."""
        validSizes = ('150x150', '420x420')
        if size in validSizes:
            if isCircular == None:
                isCircular = False
            url = f"https://thumbnails.roblox.com/v1/users/outfits?format=Png&isCircular={isCircular}&size={size}&userOutfitIds={outfitId}"
            r = requests.get(url)
            j = json.loads(r.text)
            imageUrl = j['data']['imageUrl']
            r = requests.get(imageUrl)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                print(f'Image successfully downloaded: {filename}')
                i = Image.open(filename, mode='r')
                i.show()
                return i
            else:
                warnings.warn(f"Error, could not download image, request returned code {r.status_code}")
                return f"Error Code {r.status_code}"
        else:
            Exception(f"Please enter one of the valid sizes: {validSizes}")
            return