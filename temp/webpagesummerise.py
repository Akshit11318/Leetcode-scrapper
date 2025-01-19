from groq import Groq

# Initialize the Groq client
client = Groq()

# Generate the dynamic link
from linkgen import get_title_slug_link_by_id
link = get_title_slug_link_by_id(101)

from filenamegen import get_file_name
filename = get_file_name(101)

# Create a completion request
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert at solving programming problems. For each problem, provide:\n"
                "1. A brute force approach as the starting point\n"
                "2. An optimal solution (required for all problems)\n"
                "3. A better approach (only if it exists as an intermediate step between brute and optimal)\n"
                "4. Alternative approaches (only if they offer unique insights)\n"
                "Ensure clear progression from simpler to more sophisticated solutions."
            )
        },
        {
            "role": "user",
            "content": (
                f"Generate detailed solution notes for {link} "
                "following this template. The optimal approach is mandatory. Include a better approach "
                "only if there's an intermediate solution between brute force and optimal.\n\n"
                
                "## [Problem Name]\n\n"
                f"**Problem Link:** [{link}]({link})\n\n"
                
                "**Problem Statement:**\n"
                "- Input format and constraints\n"
                "- Expected output format\n"
                "- Key requirements and edge cases to consider\n"
                "- Example test cases with explanations\n\n"
                
                "---\n\n"
                "### Brute Force Approach\n\n"
                "**Explanation:**\n"
                "- Initial thought process\n"
                "- Step-by-step breakdown of the solution\n"
                "- Why this approach comes to mind first\n\n"
                
                "```cpp\n"
                "// Well-commented code with:\n"
                "// - Clear variable names\n"
                "// - Input validation\n"
                "// - Edge case handling\n"
                "[Insert Code in Cpp]\n"
                "```\n\n"
                
                "> Complexity Analysis:\n"
                "> - **Time Complexity:** [Big O notation with detailed breakdown]\n"
                "> - **Space Complexity:** [Memory usage analysis with explanation]\n"
                "> - **Why these complexities occur:** [Explain which operations cause these complexities]\n\n"
                
                "---\n\n"
                "[INCLUDE THIS SECTION ONLY IF THERE'S AN INTERMEDIATE SOLUTION BETWEEN BRUTE FORCE AND OPTIMAL:]\n\n"
                "### Better Approach\n\n"
                "**Explanation:**\n"
                "- Key insight that leads to improvement\n"
                "- How it improves upon the brute force\n"
                "- Why this isn't yet the optimal solution\n"
                "- Step-by-step breakdown\n\n"
                
                "```cpp\n"
                "// Well-structured code with:\n"
                "// - Error handling\n"
                "// - Input validation\n"
                "// - Clear optimizations\n"
                "[Insert Code in cpp]\n"
                "```\n\n"
                
                "> Complexity Analysis:\n"
                "> - **Time Complexity:** [Detailed analysis with mathematical reasoning]\n"
                "> - **Space Complexity:** [Memory usage patterns and trade-offs]\n"
                "> - **Improvement over brute force:** [Quantify the improvement]\n\n"
                
                "---\n\n"
                "### Optimal Approach (Required)\n\n"
                "**Explanation:**\n"
                "- Key insight that leads to optimal solution\n"
                "- Detailed breakdown of the approach\n"
                "- Proof of optimality\n"
                "- Why further optimization is impossible\n\n"
                
                "```cpp\n"
                "// Production-ready code with:\n"
                "// - Complete error handling\n"
                "// - Input validation\n"
                "// - Optimal implementation\n"
                "[Insert Code in cpp]\n"
                "```\n\n"
                
                "> Complexity Analysis:\n"
                "> - **Time Complexity:** [Prove this is optimal]\n"
                "> - **Space Complexity:** [Memory usage analysis]\n"
                "> - **Optimality proof:** [Explain why this is the best possible complexity]\n\n"
                
                "---\n\n"
                "[INCLUDE THIS SECTION ONLY IF AN ALTERNATIVE APPROACH WITH DIFFERENT TRADE-OFFS EXISTS:]\n\n"
                "### Alternative Approach\n\n"
                "**Explanation:**\n"
                "- Different perspective or technique\n"
                "- Unique trade-offs\n"
                "- Scenarios where this approach might be preferred\n"
                "- Comparison with optimal approach\n\n"
                
                "```cpp\n"
                "[Insert Code with detailed comments]\n"
                "```\n\n"
                
                "> Complexity Analysis:\n"
                "> - **Time Complexity:** [Analysis with practical implications]\n"
                "> - **Space Complexity:** [Trade-offs in memory usage]\n"
                "> - **Trade-off analysis:** [When to choose this over optimal approach]\n\n"
                
                "---\n\n"
                "### Final Notes\n\n"
                "**Learning Points:**\n"
                "- Key algorithmic concepts demonstrated\n"
                "- Problem-solving patterns identified\n"
                "- Optimization techniques learned\n"
                "- Similar problems to practice\n\n"
                
                "**Mistakes to Avoid:**\n"
                "- Common implementation errors\n"
                "- Edge cases to watch for\n"
                "- Performance pitfalls\n"
                "- Testing considerations\n\n"
                "---"
            )
        }
    ],
    temperature=0.7,
    max_completion_tokens=3072,
    top_p=0.95,
    stream=True,
    stop=None,
)

# Write output to file with error handling
try:
    with open(filename, "w") as file:
        for chunk in completion:
            content = chunk.choices[0].delta.content
            file.write(content)
            print(content, end="", flush=True)
except Exception as e:
    print(f"Error writing to file: {e}")