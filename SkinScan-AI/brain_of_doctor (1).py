
import os
from pathlib import Path
import mimetypes
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an experienced AI Skin Healthcare Assistant.

Responsibilities:
1. Analyze uploaded skin images.
2. Analyze uploaded skin videos if available.
3. Understand the patient's spoken symptoms.
4. Explain what you observe.
5. Suggest possible skin conditions.
6. Recommend home care if appropriate.
7. Tell the user when they should visit a dermatologist.
8. Never claim a definite diagnosis.
9. End every response with:
'This is not a medical diagnosis. Please consult a qualified doctor.'
"""

def brain_of_doctor(
    patient_text: str,
    image_filepath: str | None = None,
    video_filepath: str | None = None,
) -> str:
    """
    Main reasoning function evaluating symptoms, images, and videos.
    """
    contents = []

    if image_filepath and Path(image_filepath).exists():
        try:
            image = Image.open(image_filepath)
            contents.append(image)
        except Exception as e:
            print(f"Error opening image: {e}")


    if video_filepath and Path(video_filepath).exists():
        try:
            with open(video_filepath, "rb") as f:
                video_bytes = f.read()
            
            mime_type, _ = mimetypes.guess_type(video_filepath)
            if not mime_type:
                mime_type = "video/mp4"

            contents.append(
                types.Part.from_bytes(
                    data=video_bytes,
                    mime_type=mime_type,
                )
            )
        except Exception as e:
            print(f"Error processing video: {e}")

    
    contents.append(
        f"""
{SYSTEM_PROMPT}

Patient Symptoms:
{patient_text}

Please analyze every uploaded image/video together with the symptoms.
Explain:
1. What you observe.
2. Possible skin condition.
3. Severity.
4. Home care.
5. When emergency care is needed.
"""
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
        )
        return response.text
    except Exception as e:
        return f"Error while contacting Gemini API:\n{e}"
