import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize('pkg', [
  'mongodb-org',
  'elasticsearch-oss',
  'graylog-server',
  'nginx'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
  'mongod',
  'elasticsearch',
  'graylog-server',
  'nginx'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled
