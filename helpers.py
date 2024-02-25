from urllib.parse import urlparse
import os

def get_file_name_from_url(url):
    return os.path.basename(urlparse(url).path)

