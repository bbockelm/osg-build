"""Global constants for osg-build"""
import os
import sys

WD_RESULTS = '_build_results'
WD_PREBUILD = '_final_srpm_contents'
WD_UNPACKED = '_upstream_srpm_contents'
WD_UNPACKED_TARBALL = '_upstream_tarball_contents'
AFS_CACHE_PATH = '/p/vdt/public/html/upstream'
AFS_CACHE_PREFIX = 'file://' + AFS_CACHE_PATH
WEB_CACHE_PREFIX = 'http://vdt.cs.wisc.edu/upstream'
DEFAULT_CONFIG_FILE = os.path.expanduser("~/.osg-build.ini")
ALT_DEFAULT_CONFIG_FILE = os.path.expanduser("~/.vdt-build.ini")

KOJI_USER_CONFIG_DIR = os.path.expanduser("~/.koji")
OSG_KOJI_USER_CONFIG_DIR = os.path.expanduser("~/.osg-koji")
KOJI_CLIENT_CERT = os.path.join(KOJI_USER_CONFIG_DIR, "client.crt")

KOJI_CONF = "osg-koji-site.conf"
OLD_KOJI_CONF = "osg-koji.conf"
DATA_DIR = "/usr/share/osg-build"

KOJI_HUB = "http://koji-hub.batlab.org"

DATA_FILE_SEARCH_PATH = [sys.path[0],
                         os.path.join(sys.path[0], "data"),
                         DATA_DIR]

SVN_ROOT = "https://vdt.cs.wisc.edu/svn"


DEFAULT_BUILDOPTS_COMMON = {
    'autoclean': False,
    'cache_prefix': 'AUTO',
    'full_extract': False,
    'kojilogin': None,
    'koji_wrapper': True,
    'mock_clean': True,
    'mock_config': 'AUTO',
    'mock_config_from_koji': None,
    'no_wait': False,
    'redhat_release': '5',
    'regen_repos': False,
    'scratch': False,
    'svn': None,
    'target_arch': None,
    'working_directory': '.',
}

ALLBUILD_BUILDOPTS = DEFAULT_BUILDOPTS_COMMON.copy()
ALLBUILD_BUILDOPTS.update({
    'no_wait': True,
    'regen_repos': False,
    'scratch': False,
    'svn': True
})

ALLBUILD_ALLOWED_OPTNAMES = [
    'kojilogin', 'koji_wrapper', 'no_wait', 'scratch']

DEFAULT_BUILDOPTS_BY_REDHAT_RELEASE = {
    '5': {
        'distro_tag': 'osg.el5',
        'koji_tag': 'el5-osg',
        'koji_target': 'el5-osg',
    },
    '6': {
        'distro_tag': 'osg.el6',
        'koji_tag': 'el6-osg',
        'koji_target': 'el6-osg',
    }
}

REDHAT_RELEASES = DEFAULT_BUILDOPTS_BY_REDHAT_RELEASE.keys()

