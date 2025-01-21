## Minimize Max Distance to Gas Station

**Problem Link:** https://leetcode.com/problems/minimize-max-distance-to-gas-station/description

**Problem Statement:**
- Input format: `stations`, an array of integers representing the positions of gas stations, and `K`, an integer representing the maximum number of new gas stations that can be built.
- Constraints: `10 <= stations.length <= 10^5`, `0 <= stations[i] <= 10^8`, `stations[i] < stations[i + 1]`, `1 <= K <= stations.length - 1`.
- Expected output format: The minimum possible maximum distance between adjacent gas stations after adding at most `K` new stations.
- Key requirements and edge cases to consider:
  - The distance between two adjacent gas stations is the difference between their positions.
  - New gas stations can be built anywhere between two existing gas stations.
  - The goal is to minimize the maximum distance between any two adjacent gas stations after adding new stations.
- Example test cases with explanations:
  - Example 1: `stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9`, Output: `0`. Explanation: We can build a new station at each integer point from `1` to `10`, resulting in a maximum distance of `0`.
  - Example 2: `stations = [23, 34, 60, 98, 122], K = 3`, Output: `20`. Explanation: We can build new stations at positions `43`, `73`, and `103`, resulting in a maximum distance of `20`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of adding new gas stations between existing ones.
- We calculate the maximum distance between any two adjacent stations after adding each combination of new stations.
- We keep track of the minimum maximum distance found across all combinations.

```cpp
class Solution {
public:
    int minmaxGasDist(vector<int>& stations, int K) {
        int n = stations.size();
        vector<int> dists;
        for (int i = 0; i < n - 1; i++) {
            dists.push_back(stations[i + 1] - stations[i]);
        }
        int minDist = INT_MAX;
        for (int mask = 0; mask < (1 << (n - 1)); mask++) {
            if (__builtin_popcount(mask) > K) continue;
            vector<int> newDists = dists;
            for (int i = 0; i < n - 1; i++) {
                if ((mask & (1 << i))) {
                    newDists[i] /= 2;
                }
            }
            int maxDist = *max_element(newDists.begin(), newDists.end());
            minDist = min(minDist, maxDist);
        }
        return minDist;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1} \cdot n)$, where $n$ is the number of gas stations. This is because we generate all possible masks of length $n-1$ and for each mask, we calculate the maximum distance.
> - **Space Complexity:** $O(n)$, as we store the distances between adjacent gas stations.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to generating all possible masks, and a linear space complexity due to storing the distances.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search approach to find the minimum maximum distance.
- We define a function `possible` that checks if it's possible to achieve a maximum distance of `mid` by adding at most `K` new gas stations.
- We use binary search to find the minimum `mid` for which `possible` returns `true`.

```cpp
class Solution {
public:
    int minmaxGasDist(vector<int>& stations, int K) {
        int n = stations.size();
        int low = 1, high = stations[n - 1] - stations[0];
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (possible(stations, K, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
    
    bool possible(vector<int>& stations, int K, int mid) {
        int count = 0;
        for (int i = 0; i < stations.size() - 1; i++) {
            count += (stations[i + 1] - stations[i] - 1) / mid;
        }
        return count <= K;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log D)$, where $n$ is the number of gas stations and $D$ is the maximum possible distance between two gas stations. This is because we perform a binary search over the range of possible distances.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `low`, `high`, and `mid` variables.
> - **Optimality proof:** This approach is optimal because it uses a binary search to find the minimum maximum distance, which reduces the search space exponentially. The `possible` function checks if it's possible to achieve a maximum distance of `mid` by adding at most `K` new gas stations, which ensures that the solution is correct.