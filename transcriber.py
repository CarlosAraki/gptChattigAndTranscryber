import whisper
# import os
# if os.path.exists('historicotrans.txt'):
#     with open('historicotrans.txt', 'r') as arquivo:
#         historico = arquivo.read().splitlines()

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("rc.webm")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(fp16 = False)

result = whisper.decode(model, mel, options)

# print the recognized text
#print(result.text)

result = model.transcribe("rc.webm",initial_prompt='Reunião de tecnologia informal com termos voltados a segurança do trabalho sem nenhum termo em inglês o cliente chama Acelen ',fp16 = False)
print(result["text"])
