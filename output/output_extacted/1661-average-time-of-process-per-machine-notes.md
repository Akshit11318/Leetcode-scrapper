## Average Time of Process Per Machine
**Problem Link:** https://leetcode.com/problems/average-time-of-process-per-machine/description

**Problem Statement:**
- Input format: `jobs` - a 2D array where each sub-array contains two integers representing the processing time and the machine index of a job.
- Constraints: $1 \leq jobs.length \leq 10^5$, $1 \leq jobs[i][0] \leq 10^4$, $1 \leq jobs[i][1] \leq M$, where $M$ is the number of machines.
- Expected output format: The average time per machine for each machine.
- Key requirements and edge cases to consider: Handling cases where the input array is empty or contains a single element, and ensuring that the solution scales well for large inputs.

Example test cases with explanations:
- `jobs = [[1,2],[2,3],[3,1]]`: The first machine processes a job of time 3, the second machine processes a job of time 1, and the third machine processes a job of time 2. The average time per machine is `(3 + 1 + 2) / 3 = 2`.
- `jobs = [[2,1],[3,1],[1,2]]`: Both the first and second jobs are processed by the first machine, so the total time for the first machine is `2 + 3 = 5`. The third job is processed by the second machine, so the total time for the second machine is `1`. The average time per machine is `(5 + 1) / 2 = 3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves iterating through each job and calculating the total time for each machine by summing up the processing times of the jobs assigned to it.
- Step-by-step breakdown of the solution:
  1. Initialize an array `machine_times` to store the total time for each machine.
  2. Iterate through each job in the `jobs` array.
  3. For each job, add the processing time to the corresponding machine's total time in `machine_times`.
  4. Calculate the average time per machine by dividing the total time for each machine by the number of machines.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
vector<double> averageTimePerMachine(vector<vector<int>>& jobs) {
    int M = 0; // number of machines
    for (auto& job : jobs) {
        M = max(M, job[1]);
    }
    
    vector<int> machine_times(M, 0);
    for (auto& job : jobs) {
        machine_times[job[1] - 1] += job[0];
    }
    
    vector<double> average_times(M);
    for (int i = 0; i < M; i++) {
        average_times[i] = (double)machine_times[i] / M;
    }
    
    return average_times;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of jobs and $M$ is the number of machines. This is because we iterate through each job once and then through each machine once.
> - **Space Complexity:** $O(M)$, where $M$ is the number of machines. This is because we need to store the total time for each machine.
> - **Why these complexities occur:** The time complexity occurs because we perform a constant amount of work for each job and each machine. The space complexity occurs because we need to store the total time for each machine.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use the same approach as the brute force solution but optimize the calculation of the average time per machine by dividing the total time for each machine by the total number of machines only once.
- Detailed breakdown of the approach:
  1. Initialize an array `machine_times` to store the total time for each machine.
  2. Iterate through each job in the `jobs` array and add the processing time to the corresponding machine's total time in `machine_times`.
  3. Calculate the average time per machine by dividing the total time for each machine by the total number of machines.
- Proof of optimality: This approach is optimal because it only requires a single pass through the jobs array and a single pass through the machines array, resulting in a time complexity of $O(N + M)$.

```cpp
vector<double> averageTimePerMachine(vector<vector<int>>& jobs) {
    int M = 0; // number of machines
    for (auto& job : jobs) {
        M = max(M, job[1]);
    }
    
    vector<int> machine_times(M, 0);
    for (auto& job : jobs) {
        machine_times[job[1] - 1] += job[0];
    }
    
    vector<double> average_times(M);
    for (int i = 0; i < M; i++) {
        average_times[i] = (double)machine_times[i] / M;
    }
    
    return average_times;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N + M)$, where $N$ is the number of jobs and $M$ is the number of machines. This is because we iterate through each job once and then through each machine once.
> - **Space Complexity:** $O(M)$, where $M$ is the number of machines. This is because we need to store the total time for each machine.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the jobs array and a single pass through the machines array, resulting in a time complexity of $O(N + M)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, array manipulation, and basic arithmetic operations.
- Problem-solving patterns identified: The problem can be solved by iterating through each job and calculating the total time for each machine.
- Optimization techniques learned: The calculation of the average time per machine can be optimized by dividing the total time for each machine by the total number of machines only once.
- Similar problems to practice: Problems that involve iterating through an array and performing basic arithmetic operations.

**Mistakes to Avoid:**
- Common implementation errors: Failing to initialize the `machine_times` array or forgetting to divide the total time for each machine by the total number of machines.
- Edge cases to watch for: Handling cases where the input array is empty or contains a single element.
- Performance pitfalls: Failing to optimize the calculation of the average time per machine, resulting in a higher time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure correctness and performance.