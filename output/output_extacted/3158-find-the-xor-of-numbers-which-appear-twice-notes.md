## Find the XOR of Numbers Which Appear Twice
**Problem Link:** https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums`, find the XOR of all the numbers that appear twice in the array.
- Expected output format: The XOR of all the numbers that appear twice.
- Key requirements and edge cases to consider: All numbers in the array are non-negative integers, and the array contains at least one pair of numbers that appear twice.
- Example test cases with explanations:
  - Example 1: Input: `nums = [2, 3, 1, 2]`, Output: `6` (Explanation: `2` appears twice, and `2 XOR 2 = 0`. However, there is no other number that appears twice, so the XOR of all numbers that appear twice is `0 XOR 2 XOR 2 = 2 XOR 2 = 0`, but since 2 appears twice, we can also consider the XOR with another number that appears twice, which in this case is not present, but the given example in the question has a different array `[2,1,2]` with output `2`, hence `2 XOR 2 = 0`, and `0 XOR 1 = 1` is not the correct answer, but `2` appears twice so `2 XOR 2 = 0` and `0 XOR 2 = 2` hence `2` is the answer, as there are no other numbers that appear twice)
  - Example 2: Input: `nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]`, Output: `1` (Explanation: `1` appears twice, and `1 XOR 1 = 0`. However, there is no other number that appears twice, so the XOR of all numbers that appear twice is `1 XOR 1 = 0`, but since `1` appears twice, we consider the XOR with `1` itself, hence `1` is the answer)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the XOR of all numbers that appear twice, we can first identify all the numbers that appear twice and then calculate their XOR.
- Step-by-step breakdown of the solution:
  1. Create a frequency map of the numbers in the array.
  2. Identify the numbers that appear twice.
  3. Calculate the XOR of these numbers.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves counting the frequency of each number and then calculating the XOR of the numbers that appear twice.

```cpp
vector<int> findDuplicates(vector<int>& nums) {
    unordered_map<int, int> freqMap;
    for (int num : nums) {
        if (freqMap.find(num) != freqMap.end()) {
            freqMap[num]++;
        } else {
            freqMap[num] = 1;
        }
    }
    int xorResult = 0;
    for (auto& pair : freqMap) {
        if (pair.second == 2) {
            xorResult ^= pair.first;
        }
    }
    return {xorResult};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are scanning the array twice: once to create the frequency map and once to calculate the XOR.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements in the frequency map.
> - **Why these complexities occur:** The time complexity is linear because we are scanning the array a constant number of times. The space complexity is also linear because we are storing the frequency of each number in the array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the XOR of all numbers in the array and the XOR of all numbers from 1 to $n$, where $n$ is the length of the array. The XOR of these two results will give us the XOR of the numbers that appear twice.
- Detailed breakdown of the approach:
  1. Calculate the XOR of all numbers in the array.
  2. Calculate the XOR of all numbers from 1 to $n$.
  3. Calculate the XOR of the results from steps 1 and 2.
- Proof of optimality: This approach is optimal because it only requires scanning the array once and calculating the XOR of numbers from 1 to $n$, which can be done in $O(n)$ time.

```cpp
int findDuplicateXOR(vector<int>& nums) {
    int xorResult = 0;
    for (int num : nums) {
        xorResult ^= num;
    }
    for (int i = 1; i <= nums.size(); i++) {
        xorResult ^= i;
    }
    for (int num : nums) {
        if (nums.count(num) > 1) {
            xorResult ^= num;
        }
    }
    return xorResult;
}
// However this is not the optimal solution as it has extra operations and does not give correct results for all cases

// A better optimal solution would be 
int findDuplicateXOR(vector<int>& nums) {
    int n = nums.size() - 1;
    int xorAll = 0, xorNums = 0;
    for (int i = 1; i <= n; i++) {
        xorAll ^= i;
    }
    for (int num : nums) {
        xorNums ^= num;
    }
    return xorAll ^ xorNums;
}
```
However this will give the XOR of the single number which is present twice in the array if the array is in the format where all numbers from 1 to n are present and one number is duplicate.
For the case when there are numbers which are not in the range from 1 to n and also there can be more than one duplicates.
```cpp
int findDuplicateXOR(vector<int>& nums) {
    unordered_map<int, int> count;
    int xorResult = 0;
    for (int num : nums) {
        count[num]++;
        if (count[num] == 2) {
            xorResult ^= num;
        }
    }
    return xorResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are scanning the array once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements in the frequency map.
> - **Optimality proof:** This approach is optimal because it only requires scanning the array once and calculating the XOR of the numbers that appear twice, which can be done in $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, XOR calculation.
- Problem-solving patterns identified: Identifying duplicates in an array, calculating XOR of duplicates.
- Optimization techniques learned: Reducing the number of scans of the array, using a frequency map to count duplicates.
- Similar problems to practice: Finding the single number in an array that appears only once, finding the first duplicate in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the frequency map correctly, not handling the case where a number appears more than twice.
- Edge cases to watch for: Empty array, array with only one element, array with all elements appearing only once.
- Performance pitfalls: Scanning the array multiple times, using a data structure with high overhead.
- Testing considerations: Test the function with arrays of different sizes, test the function with arrays containing duplicates, test the function with arrays containing no duplicates.