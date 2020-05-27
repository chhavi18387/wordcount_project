from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
	return render(request,'home.html' )
def count(request): 
	fulltext1= request.GET["fulltext"]
	l=fulltext1.split()
	wordcount={}
	for i in l:
		if i in wordcount:
			wordcount[i]=wordcount[i]+1
		else:
			wordcount[i]=1
	print(fulltext1)
	sortedwordcount=sorted(wordcount.items() , key=operator.itemgetter(1),reverse=True)
	return render(request,'count.html',{'text':fulltext1  , 'count':len(l) , 'wordcount':sortedwordcount}  )

def aboutt(request):
	return render(request,'aboutt.html')