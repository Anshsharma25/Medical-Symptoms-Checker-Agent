from gtts import gTTS

def speak_report(text, language="en", output_file="outputs/medical_report_audio.mp3"):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)
    print(f"Audio report saved as {output_file}.")