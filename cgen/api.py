from tastypie.resources import ModelResource
from tastypie.api import NamespacedApi
from cgen.models import Character, ClassChassis, Race


class CharacterResource(ModelResource):
	class Meta:
		queryset = Character.objects.all()


class ClassChassisResource(ModelResource):
	class Meta:
		queryset = ClassChassis.objects.all()


class RaceResource(ModelResource):
	class Meta:
		queryset = Race.objects.all()

	def dehydrate_size(self, bundle):
		return bundle.obj.get_size_display()


def register_api():
	api = NamespacedApi(api_name='v1', urlconf_namespace='cgen')
	api.register(CharacterResource())
	api.register(ClassChassisResource())
	api.register(RaceResource())

	return api