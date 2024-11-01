import instagrapi
import os
import dotenv

dotenv.load_dotenv()

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

client = instagrapi.Client()

client.login(IG_USERNAME, IG_PASSWORD)

userID = client.user_id_from_username(IG_USERNAME)
followers = client.user_followers(userID, 0)
following = client.user_following(userID, 0)


