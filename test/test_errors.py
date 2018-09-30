from helper import run, config


def test_no_config():
    cp = run('')
    assert cp.returncode == 1
    assert not cp.stdout
    assert (
        cp.stderr == 'Auth configuration not supplied!\n' or
        cp.stderr == 'Labels configuration not supplied!\n'
    )


def test_no_auth_config():
    cp = run(f'--config-labels "{config("labels.empty.cfg")}"')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Auth configuration not supplied!\n'


def test_unusable_auth_config():
    cp = run(f'--config-auth "{config("empty_file.cfg")}" '
             f'--config-labels "{config("labels.empty.cfg")}"')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Auth configuration not usable!\n'


def test_no_labels_config():
    cp = run(f'--config-auth "{config("auth.fff.cfg")}"')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Labels configuration not supplied!\n'


def test_unusable_labels_config():
    cp = run(f'--config-labels "{config("empty_file.cfg")}" '
             f'--config-auth "{config("auth.fff.cfg")}"')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Labels configuration not usable!\n'


def test_invalid_repolsug():
    cp = run(f'--config-labels "{config("labels.empty.cfg")}" '
             f'--config-auth "{config("auth.fff.cfg")}" '
             'foobar')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Reposlug foobar not valid!\n'


def test_invalid_second_repolsug():
    cp = run(f'--config-labels "{config("labels.empty.cfg")}" '
             f'--config-auth "{config("auth.fff.cfg")}" '
             'xyz/abc foobar')
    assert cp.returncode == 1
    assert not cp.stdout
    assert cp.stderr == 'Reposlug foobar not valid!\n'