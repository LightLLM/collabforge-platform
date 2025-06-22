from fastapi import APIRouter, Request
from agents.collaborative_webapp_generator import CollaborativeWebAppGenerator

router = APIRouter()
generator = CollaborativeWebAppGenerator()

@router.post("/generate-plan")
async def generate_plan(request: Request):
    body = await request.json()
    user_prompt = body.get("user_prompt", "")
    result = generator.generate(user_prompt)
    return result
