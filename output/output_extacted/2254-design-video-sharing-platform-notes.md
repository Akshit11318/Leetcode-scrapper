## Design Video Sharing Platform

**Problem Link:** https://leetcode.com/problems/design-video-sharing-platform/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a video sharing platform with methods to upload, remove, and watch videos, as well as like and dislike videos.
- Expected output format: The output should be the result of the corresponding method calls.
- Key requirements and edge cases to consider:
  - Video ID should be unique for each video.
  - A user can only like or dislike a video once.
  - A user can watch a video multiple times.
- Example test cases with explanations:
  - Uploading a video and then watching it should return the video's ID.
  - Liking a video should increase the video's like count by 1.
  - Disliking a video should increase the video's dislike count by 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a simple data structure like a map to store video information.
- Step-by-step breakdown of the solution:
  1. Create a map to store video information, where the key is the video ID and the value is a struct containing the video's title, like count, dislike count, and watch count.
  2. Implement the upload method by adding a new video to the map.
  3. Implement the remove method by removing a video from the map.
  4. Implement the watch method by incrementing the watch count of the video.
  5. Implement the like method by incrementing the like count of the video and decrementing the dislike count if the video was previously disliked.
  6. Implement the dislike method by incrementing the dislike count of the video and decrementing the like count if the video was previously liked.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
class VideoSharingPlatform {
public:
    map<int, Video> videos;
    int videoId = 1;

    int uploadVideo(string video) {
        videos[videoId] = {videoId, video, 0, 0, 0};
        return videoId++;
    }

    void removeVideo(int videoId) {
        videos.erase(videoId);
    }

    int watchVideo(int videoId) {
        if (videos.find(videoId) == videos.end()) return -1;
        videos[videoId].watchCount++;
        return videoId;
    }

    void likeVideo(int videoId) {
        if (videos.find(videoId) == videos.end()) return;
        if (videos[videoId].dislikeCount > 0) {
            videos[videoId].dislikeCount--;
        }
        videos[videoId].likeCount++;
    }

    void dislikeVideo(int videoId) {
        if (videos.find(videoId) == videos.end()) return;
        if (videos[videoId].likeCount > 0) {
            videos[videoId].likeCount--;
        }
        videos[videoId].dislikeCount++;
    }
};

struct Video {
    int id;
    string title;
    int likeCount;
    int dislikeCount;
    int watchCount;
    Video(int id, string title, int likeCount, int dislikeCount, int watchCount) 
        : id(id), title(title), likeCount(likeCount), dislikeCount(dislikeCount), watchCount(watchCount) {}
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods, since we are using a map to store video information and each operation takes constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of videos, since we are storing all video information in a map.
> - **Why these complexities occur:** The time complexity is $O(1)$ because map operations take constant time. The space complexity is $O(n)$ because we are storing all video information in a map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal, since we are using a map to store video information and each operation takes constant time.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: The time complexity is already $O(1)$ for all methods, which is optimal.
- Why further optimization is impossible: We are already using the most efficient data structure (map) and each operation takes constant time, so further optimization is not possible.

```cpp
// Same as the brute force approach
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for all methods, since we are using a map to store video information and each operation takes constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of videos, since we are storing all video information in a map.
> - **Optimality proof:** The time complexity is already $O(1)$ for all methods, which is optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store video information and each operation takes constant time.
- Problem-solving patterns identified: Using a map to store information and each operation takes constant time.
- Optimization techniques learned: Using the most efficient data structure (map) and each operation takes constant time.
- Similar problems to practice: Problems that involve storing and retrieving information using a map.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a video exists before watching, liking, or disliking it.
- Edge cases to watch for: When a video is removed, we should not be able to watch, like, or dislike it.
- Performance pitfalls: Using a data structure that takes more than constant time for each operation.
- Testing considerations: We should test the platform with different scenarios, such as uploading, removing, watching, liking, and disliking videos.