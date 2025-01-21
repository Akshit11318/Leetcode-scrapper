## Parallel Execution of Promises for Individual Results Retrieval

**Problem Link:** https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/description

**Problem Statement:**
- Input format and constraints: The problem requires executing a list of promises in parallel and retrieving individual results. The input is a list of promises, and the constraint is that each promise may take a different amount of time to resolve.
- Expected output format: The expected output is a list of results corresponding to the input promises, in the order they were received.
- Key requirements and edge cases to consider: The key requirement is to execute the promises in parallel and handle any potential errors that may occur during execution. Edge cases include handling promises that reject with an error, and promises that never resolve.
- Example test cases with explanations: 
    - Test case 1: Executing a list of promises that all resolve successfully.
    - Test case 2: Executing a list of promises where one or more promises reject with an error.
    - Test case 3: Executing a list of promises where one or more promises never resolve.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to execute each promise sequentially, waiting for the previous promise to resolve before executing the next one. However, this approach does not take advantage of the parallel nature of promises.
- Step-by-step breakdown of the solution: 
    1. Create an empty list to store the results.
    2. Iterate over the input list of promises.
    3. For each promise, wait for it to resolve using `await` or `.then()`.
    4. Once a promise resolves, add its result to the list.
    5. Repeat steps 3-4 until all promises have been executed.
- Why this approach comes to mind first: This approach comes to mind first because it is a simple, straightforward way to execute promises. However, it does not take advantage of the parallel nature of promises, which can lead to slower execution times.

```cpp
#include <iostream>
#include <vector>
#include <future>

// Define a function to execute a promise and retrieve its result
std::string executePromise(std::function<std::string()> promise) {
    return promise();
}

// Define the brute force function
std::vector<std::string> bruteForce(std::vector<std::function<std::string()>> promises) {
    std::vector<std::string> results;
    for (auto& promise : promises) {
        results.push_back(executePromise(promise));
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times t)$, where $n$ is the number of promises and $t$ is the average time it takes for a promise to resolve.
> - **Space Complexity:** $O(n)$, where $n$ is the number of promises.
> - **Why these complexities occur:** The time complexity occurs because the brute force approach executes each promise sequentially, waiting for the previous promise to resolve before executing the next one. The space complexity occurs because the brute force approach stores the results of each promise in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use `std::async` or `std::thread` to execute the promises in parallel, allowing the program to take advantage of multiple CPU cores.
- Detailed breakdown of the approach: 
    1. Create a list to store the futures returned by `std::async`.
    2. Iterate over the input list of promises.
    3. For each promise, use `std::async` to execute it in parallel.
    4. Add the future returned by `std::async` to the list.
    5. Use `std::future::get` to retrieve the result of each promise.
    6. Add the result to the list of results.
- Proof of optimality: The optimal approach is optimal because it takes advantage of multiple CPU cores to execute the promises in parallel, reducing the overall execution time.
- Why further optimization is impossible: Further optimization is impossible because the optimal approach already takes advantage of the parallel nature of promises and multiple CPU cores.

```cpp
// Define the optimal function
std::vector<std::string> optimal(std::vector<std::function<std::string()>> promises) {
    std::vector<std::future<std::string>> futures;
    std::vector<std::string> results;
    for (auto& promise : promises) {
        futures.push_back(std::async(std::launch::async, promise));
    }
    for (auto& future : futures) {
        results.push_back(future.get());
    }
    return results;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(t)$, where $t$ is the time it takes for the longest promise to resolve.
> - **Space Complexity:** $O(n)$, where $n$ is the number of promises.
> - **Optimality proof:** The optimal approach is optimal because it takes advantage of multiple CPU cores to execute the promises in parallel, reducing the overall execution time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concepts demonstrated are parallel execution of promises and retrieval of individual results.
- Problem-solving patterns identified: The problem-solving pattern identified is to use `std::async` or `std::thread` to execute promises in parallel.
- Optimization techniques learned: The optimization technique learned is to take advantage of multiple CPU cores to execute promises in parallel.
- Similar problems to practice: Similar problems to practice include executing a list of tasks in parallel and retrieving individual results.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to execute promises sequentially, waiting for the previous promise to resolve before executing the next one.
- Edge cases to watch for: Edge cases to watch for include promises that reject with an error, and promises that never resolve.
- Performance pitfalls: A performance pitfall is to execute promises sequentially, which can lead to slower execution times.
- Testing considerations: Testing considerations include testing the optimal approach with different types of promises, including promises that resolve successfully, promises that reject with an error, and promises that never resolve.