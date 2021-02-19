from django.shortcuts import render

# Create your views here.
def home(request):
   return render(request, "home.html")

def result(request):
    sentence = request.GET['sentence']
    
    wordList = sentence.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request, "result.html", {'fulltext' : sentence, 'count' : len(wordList), 'wordDict' : wordDict.items})
    # 넘겨줄 값: 입력값 전체, 총 단어 수, Dict 파일
    # 각 단어 이름과 단어가 쓰인 개수를 알려줘야 해서 'wordDict' : wordDict 하면 안됨
    # .items 하면 각각 키값과 value 값이 쌍으로 넘어감