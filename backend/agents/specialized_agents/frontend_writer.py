# backend/agents/specialized_agents/frontend_writer.py

from google.adk.agents import Agent
from typing import Dict
from agents.specialized_agents.planner_agent import PlannerAgent

#this is gemini embedding to generate code using Gemini Pro
from google.generativeai import configure, GenerativeModel
import os

configure(api_key=os.getenv("GEMINI_API_KEY"))

model = GenerativeModel("gemini-pro")

def generate_ui_code(prompt):
    response = model.generate_content(f"Generate UI code for: {prompt}")
    return response.text
#this is updated FrontendWriterAgent to use Gemini Pro for code generation
class FrontendWriterAgent(Agent):
    def __init__(self):
        super().__init__(name="FrontendWriterAgent")
        self.planner = PlannerAgent()

    def run(self, user_prompt: str) -> dict:
        plan = self.planner.run(user_prompt)
        frontend_code = generate_ui_code(user_prompt)
        return {
            "project_name": plan["project_name"],
            "tech_stack": plan["tech_stack"]["frontend"],
            "generated_ui": frontend_code
        }