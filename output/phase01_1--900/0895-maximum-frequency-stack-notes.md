## Maximum Frequency Stack
**Problem Link:** [https://leetcode.com/problems/maximum-frequency-stack/description](https://leetcode.com/problems/maximum-frequency-stack/description)

**Problem Statement:**
- Input: A list of operations where each operation is either `push(x)` or `pop()`.
- Constraints: $1 \leq x \leq 10^6$, $1 \leq \text{number of operations} \leq 10^5$.
- Expected Output: The maximum frequency of the top element after each `pop()` operation.
- Key Requirements: 
  - Handle `push(x)` and `pop()` operations efficiently.
  - Keep track of the frequency of each element.
  - Identify the maximum frequency element at the top after each `pop()` operation.
- Edge Cases:
  - Empty stack.
  - Stack with a single element.
  - Stack with multiple elements having the same maximum frequency.

Example Test Cases:
- `["FreqStack","push","push","freq","push","freq","push","freq","push","freq","pop","pop","pop","pop"]`, `[[],[5],[7],[],[5],[],[7],[],[4],[],[],[],[]]`.
- `["FreqStack","push","push","push","freq","freq"]`, `[[],[5],[5],[5],[],[]]`.

### Brute Force Approach

**Explanation:**
- The initial thought process involves using a stack to keep track of the elements and a map to store their frequencies.
- Upon each `push(x)` operation, increment the frequency of `x` in the map.
- Upon each `pop()` operation, find the element with the maximum frequency at the top of the stack and decrement its frequency in the map.

```cpp
class FreqStack {
private:
    stack<int> st;
    unordered_map<int, int> freq;

public:
    FreqStack() {}

    void push(int x) {
        st.push(x);
        freq[x]++;
    }

    int pop() {
        int maxFreq = 0;
        for (int i = st.size() - 1; i >= 0; i--) {
            maxFreq = max(maxFreq, freq[st[i]]);
        }
        for (int i = st.size() - 1; i >= 0; i--) {
            if (freq[st[i]] == maxFreq) {
                int res = st[i];
                st.pop();
                freq[res]--;
                if (freq[res] == 0) freq.erase(res);
                return res;
            }
        }
        return -1; // In case stack is empty
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `pop()` operation in the worst case where $n$ is the number of elements in the stack, because we potentially scan the entire stack to find the maximum frequency element.
> - **Space Complexity:** $O(n)$ for storing elements in the stack and their frequencies in the map.
> - **Why these complexities occur:** The brute force approach involves scanning the stack for each `pop()` operation to find the maximum frequency element, leading to linear time complexity. The space complexity is linear because in the worst case, we store all elements and their frequencies.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a combination of a stack and a map where the map values are stacks themselves. Each map entry corresponds to a frequency, and its value is a stack of elements having that frequency.
- Upon each `push(x)` operation, increment the frequency of `x` and push `x` onto the stack corresponding to its new frequency.
- Upon each `pop()` operation, pop the top element from the stack with the maximum frequency and decrement its frequency. If the stack becomes empty, remove the entry from the map.

```cpp
class FreqStack {
private:
    int maxFreq;
    unordered_map<int, stack<int>> freqStack;
    unordered_map<int, int> freq;

public:
    FreqStack() : maxFreq(0) {}

    void push(int x) {
        freq[x]++;
        int f = freq[x];
        maxFreq = max(maxFreq, f);
        freqStack[f].push(x);
    }

    int pop() {
        int res = freqStack[maxFreq].top();
        freqStack[maxFreq].pop();
        freq[res]--;
        if (freqStack[maxFreq].empty()) maxFreq--;
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for both `push()` and `pop()` operations because we directly access and manipulate the elements in the map and stacks.
> - **Space Complexity:** $O(n)$ for storing elements in the stacks and their frequencies in the map.
> - **Optimality proof:** This approach is optimal because we directly access and manipulate the maximum frequency elements without scanning the entire data structure, achieving constant time complexity for both operations.

### Final Notes

**Learning Points:**
- Using a combination of data structures (stack and map) to achieve efficient operations.
- Keeping track of the maximum frequency to optimize the `pop()` operation.
- Efficiently updating frequencies and removing elements.

**Mistakes to Avoid:**
- Not updating the maximum frequency correctly.
- Not handling the case when the stack with the maximum frequency becomes empty.
- Incorrectly decrementing frequencies or removing elements.