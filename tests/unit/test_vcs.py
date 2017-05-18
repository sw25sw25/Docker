from tests.lib import pyversion
from pip.vcs import VersionControl
from pip.vcs.bazaar import Bazaar
from pip.vcs.git import Git
from mock import Mock

if pyversion >= '3':
    VERBOSE_FALSE = False
else:
    VERBOSE_FALSE = 0


def test_git_get_src_requirements():
    git_url = 'http://github.com/pypa/pip-test-package'
    refs = {
        '0.1': 'a8992fc7ee17e5b9ece022417b64594423caca7c',
        '0.1.1': '7d654e66c8fa7149c165ddeffa5b56bc06619458',
        '0.1.2': 'f1c1020ebac81f9aeb5c766ff7a772f709e696ee',
        'foo': '5547fa909e83df8bd743d3978d6667497983a4b7',
        'bar': '5547fa909e83df8bd743d3978d6667497983a4b7',
        'master': '5547fa909e83df8bd743d3978d6667497983a4b7',
        'origin/master': '5547fa909e83df8bd743d3978d6667497983a4b7',
        'origin/HEAD': '5547fa909e83df8bd743d3978d6667497983a4b7',
    }
    sha = refs['foo']

    git = Git()
    git.get_url = Mock(return_value=git_url)
    git.get_revision = Mock(return_value=sha)
    git.get_refs = Mock(return_value=refs)
    dist = Mock()
    dist.egg_name = Mock(return_value='pip_test_package')
    ret = git.get_src_requirement(dist, location='.', find_tags=None)

    assert ret == ''.join([
        'git+http://github.com/pypa/pip-test-package',
        '@5547fa909e83df8bd743d3978d6667497983a4b7',
        '#egg=pip_test_package-bar'
    ])


def test_translate_egg_surname():
    vc = VersionControl()
    assert vc.translate_egg_surname("foo") == "foo"
    assert vc.translate_egg_surname("foo/bar") == "foo_bar"
    assert vc.translate_egg_surname("foo/1.2.3") == "foo_1.2.3"


def test_bazaar_simple_urls():
    """
    Test bzr url support.

    SSH and launchpad have special handling.
    """
    http_bzr_repo = Bazaar(
        url='bzr+http://bzr.myproject.org/MyProject/trunk/#egg=MyProject'
    )
    https_bzr_repo = Bazaar(
        url='bzr+https://bzr.myproject.org/MyProject/trunk/#egg=MyProject'
    )
    ssh_bzr_repo = Bazaar(
        url='bzr+ssh://bzr.myproject.org/MyProject/trunk/#egg=MyProject'
    )
    ftp_bzr_repo = Bazaar(
        url='bzr+ftp://bzr.myproject.org/MyProject/trunk/#egg=MyProject'
    )
    sftp_bzr_repo = Bazaar(
        url='bzr+sftp://bzr.myproject.org/MyProject/trunk/#egg=MyProject'
    )
    launchpad_bzr_repo = Bazaar(
        url='bzr+lp:MyLaunchpadProject#egg=MyLaunchpadProject'
    )

    assert http_bzr_repo.get_url_rev() == (
        'http://bzr.myproject.org/MyProject/trunk/', None,
    )
    assert https_bzr_repo.get_url_rev() == (
        'https://bzr.myproject.org/MyProject/trunk/', None,
    )
    assert ssh_bzr_repo.get_url_rev() == (
        'bzr+ssh://bzr.myproject.org/MyProject/trunk/', None,
    )
    assert ftp_bzr_repo.get_url_rev() == (
        'ftp://bzr.myproject.org/MyProject/trunk/', None,
    )
    assert sftp_bzr_repo.get_url_rev() == (
        'sftp://bzr.myproject.org/MyProject/trunk/', None,
    )
    assert launchpad_bzr_repo.get_url_rev() == (
        'lp:MyLaunchpadProject', None,
    )
