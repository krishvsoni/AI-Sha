from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import openai

openai.api_key = "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"


def chat(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chatAPI(request):
    if request.method == "POST":

        json_data=json.loads(request.body.decode("utf-8"))
        prompt = json_data["prompt"]
        print(prompt)
        # prompt is accessed here but i dont have api key so i cant test it
        
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
        return JsonResponse({"data": "send data here"})
    return HttpResponse(status=405)
