# config.py

from authomatic.providers import oauth2

CONFIG = {
    
#    'tw': { # Your internal provider name
#           
#        # Provider class
#        'class_': oauth1.Twitter,
#        
#        # Twitter is an AuthorizationProvider so we need to set several other properties too:
#        'consumer_key': '########################',
#        'consumer_secret': '########################',
#    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        # Facebook is an AuthorizationProvider too.
        'consumer_key': '1659602740995615',
        'consumer_secret': '75aa0d2409d9e50e9f3796aeb64a7e99',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['user_about_me', 'email', 'publish_stream'],

    },
    'google': {
         'class_': oauth2.Google, # Can be a fully qualified string path.

         # Provider type specific keyword arguments:
         'short_name': 2, # use authomatic.short_name() to generate this automatically
         'consumer_key': '683188869719-rh2ggaee3jovi6vni5k0rebj51o4u1mv.apps.googleusercontent.com',
         'consumer_secret': 'VxRSb62WkhQdse6z7BPe3mR',
         'scope': ['https://www.googleapis.com/auth/userinfo.profile',
                   'https://www.googleapis.com/auth/userinfo.email']
    },
    
#    'oi': {
#           
#        # OpenID provider dependent on the python-openid package.
#        'class_': openid.OpenID,
#    }
}

