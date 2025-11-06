# Simple Makefile for RAG Chat Assistant 💬

run:
	@echo "🚀 Starting RAG Chat Assistant..."
	@echo "🐍 Creating virtual environment..."
	@python3 -m venv myenv
	@echo "🐍 Activating virtual environment..."
	@source myenv/Scripts/activate
	@echo "📦 Installing dependencies, please wait..."
	@echo "This may take a while..."
	@myenv/Scripts/pip install --upgrade pip -q
	@myenv/Scripts/pip install -r requirements.txt -q
	@echo "✅ Environment ready. Launching Streamlit app..."
	@streamlit run app/app.py
