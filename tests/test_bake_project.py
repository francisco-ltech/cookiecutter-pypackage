import pytest


@pytest.fixture
def custom_template(tmpdir):
    template = tmpdir.ensure("cookiecutter-pypackage", dir=True)
    template.join("cookiecutter.json").write('{"repo_name": "my-project-repo"}')

    repo_dir = template.ensure("{{cookiecutter.repo_name}}", dir=True)
    repo_dir.join("README.md").write("{{cookiecutter.repo_name}}")

    return template


def test_bake_custom_project(cookies, custom_template):
    """Test for 'cookiecutter-template'."""
    result = cookies.bake(template=str(custom_template))

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "my-project-repo"
    assert result.project_path.is_dir()