# ------------------------
# TweetHub Demo Script v1.0
# ------------------------

from TweetHub import TweetHub

# Create users
amit = TweetHub("amit")
raj = TweetHub("raj")
neha = TweetHub("neha")
arjun = TweetHub("arjun")

# Profile setup
amit.change_bio("Python Dev | Building projects daily 🚀")
raj.change_bio("Backend lover | #AI #Python enthusiast")
neha.change_bio("Data scientist in making | #ML #AI")
arjun.change_bio("Just exploring TweetHub 😎")

amit.change_location("Bhopal")
raj.change_location("Delhi")
neha.change_location("Pune")
arjun.change_location("Mumbai")

amit.change_age(20)
raj.change_age(21)
neha.change_age(22)

# Follow system
amit.follow("raj")
amit.follow("neha")
raj.follow("amit")
neha.follow("raj")
arjun.follow("neha")
neha.follow("amit")

# Tweets
amit.tweet("Just finished my Twitter clone — #TweetHub is live! 🐦 #Python #OOP")
raj.tweet("Working on database integration soon! #AI #SQL")
neha.tweet("Just published my first #MachineLearning model! #AI #DataScience")
arjun.tweet("Who else loves building new projects? #motivation #coding")

# Likes + Comments (with mentions + hashtags inside comments)
raj.like("amit", 1)
neha.like("amit", 1)
neha.comment("amit", 1, "That's awesome @amit! Congrats 🎉 #motivation")
amit.comment("neha", 1, "Great work @neha, keep shining! #AI")

# Mention edge case
raj.tweet("@amit You should create #group")

# Retweet + Share
amit.retweet("neha", 1)
raj.share("amit", "neha", 1)

# Group Creation + Messages
amit.create_group("DevHub", ["raj", "neha"])
amit.group_message("DevHub", "Hey @neha @raj let's discuss #AI project updates.")
neha.group_message("DevHub", "Sure! I’ll share my latest #ML model soon.")
raj.view_group_messages("DevHub")

# Group admin test
amit.add_group_admin("DevHub", "neha") #add admin
neha.remove_group_member("DevHub", "raj")      # remove from group
raj.group_message("DevHub", "Can I still message?")  # should show restricted
amit.add_group_member("DevHub", "raj")         # re-add user
amit.view_group("DevHub")

# Save / Unsave Tweets
amit.save_tweet("raj", 1)
amit.view_saved_tweets()
amit.unsave_tweet("raj", 1)
amit.view_saved_tweets()

# Personalized Feed shows tweets based on user interest,likes
amit.myfeed()

# Notifications
amit.view_notifications()
raj.view_notifications()
neha.view_notifications()

# Hashtag search + Trending
amit.search_hashtags("AI")
amit.trending_hashtags()

# Trending Tweets (most liked tweets)
amit.trending_tweets()

# User Search
amit.search_users("raj")
neha.search_users("AI")

# View tweet / profile / followers
amit.view_tweet("neha", 1)
amit.view_profile("neha")
amit.view_followers("raj")
amit.view_following("amit")

# Edge cases
amit.follow("amit")                # cannot follow self
neha.like("arjun", 10)             # tweet not found
arjun.comment("raj", 5, "Cool!")   # tweet not found
neha.retweet("raj", 10)            # retweet non-existent tweet
raj.view_group_messages("Unknown") # group not found

# End of demo
print("\n✅ All TweetHub features successfully tested.")