# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from tastypie import fields
from tastypie.resources import ModelResource
from rsr.models import Project, Category, Link

#.GenericRelation(Location)


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'


class ProjectResource(ModelResource):
    categories = fields.ManyToManyField(CategoryResource, 'categories')
    links = fields.ToManyField('akvo.rsr.api.resources.LinkResource', 'links')
    
    class Meta:
        queryset = Project.objects.active()
        resource_name = 'project'


class LinkResource(ModelResource):
    project = fields.ToOneField(ProjectResource, 'project')
    
    class Meta:
        queryset = Link.objects.all()
        resource_name = 'links'
