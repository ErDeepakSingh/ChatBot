from django.shortcuts import render

# Create your views here.
#
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
#
# #creating a new chatbot
# chatbot=ChatBot("Deepak")
# trainer=ListTrainer(chatbot)
# trainer.train(['hi,can i help you find a plan',"sure I'd love to find you a plan","Your plan have been selected"])
#
# # getting a response from the chatbot
# response=chatbot.get_response("I want a plan")
# print(response)



from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#creating a new chatbot
english_bot=ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer=ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


def jarvis_chat_bot(request):
    template_name='JarvisBot/jarvis_chat_bot.html'
    if request.method=="POST":
        print("request.POST", request.POST)
        user_text = request.POST['msg']
        response=str(english_bot.get_response(user_text))
        context={
            "response":response
        }
        return render(request, template_name, context)
    return render(request,template_name)



#getting a response from the chatbot
from django.http import HttpResponse
def getBotResponse(request):
    if request.method=='GET':
        print("request.GET",request.GET)
        userText = request.GET['msg']
        print("userText",userText)
        response=str(english_bot.get_response(userText))
        print("response : ",response)
        return HttpResponse(response)
        return response

