from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.email_app.forms import TemplateForm
from apps.email_app.models.template import Template


class EmailTemplateUploadView(LoginRequiredMixin, FormView):
    form_class = TemplateForm
    template_name = 'email_app/template_upload_form.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        files = self.request.FILES.getlist('template_file')
        for file in files:
            Template.objects.create(
                user=self.request.user,
                name=file.name,
                template_file=file
            )
        return super().form_valid(form)
