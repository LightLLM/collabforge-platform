#!/bin/bash

echo "🔥 Setting up CollabForge Platform..."

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "✅ CollabForge setup complete!"
echo ""
echo "🚀 To start the platform:"
echo "Backend:  cd backend && python main.py"
echo "Frontend: cd frontend && npm start"
echo ""
echo "🌐 Access the platform at: http://localhost:3000"
