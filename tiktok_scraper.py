from TikTokApi import TikTokApi
from requests.api import delete
import os.path, os, re, logging, random

# Unofficial TikTok Api Config
verifyFp = ''
logging.basicConfig(filename='scraper.log', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%m:%S')
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

hashtags = []
path = f"{os.getcwd()}\\Desktop\\note.txt"
f = open(path, "r+", encoding="utf8")
hashtags_from_file = f.readlines()
hashtags_strip = [hashtags_from_file[x].strip("\n#") for x in range(len(hashtags_from_file))]
for x in range(3):
    hashtag = hashtags_strip[random.randint(1, len(hashtags_strip))]
    hashtags.append(hashtag)
    with open(path, 'w') as f:
        delete
        
with open(path, 'a', encoding="utf8") as f:
    for x in range(len(hashtags_strip)):
        if hashtags_strip[x] not in hashtags:
            f.write(hashtags_strip[x]+'\n')

print(hashtags)
f.close()
values= ()
def Get_Tiktok_Data(hashtags, values):
    for x in range(len(hashtags)):
        tiktoks = api.by_hashtag(hashtags[x], count=1000) 
        for tiktok in tiktoks:
            user = tiktok.get('author', {})
            username = user.get('uniqueId')
            userdescription = user.get('signature')
            email = re.findall('[\w\.-]+@[\w\.-]+', userdescription)
            if email:
                values = values + ((username, userdescription.replace("\n", ""), email[0]),)
    return tuple(set(values))
    
func = Get_Tiktok_Data(hashtags, values)

while True:   
    try:
        func
        break
    except:
        pass

print(func)
# print('saved to file')