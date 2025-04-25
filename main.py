from ollama import Client
from langchain.agents import initialize_agent, Tool, AgentType

# # === Step 1: Load LLaMA 3.2 via Ollama ===
# print("🔄 Loading LLaMA 3.2 model via Ollama...")
# llm = Ollama(model="llama3.2:3b")  # You can also use "llama3.2:1b" for a lighter model
# print("✅ LLaMA 3.2 model is ready.")

# # === Step 2: Define Medical Q&A Tool ===
# def dynamic_medical_tool(query: str) -> str:
#     prompt = (
#         f"You are a knowledgeable and responsible medical assistant. Answer clearly and accurately:\n\n"
#         f"Question: {query}\n"
#         f"Answer:"
#     )
#     result = llm(prompt)
#     return result

# tools = [
#     Tool(
#         name="MedicalQnA",
#         func=dynamic_medical_tool,
#         description="Use this to answer medical questions like symptoms, treatments, or diseases.",
#     )
# ]

# # === Step 3: Initialize Agent ===
# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True
# )

def call_groq_api(user_query):
    try:
        # 🧠 Enhanced prompt: adding more clear instructions to the model
        system_prompt = (
            "You are a knowledgeable and responsible medical assistant. Answer clearly and accurately:\n\n\n\n"
            f"### Question:\n{user_query}\n"
        )

        # Initialize Ollama client
        client = Client()

        # Call the Ollama API with the refined prompt
        response = client.chat(
            model="llama3.2:latest",
            messages=[
                {"role": "user", "content": system_prompt}
            ]
        )

        # Extract and print the answer
        answer = response['message']['content'].strip()
        print("\n\nAnswer:", answer)
        return answer

    except Exception as e:
        print(f"Error calling Ollama API: {e}")
        return "Sorry, I couldn't process your request at the moment."


# === Step 4: Test User Query ===
user_query = input("💬 Enter your medical question: ")
print("\n🧠 Running Agent...")
response = call_groq_api(user_query)

print("\n🩺 Agent Response:")
print(response)
