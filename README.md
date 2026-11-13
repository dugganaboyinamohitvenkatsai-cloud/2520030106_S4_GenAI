# 2520030106_S4_GenAI - Generative AI Lab

This repository contains lab assignments, implementation code, and documentation for the Generative AI (GenAI) course.

## Repository Structure

```
├── Week1/
│   ├── main.py              # Initial Gemini API call implementation
│   ├── .env.example         # Environment template for Gemini API key
│   └── .gitignore
├── Week2/
│   ├── llm_client.py        # Multi-provider client (Gemini & Ollama)
│   ├── main.py              # CLI interactive menu
│   ├── test_client.py       # Test suite for client providers
│   ├── requirements.txt     # Dependencies for Week 2
│   └── .env.example
├── Week3/
│   ├── llm_client.py        # Abstract LLM provider interface & retry mechanism
│   ├── cost_calculator.py   # Token cost estimation across models
│   ├── mongo_logger.py      # MongoDB logger for latency, tokens, cost, and errors
│   ├── main.py              # Driver script with MongoDB logging
│   ├── requirements.txt     # Dependencies for Week 3
│   └── .env.example
├── 2522030106_Week1.docx     # Week 1 Lab Documentation
├── 2522030106_Week2.docx     # Week 2 Lab Documentation
├── 2520030106_Week3.docx     # Week 3 Lab Documentation
└── README.md
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dugganaboyinamohitvenkatsai-cloud/2520030106_S4_GenAI.git
   cd 2520030106_S4_GenAI
   ```

2. **Configure Environment:**
   In each week folder (e.g., `Week1`, `Week2`, `Week3`), copy `.env.example` to `.env` and add your Gemini API key:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r Week2/requirements.txt
   pip install -r Week3/requirements.txt
   ```
