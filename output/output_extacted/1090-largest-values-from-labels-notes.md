## Largest Values From Labels

**Problem Link:** https://leetcode.com/problems/largest-values-from-labels/description

**Problem Statement:**
- Input format: `labels` and `limits` are given as input, where `labels` is a 2D array containing two integers each (label and value), and `limits` is an array of integers representing the limit for each label.
- Expected output format: Return the maximum sum of values that can be obtained by selecting a subset of the labels.
- Key requirements and edge cases to consider: 
    - Each label can only be used once, 
    - The total number of labels used for each label type cannot exceed the corresponding limit in `limits`.
- Example test cases with explanations:
    - Example 1: labels = [[5,4],[6,2]], limits = [3,3]. The maximum sum of values is 10, obtained by selecting the label with value 4 and the label with value 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of labels and calculate the sum of values for each subset.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsets of labels.
    2. For each subset, calculate the sum of values.
    3. For each subset, check if the total number of labels used for each label type exceeds the corresponding limit in `limits`.
    4. If not, update the maximum sum of values.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves checking all possible combinations of labels.

```cpp
class Solution {
public:
    int largestValsFromLabels(vector<vector<int>>& labels, vector<int>& limits) {
        int n = labels.size();
        int m = limits.size();
        int max_sum = 0;
        
        // Generate all possible subsets of labels
        for (int mask = 0; mask < (1 << n); mask++) {
            int sum = 0;
            vector<int> count(m, 0);
            
            // Calculate the sum of values for the current subset
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    sum += labels[i][1];
                    count[labels[i][0]]++;
                }
            }
            
            // Check if the total number of labels used for each label type exceeds the limit
            bool valid = true;
            for (int i = 0; i < m; i++) {
                if (count[i] > limits[i]) {
                    valid = false;
                    break;
                }
            }
            
            // Update the maximum sum of values if the current subset is valid
            if (valid) {
                max_sum = max(max_sum, sum);
            }
        }
        
        return max_sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \times n \times m)$, where $n$ is the number of labels and $m$ is the number of limits. This is because we generate all possible subsets of labels and for each subset, we calculate the sum of values and check if the total number of labels used for each label type exceeds the limit.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of labels and $m$ is the number of limits. This is because we need to store the labels, limits, and the count of labels used for each label type.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible subsets of labels, which has a time complexity of $O(2^n)$. The space complexity occurs because we need to store the labels, limits, and the count of labels used for each label type.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to select the labels with the maximum value first.
- Detailed breakdown of the approach:
    1. Sort the labels in descending order of their values.
    2. Initialize a count array to keep track of the number of labels used for each label type.
    3. Iterate over the sorted labels and select the labels that do not exceed the limit for their label type.
    4. Update the maximum sum of values and the count of labels used for each label type.
- Proof of optimality: The greedy approach ensures that we select the labels with the maximum value first, which maximizes the sum of values. The count array ensures that we do not exceed the limit for each label type.

```cpp
class Solution {
public:
    int largestValsFromLabels(vector<vector<int>>& labels, vector<int>& limits) {
        int m = limits.size();
        int max_sum = 0;
        
        // Sort the labels in descending order of their values
        sort(labels.begin(), labels.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] > b[1];
        });
        
        vector<int> count(m, 0);
        
        // Iterate over the sorted labels and select the labels that do not exceed the limit for their label type
        for (const auto& label : labels) {
            if (count[label[0]] < limits[label[0]]) {
                max_sum += label[1];
                count[label[0]]++;
            }
        }
        
        return max_sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \times m)$, where $n$ is the number of labels and $m$ is the number of limits. This is because we sort the labels and then iterate over them to select the labels that do not exceed the limit for their label type.
> - **Space Complexity:** $O(n + m)$, where $n$ is the number of labels and $m$ is the number of limits. This is because we need to store the labels, limits, and the count of labels used for each label type.
> - **Optimality proof:** The greedy approach ensures that we select the labels with the maximum value first, which maximizes the sum of values. The count array ensures that we do not exceed the limit for each label type.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Maximization problems, constraint satisfaction.
- Optimization techniques learned: Greedy approach, sorting.
- Similar problems to practice: Maximization problems, constraint satisfaction problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the count array, not checking if the total number of labels used for each label type exceeds the limit.
- Edge cases to watch for: Empty input, duplicate labels.
- Performance pitfalls: Not using a greedy approach, not sorting the labels.
- Testing considerations: Test cases with different input sizes, test cases with duplicate labels.