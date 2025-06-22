"""
CollabForge Platform - Main FastAPI Application
AI-Powered Collaborative Web Application Generator
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime
from api.v2 import collaborative_generation

# Initialize FastAPI app
app = FastAPI(
    title="CollabForge Platform",
    description="AI-Powered Collaborative Web Application Generator - Where AI Agents Collaborate to Forge the Future of Development",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app = FastAPI()
app.include_router(collaborative_generation.router, prefix="/api/v2")  # ✅ this makes /generate-plan available at /api/v2/generate-plan

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "🔥 Welcome to CollabForge Platform!",
        "tagline": "Forging the Future of Development",
        "description": "AI-Powered Collaborative Web Application Generator",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "message": "CollabForge backend is running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "platform": "CollabForge",
        "timestamp": datetime.now().isoformat(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/agents/available")
async def get_available_agents():
    """Get available AI agents"""
    agents = [
        {
            "id": "business_analyst",
            "name": "Sarah Chen - Business Analyst",
            "role": "Market Strategy & Requirements",
            "expertise": ["Product Strategy", "User Research", "Business Metrics"],
            "status": "active"
        },
        {
            "id": "technical_architect",
            "name": "Marcus Rodriguez - Technical Architect", 
            "role": "System Design & Architecture",
            "expertise": ["Distributed Systems", "Cloud Architecture", "Scalability"],
            "status": "active"
        },
        {
            "id": "security_expert",
            "name": "Dr. Aisha Patel - Security Expert",
            "role": "Application Security & Compliance", 
            "expertise": ["Threat Modeling", "Authentication", "Compliance"],
            "status": "active"
        },
        {
            "id": "ux_designer",
            "name": "Jordan Kim - UX Designer",
            "role": "User Experience & Interface Design",
            "expertise": ["User-Centered Design", "Accessibility", "Design Systems"],
            "status": "active"
        },
        {
            "id": "performance_optimizer",
            "name": "Alex Thompson - Performance Engineer",
            "role": "Speed & Scalability Optimization",
            "expertise": ["Performance Analysis", "Caching", "Optimization"],
            "status": "active"
        },
        {
            "id": "qa_expert",
            "name": "Emma Wilson - QA Lead",
            "role": "Quality Assurance & Testing",
            "expertise": ["Testing Strategies", "Quality Standards", "Automation"],
            "status": "active"
        }
    ]
    
    return {
        "platform": "CollabForge",
        "total_agents": len(agents),
        "agents": agents,
        "collaboration_status": "ready"
    }

@app.post("/api/v1/generate")
async def generate_webapp_demo():
    """Demo endpoint for web app generation"""
    return {
        "status": "success",
        "message": "🔥 CollabForge Demo - Agent Collaboration Simulation",
        "project_id": f"demo_{int(datetime.now().timestamp())}",
        "collaboration": {
            "agents_participated": 6,
            "consensus_reached": True,
            "generation_time": "45 seconds",
            "quality_score": "95%"
        },
        "generated_app": {
            "frontend": "React with TypeScript",
            "backend": "FastAPI with Python",
            "database": "PostgreSQL",
            "deployment": "Google Cloud Run",
            "features": [
                "User Authentication",
                "Responsive Design", 
                "Real-time Features",
                "Enterprise Security",
                "Performance Optimization"
            ]
        },
        "demo_note": "This is a demo response. Full multi-agent collaboration system available in production version."
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)