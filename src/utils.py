#!/usr/bin/env python

from collections import MutableMapping, MutableSequence, MutableSet


__author__ = "Dibyo Majumdar"
__email__ = "dibyo.majumdar@gmail.com"


def _deepcopy_dict(d):
    copy = {}
    for k, v in d.iteritems():
        if isinstance(v, MutableMapping):
            copy[k] = _deepcopy_dict(v)
        elif isinstance(v, MutableSequence):
            copy[k] = _deepcopy_list(v)
        elif isinstance(v, MutableSet):
            copy[k] = _deepcopy_set(v)
        else:
            copy[k] = v
    return copy


def _deepcopy_list(l):
    copy = []
    for e in l:
        if isinstance(e, MutableMapping):
            copy.append(_deepcopy_dict(e))
        elif isinstance(e, MutableSequence):
            copy.append(_deepcopy_list(e))
        elif isinstance(e, MutableSet):
            copy.append()
        else:
            copy.append(e)
    return copy


def _deepcopy_set(s):
    copy = set()
    for e in s:
        copy.add(e)
    return copy


def merge_dicts(d1, d2):
    merged = _deepcopy_dict(d1)
    for k, v in d2.iteritems():
        if k in merged:
            if isinstance(v, MutableMapping):
                old_v = merged[k]
                if not isinstance(old_v, MutableMapping):
                    raise TypeError('attribute {} of {} and {} do not have the same type',
                                    k, d1, d2)
                merged[k] = merge_dicts(old_v, v)
                continue
            if isinstance(v, MutableSequence):
                if not isinstance(merged[k], MutableSequence):
                    raise TypeError('attribute {} of {} and {} do not have the same type',
                                    k, d1, d2)
                merged[k].extend(v)
                continue
        merged[k] = v
    return merged