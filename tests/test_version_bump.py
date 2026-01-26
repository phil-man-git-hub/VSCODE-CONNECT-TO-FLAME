from scripts.bump_flame_versions import next_version


def test_next_version_basic():
    assert next_version('0.0.0') == '0.0.1'
    assert next_version('0.0.8') == '0.0.9'
    assert next_version('0.0.9') == '0.1.0'
    assert next_version('0.9.9') == '1.0.0'
    assert next_version('1.9.9') == '2.0.0'
    assert next_version('9.9.9') == '10.0.0'
