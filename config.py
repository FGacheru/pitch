import os

class Config:
    
    
    
class ProdConfig(Config):    
    
    
    
class DevConfig(Config):    
    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}    
    
    