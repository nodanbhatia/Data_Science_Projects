import gradio as gr
from voice_of_the_patient import transcribe_patient_voice
from brain_of_doctor import brain_of_doctor
from voice_of_the_doctor import convert_text_to_doctor_audio

def process_inputs(audio_path, image_filepath, video_filepath):
  
   
    patient_text = transcribe_patient_voice(audio_path)
    
  
    doctor_text = brain_of_doctor(
        patient_text=patient_text,
        image_filepath=image_filepath,
        video_filepath=video_filepath,
    )


    doctor_audio_path = convert_text_to_doctor_audio(doctor_text)

    return patient_text, doctor_text, doctor_audio_path



iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone", "upload"], type="filepath", label="Patient Voice Input"),
        gr.Image(type="filepath", label="Skin Area Image"),
        gr.Video(label="Skin Area Video (Optional)"),
    ],
    outputs=[
        gr.Textbox(label="Patient Voice Transcribed"),
        gr.Textbox(label="Doctor's Assessment & Recommendations"),
        gr.Audio(label="Doctor's Spoken Voice Response", type="filepath"),
    ],
    title="< AI SKIN SPEACIALIST >",
    description="""Your skin has a story. Tell us what you're experiencing in your own voice, share a photo, and let our secure AI guide your path to clear skin."
Why it works: Emphasizes care, security, and human-centric wellness. It feels warm and reduces clinical anxiety.""",
)

if __name__ == "__main__":
    iface.launch(debug=True)
