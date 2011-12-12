#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management import setup_environ
import settings
setup_environ(settings)

from django.contrib.sites.models import Site


def remove_old_sites():
    sites = Site.objects.all()
    for site in sites:
        site.delete()
        print 'Removed site %s.' % site.domain


def create_new_sites():
    sites = ((1, 'www'), (2, 'test'), (3, 'test2'),
             (4, 'gabriel'), (5, 'daniel'), (6, 'paul'),
             (7, 'demo'), (8, 'uat'))
    for id, hostname in sites:
        domain = '%s.akvo.org' % hostname
        site = Site(id=id, domain=domain, name=domain)
        site.save()
        print 'Created site object for %s.' % domain


if __name__ == '__main__':
    remove_old_sites()
    create_new_sites()
    print 'Success!'