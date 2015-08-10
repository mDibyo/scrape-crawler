#!/usr/bin/env python

import scrapecrawler.utils as utils
import pytest

__author__ = "Dibyo Majumdar"
__email__ = "dibyo.majumdar@gmail.com"


@pytest.fixture(scope='function')
def dict1():
    """Example dictionary. """
    return {
        't1': 'v1',
        't2': {
            't3': 'v2',
            't4': ['v3', 'v4'],
        }
    }

@pytest.fixture(scope='function')
def dict2():
    """Example dictionary. """
    return {
        't5': 'v5',
        't2': {
            't6': 'v6',
            't4': ['v7', 'v8'],
        }
    }

def test_merge_dict(dict1, dict2):
    merged = {
        't1': 'v1',
        't2': {
            't3': 'v2',
            't4': ['v3', 'v4', 'v7', 'v8'],
            't6': 'v6'
        },
        't5': 'v5'
    }
    assert utils.merge_dicts(dict1, dict2) == merged