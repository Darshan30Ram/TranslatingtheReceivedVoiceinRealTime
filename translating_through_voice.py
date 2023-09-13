from translate import Translator
import speech_recognition as sr


def translate_word(c, d):
    translator = Translator(to_lang=d)  # object is being created which is configured to convert source lang to
    # target lang
    translated = translator.translate(c)  # using the object we are calling the function og Translator class and
    # passing it the parameter i.e. the source and the returned value will be the translated words which will be
    # stored in the translated variable
    return translated


r = sr.Recognizer()  # New instance of the Recognizer class from speech recognition package is being created which
# manages and controls  the speech rec process
while True:
    with sr.Microphone() as source:  # sr.Microphone for to listen live voice
        r.adjust_for_ambient_noise(source, duration=0.5)  # removes the noises and improves the actual voice it should
        # be recognizing
        print("Speak now")
        audio = r.listen(source)  # captures voice and stores in audio variable

        try:
            text = r.recognize_google(audio)  # this line uses Google's web Speech API
            # It is used to perform speech recognition
            if text == 'exit':
                break
            print(text)
            print(""""ar = Arabic, et = Armenian, art = Artificial Langauge,
                     sq = Albanian,bn = Bangla, bh = Bhojpuri,
                    bul = Bulgarian, cai = Central American Indian Language,
                     cze = Caech, dan = Danish, ger = German, eg = Egyptian, en = English,
                     fre = french, gon = Gondi, grc = Greek, gsw = Swiss German, hi = Hindi,ind=Indonesian, 
                    ita = Italian, ja = Japanese, kn = Kannada,kas = Kashmiri, geo = Georgian, kor = Korean,
                    lat = Latin,mar = Marathi, mni = Manipuri,mul = Multiple Languages,dut = Dutch,te = Telugu,
                    ta = Tamil,cy = Welsh""")  # ISO 639 international-standard language-code

            target_language = input("Enter the target language (e.g., 'kn' for kannada): ")

            translated_word = translate_word(text, target_language)  # calling the translator function
            print(f"Translated word: {translated_word}")
            a = input("If you want to change this translated to words to any other language type yes: ").lower()  #
            # asking the user whether he wants to translate the words again
            if a == 'yes':
                t_language = input("Enter the target language (e.g., 'kn' for kannada): ")
                t_word = translate_word(translated_word, t_language)
                print(f"Translated word is {t_word}")

        except sr.UnknownValueError:
            print("Please say again...!")
