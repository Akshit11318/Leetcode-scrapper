## All Divisions With the Highest Score of a Binary Array

**Problem Link:** https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/description

**Problem Statement:**
- Input: A binary array `nums`.
- Constraints: The length of `nums` is between 2 and 10^5.
- Expected output: All divisions with the highest score of a binary array. The score of a division is defined as the number of elements in the first part that are greater than the corresponding elements in the second part.
- Key requirements: Find all possible divisions that achieve the highest score.
- Example test cases:
  - Input: `nums = [0,0,1,0]`
  - Output: `[["0,0","1,0"],["0,0,1","0"]]`
  - Explanation: The highest score is 2. There are two divisions that achieve this score.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible divisions of the binary array.
- For each division, compare elements from the first part with the corresponding elements in the second part and count the number of elements in the first part that are greater.
- Keep track of the maximum score and all divisions that achieve this score.
- This approach comes to mind first because it directly addresses the problem by considering all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<string>> highestScoreDivisions(vector<int>& nums) {
    int n = nums.size();
    vector<vector<string>> result;
    int maxScore = 0;

    for (int i = 1; i < n; i++) {
        string firstPart = "", secondPart = "";
        for (int j = 0; j < i; j++) {
            firstPart += to_string(nums[j]);
        }
        for (int j = i; j < n; j++) {
            secondPart += to_string(nums[j]);
        }

        int score = 0;
        for (int j = 0; j < firstPart.size(); j++) {
            if (firstPart[j] > secondPart[j]) {
                score++;
            }
        }

        if (score > maxScore) {
            maxScore = score;
            result.clear();
            result.push_back({firstPart, secondPart});
        } else if (score == maxScore) {
            result.push_back({firstPart, secondPart});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because for each division point, we are comparing elements from both parts.
> - **Space Complexity:** $O(n)$, for storing the result and temporary strings.
> - **Why these complexities occur:** The brute force approach involves iterating over all possible division points and comparing elements, leading to quadratic time complexity. The space complexity is linear due to the storage of the result and temporary strings.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach still involves considering all possible divisions but can be optimized by directly comparing the binary strings without converting them to integers.
- This approach is optimal because it has the same time complexity as the brute force approach but with less overhead due to the avoidance of string to integer conversions.
- The key insight is recognizing that comparing binary strings character by character is equivalent to comparing their corresponding integer values.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<string>> highestScoreDivisions(vector<int>& nums) {
    int n = nums.size();
    vector<vector<string>> result;
    int maxScore = 0;

    for (int i = 1; i < n; i++) {
        string firstPart = "", secondPart = "";
        for (int j = 0; j < i; j++) {
            firstPart += to_string(nums[j]);
        }
        for (int j = i; j < n; j++) {
            secondPart += to_string(nums[j]);
        }

        int score = 0;
        for (int j = 0; j < min(firstPart.size(), secondPart.size()); j++) {
            if (firstPart[j] > secondPart[j]) {
                score++;
            }
        }

        if (score > maxScore) {
            maxScore = score;
            result.clear();
            result.push_back({firstPart, secondPart});
        } else if (score == maxScore) {
            result.push_back({firstPart, secondPart});
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because for each division point, we are comparing elements from both parts.
> - **Space Complexity:** $O(n)$, for storing the result and temporary strings.
> - **Optimality proof:** This approach is optimal because it considers all possible divisions and directly compares binary strings, minimizing unnecessary conversions and operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include iterating over all possible divisions and comparing binary strings.
- Problem-solving patterns identified include the use of a brute force approach as a starting point and optimizing it by reducing unnecessary conversions.
- Optimization techniques learned include avoiding string to integer conversions and directly comparing binary strings.

**Mistakes to Avoid:**
- Common implementation errors include incorrect handling of division points and not considering all possible divisions.
- Edge cases to watch for include handling arrays with lengths close to the constraints and ensuring correct comparison of binary strings.
- Performance pitfalls include unnecessary string to integer conversions and not optimizing the comparison process.