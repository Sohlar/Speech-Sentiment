import speech_recognition as sr
def record_data():
    r = sr.Recognizer()
    with sr.Microphone() as input:
        print("Recording")
        data = r.listen(input)
    try:
        print("Google thinks you said " + r.recognize_google(data))
        return r.recognize_google(data)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return 0
    except sr.RequestError as e:
        print("Could not request results ; {0}".format(e))
        return 0