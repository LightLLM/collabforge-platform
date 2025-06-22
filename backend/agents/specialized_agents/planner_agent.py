# backend/agents/specialized_agents/planner_agent.py
from google.adk.agents import Agent  # ✅ key ADK import

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__(name="PlannerAgent")
    
    def run(self, prompt: str) -> dict:
        # Simulated planning logic (same as your `plan` function)
        return {
            "project_name": prompt.strip().replace(" ", "-").lower(),
            "features": [
                "Landing Page", "Contact Form", "Admin Dashboard",
                "User Authentication", "Blog Module"
            ],
            "tech_stack": {
                "frontend": "React + TailwindCSS",
                "backend": "FastAPI",
                "database": "PostgreSQL"
            }
        }
