## Video Stitching

**Problem Link:** [https://leetcode.com/problems/video-stitching/description](https://leetcode.com/problems/video-stitching/description)

**Problem Statement:**
- Input format: You are given a list of clips, where each clip is a pair of integers representing the start and end time of a video clip.
- Constraints: The start time of a clip is always less than or equal to the end time.
- Expected output format: The minimum number of clips needed to cover the entire video.
- Key requirements and edge cases to consider: 
  - The video starts at time 0 and ends at time T.
  - If it's impossible to cover the entire video, return -1.
- Example test cases with explanations:
  - Example 1: Input: `clips = [[0,2],[4,6],[8,10],[1,9]]`, T = 10. Output: 3. Explanation: We can cover the video by taking the clips [0,2], [8,10], and [1,9].
  - Example 2: Input: `clips = [[0,1],[1,2]]`, T = 5. Output: -1. Explanation: We can't cover the entire video.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of clips to cover the video.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of clips.
  2. For each combination, check if it covers the entire video.
  3. If a combination covers the entire video, calculate its length (number of clips).
  4. Keep track of the minimum length combination that covers the entire video.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

int videoStitchingBrute(vector<vector<int>>& clips, int T) {
    // Generate all possible combinations of clips
    int n = clips.size();
    int minClips = INT_MAX;
    for (int mask = 0; mask < (1 << n); mask++) {
        int start = 0, end = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (clips[i][0] <= start) {
                    end = max(end, clips[i][1]);
                    count++;
                }
            }
        }
        if (end >= T) {
            minClips = min(minClips, count);
        }
    }
    return minClips == INT_MAX ? -1 : minClips;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of clips. This is because we generate all possible combinations of clips (2^n) and for each combination, we iterate over the clips (n).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum length combination.
> - **Why these complexities occur:** The time complexity is high because we exhaustively search all possible combinations of clips. The space complexity is low because we only keep track of a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. The idea is to always choose the clip that covers the most new area.
- Detailed breakdown of the approach:
  1. Sort the clips by their start time.
  2. Initialize the current end time and the number of clips used.
  3. Iterate over the sorted clips. For each clip, if its start time is less than or equal to the current end time, update the current end time to be the maximum of the current end time and the clip's end time.
  4. If the current end time is greater than the previous end time, increment the number of clips used.
- Proof of optimality: This approach is optimal because it always chooses the clip that covers the most new area, which minimizes the number of clips needed.

```cpp
int videoStitchingOptimal(vector<vector<int>>& clips, int T) {
    sort(clips.begin(), clips.end());
    int n = clips.size();
    int count = 0, start = 0, end = 0;
    for (int i = 0; i < n; i++) {
        if (start == end) {
            if (clips[i][0] > end) return -1;
            start = end;
            end = clips[i][1];
            count++;
        } else {
            end = max(end, clips[i][1]);
        }
    }
    if (end < T) return -1;
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of clips. This is because we sort the clips (n log n) and then iterate over them (n).
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current end time and the number of clips used.
> - **Optimality proof:** This approach is optimal because it always chooses the clip that covers the most new area, which minimizes the number of clips needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Always choose the option that covers the most new area.
- Optimization techniques learned: Avoid exhaustive search by using a greedy approach.
- Similar problems to practice: Other problems that involve covering a range with minimum number of intervals.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where it's impossible to cover the entire video.
- Edge cases to watch for: When the start time of a clip is greater than the end time of the previous clip.
- Performance pitfalls: Using an exhaustive search approach.
- Testing considerations: Test the function with different inputs, including edge cases.