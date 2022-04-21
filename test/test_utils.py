# third party imports
import pytest

# local imports
from ..src import utils


trailing_punc_inputs = [
    "test",
    "test.",
    "test?",
    "test!",
]
trailing_punc_expected = [
    "test.",
    "test.",
    "test?",
    "test!",
]


@pytest.mark.parametrize(
    "test_input,expected", zip(trailing_punc_inputs, trailing_punc_expected)
)
def test_fix_trailing_punc(test_input: str, expected: str):
    assert utils.fix_trailing_punc(test_input) == expected


punc_whitespace_inputs = [
    "test.test.",
    "Test.Test.",
    "test!test!",
    "Test!Test!",
    "test?test?",
    "Test?Test?",
    "1.0",
]
punc_whitespace_expected = [
    "test. test.",
    "Test. Test.",
    "test! test!",
    "Test! Test!",
    "test? test?",
    "Test? Test?",
    "1.0",
]


@pytest.mark.parametrize(
    "test_input,expected", zip(punc_whitespace_inputs, punc_whitespace_expected)
)
def test_fix_punc_whitespace(test_input: str, expected: str):
    assert utils.fix_punc_whitespace(test_input) == expected
