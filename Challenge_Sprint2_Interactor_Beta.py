import pyttsx3
import speech_recognition as sr
import pyaudio

recon = sr.Recognizer()

en = pyttsx3.init()
en.setProperty('rate', 155)
en.setProperty('volume', 1)
en.setProperty('voice', b'brasil')

def avaliacao_funcionario():
    print("Digite uma nota de 0 a 10 para a presença do funcionário: ")
    en.say("Digite uma nota de 0 a 10 para a presença do funcionário: ")
    en.runAndWait()
    faltas = int(input())

    print("Digite uma nota de 0 a 10 para as entregas do funcionário: ")
    en.say("Digite uma nota de 0 a 10 para as entregas do funcionário: ")
    en.runAndWait()
    entregas = int(input())


    print("Digite uma nota de 0 a 10 para o comprometimento do funcionário: ")
    en.say("Digite uma nota de 0 a 10 para o comprometimento do funcionário: ")
    en.runAndWait()
    comprometimento = int(input())

    print("Digite uma nota de 0 a 10 para a pontualidade do funcionário: ")
    en.say("Digite uma nota de 0 a 10 para a pontualidade do funcionário: ")
    en.runAndWait()
    pontualidade = int(input())


    if faltas <0 or faltas >10 or entregas <0 or entregas >10 or comprometimento <0 or comprometimento >10 or pontualidade <0 or pontualidade >10:
        print("Valores inválidos, digite novamente.")
        en.say("Valores inválidos, digite novamente.")
        en.runAndWait()
    else:
        media_func = (faltas + entregas + comprometimento + pontualidade) / 4

        if media_func <=3:
            print("O funcionário está performando mal, deseja enviar um feedback direcionado e adicionar opções de curso com desconto para melhorar a performace do colaborador?")
            en.say("O funcionário está performando mal, deseja enviar um feedback direcionado e adicionar opções de curso com desconto para melhorar a performace do colaborador?")
            en.runAndWait()
            with sr.Microphone() as source:
                feedback = recon.listen(source)
                fb = recon.recognize_google(feedback, language='pt-BR')
                if fb == "sim":
                    print("Feedback enviado, e cursos com desconto oferecidos.")
                    en.say("Feedback enviado, e cursos com desconto oferecidos.")
                    en.runAndWait()
                else:
                    breakpoint()
        elif media_func <=5:
            print("O funcionário está performando abaixo da média, gostaria de enviar um feedback direcionado ao erro do colaborador?")
            en.say("O funcionário está performando abaixo da média, gostaria de enviar um feedback direcionado ao erro do colaborador?")
            en.runAndWait()
            with sr.Microphone() as source:
                feedback = recon.listen(source)
                fb = recon.recognize_google(feedback, language='pt-BR')
                if fb == "sim":
                    print("Feedback enviado com sucesso.")
                    en.say("Feedback enviado com sucesso.")
                    en.runAndWait()
                else:
                    breakpoint()
        elif media_func <= 7:
            print("O funcionário está performando na média, gostaria de enviar um feedback para agregar ainda mais na parte técnica do profissional?")
            en.say("O funcionário está performando na média, gostaria de enviar um feedback para agregar ainda mais na parte técnica do profissional?")
            en.runAndWait()
            with sr.Microphone() as source:
                feedback = recon.listen(source)
                fb = recon.recognize_google(feedback, language='pt-BR')
                if fb == "sim":
                    print("Feedback enviado com sucesso.")
                    en.say("Feedback enviado com sucesso.")
                    en.runAndWait()
                else:
                    breakpoint()
        else:
            print("O funcionário está performando muito bem, gostaria de enviar um feedback positivo o parabenizando?")
            en.say("O funcionário está performando muito bem, gostaria de enviar um feedback positivo o parabenizando?")
            en.runAndWait()
            with sr.Microphone() as source:
                feedback = recon.listen(source)
                fb = recon.recognize_google(feedback, language='pt-BR')
                if fb == "sim":
                    print("Feedback enviado com sucesso.")
                    en.say("Feedback enviado com sucesso.")
                    en.runAndWait()
                else:
                    breakpoint()

avaliacao_funcionario()