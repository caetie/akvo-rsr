# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module. 
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.simple import direct_to_template

from akvo.rsr.feeds import ProjectUpdates, OrganisationUpdates, AllProjectUpdates
from akvo.rsr.forms import RSR_PasswordResetForm, RSR_SetPasswordForm

from paypal.standard.ipn.views import ipn as paypal_ipn

# Enable the admin and load each admin.py file:
from django.contrib import admin
admin.autodiscover()

# Enable djangoembed in the admin
import oembed
oembed.autodiscover()

urlpatterns = patterns('',
    
    # Front page
    (r'^rsr/$', 'akvo.rsr.views.rsr.oldindex', ),

    # Data collections
    url(r'^rsr/data/overview/$', 'akvo.rsr.views.rsr.data_overview', name='akvo_at_a_glance'),
            
    # Project listing
    #url(r'^rsr/projects/$','akvo.rsr.views.rsr.projectlist', name='project_list'),
    #url(r'^rsr/projects/(?P<org_id>\d+)/$','akvo.rsr.views.rsr.filteredprojectlist',name='filtered_project_list'),

    # Project
    url(r'^rsr/project/(?P<project_id>\d+)/details/$', 'akvo.rsr.views.rsr.projectdetails', name='project_details'),
    url(r'^rsr/project/(?P<project_id>\d+)/funding/$', 'akvo.rsr.views.rsr.projectfunding', name='project_funding'),
    url(r'^rsr/project/(?P<project_id>\d+)/partners/$','akvo.rsr.views.rsr.projectpartners', name='project_partners'),
    url(r'^rsr/project/(?P<project_id>\d+)/comments/$', 'akvo.rsr.views.rsr.projectcomments', name='project_comments'),
    url(r'^rsr/project/(?P<project_id>\d+)/get-a-widget/$', 'akvo.rsr.views.rsr.getwidget', name='project_get_widget'),
    (r'^rsr/project/(?P<project_id>\d+)/comment/$', 'akvo.rsr.views.rsr.commentform', ),
    
    
    # Payment engines
    url(r'^rsr/mollie/report/$', 'akvo.rsr.views.rsr.mollie_report', name='mollie_report'),
    url(r'^rsr/invoice/(?P<invoice_id>\d+)/(?P<action>\w+)/$', 'akvo.rsr.views.rsr.void_invoice', name='void_invoice'),
    url(r'^rsr/project/(?P<project_id>\d+)/donate/(?P<engine>\w+)/$',
        'akvo.rsr.views.rsr.donate', name='complete_donation'),
    url(r'^rsr/project/(?P<project_id>\d+)/donate/$', 'akvo.rsr.views.rsr.setup_donation', name='project_donate'),
    url(r'^rsr/donate/ideal/thanks/$', 'akvo.rsr.views.rsr.mollie_thanks', name='mollie_thanks'),
    url(r'^rsr/donate/paypal/thanks/$', 'akvo.rsr.views.rsr.paypal_thanks', name='paypal_thanks'), 
    url(r'^rsr/donate/500/$', direct_to_template, {'template': 'rsr/donate_500.html'}, name='donate_500'),
    url(r'^rsr/donate/paypal/ipn/$', csrf_exempt(paypal_ipn), name='paypal_ipn'),
    
)


urlpatterns += patterns('',

    (r'^rsr/admin/', include(admin.site.urls)),

    # Home page
    url(r'^$', 'akvo.rsr.views.rsr.index', name='index'),    
    url(r'^rsr/index-preview/(?P<cms_id>\d+)/$', 'akvo.rsr.views.rsr.index', name='index_preview'),

    # Project listing
    #url(r'^rsr/projects/all/$', 'akvo.rsr.views.rsr.project_list', name='project_list' ),
    url(r'^rsr/projects/$', 'akvo.rsr.views.rsr.old_project_list', name='old_project_list' ),
    #url(r'^rsr/projects/(?P<org_id>\d+)/$', 'akvo.rsr.views.rsr.project_list', name='project_list_for_org' ),
    url(r'^rsr/projects/(?P<slug>[_\-a-zA-Z0-9]+)/$', 'akvo.rsr.views.rsr.project_list', name='project_list' ),

    # Project
    url(r'^rsr/project/(?P<project_id>\d+)/$', 'akvo.rsr.views.rsr.projectmain', name='project_main'),
    url(r'^rsr/project/(?P<project_id>\d+)/updates/$', 'akvo.rsr.views.rsr.projectupdates', name='project_updates'),
    url(r'^rsr/project/(?P<project_id>\d+)/update/(?P<update_id>\d+)/edit/$', 'akvo.rsr.views.rsr.updateform', name='project_edit_update'),
    url(r'^rsr/project/(?P<project_id>\d+)/update/$', 'akvo.rsr.views.rsr.updateform', name='project_add_update'),
    url(r'^rsr/project/(?P<project_id>\d+)/update/(?P<update_id>\d+)/$', 'akvo.rsr.views.rsr.projectupdate', name='update_main'),
    
    # Maps
    url(r'^rsr/maps/projects/all/$', direct_to_template, {'template': 'rsr/project/global_project_map.html'},
        name='global_project_map'),
    url(r'^rsr/maps/organisations/all/$', direct_to_template, {'template': 'rsr/organisation/global_organisation_map.html'},
        name='global_organisation_map'),

    # Organisation
    url(r'^rsr/organisations/$', 'akvo.rsr.views.rsr.orglist', name='rsr_org_list'),
    url(r'^rsr/organisations/(?P<org_type>[_a-zA-Z]+)/$', 'akvo.rsr.views.rsr.orglist', name='rsr_org_list_filtered'),
    url(r'^rsr/organisation/(?P<org_id>\d+)/$', 'akvo.rsr.views.rsr.orgdetail', name='organisation_main'),

    # Landing pages
    url(r'^rsr/liveearth/$', 'akvo.rsr.views.rsr.liveearth', name='live_earth_landing_page',),
    url(r'^rsr/walking-for-water/$', 'akvo.rsr.views.rsr.walking_for_water', name='wfw_landing_page',),
    url(r'^rsr/rabobank/$', 'akvo.rsr.views.rsr.rabobank', name='rabobank_landing_page',),
    
    # Account
    url(r'^rsr/signin/$', 'akvo.rsr.views.rsr.login', {'template_name': 'rsr/sign_in.html'}, name='signin'),
    url(r'^rsr/signout/$', 'akvo.rsr.views.rsr.signout', name='signout'),
    url(r'^rsr/accounts/register1/$', 'akvo.rsr.views.rsr.register1', name='register1'),
    url(r'^rsr/accounts/register2/$', 'akvo.rsr.views.rsr.register2', name='register2'),
    url(r'^rsr/accounts/activate/(?P<activation_key>\w+)/$', 'akvo.rsr.views.rsr.activate', name='registration_activate', ),
    #url(r'^rsr/accounts/update/$', 'akvo.rsr.views.rsr.update_user_profile', name='registration_update', ),
    url(r'^rsr/accounts/password/change/$', 'akvo.rsr.views.rsr.password_change', name='password_change'),
    url(r'^rsr/accounts/password/reset/$',
        auth_views.password_reset,
        {'password_reset_form': RSR_PasswordResetForm,
            'post_reset_redirect': '/rsr/accounts/password/reset/done/'},
        name='rsr_password_reset'
    ),
    url(r'^rsr/accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'set_password_form': RSR_SetPasswordForm},
        name='auth_password_reset_confirm'),
    url(r'^rsr/accounts/update/complete/$', direct_to_template, {'template': 'registration/update_complete.html'}, name='registration_update_complete' ),
    (r'^rsr/accounts/', include('registration.urls')),
    
    
    # MyAkvo
    url(r'^rsr/myakvo/mobile/$', 'akvo.rsr.views.rsr.myakvo_mobile', name='myakvo_mobile'),
    url(r'^rsr/myakvo/mobile/number/$', 'akvo.rsr.views.rsr.myakvo_mobile_number', name='myakvo_mobile_number'),
    url(r'^rsr/myakvo/mobile/cancel-reporter/(?P<reporter_id>\d+)/$', 'akvo.rsr.views.rsr.myakvo_cancel_reporter', name='myakvo_cancel_reporter'),
    url(r'^rsr/myakvo/$', 'akvo.rsr.views.rsr.update_user_profile', name='myakvo'),

    (r'^rsr/notices/', include('notification.urls')),
    
    (r'^rsr/gateway/', include('akvo.gateway.urls')),
    

    # Widgets
    url(r'^rsr/partners-widget/$', 'akvo.rsr.views.rsr.partners_widget', name='rsr_partners_widget'),
    url(r'^rsr/widget/all-organisations/$', 'akvo.rsr.views.rsr.partners_widget', name='rsr_partners_widget'),
    url(r'^rsr/widget/one-from-organisation/(?P<org_id>\d+)/$', 'akvo.rsr.views.rsr.select_project_widget', name='select_project_widget', ),
    url(r'^rsr/widget/(?P<template>[\w-]+)/project/(?P<project_id>\d+)/$','akvo.rsr.views.rsr.project_widget', name='project_widget', ),
    url(r'^rsr/widget/(?P<template>[\w-]+)/$','akvo.rsr.views.rsr.project_widget', name='project_widget_default', ),


	url(r'^rsr/widget/project-list/all/$', 'akvo.rsr.views.rsr.project_list_widget', name='project_list_widget', ),
	url(r'^rsr/widget/project-list/organisation/(?P<org_id>\d+)/$', 'akvo.rsr.views.rsr.project_list_widget', name='project_list_widget_for_org', ),
	url(r'^rsr/widget/project-map/organisation/(?P<org_id>\d+)/$', 'akvo.rsr.views.rsr.project_map_widget', name='project_map_widget_for_org', ),
	
    # django_counter
    (r'^rsr/counter/', include('django_counter.urls')),
        

    url(r'^rsr/error/access_denied/$',
        direct_to_template,
        {'template': 'rsr/error_access_denied.html'},
        name='access_denied'),
    
    #url(r'^rsr/rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}, name='akvo_feeds'),

    url(r'^rsr/rss/updates/(?P<project_id>\d+)/$', ProjectUpdates(), name="rss_project_updates"),
    url(r'^rsr/rss/org-updates/(?P<org_id>\d+)/$', OrganisationUpdates(), name="rss_org_updates"),
    url(r'^rsr/rss/all-updates/$', AllProjectUpdates(), name="rss_all_updates"),

    # Phone
    #(r'^rsr/mosms/$', 'akvo.rsr.views.rsr.sms_update', ),    
    #(r'^rsr/momms/$', 'akvo.rsr.views.rsr.mms_update', ),

    #django-piston
    (r'^rsr/api/', include('akvo.api.urls')),

    (r'^i18n/', include('django.conf.urls.i18n')),
)    
        

handler500 = 'akvo.rsr.views.rsr.server_error'
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^500/$', 'akvo.rsr.views.rsr.server_error'),
    )

#if settings.DEBUG:
urlpatterns += patterns('',
    (r'^rsr/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rsr/rosetta/', include('rosetta.urls')),
    )
