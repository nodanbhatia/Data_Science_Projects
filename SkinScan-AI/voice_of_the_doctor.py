import os
from pathlib import Path
from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPGRAM_API_KEY")

def convert_text_to_doctor_audio(text: str) -> str | None:
   
    if not api_key:
        print("Deepgram API Key not configured.")
        return None

    if not text or text.strip() == "":
        return None


    clean_text = text.replace("*", "").replace("#", "").strip()

    try:
        deepgram = DeepgramClient(api_key=api_key)
        
      
        audio_response = deepgram.speak.v1.audio.generate(
            text=clean_text,
            model="aura-2-thalia-en",
            encoding="mp3",
        )

        output_file = "doctor_response.mp3"
        audio_path = Path(output_file)

        
        with audio_path.open("wb") as file:
            for chunk in audio_response:
                file.write(chunk)

        return str(audio_path)

    except Exception as e:
        print(f"Error generating doctor voice: {e}")
        return None
