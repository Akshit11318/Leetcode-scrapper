## Count Artist Occurrences on Spotify Ranking List

**Problem Link:** https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/description

**Problem Statement:**
- Input format and constraints: Given a list of songs where each song is represented by a unique `song_id` and the `artist_id` of the artist who performed the song. 
- Expected output format: Return a list of tuples where each tuple contains an `artist_id` and the number of times the artist appears in the input list.
- Key requirements and edge cases to consider: 
    - Each song has a unique `song_id`.
    - An artist can have multiple songs in the list.
    - The input list can be empty.
- Example test cases with explanations: 
    - Input: `songs = [[1,1],[2,1],[3,2]]`
      Output: `[[1,2],[2,1]]`
      Explanation: Artist 1 has two songs, and artist 2 has one song.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate through the list of songs and count the occurrences of each artist.
- Step-by-step breakdown of the solution:
    1. Initialize an empty map to store the count of each artist.
    2. Iterate through the list of songs.
    3. For each song, get the artist's ID and increment the count in the map.
    4. After iterating through all songs, convert the map to a list of tuples and return it.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It directly addresses the problem statement by counting the occurrences of each artist.

```cpp
#include <iostream>
#include <vector>
#include <map>

vector<vector<int>> artistCount(vector<vector<int>>& songs) {
    // Initialize an empty map to store the count of each artist
    map<int, int> artistMap;

    // Iterate through the list of songs
    for (auto& song : songs) {
        // Get the artist's ID and increment the count in the map
        artistMap[song[1]]++;
    }

    // Convert the map to a list of tuples and return it
    vector<vector<int>> result;
    for (auto& pair : artistMap) {
        result.push_back({pair.first, pair.second});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of songs. This is because we iterate through the list of songs once.
> - **Space Complexity:** $O(m)$ where $m$ is the number of unique artists. This is because we use a map to store the count of each artist.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate through each song to count the occurrences of each artist. The space complexity occurs because we need to store the count of each artist in a map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal for this problem because we need to iterate through each song to count the occurrences of each artist.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach. We use a map to store the count of each artist and iterate through the list of songs to increment the count.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem. We need to iterate through each song at least once to count the occurrences of each artist.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate through each song to count the occurrences of each artist. Any approach that tries to avoid iterating through each song will not be able to accurately count the occurrences of each artist.

```cpp
#include <iostream>
#include <vector>
#include <map>

vector<vector<int>> artistCount(vector<vector<int>>& songs) {
    // Initialize an empty map to store the count of each artist
    map<int, int> artistMap;

    // Iterate through the list of songs
    for (auto& song : songs) {
        // Get the artist's ID and increment the count in the map
        artistMap[song[1]]++;
    }

    // Convert the map to a list of tuples and return it
    vector<vector<int>> result;
    for (auto& pair : artistMap) {
        result.push_back({pair.first, pair.second});
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of songs.
> - **Space Complexity:** $O(m)$ where $m$ is the number of unique artists.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to count the occurrences of each artist.
- Problem-solving patterns identified: Iterating through a list to count the occurrences of each item.
- Optimization techniques learned: Using a map to store the count of each artist instead of using a list or array.
- Similar problems to practice: Counting the occurrences of each item in a list, finding the most frequent item in a list.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the map before using it, not checking if the artist is already in the map before incrementing the count.
- Edge cases to watch for: An empty list of songs, a list with no unique artists.
- Performance pitfalls: Using a list or array to store the count of each artist instead of using a map.
- Testing considerations: Testing with an empty list of songs, testing with a list with no unique artists, testing with a list with a large number of unique artists.