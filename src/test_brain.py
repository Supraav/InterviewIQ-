import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_client():
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in env")

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    return client

def test_connection():
    try:
        client = get_client()

        completion = client.chat.completions.create(
            model="qwen/qwen3-coder:free",
            messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "i am sad "}
                ],
        )
        print("connected to openrouter API")
        print("Model Response:", completion.choices[0].message.content)
        # import pdb;pdb.set_trace()
    
    except Exception as e:
        print("Failed to connect to openrouter API", str(e))

if __name__ == "__main__":
    test_connection()