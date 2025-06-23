import React, { useState } from 'react';

const GeneratedPlanViewer = () => {
  const [prompt, setPrompt] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');
  const [activeTab, setActiveTab] = useState('code');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/v2/generate-plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_prompt: prompt }),
      });

      const data = await response.json();
      const injectedCode = `
        ${data.frontend.generated_ui}
        <script>
          document.addEventListener('DOMContentLoaded', function () {
            const taskList = document.getElementById('task-list');
            const taskInput = document.getElementById('new-task');
            const addButton = document.getElementById('add-task-button');
            const taskCount = document.getElementById('task-count');

            let tasks = [];

            function renderTasks(filter = 'all') {
              taskList.innerHTML = '';
              let filtered = tasks;
              if (filter === 'active') filtered = tasks.filter(t => !t.done);
              if (filter === 'completed') filtered = tasks.filter(t => t.done);

              filtered.forEach((task, index) => {
                const li = document.createElement('li');
                li.textContent = task.text;
                li.style.textDecoration = task.done ? 'line-through' : 'none';
                li.onclick = () => {
                  tasks[index].done = !tasks[index].done;
                  renderTasks(filter);
                };
                taskList.appendChild(li);
              });

              taskCount.textContent = tasks.length;
            }

            addButton.onclick = () => {
              const text = taskInput.value.trim();
              if (text) {
                tasks.push({ text, done: false });
                taskInput.value = '';
                renderTasks();
              }
            };

            document.querySelectorAll('.filter-button').forEach(btn => {
              btn.onclick = () => {
                document.querySelectorAll('.filter-button').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                renderTasks(btn.dataset.filter);
              };
            });

            renderTasks();
          });
        </script>
      `;
      setGeneratedCode(injectedCode);
    } catch (error) {
      console.error('Error generating code:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-gradient-to-b from-indigo-800 to-violet-900 rounded-2xl shadow-lg text-white">
      <h1 className="text-3xl font-bold mb-4 text-center">⚡ CollabForge WebApp Generator</h1>

      <div className="flex items-center gap-4 mb-6">
        <input
          type="text"
          placeholder="e.g. Build a calendar app"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="flex-grow p-3 rounded-lg text-black"
        />
        <button
          onClick={handleGenerate}
          disabled={loading || !prompt}
          className="bg-orange-500 px-6 py-3 rounded-lg font-bold hover:bg-orange-600"
        >
          {loading ? 'Generating...' : 'Generate Plan'}
        </button>
      </div>

      {generatedCode && (
        <div className="bg-white rounded-xl text-black mt-6 p-4 shadow-lg">
          <div className="flex gap-4 mb-2 border-b pb-2">
            <button
              onClick={() => setActiveTab('code')}
              className={`font-semibold px-3 py-1 rounded ${activeTab === 'code' ? 'bg-indigo-100' : 'hover:bg-gray-100'}`}
            >
              🧠 Code View
            </button>
            <button
              onClick={() => setActiveTab('preview')}
              className={`font-semibold px-3 py-1 rounded ${activeTab === 'preview' ? 'bg-indigo-100' : 'hover:bg-gray-100'}`}
            >
              🎨 Live Preview
            </button>
          </div>

          {activeTab === 'code' ? (
            <pre className="overflow-x-auto text-sm bg-gray-900 text-green-200 p-4 rounded-lg">
              <code>{generatedCode}</code>
            </pre>
          ) : (
            <iframe
              srcDoc={generatedCode}
              title="Live UI Preview"
              sandbox="allow-scripts allow-same-origin"
              style={{ width: '100%', height: '500px', border: '1px solid #ccc', borderRadius: '12px' }}
            />
          )}
        </div>
      )}
    </div>
  );
};

export default GeneratedPlanViewer;
