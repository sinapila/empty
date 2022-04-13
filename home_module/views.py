from django.shortcuts import render
from django.views.generic.base import TemplateView

# class HomeView(View):
#     def get(self,request):
#         return render(request, 'home_module/index_page.html')
from site_module.models import SiteSetting, FooterLinkBox, Slider


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        sliders = Slider.objects.filter(is_active=True)
        context['slders'] = sliders
        return context


class AboutView(TemplateView):
    template_name = 'home_module/About_page.html'

    def get_context_data(self, **kwargs):
        contaxt = super(AboutView, self).get_context_data()
        settings: SiteSetting = SiteSetting.objects.filter(is_main_settings=True).first()
        contaxt['settings'] = settings
        return contaxt


def site_header_component(request):
    settings: SiteSetting = SiteSetting.objects.filter(is_main_settings=True).first()
    return render(request, 'shared/site_header_partial.html', {
        'settings': settings
    })


def site_footer_component(request):
    settings: SiteSetting = SiteSetting.objects.filter(is_main_settings=True).first()
    linkboxes : FooterLinkBox = FooterLinkBox.objects.all()
    return render(request, 'shared/site_footer_partial.html', {
        'settings': settings,
        'linkboxes': linkboxes,
    })
