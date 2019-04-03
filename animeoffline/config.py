from animeoffline import *

# mal: MyAnimeLIst

jikan_rest_url = "localhost"
jikan_rest_port = 8000
jikan_rest_version = "v3"
jikan_url = f"http://{jikan_rest_url}:{jikan_rest_port}/{jikan_rest_version}/"

def list_config():
    pprint.pprint({k:v for k, v in globals().items()
                    if not k.startswith("__") and
                    type(v) != type(sys) and
                    type(v) != type(list_config)})
