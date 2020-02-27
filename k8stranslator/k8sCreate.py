import yaml

from toscaparser.tosca_template import ToscaTemplate

API_VERSION = 'apiVersion'
API_GROUP = 'apiGroup'
TYPE = 'type'


class KubernetesObj(object):
    def __init__(self, kind=None, api_version=None, properties=None):
        self.properties = properties
        self.api_version = api_version
        self.kind = kind

    def get_props(self):
        return self.properties

    def get_version(self):
        return self.api_version

    def get_kind(self):
        return self.kind


# Todo: exception
def load_template(template_file, validate_only=False):
    return ToscaTemplate(path=template_file, a_file=True)


# Todo: exception
def translate(template_file):
    k8s_template = load_template(template_file)
    node_templates = k8s_template.topology_template.nodetemplates
    k8s_list = []
    for template in node_templates:
        props_list = [prop.value for prop in template.get_properties_objects() if
                      prop.name != API_VERSION and prop.name != API_GROUP]
        k8s_list.append(
            KubernetesObj(template.entity_tpl.get(TYPE).split('.'),
                          template.get_property_value(API_GROUP) + '/' + template.get_property_value(API_VERSION),
                          props_list))
    for k8s_obj in k8s_list:
        complete_yaml = yaml.dump([dict(
            apiVersion=k8s_obj.get_version(),
            kind=k8s_obj.get_kind()[2],
            spec=k8s_obj.get_props()
        )])
        print(complete_yaml)
