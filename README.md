TweetHub is a Twitter-like social media platform built entirely in Python (Object-Oriented Programming) — no frameworks, no database (yet)!
It simulates all real Twitter features like tweets, likes, follows, groups, hashtags, mentions, comments, retweets, and more — fully in the console.


---

🌟 Features

✅ Create users and manage profiles
✅ Tweet, comment, like, and retweet posts
✅ Follow / unfollow other users
✅ Send direct messages
✅ Create and manage groups (with admin control)
✅ Mention users with @username
✅ Add and search hashtags #topic
✅ Personalized feed based on interests
✅ Notifications system
✅ Save and share tweets
✅ Trending tweets detection
✅ Error-free handling (e.g. “You can’t follow yourself”, “No tweets found”)


⚙ Tech Stack

Component	Description

Language	Python 🐍
Concepts Used	Object-Oriented Programming (OOP), Dictionaries, Sets, Lists, File Handling
Libraries Used	random, heapq, re
Future Update (v2.0)	SQL Database Integration (coming within 7 days 🚀)


---

🧪 How to Run

1. Download the project:

Click on Code → Download ZIP

Extract the folder on your computer



2. Open the folder in VS Code / PyCharm / Thonny


3. Run the demo script:

python demo_script.py


## 💡 All Features / User Actions (Functions)


Here are all the functions available in TweetHub, grouped by category for better readability 👇

---

📝 Tweet Actions

tweet(tweet) → Post a new tweet (supports hashtags # and mentions @).

delete_tweet(number) → Delete your tweet.

view_tweet(username, post_no) → View a single tweet (with likes/comments).

view_all_tweets(username) → View all tweets by a user.

retweet(username, post_no) → Retweet someone’s tweet.

share(username, post_user, post_no) → Share a tweet via direct message.

save_tweet(username, post_no) → Save a tweet for later.

unsave_tweet(username, post_no) → Remove a tweet from saved.

view_saved_tweets() → View all your saved tweets.

trending_tweets() → Show currently trending tweets.

random_tweets(limit) → Display random tweets from the platform.



---

💬 Comment Actions

comment(username, post_no, commentt) → Comment on a tweet (supports hashtags & mentions).

view_comments(username, post_no) → View all comments on a tweet.



---

❤ Like Actions

like(username, post_no) → Like a tweet.

unlike(username, post_no) → Unlike a tweet.

view_likes(username, post_no) → View who liked a tweet.

view_my_liked_tweets() → View all tweets you liked.



---

👥 Follow System

follow(username) → Follow a user.

unfollow(username) → Unfollow a user.

view_followers(username) → View followers list.

view_following(username) → View following list.

view_mutual_followers(username) → See mutual followers between two users.



---

💌 Messaging

message(username, message) → Send a private message.

view_messages() → View your inbox messages.

share(username, post_user, post_no) → Share any tweet via message.



---

👪 Groups

create_group(groupname, members) → Create a group with selected members.

view_group(groupname) → View full group details.

view_group_messages(groupname) → See all messages in a group.

group_message(groupname, message) → Send a message in a group (mentions supported).

view_my_groups() → View all your groups.

leave_group(groupname) → Leave a group.

add_group_member(groupname, username) → Add new member (if you’re admin).

remove_group_member(groupname, username) → Remove member (if you’re admin).

add_group_admin(groupname, username) → Promote member to admin.

remove_group_admin(groupname, username) → Remove admin rights.



---

🧠 Feed & Recommendations

myfeed() → View personalized feed (based on interests, following, and random mix).


---

🔍 Search

search_users(keyword) → Search users by name or bio.

search_hashtags(hashtag) → Search tweets and comments by hashtag.

trending_hashtags(limit=5) → Show top trending hashtags.



---

🔔 Notifications & Mentions

view_notifications() → View all new notifications.

view_all_mentions() → See where you’ve been mentioned.


---

👤 Profile Management

view_profile(username) → View any user’s profile (followers, mutuals, tweets).

change_bio(newbio) → Update bio.

change_age(newage) → Update age.

change_location(newlocation) → Update location.



---

⚙ System Internals / Edge Case Handling

Handles all invalid cases like:

Trying to follow yourself.

Mentioning non-existent users.

Liking or commenting on deleted tweets.

Repeated group additions/removals.

Auto-notifications on all actions (follow, like, retweet, group actions, mentions).


Graceful message returns instead of errors (no crashes).

---

💻 DEMO SCRIPT PREVIEW --->

from TweetHub import TweetHub

amit = TweetHub("amit")
raj = TweetHub("raj")
neha = TweetHub("neha")
arjun = TweetHub("arjun")
amit.follow("neha")
raj.follow("amit")
Amit.tweet("Just finished my Twitter clone — #TweetHub is live! 🐦 #Python #OOP")
raj.tweet("Working on database integration soon! #AI #SQL")
raj.like("amit", 1)
raj.tweet("@amit You should create #group")
amit.create_group("DevHub", ["raj", "neha"])
amit.group_message("DevHub", "Hey @neha @raj let's discuss #AI project updates.")
amit.view_notifications()
# Personalized Feed shows tweets based on user interest,likes
amit.myfeed()

AND MANY OTHER OPTIONS...

🧠 What I Learned

During the development of TweetHub, I explored a wide range of real-world programming concepts and software design ideas beyond basic syntax.
Here’s what I gained from this project 👇

🧩 Object-Oriented Programming (OOP) — implemented real-world classes and relationships just like actual social media systems.

⚙ Data Structures in Practice — used Python’s dictionaries, lists, and sets to manage tweets, likes, followers, and groups efficiently.

💬 User Interaction Logic — designed realistic conditions and validations (like “can’t follow yourself”, “user not found”, etc.) to avoid crashes and edge case errors.

🔁 Feature Planning & Modularity — learned how to divide a large application into multiple manageable features and functions.

🧮 Algorithmic Thinking — used sorting, searching, and heapq for trending tweets and personalized feeds.

🧠 Regex (Regular Expressions) — used re module to detect hashtags #topic and mentions @user.

🪄 Error Handling — added safe fallback messages for every possible invalid action instead of throwing runtime errors.

🚀 Project Structure & Maintainability — understood how to separate the main logic and demo script for clean, testable code.

🧱 Future Database Integration — learned how SQL could replace in-memory dictionaries to make the project scalable and persistent.

💡 GitHub Workflow — understood how to structure, document, and publish a Python project professionally.

---

🚀 Upcoming Update (Version 2.0)

I’ll be integrating SQL Database in the next version for:

Storing user data permanently

Fetching personalized feeds

Real-time tweet and comment storage

Stay tuned for TweetHub v2.0 (with SQL) 👀

💬 Connect With Me

👤 Amit Dubey
🎓 M.Tech Intergrated (IT) 1st Year, DAVV IIPS
📍 INDORE, India

LINKEDLN --> https://www.linkedin.com/in/amit-dubey-613355371
