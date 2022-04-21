# standard library imports
import re

# third party imports
from summa.summarizer import summarize


def fix_trailing_punc(rev: str) -> str:
    """_summary_

    Args:
        rev (_type_): _description_

    Returns:
        _type_: _description_
    """
    # add trailing punctuation if missing
    if rev[-1] not in (".", "!", "?"):
        rev = rev + "."
    return rev


def fix_punc_whitespace(rev: str) -> str:
    """_summary_

    Args:
        rev (_type_): _description_

    Returns:
        _type_: _description_
    """
    # fix sentence endings lacking trailing whitespace
    return re.sub(
        r"\?(?=[A-Za-z])",
        "? ",
        re.sub(r"\!(?=[A-Za-z])", "! ", re.sub(r"\.(?=[A-Za-z])", ". ", rev)),
    )


def summa_wrapper(revs: str) -> list[tuple[str, float]]:
    """_summary_

    Args:
        revs (_type_): _description_

    Returns:
        _type_: _description_
    """
    rev_sums = summarize(
        revs,
        words=300,
        split=True,
        scores=True,
    )
    # sort by relevance score (descending)
    return sorted(rev_sums, key=lambda x: x[1], reverse=True)
