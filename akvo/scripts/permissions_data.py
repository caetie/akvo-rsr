GROUP_LIST = [u'RSR editors',
              u'RSR users',
              u'RSR partner admins',
              u'RSR partner editors',
              u'SMS updater',
              u'SMS manager',
              u'RSR managers']
PERMS_DICT = {u'RSR editors': [{'app_label': u'auth',
                                'codename': u'change_user',
                                'model': u'user',
                                'name': u'Can change user'},
        {'app_label': u'registration',
         'codename': u'add_registrationprofile',
         'model': u'registrationprofile',
         'name': u'Can add registration profile'},
        {'app_label': u'registration',
         'codename': u'change_registrationprofile',
         'model': u'registrationprofile',
         'name': u'Can change registration profile'},
        {'app_label': u'registration',
         'codename': u'delete_registrationprofile',
         'model': u'registrationprofile',
         'name': u'Can delete registration profile'},
        {'app_label': u'rsr',
         'codename': u'add_benchmark',
         'model': u'benchmark',
         'name': u'Can add benchmark'},
        {'app_label': u'rsr',
         'codename': u'change_benchmark',
         'model': u'benchmark',
         'name': u'Can change benchmark'},
        {'app_label': u'rsr',
         'codename': u'delete_benchmark',
         'model': u'benchmark',
         'name': u'Can delete benchmark'},
        {'app_label': u'rsr',
         'codename': u'add_budgetitem',
         'model': u'budgetitem',
         'name': u'Can add Budget item'},
        {'app_label': u'rsr',
         'codename': u'change_budgetitem',
         'model': u'budgetitem',
         'name': u'Can change Budget item'},
        {'app_label': u'rsr',
         'codename': u'delete_budgetitem',
         'model': u'budgetitem',
         'name': u'Can delete Budget item'},
        {'app_label': u'rsr',
         'codename': u'add_country',
         'model': u'country',
         'name': u'Can add country'},
        {'app_label': u'rsr',
         'codename': u'change_country',
         'model': u'country',
         'name': u'Can change country'},
        {'app_label': u'rsr',
         'codename': u'delete_country',
         'model': u'country',
         'name': u'Can delete country'},
        {'app_label': u'rsr',
         'codename': u'add_link',
         'model': u'link',
         'name': u'Can add link'},
        {'app_label': u'rsr',
         'codename': u'change_link',
         'model': u'link',
         'name': u'Can change link'},
        {'app_label': u'rsr',
         'codename': u'delete_link',
         'model': u'link',
         'name': u'Can delete link'},
        {'app_label': u'rsr',
         'codename': u'add_location',
         'model': u'location',
         'name': u'Can add location'},
        {'app_label': u'rsr',
         'codename': u'change_location',
         'model': u'location',
         'name': u'Can change location'},
        {'app_label': u'rsr',
         'codename': u'delete_location',
         'model': u'location',
         'name': u'Can delete location'},
        {'app_label': u'rsr',
         'codename': u'add_organisation',
         'model': u'organisation',
         'name': u'Can add organisation'},
        {'app_label': u'rsr',
         'codename': u'change_organisation',
         'model': u'organisation',
         'name': u'Can change organisation'},
        {'app_label': u'rsr',
         'codename': u'delete_organisation',
         'model': u'organisation',
         'name': u'Can delete organisation'},
        {'app_label': u'rsr',
         'codename': u'add_organisationaccount',
         'model': u'organisationaccount',
         'name': u'Can add organisation account'},
        {'app_label': u'rsr',
         'codename': u'change_organisationaccount',
         'model': u'organisationaccount',
         'name': u'Can change organisation account'},
        {'app_label': u'rsr',
         'codename': u'delete_organisationaccount',
         'model': u'organisationaccount',
         'name': u'Can delete organisation account'},
        {'app_label': u'rsr',
         'codename': u'add_project',
         'model': u'project',
         'name': u'Can add project'},
        {'app_label': u'rsr',
         'codename': u'change_project',
         'model': u'project',
         'name': u'Can change project'},
        {'app_label': u'rsr',
         'codename': u'delete_project',
         'model': u'project',
         'name': u'Can delete project'},
        {'app_label': u'rsr',
         'codename': u'add_projectcomment',
         'model': u'projectcomment',
         'name': u'Can add project comment'},
        {'app_label': u'rsr',
         'codename': u'change_projectcomment',
         'model': u'projectcomment',
         'name': u'Can change project comment'},
        {'app_label': u'rsr',
         'codename': u'delete_projectcomment',
         'model': u'projectcomment',
         'name': u'Can delete project comment'},
        {'app_label': u'rsr',
         'codename': u'add_projectupdate',
         'model': u'projectupdate',
         'name': u'Can add project update'},
        {'app_label': u'rsr',
         'codename': u'change_projectupdate',
         'model': u'projectupdate',
         'name': u'Can change project update'},
        {'app_label': u'rsr',
         'codename': u'delete_projectupdate',
         'model': u'projectupdate',
         'name': u'Can delete project update'},
        {'app_label': u'rsr',
         'codename': u'add_publishingstatus',
         'model': u'publishingstatus',
         'name': u'Can add publishing status'},
        {'app_label': u'rsr',
         'codename': u'change_publishingstatus',
         'model': u'publishingstatus',
         'name': u'Can change publishing status'},
        {'app_label': u'rsr',
         'codename': u'delete_publishingstatus',
         'model': u'publishingstatus',
         'name': u'Can delete publishing status'},
        {'app_label': u'rsr',
         'codename': u'change_userprofile',
         'model': u'userprofile',
         'name': u'Can change user profile'}],
              u'RSR managers': [{'app_label': u'rsr',
                                 'codename': u'add_benchmarkname',
                                 'model': u'benchmarkname',
                                 'name': u'Can add benchmark name'},
                      {'app_label': u'rsr',
                       'codename': u'change_benchmarkname',
                       'model': u'benchmarkname',
                       'name': u'Can change benchmark name'},
                      {'app_label': u'rsr',
                       'codename': u'delete_benchmarkname',
                       'model': u'benchmarkname',
                       'name': u'Can delete benchmark name'},
                      {'app_label': u'rsr',
                       'codename': u'add_budgetitemlabel',
                       'model': u'budgetitemlabel',
                       'name': u'Can add budget item label'},
                      {'app_label': u'rsr',
                       'codename': u'change_budgetitemlabel',
                       'model': u'budgetitemlabel',
                       'name': u'Can change budget item label'},
                      {'app_label': u'rsr',
                       'codename': u'delete_budgetitemlabel',
                       'model': u'budgetitemlabel',
                       'name': u'Can delete budget item label'},
                      {'app_label': u'rsr',
                       'codename': u'add_category',
                       'model': u'category',
                       'name': u'Can add category'},
                      {'app_label': u'rsr',
                       'codename': u'change_category',
                       'model': u'category',
                       'name': u'Can change category'},
                      {'app_label': u'rsr',
                       'codename': u'delete_category',
                       'model': u'category',
                       'name': u'Can delete category'},
                      {'app_label': u'rsr',
                       'codename': u'add_minicms',
                       'model': u'minicms',
                       'name': u'Can add MiniCMS'},
                      {'app_label': u'rsr',
                       'codename': u'change_minicms',
                       'model': u'minicms',
                       'name': u'Can change MiniCMS'},
                      {'app_label': u'rsr',
                       'codename': u'delete_minicms',
                       'model': u'minicms',
                       'name': u'Can delete MiniCMS'},
                      {'app_label': u'rsr',
                       'codename': u'add_partnership',
                       'model': u'partnership',
                       'name': u'Can add Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'change_partnership',
                       'model': u'partnership',
                       'name': u'Can change Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'delete_partnership',
                       'model': u'partnership',
                       'name': u'Can delete Project partner'},
                      {'app_label': u'auth',
                       'codename': u'change_user',
                       'model': u'user',
                       'name': u'Can change user'},
                      {'app_label': u'registration',
                       'codename': u'add_registrationprofile',
                       'model': u'registrationprofile',
                       'name': u'Can add registration profile'},
                      {'app_label': u'registration',
                       'codename': u'change_registrationprofile',
                       'model': u'registrationprofile',
                       'name': u'Can change registration profile'},
                      {'app_label': u'registration',
                       'codename': u'delete_registrationprofile',
                       'model': u'registrationprofile',
                       'name': u'Can delete registration profile'},
                      {'app_label': u'rsr',
                       'codename': u'add_benchmark',
                       'model': u'benchmark',
                       'name': u'Can add benchmark'},
                      {'app_label': u'rsr',
                       'codename': u'change_benchmark',
                       'model': u'benchmark',
                       'name': u'Can change benchmark'},
                      {'app_label': u'rsr',
                       'codename': u'delete_benchmark',
                       'model': u'benchmark',
                       'name': u'Can delete benchmark'},
                      {'app_label': u'rsr',
                       'codename': u'add_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can add Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'change_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can change Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'delete_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can delete Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'add_country',
                       'model': u'country',
                       'name': u'Can add country'},
                      {'app_label': u'rsr',
                       'codename': u'change_country',
                       'model': u'country',
                       'name': u'Can change country'},
                      {'app_label': u'rsr',
                       'codename': u'delete_country',
                       'model': u'country',
                       'name': u'Can delete country'},
                      {'app_label': u'rsr',
                       'codename': u'add_link',
                       'model': u'link',
                       'name': u'Can add link'},
                      {'app_label': u'rsr',
                       'codename': u'change_link',
                       'model': u'link',
                       'name': u'Can change link'},
                      {'app_label': u'rsr',
                       'codename': u'delete_link',
                       'model': u'link',
                       'name': u'Can delete link'},
                      {'app_label': u'rsr',
                       'codename': u'add_location',
                       'model': u'location',
                       'name': u'Can add location'},
                      {'app_label': u'rsr',
                       'codename': u'change_location',
                       'model': u'location',
                       'name': u'Can change location'},
                      {'app_label': u'rsr',
                       'codename': u'delete_location',
                       'model': u'location',
                       'name': u'Can delete location'},
                      {'app_label': u'rsr',
                       'codename': u'add_organisation',
                       'model': u'organisation',
                       'name': u'Can add organisation'},
                      {'app_label': u'rsr',
                       'codename': u'change_organisation',
                       'model': u'organisation',
                       'name': u'Can change organisation'},
                      {'app_label': u'rsr',
                       'codename': u'delete_organisation',
                       'model': u'organisation',
                       'name': u'Can delete organisation'},
                      {'app_label': u'rsr',
                       'codename': u'add_organisationaccount',
                       'model': u'organisationaccount',
                       'name': u'Can add organisation account'},
                      {'app_label': u'rsr',
                       'codename': u'change_organisationaccount',
                       'model': u'organisationaccount',
                       'name': u'Can change organisation account'},
                      {'app_label': u'rsr',
                       'codename': u'delete_organisationaccount',
                       'model': u'organisationaccount',
                       'name': u'Can delete organisation account'},
                      {'app_label': u'rsr',
                       'codename': u'add_project',
                       'model': u'project',
                       'name': u'Can add project'},
                      {'app_label': u'rsr',
                       'codename': u'change_project',
                       'model': u'project',
                       'name': u'Can change project'},
                      {'app_label': u'rsr',
                       'codename': u'delete_project',
                       'model': u'project',
                       'name': u'Can delete project'},
                      {'app_label': u'rsr',
                       'codename': u'add_projectcomment',
                       'model': u'projectcomment',
                       'name': u'Can add project comment'},
                      {'app_label': u'rsr',
                       'codename': u'change_projectcomment',
                       'model': u'projectcomment',
                       'name': u'Can change project comment'},
                      {'app_label': u'rsr',
                       'codename': u'delete_projectcomment',
                       'model': u'projectcomment',
                       'name': u'Can delete project comment'},
                      {'app_label': u'rsr',
                       'codename': u'add_projectupdate',
                       'model': u'projectupdate',
                       'name': u'Can add project update'},
                      {'app_label': u'rsr',
                       'codename': u'change_projectupdate',
                       'model': u'projectupdate',
                       'name': u'Can change project update'},
                      {'app_label': u'rsr',
                       'codename': u'delete_projectupdate',
                       'model': u'projectupdate',
                       'name': u'Can delete project update'},
                      {'app_label': u'rsr',
                       'codename': u'add_publishingstatus',
                       'model': u'publishingstatus',
                       'name': u'Can add publishing status'},
                      {'app_label': u'rsr',
                       'codename': u'change_publishingstatus',
                       'model': u'publishingstatus',
                       'name': u'Can change publishing status'},
                      {'app_label': u'rsr',
                       'codename': u'delete_publishingstatus',
                       'model': u'publishingstatus',
                       'name': u'Can delete publishing status'},
                      {'app_label': u'rsr',
                       'codename': u'change_userprofile',
                       'model': u'userprofile',
                       'name': u'Can change user profile'}],
              u'RSR partner admins': [{'app_label': u'rsr',
                                       'codename': u'change_benchmark',
                                       'model': u'benchmark',
                                       'name': u'Can change benchmark'},
                      {'app_label': u'rsr',
                       'codename': u'add_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can add Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'change_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can change Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'delete_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can delete Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'add_country',
                       'model': u'country',
                       'name': u'Can add country'},
                      {'app_label': u'rsr',
                       'codename': u'change_country',
                       'model': u'country',
                       'name': u'Can change country'},
                      {'app_label': u'rsr',
                       'codename': u'add_goal',
                       'model': u'goal',
                       'name': u'Can add goal'},
                      {'app_label': u'rsr',
                       'codename': u'change_goal',
                       'model': u'goal',
                       'name': u'Can change goal'},
                      {'app_label': u'rsr',
                       'codename': u'delete_goal',
                       'model': u'goal',
                       'name': u'Can delete goal'},
                      {'app_label': u'rsr',
                       'codename': u'add_link',
                       'model': u'link',
                       'name': u'Can add link'},
                      {'app_label': u'rsr',
                       'codename': u'change_link',
                       'model': u'link',
                       'name': u'Can change link'},
                      {'app_label': u'rsr',
                       'codename': u'delete_link',
                       'model': u'link',
                       'name': u'Can delete link'},
                      {'app_label': u'rsr',
                       'codename': u'add_location',
                       'model': u'location',
                       'name': u'Can add location'},
                      {'app_label': u'rsr',
                       'codename': u'change_location',
                       'model': u'location',
                       'name': u'Can change location'},
                      {'app_label': u'rsr',
                       'codename': u'delete_location',
                       'model': u'location',
                       'name': u'Can delete location'},
                      {'app_label': u'rsr',
                       'codename': u'rsr_limited_change_organisation',
                       'model': u'organisation',
                       'name': u'RSR limited change organisation'},
                      {'app_label': u'rsr',
                       'codename': u'add_partnership',
                       'model': u'partnership',
                       'name': u'Can add Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'change_partnership',
                       'model': u'partnership',
                       'name': u'Can change Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'delete_partnership',
                       'model': u'partnership',
                       'name': u'Can delete Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'rsr_limited_change_partnersite',
                       'model': u'partnersite',
                       'name': u'RSR limited change partnersite'},
                      {'app_label': u'rsr',
                       'codename': u'add_project',
                       'model': u'project',
                       'name': u'Can add project'},
                      {'app_label': u'rsr',
                       'codename': u'rsr_limited_change_project',
                       'model': u'project',
                       'name': u'RSR limited change project'},
                      {'app_label': u'rsr',
                       'codename': u'rsr_limited_change_userprofile',
                       'model': u'userprofile',
                       'name': u'RSR limited change user profile'}],
              u'RSR partner editors': [{'app_label': u'rsr',
                                        'codename': u'change_benchmark',
                                        'model': u'benchmark',
                                        'name': u'Can change benchmark'},
                      {'app_label': u'rsr',
                       'codename': u'add_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can add Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'change_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can change Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'delete_budgetitem',
                       'model': u'budgetitem',
                       'name': u'Can delete Budget item'},
                      {'app_label': u'rsr',
                       'codename': u'add_country',
                       'model': u'country',
                       'name': u'Can add country'},
                      {'app_label': u'rsr',
                       'codename': u'change_country',
                       'model': u'country',
                       'name': u'Can change country'},
                      {'app_label': u'rsr',
                       'codename': u'add_goal',
                       'model': u'goal',
                       'name': u'Can add goal'},
                      {'app_label': u'rsr',
                       'codename': u'change_goal',
                       'model': u'goal',
                       'name': u'Can change goal'},
                      {'app_label': u'rsr',
                       'codename': u'delete_goal',
                       'model': u'goal',
                       'name': u'Can delete goal'},
                      {'app_label': u'rsr',
                       'codename': u'add_link',
                       'model': u'link',
                       'name': u'Can add link'},
                      {'app_label': u'rsr',
                       'codename': u'change_link',
                       'model': u'link',
                       'name': u'Can change link'},
                      {'app_label': u'rsr',
                       'codename': u'delete_link',
                       'model': u'link',
                       'name': u'Can delete link'},
                      {'app_label': u'rsr',
                       'codename': u'add_location',
                       'model': u'location',
                       'name': u'Can add location'},
                      {'app_label': u'rsr',
                       'codename': u'change_location',
                       'model': u'location',
                       'name': u'Can change location'},
                      {'app_label': u'rsr',
                       'codename': u'delete_location',
                       'model': u'location',
                       'name': u'Can delete location'},
                      {'app_label': u'rsr',
                       'codename': u'add_partnership',
                       'model': u'partnership',
                       'name': u'Can add Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'change_partnership',
                       'model': u'partnership',
                       'name': u'Can change Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'delete_partnership',
                       'model': u'partnership',
                       'name': u'Can delete Project partner'},
                      {'app_label': u'rsr',
                       'codename': u'rsr_limited_change_project',
                       'model': u'project',
                       'name': u'RSR limited change project'}],
              u'RSR users': [{'app_label': u'rsr',
                              'codename': u'add_projectcomment',
                              'model': u'projectcomment',
                              'name': u'Can add project comment'},
                      {'app_label': u'rsr',
                       'codename': u'add_projectupdate',
                       'model': u'projectupdate',
                       'name': u'Can add project update'}],
              u'SMS manager': [],
              u'SMS updater': []}