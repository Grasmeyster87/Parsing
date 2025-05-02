import vosk
import wave
import json
from pydub import AudioSegment


def get_text_from_audio():
    """MP3 в текст"""
    model_path = "./vosk-model-small-en-us-0.15"  # путь к модели
    vosk.SetLogLevel(-1)
    model = vosk.Model(model_path)

    audio_file = "audio (1).mp3"  # путь к mp3
    wav_file = "audio.wav"

    # Конвертируем MP3 в WAV
    audio = AudioSegment.from_mp3(audio_file)
    audio.export(wav_file, format="wav")

    # Открываем WAV файл
    wf = wave.open(wav_file, "rb")

    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    full_text = []

    # Распознавание речи
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            full_text.append(result.get("text", ""))

    # Добавляем финальный результат (остатки буфера)
    final_result = json.loads(rec.FinalResult())
    full_text.append(final_result.get("text", ""))

    recognized_text = " ".join(full_text)
    print(recognized_text)
    return recognized_text


get_text_from_audio()
