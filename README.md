# Trade Opportunities API

## Overview
Get market analysis reports using AI for sectors like pharmaceuticals, technology, agriculture.

## Features
- Sector-based analysis using Google Gemini
- Markdown output
- Token-based auth

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set your Gemini API key [in ai_analyzer.py]:
```bash
GOOGLE_API_KEY="your_key_here"
```
“You’ll need to generate your own Gemini API key from Google AI Studio and replace the placeholder in the script.”

Run server:
```bash
uvicorn main:app --reload
```

## Usage
```http
GET /analyze/pharmaceuticals
Header: token: "DEyZwVbMaSz0DMb7rSCRc1dKEGLwmKANWC7G"
```