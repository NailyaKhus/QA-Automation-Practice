from my_funcs.utils import division
import pytest

@pytest.mark.parametrize("a, b, expected_result", [(10,2,5),
                                                   (20, 4, 5),
                                                   (5, 2, 2.5),
                                                   (10, -2, -5)])
def test_division_ok(a,b,expected_result):
    assert division(a,b)==expected_result

@pytest.mark.parametrize('expected_exception, divider, divis',[(ZeroDivisionError, 0, 10),
                                                        (TypeError, "2", 50)])
def test_division_with_error(expected_exception, divider, divis):
    with pytest.raises(expected_exception):
        division(divis, divider)