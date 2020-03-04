from toscatranslator.common import snake_case

from toscatranslator.providers.common.provider_resource import ProviderResource


class KubernetesProviderResource(ProviderResource):

    NODE_PRIORITY_BY_TYPE = dict(
        Deployment=0,
        Service=1,
    )

    ANSIBLE_MODULE_PREFIX = 'os_'
    ANSIBLE_DESCRIPTION_PREFIX = 'Create '

    PROVIDER = 'kubernetes'

    def ansible_description_by_type(self):
        desc = self.ANSIBLE_DESCRIPTION_PREFIX + self.type_name
        return desc

    def ansible_module_by_type(self):
        module_name = self.ANSIBLE_MODULE_PREFIX + snake_case.convert(self.type_name)
        return module_name

