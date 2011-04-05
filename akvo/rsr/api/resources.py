# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

import inspect

from lxml import etree
from lxml.builder import ElementMaker #, E

from rsr.models import Project, Category, Link

#.GenericRelation(Location)

def who_is_parent():
    """
    introspecting function returning the name of the caller of the function
    where who_is_parent is called
    """
    return inspect.stack()[2][3]

XML_NS      = "http://www.w3.org/XML/1998/namespace"
AKVO_NS     = "http://www.akvo.org/rsr/api"
NS_MAP = {
    "xml":   XML_NS,
    "akvo":  AKVO_NS,
}        
A = ElementMaker(nsmap=NS_MAP, namespace=AKVO_NS)
E = ElementMaker(nsmap=NS_MAP)

class ParentedElement(object):
    def __init__(self, bundle, element, parent):
        self.bundle = bundle
        self.element = element
        self.parent = parent
    
    def set_in_tree(self):
        if self.parent:
            parent = self.bundle.data[self.parent]
            if isinstance(parent, ParentedElement):
                parent.element.append(self.element)
            else:
                parent.append(self.element)
                
    
class IATISerializer(Serializer):
    formats = ['xml',]
    content_types = {
        'xml': 'application/xml',
    }
    
    #def to_xml(self, data, options=None):
    #    #import pdb
    #    #pdb.set_trace()
    #    options = options or {}
    #    XML_NS      = "http://www.w3.org/XML/1998/namespace"
    #    AKVO_NS     = "http://www.akvo.org/rsr/api"
    #    NS_MAP = {
    #        "xml":   XML_NS,
    #        "akvo":  AKVO_NS,
    #    }
    #    #akvo namspaced element
    #    tree = self.to_etree(data, options)
    #    import pdb
    #    pdb.set_trace()
    #    
    #    A = ElementMaker(nsmap=NS_MAP, namespace=AKVO_NS)
    #
    #    import pdb
    #    pdb.set_trace()
    #    if isinstance(data, dict):
    #        return self.to_xml(data['objects'], options)
    #    if isinstance(data, (tuple, list)):
    #        for item in data:
    #            return self.to_xml(item, options)
    #    elif isinstance(data, Bundle):
    
    #def to_xml(self, data, options=None):
    #    options = options or {}
    #    XML_NS      = "http://www.w3.org/XML/1998/namespace"
    #    AKVO_NS     = "http://www.akvo.org/rsr/api"
    #    NS_MAP = {
    #        "xml":   XML_NS,
    #        "akvo":  AKVO_NS,
    #    }
    #    #akvo namspaced element
    #    A = ElementMaker(nsmap=NS_MAP, namespace=AKVO_NS)
    #    page = E(
    #        'iati-activites',
    #        E(
    #            'iati-activity',
    #            E(
    #                'iati-identifier',
    #                'Akvo-%d' % data.obj.pk
    #            ),
    #            A(
    #                'project-summary',
    #                data.obj.project_plan_summary,
    #            ),
    #            {
    #                '{%s}lang' % XML_NS: 'eng',
    #                'default-currency': 'EUR',
    #                'hierarchy': '1',
    #                'last-updated': u'Now!'
    #            },
    #        ),
    #        E(
    #            'iati-activity',
    #            {'{%s}lang' % XML_NS: 'eng'}
    #        ),
    #        {'generated-datetime':u'Närdå?'}, version='1.00'
    #    )
    #    return etree.tostring(page, pretty_print=True, xml_declaration=True, encoding='utf-8')

    def to_etree(self, data, options=None, name=None, depth=0):
        """
        Given some data, converts that data to an ``etree.Element`` suitable
        for use in the XML output.
            """
        if isinstance(data, (list, tuple)) and isinstance(data[0], ParentedElement):
            import pdb
            pdb.set_trace()
            for item in data:
                self.to_etree(item, options, name, depth)
        elif isinstance(data, ParentedElement):
            data.set_in_tree()
        else:
            return super(IATISerializer, self).to_etree(data, options, name, depth)


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'


class ProjectResource(ModelResource):
    categories = fields.ToManyField(CategoryResource, 'categories')
    links = fields.ToManyField('akvo.rsr.api.resources.LinkResource', 'links')
    
    class Meta:
        queryset = Project.objects.active()
        resource_name = 'project'

class IATIActivityResource(ModelResource):
    """
    We wanna create XML looking like this:
    
    <iati-acitvity xml:lang="en" default-currency="EUR" hierarchy="1" last-updated-datetime"2001-01-01">
      <iati-identifier>Akvo-{{Project.id}}</iati-identifier>
      <!-- describing text fields -->
      <description type="General">Project.project_plan_summary</description>
      <description akvo:type="Details">Project.project_plan_detail</description>
      <description akvo:type="Current status">Project.current_status_detail</description>
      <description akvo:type="Sustainability">Project.sustainability</description>
      <description akvo:type="Context">Project.context</description>
      <description type="Objectives">Project.goals_overview</description>
      <!-- don't think we have this info -->
      <description type="Target groups"></description>
      
    </iati-acitvity>
    """
    categories = fields.ToManyField(CategoryResource, 'categories')
    links = fields.ToManyField('akvo.rsr.api.resources.LinkResource', 'links')

    class Meta:
        queryset = Project.objects.active()
        resource_name = 'iati-activity'
        serializer = IATISerializer()
    
    def element_factory(self, bundle, tag_name, attrib=None, parent=None):
        """create an lxml Element and assign it to the bundle.data
        get the field name by removing "dehydrate_" from who_is_parent
        use the field name to get the original data from the bundle
        create the Element using the tag_name, the original data and any supplied attributes
        remove field_name data from bundle.data
        """
        field_name = '_'.join(who_is_parent().split('_')[1:])
        attrib = attrib or {}
        data = bundle.data
        element = E(
            tag_name,
            data[field_name],
            attrib
        )
        if tag_name in data:
            if isinstance(data[tag_name], ParentedElement):
                data[tag_name] = [data[tag_name]]
            data[tag_name].append(ParentedElement(bundle, element, parent))
        else:
            data[tag_name] = ParentedElement(bundle, element, parent)
        data.pop(field_name)
        
    def dehydrate_id(self, bundle):
        self.element_factory(bundle, 'iati-activity')

    def dehydrate_project_plan_summary(self, bundle):
        self.element_factory(bundle, 'description', {'type': 'General'}, 'iati-activity')

    def dehydrate_project_plan_detail(self, bundle):
        self.element_factory(bundle, 'description', {'{%s}type' % AKVO_NS: 'Details'}, 'iati-activity')

    def full_dehydrate(self, obj):
        """
        Given an object instance, extract the information from it to populate
        the resource.
        """
        bundle = Bundle(obj=obj)
        
        # Dehydrate each field.
        for field_name, field_object in self.fields.items():
            # A touch leaky but it makes URI resolution work.
            if isinstance(field_object, fields.RelatedField):
                field_object.api_name = self._meta.api_name
                field_object.resource_name = self._meta.resource_name
                
            bundle.data[field_name] = field_object.dehydrate(bundle)
            
            # Check for an optional method to do further dehydration.
            method = getattr(self, "dehydrate_%s" % field_name, None)
            
            if method:
                method(bundle)
        
        bundle = self.dehydrate(bundle)
        return bundle


class LinkResource(ModelResource):
    project = fields.ToOneField(ProjectResource, 'project')
    
    class Meta:
        queryset = Link.objects.all()
        resource_name = 'links'
