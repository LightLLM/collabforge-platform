import React from "react";

const AgentResult = ({ plan, frontend }) => {
  if (!plan || !frontend) return null;

  return (
    <div className="agent-output" style={{ marginTop: "2rem" }}>
      <section style={{ background: "#fff", padding: "1rem", borderRadius: "8px", border: "1px solid #ccc" }}>
        <h2>🧠 Planner Agent</h2>
        <p><strong>Project:</strong> {plan.project_name}</p>
        <p><strong>Features:</strong></p>
        <ul>
          {plan.features.map((f, idx) => <li key={idx}>{f}</li>)}
        </ul>
        <p><strong>Tech Stack:</strong> {plan.tech_stack.frontend}, {plan.tech_stack.backend}, {plan.tech_stack.database}</p>
      </section>

      <section style={{ background: "#f9f9f9", marginTop: "1rem", padding: "1rem", borderRadius: "8px", border: "1px solid #ddd" }}>
        <h2>🎨 FrontendWriter Agent</h2>
        <pre style={{ whiteSpace: "pre-wrap" }}>{frontend.generated_ui}</pre>
      </section>
    </div>
  );
};

export default AgentResult;
