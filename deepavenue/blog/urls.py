from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    # url(r'^d$', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$', views.sms_list, name='sms_list'),
    url(r'^sms/(?P<pk>\d+)/$', views.sms_detail, name='sms_detail'),
    url(r'^api/graphql', csrf_exempt(GraphQLView.as_view())),
    url(r'^api/graphiql', csrf_exempt(
        GraphQLView.as_view(graphiql=True, pretty=True))),
]
