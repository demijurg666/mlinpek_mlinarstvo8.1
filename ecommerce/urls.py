"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from store import views
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('update_item/', views.updateItem, name='updateItem'),

]
#imao si error sa jezicima i jsonom! ovo sa jezicima u linku dodaje sr/en/zh. json radi update_item i nije uopste mogao da radi tj nije mogao da dodaje u cart (vrv jer je json navikao da radi bez sr/en/zh u linku). resenje errora je da ubacim path sa update itemom u prvi url pattern, jer ovaj drugi(sa i18n) dodaje to sr/en/zh


urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('store.urls')),
    path('', views.store, name='store'),
    path('izdavastvo/', views.izdavastvo, name='izdavastvo'),

    path('proizvodnjaPsenicnogBrasna/', views.proizvodnjaPsenicnogBrasna, name='proizvodnjaPsenicnogBrasna'),
    path('prvopoglavljeproizvodnjapsenicnog/', views.prvopoglavljeproizvodnjapsenicnog, name='prvopoglavljeproizvodnjapsenicnog'),
    path('vademekumPdf/', views.vademekumPdf, name='vademekumPdf'),
    path('prirucnikZaMlevenjeZitaPdf/', views.prirucnikZaMlevenjeZitaPdf, name='prirucnikZaMlevenjeZitaPdf'),
    path('psenicaikvalitetbrasnaprica/', views.psenicaikvalitetbrasnaprica, name='psenicaikvalitetbrasnaprica'),

    path('priceSaTerena/', views.priceSaTerena, name='priceSaTerena'),
    path('trgovina/', views.trgovina, name='trgovina'),
    path('pecanje/', views.pecanje, name='pecanje'),
    path('pesme/', views.pesme, name='pesme'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('kurs/', views.kurs, name='kurs'),
    path('mlin/', views.mlin, name='mlin'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutPage/', views.logoutPage, name='logoutPage'),
    path('searchProducts/', views.searchProducts, name='searchProducts'),
    path('psenicaikvalitetbrasnaprica/', views.psenicaikvalitetbrasnaprica, name='psenicaikvalitetbrasnaprica'),
    path('kursTehnologije/', views.kursTehnologije, name='kursTehnologije'),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]