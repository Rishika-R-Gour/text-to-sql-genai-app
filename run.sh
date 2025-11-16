#!/bin/bash

# Text-to-SQL GenAI Application Runner
echo "🤖 Starting Text-to-SQL GenAI Application..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "📋 Copying .env.example to .env..."
    cp .env.example .env
    echo "✏️  Please edit .env and add your GEMINI_API_KEY"
    echo "💡 Get your API key from: https://aistudio.google.com/app/apikey"
    exit 1
fi

# Check if database exists
if [ ! -f "database/sample.db" ]; then
    echo "🗃️  Database not found. Creating sample database..."
    python scripts/create_sample_db.py
fi

# Run the application
echo "🚀 Starting Streamlit application..."
echo "🌐 Application will open at: http://localhost:8501"
streamlit run app.py --server.port 8501 --server.headless false
