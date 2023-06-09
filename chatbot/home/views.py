from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
import openai

openai.api_key = "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"




def chat(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def chatAPI(request):
    if request.method == "POST":


        prompt = request.POST["prompt"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response)
        return JsonResponse(response)
    return HttpResponse(status=405)




