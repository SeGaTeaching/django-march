from django.shortcuts import render, redirect
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

@login_required('login')
def create_post_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # ✨ Setze aktuellen Benutzer
            blog_post.save()
            return redirect('blog_post_success')  # oder zur Detail-/Listenansicht
    
    form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})