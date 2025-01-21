## Find Beautiful Indices in the Given Array I
**Problem Link:** https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description

**Problem Statement:**
- Input format: An array `nums` of integers and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5` and `0 <= k <= 10^5`.
- Expected output format: A vector of integers representing the beautiful indices in the array.
- Key requirements: An index `i` is beautiful if the number of elements in the array that are greater than `nums[i]` is exactly `k`.
- Edge cases to consider: Empty array, single-element array, array with duplicate elements.
- Example test cases:
  - `nums = [1, 2, 3, 4], k = 1`, expected output: `[1, 2]`.
  - `nums = [1, 1, 2, 2], k = 2`, expected output: `[0, 1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each index `i` in the array, count the number of elements that are greater than `nums[i]`.
- Step-by-step breakdown of the solution:
  1. Iterate over each index `i` in the array.
  2. For each `i`, iterate over the entire array to count the number of elements greater than `nums[i]`.
  3. If the count is equal to `k`, add `i` to the result vector.
- Why this approach comes to mind first: It directly checks the condition for each index.

```cpp
vector<int> beautifulArray(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        int count = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] > nums[i]) count++;
        }
        if (count == k) result.push_back(i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array, because for each element, we are potentially scanning the entire array.
> - **Space Complexity:** $O(n)$, for storing the result vector in the worst case when all indices are beautiful.
> - **Why these complexities occur:** The nested loop structure causes the quadratic time complexity, and the need to store all beautiful indices in the worst case leads to linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a single pass through the array to count the occurrences of each number and then calculate the number of elements greater than each number.
- Detailed breakdown of the approach:
  1. Count the occurrences of each number in the array using a hashmap.
  2. Calculate the number of elements greater than each number by summing the counts of all larger numbers.
  3. For each index, check if the calculated count equals `k`.
- Proof of optimality: This approach reduces the time complexity to linear because it avoids the nested loop structure of the brute force approach.

```cpp
vector<int> beautifulArray(vector<int>& nums, int k) {
    vector<int> result;
    unordered_map<int, int> countMap;
    for (int num : nums) {
        countMap[num]++;
    }
    
    for (int i = 0; i < nums.size(); i++) {
        int greaterCount = 0;
        for (auto& pair : countMap) {
            if (pair.first > nums[i]) {
                greaterCount += pair.second;
            }
        }
        if (greaterCount == k) {
            result.push_back(i);
        }
    }
    return result;
}
```

However, this solution still has a high time complexity due to the inner loop over the hashmap. We can further optimize it by sorting the array and then using a binary search or a two-pointer technique to find the count of elements greater than each number.

```cpp
vector<int> beautifulArray(vector<int>& nums, int k) {
    vector<int> result;
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    
    for (int i = 0; i < nums.size(); i++) {
        int greaterCount = upper_bound(sortedNums.begin(), sortedNums.end(), nums[i]) - sortedNums.begin();
        greaterCount = sortedNums.size() - greaterCount;
        if (greaterCount == k) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the array, due to the sorting step.
> - **Space Complexity:** $O(n)$, for storing the sorted array and the result vector.
> - **Optimality proof:** This is the best time complexity achievable for this problem because we must at least read the input array, and any comparison-based sorting algorithm has a lower bound of $O(n \log n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Hashmap for counting occurrences, sorting for efficient comparison, and binary search for finding counts.
- Problem-solving patterns: Breaking down the problem into smaller sub-problems (counting occurrences, calculating greater counts) and combining solutions.
- Optimization techniques: Avoiding nested loops, using efficient data structures (hashmap, sorted array), and applying algorithmic techniques (binary search).

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating counts, missing edge cases (empty array, duplicate elements).
- Edge cases to watch for: Handling arrays with duplicate elements, ensuring the solution works for the smallest and largest possible inputs.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various inputs, including edge cases, to ensure correctness and efficiency.