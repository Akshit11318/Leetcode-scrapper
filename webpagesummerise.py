from groq import Groq


# Initialize the Groq client
client = Groq()

# Generate the dynamic link
from linkgen import get_title_slug_link_by_id  # Import the function
link = get_title_slug_link_by_id(143)  # Call the function to get the link

from filenamegen import get_file_name  # Import the function
filename = get_file_name(143)  # Call the function to get the link

# Create a completion request
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": (
                f"Generate notes for {link} "
                "using the following template, making the problem link a hyperlink:\n\n"
                "## [Problem Name]\n\n"
                f"**Problem Link:** [{link}]({link})\n\n"
                "**Problem Statement (in your own words):**\n\n"
                "[Describe the problem briefly: input, output, and what needs to be achieved.]\n\n"
                "---\n\n"
                "### Brute Force Approach\n\n"
                "**Explanation:**\n\n"
                "[Provide a step-by-step explanation of the brute force solution.]\n\n"
                "```cpp\n"
                "[Insert Code in Cpp]\n"
                "```\n\n"
                "> Complexity Analysis:\n> \n> **Time Complexity:** [Explain the time complexity and why with formula.]\n> \n> **Space Complexity:** [Explain the space usage and why with formula.]\n\n"
                "---\n\n"
                "### Optimal Approach\n\n"
                "**Explanation:**\n\n"
                "[Provide a detailed explanation of the optimal approach and key ideas.]\n\n"
                "```cpp\n"
                "[Insert Code in cpp]\n"
                "```\n\n"
                "> Complexity Analysis:\n> \n> - **Time Complexity:** [Explain the time complexity and why.]\n> - **Space Complexity:** [Explain the space usage and why.]\n\n"
                "---\n\n"
                "### Alternative/Greedy Approach (if applicable)\n\n"
                "**Explanation:**\n\n"
                "[Describe any alternative approach like greedy, two-pointer, or dynamic programming.]\n\n"
                "```cpp\n"
                "[Insert Code]\n"
                "```\n\n"
                "> Complexity Analysis:\n> \n> - **Time Complexity:** [Explain the time complexity and why.]\n> - **Space Complexity:** [Explain the space usage and why.]\n\n"
                "---\n\n"
                "### Final Notes\n\n"
                "**Learning Points:**\n\n"
                "[List key takeaways or interesting findings while solving the problem.]\n\n"
                "**Mistakes to Avoid:**\n\n"
                "[List common pitfalls or misunderstandings about the problem.]\n\n"
                "---"
            )
        }
    ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    stream=True,
    stop=None,
)

# Open a new Markdown file in write mode
with open(filename, "w") as file:
    # Fetch and write each chunk to the file as it arrives
    for chunk in completion:
        content = chunk.choices[0].delta.content
        file.write(content)
        print(content, end="")  # Optional: Print content to the console as well