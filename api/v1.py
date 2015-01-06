from api.models import Company, Job
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name']
        authentication = SessionAuthentication()


class CompanyResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Company.objects.all()
        detail_uri_name = 'slug'
        authentication = SessionAuthentication()

    def obj_create(self, bundle, **kwargs):
        return super(CompanyResource, self).obj_create(
            bundle,
            user=bundle.request.user,
        )


class JobResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Job.objects.all()
        detail_uri_name = 'slug'
        authentication = SessionAuthentication()

    def obj_create(self, bundle, **kwargs):
        return super(JobResource, self).obj_create(
            bundle,
            user=bundle.request.user,
        )


api = Api(api_name='v1')
api.register(UserResource())
api.register(CompanyResource())
api.register(JobResource())
