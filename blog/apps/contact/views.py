from apps.contact.models import Contact
from .forms import ContactAnonymousForm, ContactAuthenticatedForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


#  --------------------------------------- CONTACTO ------------------------------------------------

# CONTACTO INICIAL
class ContactUsuer(CreateView):
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('apps.contact:contact_success')
    form_class = ContactAnonymousForm

    def get_form_class(self):
        if self.request.user.is_authenticated:
            return ContactAuthenticatedForm
        else:
            return ContactAnonymousForm

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['full_name'] = self.request.user.get_full_name()
            initial['email'] = self.request.user.email
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada con exito.')
        return super().form_valid(form)


# CONTACTO EXITOSO
class ContactSuccess(TemplateView):
    template_name = 'contact/contact_success.html'




#  --------------------------------------- MENSAJES ------------------------------------------------

# LISTA DE MENSAJES
class MessagesListView(ListView):
    model = Contact
    template_name = 'contact/messages.html'
    context_object_name = 'messages'

        # VERIFICA QUE EL USUARIO SEA EL "Administrador" O "SuperUser"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# DETALLES DEL MENSAJE
class MessagesDetailView(DetailView):
    model = Contact
    template_name = 'contact/message_detail.html'
    context_object_name = 'messages'
    pk_url_kwarg = 'id'

        # VERIFICA QUE EL USUARIO SEA EL "Administrador" O "SuperUser"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# ELIMINANDO MENSAJE
class MessagesDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/message_delete.html'
    success_url = reverse_lazy('apps.contact:messages')
    pk_url_kwarg = 'id'

        # VERIFICA QUE EL USUARIO SEA EL "Administrador" O "SuperUser"
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or (request.user.username != 'Administrador' and request.user.username != 'SuperUser'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)