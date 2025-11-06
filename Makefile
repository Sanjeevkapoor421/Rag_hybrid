# Simple Makefile for RAG Chat Assistant 💬

run:
	@echo "🚀 Starting RAG Chat Assistant..."
	@echo "🐍 Creating virtual environment..."
	@python3 -m venv myenv
	@echo "📦 Installing dependencies..."
	@myenv/bin/pip install --upgrade pip -q
	@myenv/bin/pip install -r requirements.txt -q
	@echo "✅ Environment ready. Launching Streamlit app..."
	@myenv/bin/streamlit run app/app.py
