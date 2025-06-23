import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Dict
from gemini_writer import generate_webapp_code



 # make sure this function exists

router = APIRouter()

class PromptInput(BaseModel):
    user_prompt: str

@router.post("/generate-plan")
async def generate_plan(input: PromptInput) -> Dict:
    prompt = input.user_prompt

    # Generate frontend UI with Gemini
    generated_ui = await generate_webapp_code(prompt)

    return {
        "plan": {
            "project_name": "AI App Generator",
            "features": ["AI-assisted planning", "Web UI preview"],
            "tech_stack": {
                "frontend": "React + Tailwind",
                "backend": "FastAPI",
                "database": "None"
            }
        },
        "frontend": {
            "generated_ui": generated_ui
        }
    }
