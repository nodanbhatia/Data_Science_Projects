
import os
from pathlib import Path
import mimetypes
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def transcribe_patient_voice(audio_filepath: str | None) -> str:
    
    if not audio_filepath or not Path(audio_filepath).exists():
        return "No audio recording provided by the patient."

    if not API_KEY:
        return "Error: GEMINI_API_KEY is missing from environment variables."

    client = genai.Client(api_key=API_KEY)
    
    
    mime_type, _ = mimetypes.guess_type(audio_filepath)
    if not mime_type:
         mime_type = "audio/wav" # Fallback

    try:
        with open(audio_filepath, "rb") as f:
            audio_bytes = f.read()

      
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=audio_bytes,
                    mime_type=mime_type,
                ),
                "Please transcribe this audio exactly. Do not add any conversational remarks, corrections, or extra words. Just output the transcription."
            ]
        )
        return response.text.strip()
    except Exception as e:
        return f"[Speech-to-Text Error]: {e}"