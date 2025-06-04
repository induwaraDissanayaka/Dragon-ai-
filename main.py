import openai
import json
import os

# Load memory and prompts
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

with open("memory/memory.json", "r", encoding="utf-8") as f:
    memory = json.load(f)

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_darugan(user_input):
    messages = [{"role": "system", "content": system_prompt}]
    messages += memory
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    answer = response.choices[0].message["content"]
    memory.append({"role": "user", "content": user_input})
    memory.append({"role": "assistant", "content": answer})

    # Save memory
    with open("memory/memory.json", "w", encoding="utf-8") as f:
        json.dump(memory[-20:], f, ensure_ascii=False, indent=2)

    return answer

print("🌺 ඩැරුගන් AI වෙත සාදරයෙන් පිළිගනිමු!")
while True:
    user_input = input("🗣️ ඔබ: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    reply = chat_with_darugan(user_input)
    print(f"🐉 ඩැරුගන්: {reply}")
