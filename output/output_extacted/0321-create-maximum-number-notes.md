## Create Maximum Number
**Problem Link:** https://leetcode.com/problems/create-maximum-number/description

**Problem Statement:**
- Given two arrays `nums1` and `nums2`, and an integer `k`, return the maximum number that can be formed by concatenating `k` numbers from the two arrays.
- Input format: Two integer arrays `nums1` and `nums2`, and an integer `k`.
- Expected output format: The maximum number that can be formed by concatenating `k` numbers from the two arrays.
- Key requirements and edge cases to consider:
  - The numbers in the arrays can be negative.
  - The numbers in the arrays can have different numbers of digits.
  - `k` can be less than or equal to the total number of elements in the two arrays.
- Example test cases with explanations:
  - `nums1 = [3, 4, 6, 5]`, `nums2 = [9, 1, 2, 5, 8, 3]`, `k = 5`
    - The maximum number that can be formed is `98653`.
  - `nums1 = [6, 7]`, `nums2 = [6, 0, 4]`, `k = 5`
    - The maximum number that can be formed is `740`.
  - `nums1 = [3, 9]`, `nums2 = [8, 9]`, `k = 3`
    - The maximum number that can be formed is `989`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of `k` numbers from the two arrays and find the maximum number that can be formed.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `k` numbers from the two arrays.
  2. For each combination, concatenate the numbers to form a single number.
  3. Compare the numbers formed by each combination and find the maximum number.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions and finds the best one.

```cpp
class Solution {
public:
    string maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<string> candidates;
        for (int i = 0; i <= k; i++) {
            vector<int> candidate1 = getKMax(nums1, i);
            vector<int> candidate2 = getKMax(nums2, k - i);
            vector<int> candidate;
            candidate.insert(candidate.end(), candidate1.begin(), candidate1.end());
            candidate.insert(candidate.end(), candidate2.begin(), candidate2.end());
            string str;
            for (int num : candidate) {
                str += to_string(num);
            }
            candidates.push_back(str);
        }
        string maxStr = "";
        for (string str : candidates) {
            if (str > maxStr) {
                maxStr = str;
            }
        }
        return maxStr;
    }
    
    vector<int> getKMax(vector<int>& nums, int k) {
        if (k == 0) return {};
        vector<int> result;
        int drop = nums.size() - k;
        for (int i = 0; i < nums.size(); i++) {
            while (result.size() > 0 && drop > 0 && result.back() < nums[i]) {
                result.pop_back();
                drop--;
            }
            result.push_back(nums[i]);
        }
        result.resize(k);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot n \cdot m)$, where $n$ and $m$ are the sizes of the input arrays.
> - **Space Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of the input arrays.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible combinations of `k` numbers from the two arrays and compare them. The space complexity occurs because we store the candidates and the result.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a two-pointer technique to compare the numbers in the two arrays and find the maximum number that can be formed.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one for each array, to the beginning of the arrays.
  2. Compare the numbers at the current positions of the two pointers.
  3. If the number at the current position of the first pointer is greater than the number at the current position of the second pointer, move the first pointer forward.
  4. Otherwise, move the second pointer forward.
  5. Repeat steps 2-4 until one of the pointers reaches the end of its array.
  6. The remaining numbers in the other array are appended to the result.
- Proof of optimality: The two-pointer technique ensures that we compare all possible combinations of `k` numbers from the two arrays and find the maximum number that can be formed.

```cpp
class Solution {
public:
    string maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        string maxStr = "";
        for (int i = 0; i <= k; i++) {
            string candidate1 = getKMax(nums1, i);
            string candidate2 = getKMax(nums2, k - i);
            string candidate = max(candidate1 + candidate2, candidate2 + candidate1);
            if (candidate > maxStr) {
                maxStr = candidate;
            }
        }
        return maxStr;
    }
    
    string getKMax(vector<int>& nums, int k) {
        if (k == 0) return "";
        string result;
        int drop = nums.size() - k;
        for (int i = 0; i < nums.size(); i++) {
            while (result.size() > 0 && drop > 0 && result.back() < '0' + nums[i]) {
                result.pop_back();
                drop--;
            }
            result += to_string(nums[i]);
        }
        result.resize(k);
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of the input arrays.
> - **Space Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of the input arrays.
> - **Optimality proof:** The two-pointer technique ensures that we compare all possible combinations of `k` numbers from the two arrays and find the maximum number that can be formed.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the two-pointer technique.
- The problem-solving pattern identified is the use of dynamic programming to find the maximum number that can be formed.
- The optimization technique learned is the use of a two-pointer technique to compare the numbers in the two arrays.

**Mistakes to Avoid:**
- A common implementation error is to forget to handle the case where one of the pointers reaches the end of its array.
- An edge case to watch for is when the input arrays are empty.
- A performance pitfall is to use a brute force approach that tries all possible combinations of `k` numbers from the two arrays.