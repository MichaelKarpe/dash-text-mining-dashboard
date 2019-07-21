import bisect
import operator
from collections import defaultdict

import pandas as pd
import swifter  # NOQA


def default_to_regular(d):
    """Convert defaultdicts built recursively into dicts."""

    if isinstance(d, defaultdict):
        d = {k: default_to_regular(v) for k, v in d.items()}

    return d


def sort_lexicon(d):
    """Sort words in dicts built recursively."""

    if isinstance(d, dict):
        d = dict(sorted({k: sort_lexicon(v) for k, v in d.items()}.items(), key=operator.itemgetter(0)))

    return d


def build_lexicon():
    """Build lexicon from CSV file."""

    lexicon = defaultdict(lambda: defaultdict(list))
    df_lexicon = pd.read_csv("data/lexicon.csv")
    for _, row in df_lexicon.iterrows():
        bisect.insort(lexicon[row["intent"]][row["subintent"]], row["sentence"])

    lexicon = default_to_regular(lexicon)
    lexicon = sort_lexicon(lexicon)

    return lexicon


LEXIQUE = build_lexicon()


try:
    df = pd.read_csv("data/smalltalk_benchmark.csv")

except Exception:
    df = pd.read_csv("data/smalltalk.csv")
    df["number of words"] = df["sentence"].swifter.apply(lambda x: len(str(x).split(" ")))
    df.to_csv("data/saved_smalltalks.csv", index=False)


lexical_field_to_url_name = {field: "/" + field for field in set(df["intent"])}
url_name_to_lexical_field = {url: field for field, url in lexical_field_to_url_name.items()}
