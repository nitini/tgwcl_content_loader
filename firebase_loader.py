import gspread
import time
import urllib.request
import pprint
from oauth2client.service_account import ServiceAccountCredentials
import sys
import pyrebase

def get_gspread_client(creds_file_path):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)

    client = gspread.authorize(creds)
    return client

def get_firebase_ref():
    config = {
            "apiKey": "AIzaSyASzykQJnLu0XH5eV2Vmiia1G3o6GROLTE",
            "authDomain":"twcl-v1.firebaseapp.com",
            "databaseURL":"https://twgcl-v1.firebaseio.com",
            "storageBucket":"twgcl-v1.appspot.com",
            "serviceAccount":"./twgcl-v1-firebase-adminsdk-emhha-e3970eeb68.json"
            }
    firebase = pyrebase.initialize_app(config)
    return firebase

def create_database_entry(db):
    """
    Example of process to create new entry:

    message_ref = db.child("messages").push({})
    message_key = message_ref["name"]
    db.child("messages").child(message_key).update({"original":"Hello durr","UID": message_key})

    """
    outfit_ref_1 = db.child("outfits").push({})
    outfit_key_1 = outfit_ref_1["name"]
    outfit_values_1 = {
                    "uid": outfit_key_1,
                    "postDate": "3.14.2017",
                    "vibe":"Chill, urban, attitude, feeling yourself",
                    "dos":"Pair bulky sweaters with either short or tight bottoms. I really encourage the jewelry",
                    "donts": "Avoid bottoms that are both short AND tight",
                    "stylingTips": "Heels help elongate your legs to look even better in the skirt",
                    "proTip": "Loose, sassy sweaters are key to have extra room to breathe but also be stylish",
                    "collageLink": "http://i.imgur.com/rSCqJPH.png",
                    "thumbnailLink":"http://i.imgur.com/abwAbwd.jpg",
                    "outfitPieces":
                            {
                                "piece_1":
                                    {
                                        "imageLink":"http://i.imgur.com/Ev8Ut5D.jpg",
                                        "storeLink":"http://bit.ly/2mRBAcv",
                                        "pieceTitle":"Rad: Everything is Fine So Far",
                                        "price": 34.90
                                    },
                                "piece_2":
                                    {
                                        "imageLink": "http://i.imgur.com/HsIsNO2.jpg",
                                        "storeLink": "http://bit.ly/2m91RBv",
                                        "pieceTitle": "H&M: Short Skirt",
                                        "price": 29.99
                                    }
                            },                    
                    "storeDescriptions": 
                            {
                                "store_1":
                                    {
                                        "storeName": "Rad",
                                        "storeDetail":"Free shipping over $40, JASMINE20 for 20% off order"
                                    },
                                "store_2":
                                    {
                                        "storeName": "H&M",
                                        "storeDetail": "20% off one item of your choice + free shipping with newsletter"
                                    }
                            }
                    }


    db.child("outfits").child(outfit_key_1).update(outfit_values_1)

    outfit_ref_2 = db.child("outfits").push({})
    outfit_key_2 = outfit_ref_2["name"]

    outfit_values_2 = {
                    "uid": outfit_key_2,
                    "postDate": "3.12.2017",
                    "vibe":"Going out to a bar with a dance floor in NYC or LA.",
                    "dos":"Get a dress with a large slit in the middle so that it flows over the jeans",
                    "donts": "Avoid dresses with no slit at all, that will just be bulky",
                    "stylingTips": "Possible hairstyles: all down, wavy with volume, or half ponytail in a bun",
                    "proTip": "You can get kinda tipsy and rest assured your high-slit dress isn't becoming involuntarily revealing",
                    "collageLink": "http://i.imgur.com/JJ53vQP.jpg",
                    "thumbnailLink":"http://i.imgur.com/CbtPll3.jpg",
                    "outfitPieces":
                            {
                                "piece_1":
                                    {
                                        "imageLink":"http://i.imgur.com/HFyoZu9.png",
                                        "storeLink":"http://bit.ly/2mhcOSz",
                                        "pieceTitle":"Satin Crepe Wrap Dress (Champagne)",
                                        "price": 7.80
                                    },
                                "piece_2":
                                    {
                                        "imageLink": "http://i.imgur.com/992s70R.png",
                                        "storeLink": "http://bit.ly/2lRW200",
                                        "pieceTitle": "New Look Ripped Mom Jeans",
                                        "price": 46.00
                                    },
                                "piece_3": {
                                        "imageLink": "http://i.imgur.com/GdVuNev.png",
                                        "storeLink": "http://bit.ly/2neEeg5",
                                        "pieceTitle": "Faux Suede Lace-up Ankle Boots",
                                        "price": 48.00
                                    }
                            },                    
                    "storeDescriptions": 
                            {
                                "store_1":
                                    {
                                        "storeName": "Fanm Djanm",
                                        "storeDetail":"I found Fanm Djanm on Instagram a year-ish ago and I just love their aesthetic"
                                    },
                                "store_2":
                                    {
                                        "storeName": "MakeMeChic",
                                        "storeDetail": "Very very similar to Shein if you have heard me talk about that company"
                                    }
                            }
                    }
    
    db.child("outfits").child(outfit_key_2).update(outfit_values_2)



def main():
    gspread_client = get_gspread_client("./twgcl-603c11d2c10a.json")
    firebase = get_firebase_ref()
    db = firebase.database()
    create_database_entry(db)

if __name__ == "__main__":
    main()

