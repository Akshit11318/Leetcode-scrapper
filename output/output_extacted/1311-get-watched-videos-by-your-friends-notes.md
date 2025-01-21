## Get Watched Videos by Your Friends
**Problem Link:** https://leetcode.com/problems/get-watched-videos-by-your-friends/description

**Problem Statement:**
- Input format and constraints: You are given a list of watched videos by your friends and their friends. The list is represented as a 2D array `watchedVideosByFriends`, where `watchedVideosByFriends[i]` is a list of videos watched by the friends of friend `i`. 
- Expected output format: Return the list of videos watched by your friends, sorted in ascending order by video name.
- Key requirements and edge cases to consider: 
    - If two videos have the same name, they should be treated as the same video.
    - If a video is watched by multiple friends, it should only appear once in the output list.
- Example test cases with explanations: 
    - For example, if `watchedVideosByFriends = [["A","B"],["C"],["B","C"]]`, the output should be `["B","C"]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The simplest way to solve this problem is to iterate through the list of watched videos by each friend and add each video to a set to remove duplicates. Then, we can convert the set to a list and sort it.
- Step-by-step breakdown of the solution:
    1. Create an empty set to store unique videos.
    2. Iterate through the list of watched videos by each friend.
    3. For each friend, iterate through the list of videos they have watched and add each video to the set.
    4. Convert the set to a list and sort it.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideosByFriends, int numFriends, int friendId, int level, vector<vector<int>>& friendships) {
        unordered_set<string> uniqueVideos;
        unordered_set<int> visited;
        visited.insert(friendId);
        
        queue<int> q;
        q.push(friendId);
        
        for (int i = 0; i < level; i++) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int currentFriend = q.front();
                q.pop();
                
                for (auto& video : watchedVideosByFriends[currentFriend]) {
                    uniqueVideos.insert(video);
                }
                
                for (auto& friendship : friendships) {
                    if (friendship[0] == currentFriend && visited.find(friendship[1]) == visited.end()) {
                        q.push(friendship[1]);
                        visited.insert(friendship[1]);
                    } else if (friendship[1] == currentFriend && visited.find(friendship[0]) == visited.end()) {
                        q.push(friendship[0]);
                        visited.insert(friendship[0]);
                    }
                }
            }
        }
        
        vector<string> result(uniqueVideos.begin(), uniqueVideos.end());
        sort(result.begin(), result.end());
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$, where $n$ is the number of friends, $m$ is the number of videos watched by each friend, and $k$ is the level of friends.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of friends and $m$ is the number of videos watched by each friend.
> - **Why these complexities occur:** The time complexity occurs because we are iterating through the list of watched videos by each friend and adding each video to a set. The space complexity occurs because we are storing the unique videos in a set.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a queue to keep track of the friends at each level and a set to store the unique videos.
- Detailed breakdown of the approach:
    1. Create an empty set to store unique videos and an empty queue to store the friends at each level.
    2. Add the given friend to the queue and mark them as visited.
    3. Iterate through the queue and for each friend, add their watched videos to the set and their unvisited friends to the queue.
    4. Repeat step 3 until we have processed all friends at the given level.
    5. Convert the set to a list and sort it.
- Proof of optimality: This approach is optimal because we are only visiting each friend once and adding each video to the set once.

```cpp
class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideosByFriends, int numFriends, int friendId, int level, vector<vector<int>>& friendships) {
        unordered_set<string> uniqueVideos;
        unordered_set<int> visited;
        visited.insert(friendId);
        
        queue<int> q;
        q.push(friendId);
        
        for (int i = 0; i < level; i++) {
            int size = q.size();
            for (int j = 0; j < size; j++) {
                int currentFriend = q.front();
                q.pop();
                
                if (i == level - 1) {
                    for (auto& video : watchedVideosByFriends[currentFriend]) {
                        uniqueVideos.insert(video);
                    }
                }
                
                for (auto& friendship : friendships) {
                    if (friendship[0] == currentFriend && visited.find(friendship[1]) == visited.end()) {
                        q.push(friendship[1]);
                        visited.insert(friendship[1]);
                    } else if (friendship[1] == currentFriend && visited.find(friendship[0]) == visited.end()) {
                        q.push(friendship[0]);
                        visited.insert(friendship[0]);
                    }
                }
            }
        }
        
        vector<string> result(uniqueVideos.begin(), uniqueVideos.end());
        sort(result.begin(), result.end());
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$, where $n$ is the number of friends, $m$ is the number of videos watched by each friend, and $k$ is the level of friends.
> - **Space Complexity:** $O(n \times m)$, where $n$ is the number of friends and $m$ is the number of videos watched by each friend.
> - **Optimality proof:** This approach is optimal because we are only visiting each friend once and adding each video to the set once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a queue to keep track of the friends at each level and a set to store the unique videos.
- Problem-solving patterns identified: Using a queue to process the friends at each level and a set to store the unique videos.
- Optimization techniques learned: Using a queue to avoid visiting each friend multiple times and a set to avoid adding each video multiple times.
- Similar problems to practice: Problems that involve processing a graph or network, such as finding the shortest path between two nodes or finding the minimum spanning tree of a graph.

**Mistakes to Avoid:**
- Common implementation errors: Not marking the friends as visited, not checking if a friend has already been visited before adding them to the queue.
- Edge cases to watch for: The case where a friend has no watched videos, the case where a friend has no friends.
- Performance pitfalls: Using a recursive approach instead of an iterative approach, not using a set to store the unique videos.
- Testing considerations: Testing the function with different inputs, such as different numbers of friends, different numbers of videos, and different levels of friends.