from urllib.parse import urlparse
import os
import json


def get_fname_from_url(url):
    return os.path.basename(urlparse(url).path)
