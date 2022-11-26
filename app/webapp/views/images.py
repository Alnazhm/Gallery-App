from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Image
from webapp.forms import ImageForm


class IndexView(ListView):
    template_name = 'images.html'
    model = Image
    context_object_name = 'images'
    ordering = '-created_at'


class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_image.html'
    form_class = ImageForm
    model = Image



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user.username
            form.save()
            return redirect('profile', pk=self.request.user.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class ImageView(DetailView):
    template_name = 'image_detail.html'
    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.object
        users = image.users.all
        context['users'] = users
        return context


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'image_edit.html'
    form_class = ImageForm
    model = Image
    context_object_name = 'image'
    permission_required = 'webapp.change_image'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user.username

    def get_success_url(self):
        return reverse('image_detail', kwargs={'pk': self.object.pk})


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_image'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user.username


class ImageFavoriteView(View):


    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if image in user.images.all():
            user.images.remove(image)
            return redirect('index')
        user.images.add(image)
        return redirect('index')
