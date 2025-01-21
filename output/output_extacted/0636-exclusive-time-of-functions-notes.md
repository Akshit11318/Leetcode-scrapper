## Exclusive Time of Functions

**Problem Link:** https://leetcode.com/problems/exclusive-time-of-functions/description

**Problem Statement:**
- Input format: An integer `n` and a list of strings `logs`, where each log is in the format `"function_id:start/end:timestamp"`.
- Constraints: `1 <= n <= 100`, `1 <= logs.length <= 500`, `0 <= timestamp <= 10^9`, and `1 <= function_id <= 10^4`.
- Expected output format: An array of integers, where each integer represents the exclusive time of the corresponding function.
- Key requirements and edge cases to consider:
  - Handling the start and end of functions.
  - Calculating the exclusive time of each function.
  - Dealing with nested functions.

**Example Test Cases:**
- Input: `n = 2`, `logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`
  Output: `[3,4]`
- Input: `n = 1`, `logs = ["0:start:0","0:start:2","0:end:5","0:end:6"]`
  Output: `[3]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to simulate the execution of the functions by parsing the logs and updating the state of each function.
- This involves maintaining a stack to track the current function and its start time.
- When a function starts, its start time is recorded. When it ends, its exclusive time is calculated by subtracting its start time from the current timestamp and adding the exclusive time of any nested functions.

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

vector<int> exclusiveTime(int n, vector<string>& logs) {
    vector<int> result(n, 0);
    stack<pair<int, int>> stk;
    
    for (const auto& log : logs) {
        stringstream ss(log);
        string token;
        vector<string> tokens;
        
        while (getline(ss, token, ':')) {
            tokens.push_back(token);
        }
        
        int function_id = stoi(tokens[0]);
        int timestamp = stoi(tokens[2]);
        
        if (tokens[1] == "start") {
            if (!stk.empty()) {
                result[stk.top().first] += timestamp - stk.top().second;
            }
            stk.push({function_id, timestamp});
        } else {
            int duration = timestamp - stk.top().second + 1;
            result[stk.top().first] += duration;
            stk.pop();
            if (!stk.empty()) {
                stk.top().second = timestamp + 1;
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of logs. This is because we process each log once.
> - **Space Complexity:** $O(m)$, as in the worst case, the stack can grow up to the size of the number of logs.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the logs once. The space complexity is due to the use of the stack to track the function calls.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution is similar to the brute force approach but with a more efficient implementation.
- We maintain a stack to track the current function and its start time.
- When a function starts, its start time is recorded. When it ends, its exclusive time is calculated by subtracting its start time from the current timestamp and adding the exclusive time of any nested functions.
- This approach is optimal because it only requires a single pass through the logs.

```cpp
vector<int> exclusiveTime(int n, vector<string>& logs) {
    vector<int> result(n, 0);
    stack<pair<int, int>> stk;
    
    for (const auto& log : logs) {
        int function_id, timestamp;
        string type;
        sscanf(log.c_str(), "%d:%[^:]:%d", &function_id, &type, &timestamp);
        
        if (type == "start") {
            if (!stk.empty()) {
                result[stk.top().first] += timestamp - stk.top().second;
            }
            stk.push({function_id, timestamp});
        } else {
            result[function_id] += timestamp - stk.top().second + 1;
            stk.pop();
            if (!stk.empty()) {
                stk.top().second = timestamp + 1;
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of logs. This is because we process each log once.
> - **Space Complexity:** $O(m)$, as in the worst case, the stack can grow up to the size of the number of logs.
> - **Optimality proof:** This is the optimal solution because it only requires a single pass through the logs and uses a stack to efficiently track the function calls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: stack operations, parsing logs, and calculating exclusive time.
- Problem-solving patterns identified: using a stack to track function calls and calculating time differences.
- Optimization techniques learned: minimizing the number of passes through the data and using efficient data structures.

**Mistakes to Avoid:**
- Common implementation errors: incorrect parsing of logs, incorrect calculation of exclusive time, and incorrect use of the stack.
- Edge cases to watch for: handling the start and end of functions, dealing with nested functions, and handling the case where a function is not properly closed.
- Performance pitfalls: using inefficient data structures or algorithms, and not minimizing the number of passes through the data.
- Testing considerations: testing the function with different inputs, including edge cases, and verifying the correctness of the output.