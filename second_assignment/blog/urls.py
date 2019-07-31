from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:blog_id>', views.detail, name="detail"),
    # path('new/', views.new, name="new"),
]
   # path('admin/', admin.site.urls),
#     #path('',blog.views.home, name='home'),
#     #path('blog/<int:admin>/', blog.views.detail, name='detail'),

#     #path('portfolio/',portfolio.views.portfolio, name="portfolio"),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)