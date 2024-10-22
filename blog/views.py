from django.shortcuts import render




def blog_home(request):
    context = {'post_1':'Bitcoin crashed', 'post_2':'Gold rise up', 'post_3':'Barca win all games','post_4':'Real Madrid vs Dortmond'}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    
    return render(request,'blog/blog-single.html')

