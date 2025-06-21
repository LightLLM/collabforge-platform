import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [agents, setAgents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [prompt, setPrompt] = useState('');

  useEffect(() => {
    // Fetch available agents
    fetch('/agents/available')
      .then(res => res.json())
      .then(data => {
        setAgents(data.agents || []);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching agents:', err);
        setLoading(false);
      });
  }, []);

  const handleGenerate = async () => {
    if (!prompt.trim()) return;
    
    try {
      const response = await fetch('/api/v1/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ description: prompt })
      });
      const result = await response.json();
      alert(`🔥 Generated: ${result.message}\nProject ID: ${result.project_id}`);
    } catch (error) {
      alert('Error generating app: ' + error.message);
    }
  };

  if (loading) {
    return <div className="app loading">🔥 Loading CollabForge...</div>;
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="logo">
          <h1>🔥 CollabForge</h1>
          <p>Forging the Future of Development</p>
        </div>
        
        <div className="hero">
          <h2>AI-Powered Collaborative Web Application Generator</h2>
          <p>Transform your ideas into deployed web applications through advanced multi-agent AI collaboration</p>
        </div>

        <div className="demo-section">
          <h3>Quick Demo</h3>
          <div className="generate-form">
            <input
              type="text"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Describe the web app you want to build..."
              className="prompt-input"
            />
            <button onClick={handleGenerate} className="generate-btn">
              🚀 Generate App
            </button>
          </div>
        </div>

        <div className="agents-section">
          <h3>Our AI Agent Team ({agents.length} Specialists)</h3>
          <div className="agents-grid">
            {agents.map(agent => (
              <div key={agent.id} className="agent-card">
                <h4>{agent.name}</h4>
                <p className="role">{agent.role}</p>
                <p className="expertise">
                  {agent.expertise.join(' • ')}
                </p>
                <span className={`status ${agent.status}`}>
                  {agent.status}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="features">
          <h3>Platform Features</h3>
          <div className="features-grid">
            <div className="feature">
              <h4>🤖 Multi-Agent Collaboration</h4>
              <p>6 specialized AI agents working together</p>
            </div>
            <div className="feature">
              <h4>⚡ Lightning Fast</h4>
              <p>Complete apps in 60-120 seconds</p>
            </div>
            <div className="feature">
              <h4>🛡️ Enterprise Security</h4>
              <p>Built-in security best practices</p>
            </div>
            <div className="feature">
              <h4>☁️ Google Cloud Native</h4>
              <p>Seamless deployment and scaling</p>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
