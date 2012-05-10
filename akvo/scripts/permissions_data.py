GROUP_LIST = [u'RSR editors', u'RSR users', u'RSR partner admins', u'RSR partner editors', u'SMS updater', u'SMS manager', u'RSR managers']
PERMS_DICT = {u'RSR editors': [{'model': u'user', 'name': u'Can change user', 'codename': u'change_user', 'app_label': u'auth'}, {'model': u'registrationprofile', 'name': u'Can add registration profile', 'codename': u'add_registrationprofile', 'app_label': u'registration'}, {'model': u'registrationprofile', 'name': u'Can change registration profile', 'codename': u'change_registrationprofile', 'app_label': u'registration'}, {'model': u'registrationprofile', 'name': u'Can delete registration profile', 'codename': u'delete_registrationprofile', 'app_label': u'registration'}, {'model': u'country', 'name': u'Can add country', 'codename': u'add_country', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can change country', 'codename': u'change_country', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can delete country', 'codename': u'delete_country', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can add link', 'codename': u'add_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can change link', 'codename': u'change_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can delete link', 'codename': u'delete_link', 'app_label': u'rsr'}, {'model': u'organisation', 'name': u'Can add organisation', 'codename': u'add_organisation', 'app_label': u'rsr'}, {'model': u'organisation', 'name': u'Can change organisation', 'codename': u'change_organisation', 'app_label': u'rsr'}, {'model': u'organisation', 'name': u'Can delete organisation', 'codename': u'delete_organisation', 'app_label': u'rsr'}, {'model': u'organisationaccount', 'name': u'Can add organisation account', 'codename': u'add_organisationaccount', 'app_label': u'rsr'}, {'model': u'organisationaccount', 'name': u'Can change organisation account', 'codename': u'change_organisationaccount', 'app_label': u'rsr'}, {'model': u'organisationaccount', 'name': u'Can delete organisation account', 'codename': u'delete_organisationaccount', 'app_label': u'rsr'}, {'model': u'project', 'name': u'Can add project', 'codename': u'add_project', 'app_label': u'rsr'}, {'model': u'project', 'name': u'Can change project', 'codename': u'change_project', 'app_label': u'rsr'}, {'model': u'project', 'name': u'Can delete project', 'codename': u'delete_project', 'app_label': u'rsr'}, {'model': u'projectcomment', 'name': u'Can add project comment', 'codename': u'add_projectcomment', 'app_label': u'rsr'}, {'model': u'projectcomment', 'name': u'Can change project comment', 'codename': u'change_projectcomment', 'app_label': u'rsr'}, {'model': u'projectcomment', 'name': u'Can delete project comment', 'codename': u'delete_projectcomment', 'app_label': u'rsr'}, {'model': u'projectupdate', 'name': u'Can add project update', 'codename': u'add_projectupdate', 'app_label': u'rsr'}, {'model': u'projectupdate', 'name': u'Can change project update', 'codename': u'change_projectupdate', 'app_label': u'rsr'}, {'model': u'projectupdate', 'name': u'Can delete project update', 'codename': u'delete_projectupdate', 'app_label': u'rsr'}, {'model': u'publishingstatus', 'name': u'Can add publishing status', 'codename': u'add_publishingstatus', 'app_label': u'rsr'}, {'model': u'publishingstatus', 'name': u'Can change publishing status', 'codename': u'change_publishingstatus', 'app_label': u'rsr'}, {'model': u'publishingstatus', 'name': u'Can delete publishing status', 'codename': u'delete_publishingstatus', 'app_label': u'rsr'}, {'model': u'userprofile', 'name': u'Can change user profile', 'codename': u'change_userprofile', 'app_label': u'rsr'}], u'SMS manager': [], u'RSR managers': [{'model': u'benchmarkname', 'name': u'Can add benchmark name', 'codename': u'add_benchmarkname', 'app_label': u'rsr'}, {'model': u'benchmarkname', 'name': u'Can change benchmark name', 'codename': u'change_benchmarkname', 'app_label': u'rsr'}, {'model': u'benchmarkname', 'name': u'Can delete benchmark name', 'codename': u'delete_benchmarkname', 'app_label': u'rsr'}, {'model': u'budgetitemlabel', 'name': u'Can add budget item label', 'codename': u'add_budgetitemlabel', 'app_label': u'rsr'}, {'model': u'budgetitemlabel', 'name': u'Can change budget item label', 'codename': u'change_budgetitemlabel', 'app_label': u'rsr'}, {'model': u'budgetitemlabel', 'name': u'Can delete budget item label', 'codename': u'delete_budgetitemlabel', 'app_label': u'rsr'}, {'model': u'category', 'name': u'Can add category', 'codename': u'add_category', 'app_label': u'rsr'}, {'model': u'category', 'name': u'Can change category', 'codename': u'change_category', 'app_label': u'rsr'}, {'model': u'category', 'name': u'Can delete category', 'codename': u'delete_category', 'app_label': u'rsr'}, {'model': u'minicms', 'name': u'Can add MiniCMS', 'codename': u'add_minicms', 'app_label': u'rsr'}, {'model': u'minicms', 'name': u'Can change MiniCMS', 'codename': u'change_minicms', 'app_label': u'rsr'}, {'model': u'minicms', 'name': u'Can delete MiniCMS', 'codename': u'delete_minicms', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can add Project partner', 'codename': u'add_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can change Project partner', 'codename': u'change_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can delete Project partner', 'codename': u'delete_partnership', 'app_label': u'rsr'}], u'SMS updater': [], u'RSR users': [{'model': u'projectcomment', 'name': u'Can add project comment', 'codename': u'add_projectcomment', 'app_label': u'rsr'}, {'model': u'projectupdate', 'name': u'Can add project update', 'codename': u'add_projectupdate', 'app_label': u'rsr'}], u'RSR partner admins': [{'model': u'benchmark', 'name': u'Can change benchmark', 'codename': u'change_benchmark', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can add Budget item', 'codename': u'add_budgetitem', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can change Budget item', 'codename': u'change_budgetitem', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can delete Budget item', 'codename': u'delete_budgetitem', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can add country', 'codename': u'add_country', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can change country', 'codename': u'change_country', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can add goal', 'codename': u'add_goal', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can change goal', 'codename': u'change_goal', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can delete goal', 'codename': u'delete_goal', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can add link', 'codename': u'add_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can change link', 'codename': u'change_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can delete link', 'codename': u'delete_link', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can add location', 'codename': u'add_location', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can change location', 'codename': u'change_location', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can delete location', 'codename': u'delete_location', 'app_label': u'rsr'}, {'model': u'organisation', 'name': u'RSR limited change organisation', 'codename': u'rsr_limited_change_organisation', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can add Project partner', 'codename': u'add_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can change Project partner', 'codename': u'change_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can delete Project partner', 'codename': u'delete_partnership', 'app_label': u'rsr'}, {'model': u'partnersite', 'name': u'RSR limited change partnersite', 'codename': u'rsr_limited_change_partnersite', 'app_label': u'rsr'}, {'model': u'project', 'name': u'Can add project', 'codename': u'add_project', 'app_label': u'rsr'}, {'model': u'project', 'name': u'RSR limited change project', 'codename': u'rsr_limited_change_project', 'app_label': u'rsr'}, {'model': u'userprofile', 'name': u'RSR limited change user profile', 'codename': u'rsr_limited_change_userprofile', 'app_label': u'rsr'}], u'RSR partner editors': [{'model': u'benchmark', 'name': u'Can change benchmark', 'codename': u'change_benchmark', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can add Budget item', 'codename': u'add_budgetitem', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can change Budget item', 'codename': u'change_budgetitem', 'app_label': u'rsr'}, {'model': u'budgetitem', 'name': u'Can delete Budget item', 'codename': u'delete_budgetitem', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can add country', 'codename': u'add_country', 'app_label': u'rsr'}, {'model': u'country', 'name': u'Can change country', 'codename': u'change_country', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can add goal', 'codename': u'add_goal', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can change goal', 'codename': u'change_goal', 'app_label': u'rsr'}, {'model': u'goal', 'name': u'Can delete goal', 'codename': u'delete_goal', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can add link', 'codename': u'add_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can change link', 'codename': u'change_link', 'app_label': u'rsr'}, {'model': u'link', 'name': u'Can delete link', 'codename': u'delete_link', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can add location', 'codename': u'add_location', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can change location', 'codename': u'change_location', 'app_label': u'rsr'}, {'model': u'location', 'name': u'Can delete location', 'codename': u'delete_location', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can add Project partner', 'codename': u'add_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can change Project partner', 'codename': u'change_partnership', 'app_label': u'rsr'}, {'model': u'partnership', 'name': u'Can delete Project partner', 'codename': u'delete_partnership', 'app_label': u'rsr'}, {'model': u'project', 'name': u'RSR limited change project', 'codename': u'rsr_limited_change_project', 'app_label': u'rsr'}]}