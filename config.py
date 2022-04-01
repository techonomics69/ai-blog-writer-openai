##OPEN API STUFF
OPENAI_API_KEY = 'org-hqBnczD1Ke9zadEUFiGTSYXe'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
