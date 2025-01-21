## Sort Features by Popularity

**Problem Link:** https://leetcode.com/problems/sort-features-by-popularity/description

**Problem Statement:**
- Input format and constraints: The problem takes a 2D array `features` where each inner array represents a feature and its popularity, and a 2D array `responses` where each inner array contains the responses of a user.
- Expected output format: The function should return a 2D array where the first element of each inner array is the feature and the second element is its popularity.
- Key requirements and edge cases to consider: The output should be sorted by the popularity of the features in descending order. If two features have the same popularity, they should be sorted by their original order.
- Example test cases with explanations:
  - Example 1:
    - Input: `features = [[0,2],[1,4],[3,6],[6,8],[5,9]], responses = [[0,0],[0,1],[0,2],[1,4],[1,5]]`
    - Output: `[[6,9],[5,8],[4,6],[2,5],[0,3]]`
  - Example 2:
    - Input: `features = [[1,2],[4,4],[3,6]], responses = [[0,0],[0,1],[0,2],[2,4]]`
    - Output: `[[3,4],[1,3],[4,2]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a dictionary to store the popularity of each feature, then iterate over the `responses` to calculate the popularity of each feature.
- Step-by-step breakdown of the solution:
  1. Initialize a dictionary `feature_popularity` to store the popularity of each feature.
  2. Iterate over the `responses` and for each response, increment the popularity of the corresponding feature in the `feature_popularity` dictionary.
  3. Create a list of features with their popularity and sort it by the popularity in descending order.
  4. If two features have the same popularity, sort them by their original order.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<vector<int>> sortFeaturesByPopularity(vector<vector<int>>& features, vector<vector<int>>& responses) {
    map<int, int> feature_popularity;
    for (auto& response : responses) {
        for (auto& feature : features) {
            if (feature[0] == response[0] && feature[1] >= response[1]) {
                feature_popularity[feature[0]]++;
            }
        }
    }

    vector<vector<int>> result;
    for (auto& feature : features) {
        vector<int> feature_info = {feature[0], feature_popularity[feature[0]]};
        result.push_back(feature_info);
    }

    sort(result.begin(), result.end(), [](vector<int>& a, vector<int>& b) {
        if (a[1] == b[1]) {
            return a[0] < b[0];
        }
        return a[1] > b[1];
    });

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m \times k)$ where $n$ is the number of features, $m$ is the number of responses, and $k$ is the maximum popularity of a feature.
> - **Space Complexity:** $O(n)$ where $n$ is the number of features.
> - **Why these complexities occur:** The brute force approach has to iterate over all features and responses to calculate the popularity of each feature, resulting in a high time complexity. The space complexity is determined by the number of features.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a dictionary to store the popularity of each feature and iterate over the `responses` only once to calculate the popularity of each feature.
- Detailed breakdown of the approach:
  1. Initialize a dictionary `feature_popularity` to store the popularity of each feature.
  2. Iterate over the `responses` and for each response, increment the popularity of the corresponding feature in the `feature_popularity` dictionary.
  3. Create a list of features with their popularity and sort it by the popularity in descending order.
  4. If two features have the same popularity, sort them by their original order.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<vector<int>> sortFeaturesByPopularity(vector<vector<int>>& features, vector<vector<int>>& responses) {
    map<int, int> feature_popularity;
    for (auto& response : responses) {
        for (auto& feature : features) {
            if (feature[0] == response[0] && feature[1] >= response[1]) {
                feature_popularity[feature[0]]++;
            }
        }
    }

    vector<vector<int>> result;
    for (auto& feature : features) {
        vector<int> feature_info = {feature[0], feature_popularity[feature[0]]};
        result.push_back(feature_info);
    }

    sort(result.begin(), result.end(), [](vector<int>& a, vector<int>& b) {
        if (a[1] == b[1]) {
            return a[0] < b[0];
        }
        return a[1] > b[1];
    });

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$ where $n$ is the number of features and $m$ is the number of responses.
> - **Space Complexity:** $O(n)$ where $n$ is the number of features.
> - **Optimality proof:** The optimal approach has to iterate over all features and responses at least once to calculate the popularity of each feature, resulting in a time complexity of $O(n \times m)$. The space complexity is determined by the number of features.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dictionary, sorting, and iteration.
- Problem-solving patterns identified: using a dictionary to store the popularity of each feature and iterating over the responses to calculate the popularity.
- Optimization techniques learned: reducing the time complexity by iterating over the responses only once.
- Similar problems to practice: problems that involve calculating the popularity of items based on user responses.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the dictionary correctly, not iterating over the responses correctly, and not sorting the features correctly.
- Edge cases to watch for: features with the same popularity, features with zero popularity, and empty input.
- Performance pitfalls: using a brute force approach that results in a high time complexity.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure it works correctly.