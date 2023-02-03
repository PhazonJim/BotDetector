import os
import json
import yaml
import praw
from match_utils import check_comment

#===Constants===#
CONFIG_FILE = os.path.join(os.path.dirname(__file__),"config.yaml")
CACHE_FILE =  os.path.join(os.path.dirname(__file__), "cache.json")

#===Globals===#
#Config file
config = None
reddit = None

def loadConfig():
    global config
    #Load configs
    try:
        config = yaml.load(open(CONFIG_FILE).read(), Loader=yaml.FullLoader)
    except:
        print("'config.yaml' could not be located. Please ensure 'config.example' has been renamed")
        exit()

def loadCache():
    postCache = {}
    try:
        with open(CACHE_FILE, "r") as fin:
            postCache = json.load(fin)
    except Exception as e:
        print (e)
    return postCache

def initReddit():
    global reddit
    client = config["client"]
    reddit = praw.Reddit(**client)

def saveCache(postCache):
    with open(CACHE_FILE, "w") as fout:
        for chunk in json.JSONEncoder(indent=4).iterencode(postCache):
            fout.write(chunk)

def cacheIfNotExist(submission_id, cache):
    if submission_id not in cache:
        submission = reddit.submission(id=submission_id)
        cache[submission_id] = {"created_utc": submission.created_utc, "comments":{}}

if __name__ == "__main__":
    loadConfig()
    postCache = loadCache()
    initReddit()
    print("Fetching comments...")
    comments = list(reddit.subreddit(config["subreddit"]).comments(limit=1000))
    comments.reverse()
    i = 1
    for comment in comments:
        print(f"Processing {i} of {len(comments)} comments...\r", end="")
        post_id = comment.link_id.split("_")[1]
        cacheIfNotExist(post_id, postCache)
        submission_comments = postCache[post_id]["comments"]
        if comment.id not in submission_comments:
            if len(comment.body) > 10 and check_comment(comment.body, submission_comments):
                print(f"https://www.reddit.com{comment.permalink}")
            else:
                postCache[post_id]["comments"][comment.id] = comment.body
        i+=1
    saveCache(postCache)