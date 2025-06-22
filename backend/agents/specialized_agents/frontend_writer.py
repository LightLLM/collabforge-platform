# backend/agents/specialized_agents/frontend_writer.py

from google.adk.agents import Agent
from typing import Dict
from agents.specialized_agents.planner_agent import PlannerAgent

class FrontendWriterAgent(Agent):
    def __init__(self):
        super().__init__(name="FrontendWriterAgent")
        self.planner = PlannerAgent()


    def run(self, user_prompt: str) -> dict:
        plan = self.planner.run(user_prompt)

        # Simulate frontend code generation from plan
        frontend_code = f"// Generated UI for {plan['project_name']}\n"
        for feature in plan["features"]:
            frontend_code += f"<section>{feature}</section>\n"

        return {
            "project_name": plan["project_name"],
            "tech_stack": plan["tech_stack"]["frontend"],
            "generated_ui": frontend_code
        }

