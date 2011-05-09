# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from django import template
from django.conf import settings

from akvo.rsr.models import Project, Organisation


register = template.Library()


PROJECT_MARKER_ICON = getattr(settings,
    'GOOGLE_MAPS_PROJECT_MARKER_ICON', '')
ORGANISATION_MARKER_ICON = getattr(settings,
    'GOOGLE_MAPS_ORGANISATION_MARKER_ICON', '')


@register.inclusion_tag('inclusion_tags/google_map.html')
def google_map(object, zoom, marker_icon=''):
    is_project = isinstance(object, Project)
    is_organisation = isinstance(object, Organisation)
    if is_project:
        marker_icon = PROJECT_MARKER_ICON
    elif is_organisation:
        marker_icon = ORGANISATION_MARKER_ICON
    media_url = settings.MEDIA_URL
    template_context = dict(media_url=media_url, object=object,
                            zoom=zoom, marker_icon=marker_icon)
    return template_context


@register.inclusion_tag('inclusion_tags/google_global_project_map.html')
def google_global_project_map(map_type, zoom):
    projects = Project.objects.published()
    marker_icon = PROJECT_MARKER_ICON
    template_context = dict(map_type=map_type,
        marker_icon=marker_icon,
        projects=projects,
        zoom=zoom)
    return template_context


@register.inclusion_tag('inclusion_tags/google_global_organisation_map.html')
def google_global_organisation_map(map_type, zoom):
    organisations = Organisation.objects.all()
    marker_icon = ORGANISATION_MARKER_ICON
    template_context = dict(map_type=map_type,
        marker_icon=marker_icon,
        organisations=organisations,
        zoom=zoom)
    return template_context


@register.inclusion_tag('inclusion_tags/google_global_project_map.html')
def google_organisation_projects_map(org, map_type, zoom):
    projects = org.active_projects()
    marker_icon = PROJECT_MARKER_ICON
    template_context = dict(map_type=map_type,
                            marker_icon=marker_icon,
                            projects=projects,
                            zoom=zoom)
    return template_context
