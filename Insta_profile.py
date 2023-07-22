import instaloader

import instaloader

def profile_pic(PROFILENAME):
   loader = instaloader.Instaloader()
   profile = instaloader.Profile.from_username(loader.context,PROFILENAME)
   loader.download_profile(PROFILENAME, profile_pic_only=False)
   print("Here is your given profile name's DP and posts")

PROFILENAME=input("Please enter your 'Profile name': ")
profile_pic(PROFILENAME)


