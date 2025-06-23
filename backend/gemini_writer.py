import os
import json
import re
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

async def generate_webapp_code(prompt: str) -> str:
    model = GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()
    response = chat.send_message(
        f"Generate minimal HTML+TailwindCSS UI for: {prompt}. Wrap all in <html>..."
    )
    return response.text

# Load environment variables
load_dotenv()

PROJECT_ID = os.getenv("VERTEX_PROJECT_ID")
LOCATION = os.getenv("VERTEX_LOCATION", "us-central1")
MODEL_ID = os.getenv("VERTEX_MODEL_ID", "gemini-2.0-flash")

def init_vertex():
    vertexai.init(project=PROJECT_ID, location=LOCATION)

def clean_markdown_json(text: str) -> str:
    """Strip triple backticks and optional 'json' language tag from response."""
    return re.sub(r"^```json\s*|```$", "", text.strip(), flags=re.IGNORECASE | re.MULTILINE)

def generate_webapp_plan(user_prompt: str) -> dict:
    init_vertex()
    model = GenerativeModel(MODEL_ID)

    system_prompt = """
You are a multi-agent AI system designed to help users create full-stack web applications.
Given a prompt like 'to-do list app', generate:

1. A project name (kebab-case)
2. A list of 4–6 features
3. A recommended tech stack: frontend, backend, database
4. Basic frontend UI layout in HTML (placeholder elements)

Respond in this JSON format:
{
  "plan": {
    "project_name": "...",
    "features": ["...", "..."],
    "tech_stack": {
      "frontend": "...",
      "backend": "...",
      "database": "..."
    }
  },
  "frontend": {
    "generated_ui": "...HTML output..."
  }
}
"""

    try:
        response = model.generate_content(f"{system_prompt}\n\nUser prompt: {user_prompt}")
        cleaned = clean_markdown_json(response.text)
        return json.loads(cleaned)
    except Exception as e:
        raise RuntimeError(f"Error generating webapp plan: {e}")
