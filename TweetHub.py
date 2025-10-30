import random
import re
import heapq

class UsernameError(Exception):
    pass

class TweetHub:
    all_tweet = {}
    all_users = set()
    all_comments = {}
    all_likes = {}
    all_followers = {}
    all_following = {}
    all_messages = {}
    all_notifications = {}
    all_objects = {}
    all_groups = {}
    all_profiles = {}
    all_user_groups = {}
    all_followers_no = {}
    all_following_no = {}
    all_tweets_no = {}
    all_mentions = {}
    all_user_interests = {}
    all_tweet_hashtags = {}
    all_hashtags = {"tweet": {}, "comment": {}}
    all_user_liked_tweets = {}

    def __init__(self, username):
        self.id = {}
        self.username = username
        self.comments = {}
        if self.username in TweetHub.all_users:
            print("username already exists\n please try to enter new username")
            raise UsernameError
        TweetHub.all_users.add(username)
        self.post_no = 0
        self.saved_tweets = {}
        TweetHub.all_profiles[self.username] = {"username": self.username, "age": "", "bio": "", "location": ""}
        TweetHub.all_objects[self.username] = self
        TweetHub.all_notifications[self.username] = []
        TweetHub.all_followers[self.username] = set()
        TweetHub.all_following[self.username] = set()
        TweetHub.all_messages[self.username] = {}
        TweetHub.all_user_groups[self.username] = set()
        TweetHub.all_user_interests[self.username] = {}
        TweetHub.all_mentions[self.username] = []
        TweetHub.all_user_liked_tweets[self.username] = set()
        TweetHub.all_followers_no[self.username] = 0
        TweetHub.all_following_no[self.username] = 0
        TweetHub.all_tweets_no[self.username] = 0

    def tweet(self, tweet):  # tweet
        self.post_no += 1
        self.id[(self.username, self.post_no)] = tweet
        TweetHub.all_tweets_no[self.username] += 1
        self.comments[(self.username, self.post_no)] = {}
        TweetHub.all_comments[(self.username, self.post_no)] = []
        TweetHub.all_tweet[(self.username, self.post_no)] = tweet
        TweetHub.all_likes[(self.username, self.post_no)] = set()
        mentions = re.findall(r"@([A-Za-z0-9_.-]+)", tweet)
        for user in mentions:
            if user in TweetHub.all_users and user != self.username:
                TweetHub.all_mentions[user].append(f"mentioned by {self.username} on tweet--> {self.username} {self.post_no} -> {tweet}")
                TweetHub.all_notifications[user].append(f"{self.username} mentioned you in tweet-> {self.username} {self.post_no} -> {tweet}")
        hashtags = re.findall(r"#([A-Za-z0-9_.-]+)", tweet)
        TweetHub.all_tweet_hashtags[(self.username, self.post_no)] = hashtags
        for hashtag in hashtags:
            if hashtag not in TweetHub.all_hashtags["tweet"]:
                TweetHub.all_hashtags["tweet"][hashtag] = [(self.username, self.post_no, tweet), ]
            else:
                TweetHub.all_hashtags["tweet"][hashtag].append((self.username, self.post_no, tweet))

    def delete_tweet(self, number):  # delete tweet
        if (self.username, number) in self.id:
            self.id.pop((self.username, number))
            TweetHub.all_tweets_no[self.username] -= 1
            TweetHub.all_likes.pop((self.username, number))
            TweetHub.all_comments.pop((self.username, number))
            for hashtag in TweetHub.all_tweet_hashtags[(self.username, number)]:
                TweetHub.all_hashtags["tweet"][hashtag].remove((self.username, number, TweetHub.all_tweet[self.username, number]))
            TweetHub.all_tweet.pop((self.username, number))
            TweetHub.all_tweet_hashtags.pop((self.username, self.post_no))
        else:
            print(f"tweet {self.username} {number} not found")

    def view_all_tweets(self, username):
        if username in TweetHub.all_objects:
            user_obj = TweetHub.all_objects[username]
            print(username, "all tweets-->", user_obj.id)
        else:
            print("user not found")

    def comment(self, username, post_no, commentt):  # comment on tweet
        if (username, post_no) in TweetHub.all_tweet:
            TweetHub.all_comments[(username, post_no)].append((self.username, commentt))
            TweetHub.all_notifications[username].append(f"{self.username} commented {commentt} on your tweet")
            for hashtag in TweetHub.all_tweet_hashtags[(username, post_no)]:
                if hashtag in TweetHub.all_user_interests[self.username]:
                    TweetHub.all_user_interests[self.username][hashtag] += 1
                else:
                    TweetHub.all_user_interests[self.username][hashtag] = 1

            mentions = re.findall(r"@([A-Za-z0-9_.-]+)", commentt)
            for user in mentions:
                if user in TweetHub.all_users and user != self.username:
                    TweetHub.all_mentions[user].append(f"mentioned by {self.username} in comment {commentt} on tweet -> {self.username} {post_no}")
                    TweetHub.all_notifications[user].append(f"{self.username} mentioned you in comment-> {commentt} on tweet-> {username} {post_no} ")

            hashtags = re.findall(r"#([A-Za-z0-9_.-]+)", commentt)
            for hashtag in hashtags:
                if hashtag not in TweetHub.all_hashtags["comment"]:
                    TweetHub.all_hashtags["comment"][hashtag] = [(self.username, post_no, commentt), ]
                else:
                    TweetHub.all_hashtags["comment"][hashtag].append((self.username, post_no, commentt))
        else:
            print("tweet not found")

    def view_comments(self, username, post_no):  # view comments
        if (username, post_no) in TweetHub.all_tweet:
            print(username, post_no, "--> comments =", TweetHub.all_comments[(username, post_no)])
        else:
            print("tweet not found")

    def view_tweet(self, username, post_no):  # view tweet
        if (username, post_no) in TweetHub.all_tweet:
            print(f"view tweet--> {username} {post_no}")
            print(TweetHub.all_tweet[(username, post_no)])
            print(f"total {len(TweetHub.all_likes[(username, post_no)])} likes and {len(TweetHub.all_comments[(username, post_no)])} comments")
            self.view_likes(username, post_no)
            self.view_comments(username, post_no)
            for hashtag in TweetHub.all_tweet_hashtags[(username, post_no)]:
                if hashtag in TweetHub.all_user_interests[self.username]:
                    TweetHub.all_user_interests[self.username][hashtag] += 1
                else:
                    TweetHub.all_user_interests[self.username][hashtag] = 1
        else:
            print("tweet not found")

    def like(self, username, post_no):  # like tweet
        if (username, post_no) in TweetHub.all_tweet:
            TweetHub.all_likes[(username, post_no)].add(self.username)
            TweetHub.all_user_liked_tweets[self.username].add((username, post_no))
            TweetHub.all_notifications[username].append(f"{self.username} liked your tweet {post_no} -> {TweetHub.all_tweet[(username, post_no)]}")
            for hashtag in TweetHub.all_tweet_hashtags[(username, post_no)]:
                if hashtag in TweetHub.all_user_interests[self.username]:
                    TweetHub.all_user_interests[self.username][hashtag] += 1
                else:
                    TweetHub.all_user_interests[self.username][hashtag] = 1
        else:
            print(username, post_no, "tweet not found")

    def unlike(self, username, post_no):  # unlike tweet
        if (username, post_no) in TweetHub.all_tweet:
            if self.username in TweetHub.all_likes[(username, post_no)]:
                TweetHub.all_likes[(username, post_no)].remove(self.username)
                TweetHub.all_user_liked_tweets[self.username].remove((username, post_no))
                for hashtag in TweetHub.all_tweet_hashtags[(username, post_no)]:
                    if hashtag in TweetHub.all_user_interests[self.username]:
                        TweetHub.all_user_interests[self.username][hashtag] -= 2
        else:
            print(username, post_no, "tweet not found")

    def view_likes(self, username, post_no):  # view likes
        if (username, post_no) in TweetHub.all_tweet:
            print(username, post_no, "liked by--> ", TweetHub.all_likes[(username, post_no)])
        else:
            print(f"tweet {username} {post_no} not found")

    def follow(self, username):  # follow ID
        if username == self.username:
            print("you can't follow yourself!")
            return
        if username in TweetHub.all_following[self.username]:
            print(f"you already follow {username}")
            return
        if username in TweetHub.all_users:
            TweetHub.all_followers[username].add(self.username)
            TweetHub.all_following[self.username].add(username)
            TweetHub.all_followers_no[username] += 1
            TweetHub.all_following_no[self.username] += 1
            TweetHub.all_notifications[username].append(f"{self.username} started following you!")
        else:
            print("user not found")

    def unfollow(self, username):  # unfollow ID
        if self.username in TweetHub.all_followers[username]:
            TweetHub.all_followers[username].remove(self.username)
            TweetHub.all_following[self.username].remove(username)
            TweetHub.all_followers_no[username] -= 1
            TweetHub.all_following_no[self.username] -= 1

    def view_followers(self, username):  # view followers
        if username in TweetHub.all_users:
            print(username, "total followers -->", TweetHub.all_followers_no[username], TweetHub.all_followers[username])
        else:
            print(f"user {username} not found")

    def view_following(self, username):  # view_following
        if username in TweetHub.all_users:
            print(username, "total following -->", TweetHub.all_following_no[username], TweetHub.all_following[username])
        else:
            print(f"user {username} not found")

    def message(self, username, message):  # message
        if username in TweetHub.all_users:
            TweetHub.all_messages[username].setdefault(self.username, []).append(message)
            TweetHub.all_notifications[username].append(f"{self.username} sent you a message {message}")
        else:
            print("user not found")

    def view_messages(self):  # view_messages
        print(self.username, "messages -->", TweetHub.all_messages[self.username])

    def retweet(self, username, post_no):
        if username==self.username:
            print("can't retweet your own tweet")
        elif (username, post_no) in TweetHub.all_tweet:
            self.post_no += 1
            retweet_text = f"RT @{username}: {TweetHub.all_tweet[(username, post_no)]}"
            self.id[(self.username, self.post_no)] = retweet_text
            TweetHub.all_tweets_no[self.username] += 1
            TweetHub.all_comments[(self.username, self.post_no)] = []
            TweetHub.all_likes[(self.username, self.post_no)] = set()
            TweetHub.all_tweet[(self.username, self.post_no)] = retweet_text
            TweetHub.all_tweet_hashtags[(self.username, self.post_no)] = TweetHub.all_tweet_hashtags[(username, post_no)]
            TweetHub.all_notifications[username].append(f"{self.username} retweeted your tweet {post_no} -> {TweetHub.all_tweet[(username, post_no)]}")
            print(f"Retweeted {username}'s tweet {post_no}")
        else:
            print("Tweet not found")

    def share(self, username, post_user, post_no):  # send
        key = TweetHub.all_tweet[(post_user, post_no)]
        self.message(username, key)
        for hashtag in TweetHub.all_tweet_hashtags[(post_user, post_no)]:
            if hashtag in TweetHub.all_user_interests[self.username]:
                TweetHub.all_user_interests[self.username][hashtag] += 1
            else:
                TweetHub.all_user_interests[self.username][hashtag] = 1

    def trending_tweets(self):
        print("trending tweets-->")
        for x in TweetHub.all_likes:
            if len(TweetHub.all_likes[x]) >= len(TweetHub.all_users) // 5:
                print(TweetHub.all_tweet[(x[0], x[1])])
                self.view_comments(x[0], x[1])
                self.view_likes(x[0], x[1])

    def view_notifications(self):
        print("your all new notifications-->")
        print(TweetHub.all_notifications[self.username])
        TweetHub.all_notifications[self.username].clear()

    def save_tweet(self, username, post_no):
        if (username, post_no) in TweetHub.all_tweet:
            self.saved_tweets[(username, post_no)] = TweetHub.all_tweet[(username, post_no)]
            print(f"tweet {username} {post_no} saved successfully")
            for hashtag in TweetHub.all_tweet_hashtags[(username, post_no)]:
                if hashtag in TweetHub.all_user_interests[self.username]:
                    TweetHub.all_user_interests[self.username][hashtag] += 1
                else:
                    TweetHub.all_user_interests[self.username][hashtag] = 1
        else:
            print(f"tweet {username} {post_no} not found")

    def unsave_tweet(self, username, post_no):
        if (username, post_no) in TweetHub.all_tweet:
            if (username, post_no) in self.saved_tweets:
                self.saved_tweets.pop((username, post_no))
                print(f"tweet {username} {post_no} unsaved successfully")
        else:
            print(f"tweet {username} {post_no} not found")

    def view_saved_tweets(self):
        print("saved tweets-->")
        print(self.saved_tweets)

    def view_my_liked_tweets(self):
        print(TweetHub.all_user_liked_tweets[self.username])

    def search_users(self, keyword):
        results = []
        for username, profile in TweetHub.all_profiles.items():
            if keyword.lower() in username.lower() or keyword.lower() in profile["bio"].lower():
                results.append((username, profile))
        if results:
            print(f"Users matching '{keyword}':")
            for user, profile in results:
                print(f"{user}: {profile}")
        else:
            print(f"No users found for '{keyword}'")

    def create_group(self, groupname, members):
        if groupname in TweetHub.all_groups:
            print("group name already exists")
            return
        TweetHub.all_user_groups[self.username].add(groupname)
        TweetHub.all_groups[groupname] = {"creator": self.username, "members": {self.username, }, "admins": {self.username, }, "messages": {}}
        for x in members:
            if x not in TweetHub.all_users:
                print("user not found")
                return
            if x in TweetHub.all_groups[groupname]["members"]:
                print(f"user {x} already in group {groupname}")
                return
            if self.username in TweetHub.all_following[x]:
                TweetHub.all_groups[groupname]["members"].add(x)
                TweetHub.all_user_groups[x].add(groupname)
                TweetHub.all_notifications[x].append(f"{self.username} added you in group {groupname}")
            else:
                print(f"you can't add {x} because he/she don't follow you!")

    def view_group(self, groupname):
        if TweetHub.all_groups.get(groupname) and self.username in TweetHub.all_groups[groupname]["members"]:
            print(TweetHub.all_groups[groupname])
        else:
            print("group not found")

    def leave_group(self, groupname):
        if TweetHub.all_groups.get(groupname) and self.username in TweetHub.all_groups[groupname]["members"]:
            TweetHub.all_groups[groupname]["members"].remove(self.username)
            TweetHub.all_user_groups[self.username].remove(groupname)
            print("leaved group successfully")
        else:
            print("group not found")

    def remove_group_member(self, groupname, username):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
            return
        if username not in TweetHub.all_groups[groupname]["members"]:
            print("given user not found in group")
            return
        if self.username in TweetHub.all_groups[groupname]["admins"] and username != TweetHub.all_groups[groupname]["creator"]:
            TweetHub.all_groups[groupname]["members"].remove(username)
            print(f"user {username} removed successfully from group {groupname}")
            TweetHub.all_user_groups[username].remove(groupname)
            TweetHub.all_notifications[username].append(f"{self.username} removed you from group {groupname}")
        else:
            print(f"you can't remove {username} from group {groupname}")

    def add_group_member(self, groupname, username):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
            return
        if username not in TweetHub.all_users:
            print("user not found")
            return
        if self.username not in TweetHub.all_following[username]:
            print(f"you can't add {username} because he/she don't follows you!")
            return
        if username in TweetHub.all_groups[groupname]["members"]:
            print(f"user {username} already in group {groupname}")
            return
        if self.username in TweetHub.all_groups[groupname]["admins"]:
            TweetHub.all_groups[groupname]["members"].add(username)
            print(f"member {username} added successfully in group {groupname}")
            TweetHub.all_user_groups[username].add(groupname)
            TweetHub.all_notifications[username].append(f"{self.username} added you in group {groupname}")
        else:
            print("you can't add someone in group because you're not admin")

    def add_group_admin(self, groupname, username):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
            return
        if username not in TweetHub.all_users:
            print("user not found")
            return
        if self.username in TweetHub.all_groups[groupname]["admins"]:
            if username in TweetHub.all_groups[groupname]["members"]:
                TweetHub.all_groups[groupname]["admins"].add(username)
                print(f"member {username} successfully become group {groupname} admin")
                TweetHub.all_notifications[username].append(f"{self.username} made you admin of group-> {groupname}")
            else:
                if self.username in TweetHub.all_following[username]:
                    TweetHub.all_groups[groupname]["members"].add(username)
                    TweetHub.all_groups[groupname]["admins"].add(username)
                    TweetHub.all_notifications[username].append(f"{self.username} added you in group-> {groupname} and made you admin of group")
                    print(f"member {username} added successfully in group {groupname} and also become group admin successfully")
                else:
                    print(f"you can't add {username} because he/she don't follows you!")
        else:
            print("you can't add someone in group because you're not admin")

    def remove_group_admin(self, groupname, username):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
            return
        if username not in TweetHub.all_groups[groupname]["members"]:
            print("given user not found in group")
            return
        if username not in TweetHub.all_groups[groupname]["admins"]:
            print("given user not found in group admins")
            return
        if self.username in TweetHub.all_groups[groupname]["admins"] and username != TweetHub.all_groups[groupname]["creator"]:
            TweetHub.all_groups[groupname]["admins"].remove(username)
            print(f"user {username} removed successfully as admin from group {groupname}")
            TweetHub.all_notifications[username].append(f"{self.username} removed you as admin from group {groupname}")
        else:
            print(f"you can't remove {username} as admin from group {groupname}")

    def group_message(self, groupname, message):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
        else:
            TweetHub.all_groups[groupname]["messages"][self.username] = message
            mentions = re.findall(r"@([A-Za-z0-9_.-]+)", message)
            for user in mentions:
                if user in TweetHub.all_groups[groupname]["members"] and user != self.username:
                    TweetHub.all_mentions[user].append(f"mentioned by {self.username} on group {groupname} message--> {message}")
                    TweetHub.all_notifications[user].append(f"{self.username} mentioned you in groupchat {groupname},message -> {message}")
            for x in TweetHub.all_groups[groupname]["members"]:
                if x != self.username:
                    TweetHub.all_notifications[x].append(f"{self.username} sent a message {message} on group--> {groupname}")

    def view_group_messages(self, groupname):
        if not TweetHub.all_groups.get(groupname) or not self.username in TweetHub.all_groups[groupname]["members"]:
            print("group not found")
        else:
            print(f"group -->{groupname}-> messages")
            print(TweetHub.all_groups[groupname]["messages"])

    def view_my_groups(self):
        print(TweetHub.all_user_groups[self.username])

    def random_tweets(self, limit):
        print("random tweets-->")
        if not TweetHub.all_tweet:
            print("nothing to show here..")
            return
        i = 1
        seen = set()
        while i < limit:
            if len(seen) == len(TweetHub.all_tweet):
                print("nothing to show more..")
                return
            x = random.choice(list(TweetHub.all_tweet.items()))
            if x not in seen:
                print(x)
                seen.add(x)
            i += 1

    def view_profile(self, username):
        print(f"{username} Profile -->")
        print(TweetHub.all_profiles[username])
        print(f"total followers-> {TweetHub.all_followers_no[username]}")
        print(f"total following-> {TweetHub.all_following_no[username]}")
        print(f"total tweets-> {TweetHub.all_tweets_no[username]}")
        if username == self.username:
            return
        count = 0
        for x in TweetHub.all_following[self.username]:
            if x in TweetHub.all_followers[username]:
                count += 1
        print(f"mutual followers-> {count}")

    def change_bio(self, newbio):
        TweetHub.all_profiles[self.username]["bio"] = newbio
        print("bio changed successfully")

    def change_age(self, newage):
        if type(newage) == int:
            TweetHub.all_profiles[self.username]["age"] = newage
            print("age changed successfully")
        else:
            print("age must be a number")

    def change_location(self, newlocation):
        if newlocation.isalpha():
            TweetHub.all_profiles[self.username]["location"] = newlocation
            print("location changed successfully")
        else:
            print("location must only contain alpha characters")

    def view_mutual_followers(self, username):
        total = set()
        count = 0
        print(f"mutual followers of {username}")
        for x in TweetHub.all_following[self.username]:
            if x in TweetHub.all_followers[username]:
                count += 1
                total.add(x)
        print(f"{count} --> {total}")

    def view_all_mentions(self):
        print("your all mentions by other users..")
        print(TweetHub.all_mentions[self.username])

    def search_hashtags(self, hashtag):
        if hashtag in TweetHub.all_hashtags["tweet"]:
            print(f"All Tweets including #{hashtag} :-")
            print(TweetHub.all_hashtags["tweet"][hashtag])
        else:
            print(f"No Tweets found related #{hashtag}")
        if hashtag in TweetHub.all_hashtags["comment"]:
            print(f"All Comments including #{hashtag}")
            print(TweetHub.all_hashtags["comment"][hashtag])
        else:
            print(f"No Comments found related #{hashtag}")

    def trending_hashtags(self, limit=5):
        sorted_items = sorted(TweetHub.all_hashtags["tweet"].items(), key=lambda x: len(x[1]), reverse=True)
        top_hashtags = [(key, len(value)) for key, value in sorted_items[:limit]]
        print(f"top {limit} hashtags in Tweets-> {top_hashtags}")
        sorted_items2 = sorted(TweetHub.all_hashtags["comment"].items(), key=lambda x: len(x[1]), reverse=True)
        top_hashtags2 = [(key, len(value)) for key, value in sorted_items2[:limit]]
        print(f"top {limit} hashtags in Comments-> {top_hashtags2}")

    def myfeed(self):
        def interests_based_suggestions():
            suggested_tweets = set()
            if len(TweetHub.all_user_interests[self.username]) == 0:
                return suggested_tweets
            seen = TweetHub.all_user_liked_tweets[self.username]
            data = TweetHub.all_user_interests[self.username]
            top5 = heapq.nlargest(5, data, key=data.get)
            top10 = heapq.nlargest(10, data, key=data.get)
            top20 = heapq.nlargest(20, data, key=data.get)
            weighted_interest = top5 * 3 + top10 * 2 + top20
            no_of_suggestions = random.randint(10, 20)
            for i in range(no_of_suggestions):
                interest = random.choice(weighted_interest)
                if interest in TweetHub.all_hashtags["tweet"]:
                    random_tweet = random.choice(TweetHub.all_hashtags["tweet"][interest])
                    user, tweet_no, tweet = random_tweet
                    if user != self.username and (user, tweet_no) not in seen:
                        suggested_tweets.add((user, tweet_no, tweet))
                        seen.add((user, tweet_no))
            return suggested_tweets

        def following_based_suggestions():
            suggested_tweets = set()
            if len(TweetHub.all_following[self.username]) == 0:
                return suggested_tweets
            seen = TweetHub.all_user_liked_tweets[self.username]
            no_of_suggestions = random.randint(3, 10)
            for i in range(no_of_suggestions):
                random_following = random.choice(list(TweetHub.all_following[self.username]))
                if TweetHub.all_tweets_no[random_following] > 0:
                    random_tweet = random.choice(list(TweetHub.all_objects[random_following].id.keys()))
                    user, post_no = random_tweet
                    if (user, post_no) not in seen:
                        suggested_tweets.add((user, post_no, TweetHub.all_tweet[(user, post_no)]))
                        seen.add((user, post_no))
            return suggested_tweets

        def new_suggestions():
            suggested_tweets = set()
            seen = TweetHub.all_user_liked_tweets[self.username]
            no_of_suggestions = random.randint(3, 7)
            for i in range(no_of_suggestions):
                key, value = random.choice(list(TweetHub.all_tweet.items()))
                if (key, value) not in seen and key[0]!=self.username:
                    seen.add((key[0], key[1]))
                    suggested_tweets.add((key[0], key[1], value))
            return suggested_tweets

        print("My Feed --> Tweets Suggested For You --> ")
        sugg1 = interests_based_suggestions()
        sugg2 = following_based_suggestions()
        sugg3 = new_suggestions()
        all_tweets_suggestions = sugg1 | sugg2 | sugg3
        print(all_tweets_suggestions)


