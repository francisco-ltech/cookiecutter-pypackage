from {{ cookiecutter.module_name }}.ok import print_ok


def test_print_ok(capture_stdout):
    print_ok()
    assert capture_stdout["stdout"] == "Ok!\n"
