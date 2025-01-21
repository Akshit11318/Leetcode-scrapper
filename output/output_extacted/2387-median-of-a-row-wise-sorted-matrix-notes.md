## Median of a Row-Wise Sorted Matrix

**Problem Link:** https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/description

**Problem Statement:**
- Input: A `rows x cols` matrix, where each row is sorted in non-decreasing order.
- Constraints: `rows` and `cols` are between 1 and 200, inclusive. All elements are integers between -10^5 and 10^5.
- Expected Output: The median of the matrix.
- Key Requirements: Find the median of the combined elements of all rows, considering the matrix as a single sorted array.
- Edge Cases: Handle cases where the total number of elements is odd or even.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves combining all elements into a single array and then sorting it to find the median.
- Step-by-step breakdown:
  1. Create a new array to store all elements from the matrix.
  2. Iterate through each row and column, copying elements into the new array.
  3. Sort the new array.
  4. Calculate the median based on whether the total number of elements is odd or even.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    double findMedianSortedArrays(std::vector<std::vector<int>>& matrix) {
        std::vector<int> allElements;
        
        // Copy all elements into a single vector
        for (const auto& row : matrix) {
            for (const auto& element : row) {
                allElements.push_back(element);
            }
        }
        
        // Sort the vector
        std::sort(allElements.begin(), allElements.end());
        
        int n = allElements.size();
        
        // Calculate median
        if (n % 2 == 0) {
            return (allElements[n/2 - 1] + allElements[n/2]) / 2.0;
        } else {
            return allElements[n/2];
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \cdot cols \cdot \log(rows \cdot cols))$ due to the sorting of the combined array.
> - **Space Complexity:** $O(rows \cdot cols)$ for storing the combined array.
> - **Why these complexities occur:** The primary operation is sorting the combined array, which dominates the time complexity. The space complexity is directly related to storing all elements in a new array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a binary search approach to find the median without fully sorting the matrix.
- Since the matrix rows are sorted, we can use the concept of `count` of elements less than or equal to a given number to determine if it's the median.
- We binary search over the range of possible median values, from the smallest to the largest element in the matrix.

```cpp
class Solution {
public:
    double findMedianSortedArrays(std::vector<std::vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int low = matrix[0][0];
        int high = matrix[0][cols - 1];
        
        for (const auto& row : matrix) {
            low = std::min(low, row[0]);
            high = std::max(high, row[cols - 1]);
        }
        
        int total = rows * cols;
        int half = total / 2;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            int count = 0;
            
            // Count elements less than or equal to mid in each row
            for (const auto& row : matrix) {
                int left = 0;
                int right = cols - 1;
                
                while (left <= right) {
                    int pivot = left + (right - left) / 2;
                    
                    if (row[pivot] <= mid) {
                        left = pivot + 1;
                    } else {
                        right = pivot - 1;
                    }
                }
                
                count += left;
            }
            
            if (count <= half) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        
        if (total % 2 == 0) {
            int before = low;
            int countBefore = 0;
            
            for (const auto& row : matrix) {
                int left = 0;
                int right = cols - 1;
                
                while (left <= right) {
                    int pivot = left + (right - left) / 2;
                    
                    if (row[pivot] < before) {
                        left = pivot + 1;
                    } else {
                        right = pivot - 1;
                    }
                }
                
                countBefore += left;
            }
            
            int after = low;
            int countAfter = 0;
            
            for (const auto& row : matrix) {
                int left = 0;
                int right = cols - 1;
                
                while (left <= right) {
                    int pivot = left + (right - left) / 2;
                    
                    if (row[pivot] <= after) {
                        left = pivot + 1;
                    } else {
                        right = pivot - 1;
                    }
                }
                
                countAfter += left;
            }
            
            return (before + after) / 2.0;
        } else {
            return (double)low;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(rows \cdot cols \cdot \log(max - min))$ where `max` and `min` are the maximum and minimum values in the matrix. This is because for each binary search step, we perform a count operation over each row.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it reduces the problem to finding the median through binary search over the possible range of median values, leveraging the sorted nature of the rows to efficiently count elements less than or equal to a given value.

---

### Final Notes

**Learning Points:**
- **Binary Search:** Using binary search to find the median in a sorted or partially sorted data structure.
- **Counting Elements:** Leveraging the sorted nature of rows to efficiently count elements less than or equal to a given value.
- **Median Calculation:** Understanding how to calculate the median for both odd and even total numbers of elements.

**Mistakes to Avoid:**
- **Incorrect Counting:** Ensure accurate counting of elements less than or equal to a given value in each row.
- **Binary Search Boundaries:** Correctly setting and updating the boundaries for binary search.
- **Median Calculation for Even Total Elements:** Properly averaging the two middle elements when the total number of elements is even.