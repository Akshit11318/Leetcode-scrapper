## Design an Array Statistics Tracker
**Problem Link:** https://leetcode.com/problems/design-an-array-statistics-tracker/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a class `ArrayStatisticsTracker` that supports two operations: `insert` and `getStatistics`. The `insert` operation adds a number to the data structure, and the `getStatistics` operation returns an array containing the minimum, maximum, mean, median, and mode of the current numbers.
- Expected output format: The `getStatistics` method should return an array of length 5, where the elements represent the minimum, maximum, mean, median, and mode of the current numbers, respectively.
- Key requirements and edge cases to consider: The class should handle duplicate numbers, empty data, and large inputs efficiently.
- Example test cases with explanations:
  - Example 1: `insert(1)`, `insert(2)`, `insert(3)`, `getStatistics()`. The output should be `[1, 3, 2.0, 2.0, 1]`.
  - Example 2: `insert(1)`, `insert(2)`, `insert(2)`, `getStatistics()`. The output should be `[1, 2, 1.6666666666666667, 2.0, 2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to store all the inserted numbers in a vector and calculate the statistics on the fly whenever the `getStatistics` method is called.
- Step-by-step breakdown of the solution:
  1. Store all inserted numbers in a vector.
  2. When `getStatistics` is called, calculate the minimum, maximum, mean, median, and mode of the numbers in the vector.

```cpp
class ArrayStatisticsTracker {
public:
    vector<int> nums;
    
    void insert(int num) {
        nums.push_back(num);
    }
    
    vector<double> getStatistics() {
        int minVal = INT_MAX, maxVal = INT_MIN;
        double sum = 0;
        for (int num : nums) {
            minVal = min(minVal, num);
            maxVal = max(maxVal, num);
            sum += num;
        }
        double mean = sum / nums.size();
        
        // Sort the vector to calculate the median
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        double median;
        if (sortedNums.size() % 2 == 0) {
            median = (sortedNums[sortedNums.size() / 2 - 1] + sortedNums[sortedNums.size() / 2]) / 2.0;
        } else {
            median = sortedNums[sortedNums.size() / 2];
        }
        
        // Calculate the mode
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        int mode = nums[0], maxFreq = freq[nums[0]];
        for (auto& pair : freq) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second;
                mode = pair.first;
            }
        }
        
        return {static_cast<double>(minVal), static_cast<double>(maxVal), mean, median, static_cast<double>(mode)};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `insert` method and $O(n \log n)$ for the `getStatistics` method due to sorting.
> - **Space Complexity:** $O(n)$ for storing the inserted numbers.
> - **Why these complexities occur:** The brute force approach requires sorting the entire vector to calculate the median, which leads to a higher time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: To improve the time complexity, we can use a data structure that allows efficient calculation of the minimum, maximum, mean, median, and mode. A combination of a balanced binary search tree (e.g., `set` or `multiset`) and an unordered map can be used.
- Detailed breakdown of the approach:
  1. Store the inserted numbers in a `multiset` to maintain the order and calculate the median efficiently.
  2. Use an unordered map to store the frequency of each number and calculate the mode.
  3. Calculate the minimum, maximum, and mean on the fly when the `getStatistics` method is called.

```cpp
class ArrayStatisticsTracker {
public:
    multiset<int> nums;
    unordered_map<int, int> freq;
    double sum = 0;
    
    void insert(int num) {
        nums.insert(num);
        freq[num]++;
        sum += num;
    }
    
    vector<double> getStatistics() {
        double minVal = *nums.begin();
        double maxVal = *nums.rbegin();
        double mean = sum / nums.size();
        
        double median;
        if (nums.size() % 2 == 0) {
            auto it = nums.begin();
            advance(it, nums.size() / 2 - 1);
            median = (*it + *next(it)) / 2.0;
        } else {
            auto it = nums.begin();
            advance(it, nums.size() / 2);
            median = *it;
        }
        
        int mode = nums.begin()->first;
        int maxFreq = freq[nums.begin()->first];
        for (auto& pair : freq) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second;
                mode = pair.first;
            }
        }
        
        return {minVal, maxVal, mean, median, static_cast<double>(mode)};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$ for the `insert` method and $O(n)$ for the `getStatistics` method.
> - **Space Complexity:** $O(n)$ for storing the inserted numbers.
> - **Optimality proof:** The optimal approach uses a balanced binary search tree and an unordered map, which allows efficient calculation of the statistics. Further optimization is impossible because we need to store all the inserted numbers to calculate the statistics accurately.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a combination of data structures to optimize the solution.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using efficient data structures to solve them.
- Optimization techniques learned: Using a balanced binary search tree and an unordered map to improve the time complexity.
- Similar problems to practice: Designing data structures to solve other statistical problems, such as calculating the standard deviation or variance.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty data structure or duplicate numbers.
- Edge cases to watch for: Handling the case where the data structure is empty or contains duplicate numbers.
- Performance pitfalls: Using inefficient data structures or algorithms, such as sorting the entire vector to calculate the median.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure it works correctly.