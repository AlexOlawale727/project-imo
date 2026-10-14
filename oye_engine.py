import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

# Initialize FastAPI app
app = FastAPI(title="Project Ìmọ̀ Socratic Engine")

# Enable CORS so your browser frontend can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Google GenAI Client (pulls GEMINI_API_KEY from environment variables)
# Make sure to set your API key in the Codespace secrets or terminal environment
client = genai.Client()

# Request body model from the frontend UI
class QueryRequest(BaseModel):
    message: str
    track: str = "WAEC"
    subject: str = "Physics"

# Socratic System Prompt enforcing guidelines
SOCRATIC_SYSTEM_PROMPT = """
You are Ọ̀yẹ́, a warm, friendly, and expert Socratic study partner designed for West African secondary school students preparing for WAEC, JAMB, NECO, and BECE.
Your core rules:
1. NEVER give direct answers or solve equations completely for the student.
2. Guide them step-by-step by asking thoughtful, probing questions that help them discover the answer themselves.
3. Keep responses concise, engaging, and supportive (under 100 words where possible).
4. Adapt your tone to be encouraging, like a brilliant older peer wearing a cozy hoodie and oversized glasses.
"""

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    try:
        # Construct prompt combining student track, subject, and message
        full_prompt = (
            f"Exam Track: {request.track}\n"
            f"Subject: {request.subject}\n"
            f"Student Message: {request.message}"
        )

        # Call Gemini API using the official google-genai SDK
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SOCRATIC_SYSTEM_PROMPT,
                temperature=0.7,
            ),
        )

        return {"reply": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"status": "Project Ìmọ̀ Cloud Engine is running smoothly!"}
