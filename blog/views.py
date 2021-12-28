from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	result = 0
	if request.method == "POST":
		num1 = request.POST.get('num_1')
		num2 = request.POST.get('num_2')
		result = int(num1) + int(num2)
		print(request.POST)
		print(result)

	# context = {
	# 	'result': result
	# }
	# return render(request, 'blog/post_list.html', context)
	# return render(request, 'blog/post_list.html', {'posts': posts})
	return render(request, 'blog/post_list.html', {'posts': posts,'result': result})


# def calprint(request):
# 	c = calc(request)
# 	return render(request, "result.html", {"result": c})

# def post_list(request):
#   if(request.GET.get('mybtn')):
# 	mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
# return render(request,'myApp/templateHTML.html')

