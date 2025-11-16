# Development Quick Guide

## 🚀 Getting Started

### One-Command Setup
```bash
./run.sh
```
This script will:
- Create virtual environment
- Install dependencies  
- Check for .env file
- Create database if needed
- Start the application

### Manual Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Create database
python scripts/create_sample_db.py

# Run application
streamlit run app.py
```

## 🗂️ Project Structure

```
text-to-sql-app/
├── app.py              # 🎯 Main application
├── auth_system.py      # 🔐 Authentication logic
├── auth_ui.py          # 🎨 Auth UI components
├── requirements.txt    # 📦 Dependencies
├── run.sh             # 🚀 Startup script
├── README.md          # 📚 Documentation
├── .env.example       # 🔧 Environment template
├── database/          # 🗃️ Database files
└── scripts/           # 🛠️ Utility scripts
```

## 🔑 Key Files

- **app.py** - Main Streamlit application with AI agents
- **auth_system.py** - User management and permissions  
- **auth_ui.py** - Login/profile UI components
- **database/sample.db** - SQLite database with sample data
- **scripts/create_sample_db.py** - Database initialization

## 🧪 Testing

### Test Queries
```sql
-- Simple
"Show me 5 customers"

-- Analytics  
"Top customers by revenue"

-- Complex
"Customer lifetime value analysis"
```

## 📝 Key Features to Demo

1. **Natural Language Processing** - Type plain English queries
2. **Multi-Agent Analysis** - See AI reasoning (Planner → Validator → Optimizer)
3. **Role-Based Access** - Different permissions per user type
4. **Auto-Visualizations** - Charts generated from query results
5. **Chain-of-Thought** - Watch AI think step by step

## 🔧 Environment Variables

```env
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///database/sample.db
FLASK_ENV=development
```

## 🚀 Deployment Notes

- For production: Replace SQLite with PostgreSQL
- Set up proper authentication backend
- Configure rate limiting
- Use HTTPS in production
- Monitor API usage

## 📊 Database Info

- **Total Records**: 1,693+
- **Tables**: 11 interconnected tables
- **Domain**: E-commerce with customers, orders, products
- **Relationships**: Fully normalized with foreign keys
