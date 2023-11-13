import requests
import pickle


def log_users(users: list[dict], res: dict, rel: dict):
    for user in users:
        res[user["id"]] = {"id": user["id"], "username": user["username"], "email": user["email"], "posts": 0, "comments": 0}
        rel[user["email"]] = user["id"]


def log_posts(posts: list[dict], res: dict):
    for post in posts:
        userid = post["userId"]
        res[userid]["posts"] += 1


def log_comments(comments: list[dict], res: dict, rel: dict):
    for comment in comments:
        email = comment["email"]
        if email in rel:
            res[rel[comment["email"]]]["comments"] += 1


base_url = "https://jsonplaceholder.typicode.com/"
users_url = base_url + "users"
posts_url = base_url + "posts"
comments_url = base_url + "comments"

users = requests.get(url=users_url).json()
posts = requests.get(url=posts_url).json()
comments = requests.get(url=comments_url).json()


res = {}
rel = {}

log_users(users, res, rel)
log_posts(posts, res)
log_comments(comments, res, rel)
rly_res = [stat_user for stat_user in res.values()]

print(rly_res)
response = requests.post("https://webhook.site/f4aa8350-71a1-40d4-9301-ef32e3eae270", json={"statistics": rly_res})

with open("solution.pickle", "wb") as f:
    pickle.dump(response, f)
