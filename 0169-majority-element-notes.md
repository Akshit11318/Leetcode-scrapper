## Majority Element

**Problem Link:** https://leetcode.com/problems/majority-element/description

**Problem Statement:**

Given an array of integers, find the majority element that appears more than n/2 times where n is the size of the array. The array is guaranteed to have a majority element.

---

### Brute Force Approach

**Explanation:**

1. Create a frequency map to store the count of each element in the array.
2. Iterate over the array to populate the frequency map.
3. Iterate over the frequency map to find the element with a count greater than n/2.

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        for (auto& it : freq) {
            if (it.second > nums.size() / 2) {
                return it.first;
            }
        }
        return -1; // Should not reach here
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(n) because we are iterating over the array twice. The first iteration is to populate the frequency map, and the second iteration is to find the majority element. The time complexity is linear because the operations are performed sequentially.
> 
> **Space Complexity:** O(n) because in the worst case, all elements in the array might be unique, and we would need to store all of them in the frequency map.

---

### Optimal Approach

**Explanation:**

1. Initialize a candidate variable and a count variable to 0.
2. Iterate over the array, and for each element:
   - If the count is 0, set the candidate to the current element.
   - If the current element matches the candidate, increment the count.
   - If the current element does not match the candidate, decrement the count.
3. The candidate variable now holds the majority element.

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
                count = 1;
            } else if (candidate == num) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }
};
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(n) because we are making a single pass through the array.
> - **Space Complexity:** O(1) because we are using a constant amount of space to store the candidate and the count.

---

### Final Notes

**Learning Points:**

* The Boyer-Moore Voting Algorithm is an efficient method for finding the majority element in an array.
* This algorithm works by essentially maintaining a counter for the majority element. When the counter is zero, the algorithm sets the current element as the majority element.
* The algorithm then increments the counter when it encounters the same element again and decrements it when it encounters a different element.

**Mistakes to Avoid:**

* Not checking if the majority element exists before using the Boyer-Moore Voting Algorithm.
* Assuming that the Boyer-Moore Voting Algorithm works for all cases, including when there is no majority element.
* Not understanding the time and space complexity of the algorithm.