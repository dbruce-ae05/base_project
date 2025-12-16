from src.base_project.app_types import Result, ResultType


def test_result():
    test_res = Result(
        result_type=ResultType.SUCCESS,
        msg="Test Message",
        result=None,
    )

    assert test_res.result_type is ResultType.SUCCESS
    assert test_res.msg == "Test Message"
    assert test_res.result is None
