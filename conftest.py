def pytest_bdd_before_scenario(request, scenario):
    print("\nBefore Scenario")


def pytest_bdd_after_scenario(request, scenario):
    print("After Scenario")


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    print("Before Step Call")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    print("After Step Call")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print("Step Error")
