# Converte um áudio WAV para texto usando a biblioteca SpeechRecognition
# Instalar com: pip install SpeechRecognition pydub

import speech_recognition as sr

def audio_para_texto(caminho_arquivo):
    reconhecedor = sr.Recognizer()
    with sr.AudioFile(caminho_arquivo) as fonte:
        audio = reconhecedor.record(fonte)
    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        print("Texto reconhecido:", texto)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError:
        print("Erro ao acessar o serviço de reconhecimento.")

# Exemplo: substitua 'audio.wav' por um arquivo real
# audio_para_texto('audio.wav')
