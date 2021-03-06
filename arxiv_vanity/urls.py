"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .feedback.views import submit_feedback
from .papers.feeds import LatestPapersFeed
from .papers.views import HomeView, PaperListView, paper_detail, paper_convert, paper_render_state, render_update_state

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^papers/$', PaperListView.as_view(), name='paper_list'),
    url(r'^papers/feed/$', LatestPapersFeed(), name='paper_feed'),
    url(r'^papers/(?P<arxiv_id>[^/]+)/$', paper_detail, name='paper_detail'),
    url(r'^papers/(?P<arxiv_id>[^/]+)/render-state/$', paper_render_state, name='paper_render_state'),
    url(r'^renders/(?P<pk>\d+)/update-state/$', render_update_state, name='render_update_state'),
    url(r'^convert/$', paper_convert, name='paper_convert'),
    url(r'^submit-feedback/$', submit_feedback),
    url(r'^admin/', admin.site.urls),
]

# Serve uploaded files in development
if settings.DEBUG and settings.MEDIA_URL:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
