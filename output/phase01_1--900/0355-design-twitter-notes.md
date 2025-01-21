## Design Twitter

**Problem Link:** https://leetcode.com/problems/design-twitter/description

**Problem Statement:**
- Design a simplified version of Twitter where users can post tweets, follow other users, and view the 10 most recent tweets in their news feed.
- Input format and constraints:
  - The system should support the following operations:
    - `postTweet(userId, tweetId)`: Post a new tweet with the given `tweetId` by the user with `userId`.
    - `getNewsFeed(userId)`: Retrieve the 10 most recent tweet ids in the news feed of the user with `userId`.
    - `follow(followerId, followeeId)`: The user with `followerId` started following the user with `followeeId`.
    - `unfollow(followerId, followeeId)`: The user with `followerId` stopped following the user with `followeeId`.
- Expected output format:
  - The `postTweet` and `follow` operations do not return any value.
  - The `getNewsFeed` operation returns a vector of the 10 most recent tweet ids in the news feed of the user.
- Key requirements and edge cases to consider:
  - A user can follow themselves.
  - If a user is not following anyone, their news feed will contain only their own tweets.
  - If a user is following other users, their news feed will contain the most recent tweets from all users they are following, including themselves.
- Example test cases with explanations:
  - `Twitter twitter = new Twitter();`
  - `twitter.postTweet(1, 5);` // User 1 posts a new tweet (id = 5).
  - `twitter.getNewsFeed(1);` // User 1's news feed should return a list with [5].
  - `twitter.follow(1, 2);` // User 1 follows user 2.
  - `twitter.postTweet(2, 6);` // User 2 posts a new tweet (id = 6).
  - `twitter.getNewsFeed(1);` // User 1's news feed should return a list with [6, 5].
  - `twitter.unfollow(1, 2);` // User 1 unfollows user 2.
  - `twitter.getNewsFeed(1);` // User 1's news feed should return a list with [5].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store all tweets in a list and then filter the list based on the user's followings when `getNewsFeed` is called.
- Step-by-step breakdown of the solution:
  1. Create a `Twitter` class with methods for `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.
  2. Use a map to store the tweets for each user, where the key is the user ID and the value is a list of tweet IDs.
  3. Use another map to store the followings for each user, where the key is the follower ID and the value is a set of followee IDs.
  4. In the `postTweet` method, add the tweet ID to the list of tweets for the given user.
  5. In the `getNewsFeed` method, iterate over all users, and for each user, check if the given user is following them. If they are, add the user's tweets to the news feed.
  6. In the `follow` method, add the followee ID to the set of followees for the given follower.
  7. In the `unfollow` method, remove the followee ID from the set of followees for the given follower.
- Why this approach comes to mind first: It is a straightforward approach that involves storing all the data and then filtering it as needed.

```cpp
class Twitter {
public:
    map<int, vector<int>> tweets;
    map<int, set<int>> followings;
    int timestamp = 0;

    Twitter() {}

    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back(tweetId);
    }

    vector<int> getNewsFeed(int userId) {
        vector<int> newsFeed;
        for (auto& user : tweets) {
            if (followings[userId].find(user.first) != followings[userId].end() || user.first == userId) {
                for (int tweetId : user.second) {
                    newsFeed.push_back(tweetId);
                }
            }
        }
        sort(newsFeed.begin(), newsFeed.end(), greater<int>());
        return vector<int>(newsFeed.begin(), newsFeed.begin() + min(10, (int)newsFeed.size()));
    }

    void follow(int followerId, int followeeId) {
        followings[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        followings[followerId].erase(followeeId);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of users. This is because in the `getNewsFeed` method, we are iterating over all users and their tweets.
> - **Space Complexity:** $O(n)$, where $n$ is the number of users. This is because we are storing the tweets and followings for each user.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves iterating over all users and their tweets in the `getNewsFeed` method. The space complexity is relatively low because we are only storing the tweets and followings for each user.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to store the tweets for each user, where the priority is the timestamp of the tweet. This allows us to efficiently retrieve the most recent tweets.
- Detailed breakdown of the approach:
  1. Create a `Twitter` class with methods for `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.
  2. Use a map to store the tweets for each user, where the key is the user ID and the value is a priority queue of tuples containing the tweet ID and timestamp.
  3. Use another map to store the followings for each user, where the key is the follower ID and the value is a set of followee IDs.
  4. In the `postTweet` method, add the tweet ID and timestamp to the priority queue of tweets for the given user.
  5. In the `getNewsFeed` method, iterate over the followings of the given user and retrieve the most recent tweets from each followee.
  6. In the `follow` method, add the followee ID to the set of followees for the given follower.
  7. In the `unfollow` method, remove the followee ID from the set of followees for the given follower.
- Proof of optimality: The optimal approach has a time complexity of $O(\log n)$ for the `postTweet` and `getNewsFeed` methods, and $O(1)$ for the `follow` and `unfollow` methods. This is because we are using a priority queue to store the tweets, which allows us to efficiently retrieve the most recent tweets.

```cpp
class Twitter {
public:
    map<int, priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>> tweets;
    map<int, set<int>> followings;
    int timestamp = 0;

    Twitter() {}

    void postTweet(int userId, int tweetId) {
        tweets[userId].push({tweetId, timestamp++});
    }

    vector<int> getNewsFeed(int userId) {
        vector<int> newsFeed;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int followeeId : followings[userId]) {
            if (tweets.find(followeeId) != tweets.end()) {
                pq.push({followeeId, tweets[followeeId].top().second});
            }
        }
        if (tweets.find(userId) != tweets.end()) {
            pq.push({userId, tweets[userId].top().second});
        }
        while (!pq.empty() && newsFeed.size() < 10) {
            int followeeId = pq.top().first;
            pq.pop();
            newsFeed.push_back(tweets[followeeId].top().first);
            tweets[followeeId].pop();
            if (!tweets[followeeId].empty()) {
                pq.push({followeeId, tweets[followeeId].top().second});
            }
        }
        return newsFeed;
    }

    void follow(int followerId, int followeeId) {
        followings[followerId].insert(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        followings[followerId].erase(followeeId);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of tweets. This is because we are using a priority queue to store the tweets, which allows us to efficiently retrieve the most recent tweets.
> - **Space Complexity:** $O(n)$, where $n$ is the number of tweets. This is because we are storing the tweets for each user.
> - **Optimality proof:** The optimal approach has a time complexity of $O(\log n)$ for the `postTweet` and `getNewsFeed` methods, and $O(1)$ for the `follow` and `unfollow` methods. This is because we are using a priority queue to store the tweets, which allows us to efficiently retrieve the most recent tweets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a priority queue to store tweets and efficiently retrieve the most recent tweets.
- Problem-solving patterns identified: Using a map to store the tweets for each user and a set to store the followings for each user.
- Optimization techniques learned: Using a priority queue to reduce the time complexity of the `getNewsFeed` method.
- Similar problems to practice: Designing a social media platform with similar features.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when a user is not following anyone.
- Edge cases to watch for: When a user is not following anyone, their news feed should contain only their own tweets.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the `postTweet`, `getNewsFeed`, `follow`, and `unfollow` methods with different input scenarios.