# Create your views here.
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, UpdateView, DetailView

from post.forms import PostForm
from registration.models import Post


class IndexView(ListView):
    model = Post
    template_name = 'post/index.html'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Post.objects.filter(
                Q(user__username=q_word) | Q(text__icontains=q_word)
            )
        else:
            object_list = Post.objects.all().order_by('published_at')

        return object_list


class PostFormView(FormView):
    form_class = PostForm
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post:index')

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        Post.objects.filter(user=self.request.user)
        form.save()
        return super(PostFormView, self).form_valid(form)


class TextUpdateView(UpdateView):
    template_name = 'post/text_updateview.html'
    model = Post
    fields = ['text', ]

    def get_success_url(self):
        return reverse('post:index')

    def get_form(self, form_class=None):
        form = super(TextUpdateView, self).get_form()
        form.fields['text'].label = 'text'
        return form


class UserDetailView(DetailView):
    template_name = 'post/user_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)

        context['texts'] = Post.objects.filter(user=self.request.user)
        return context
