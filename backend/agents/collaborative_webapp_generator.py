from agents.specialized_agents.planner_agent import PlannerAgent
from agents.specialized_agents.frontend_writer import FrontendWriterAgent

class CollaborativeWebAppGenerator:
    def __init__(self):
        self.planner_agent = PlannerAgent()
        self.frontend_writer = FrontendWriterAgent()

    def generate(self, user_prompt: str):
        plan = self.planner_agent.run(user_prompt)
        frontend = self.frontend_writer.run(user_prompt)  # ✅ FIXED - pass prompt
        return {
            "plan": plan,
            "frontend": frontend
        }
