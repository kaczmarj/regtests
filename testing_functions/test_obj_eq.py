"""Checking if lists from two json files are equal"""
from __future__ import division
import os, json, pdb
import inspect

def test_obj_eq(file_out, file_ref=None, name=None, **kwargs):

    with open(file_out) as f:
        try:
            obj_out = json.load(f)
        except:
            obj_out = f.read().strip()

    with open(file_ref) as f:
        try:
            obj_ref = json.load(f)
        except:
            obj_ref = f.read().strip()

    report_filename = "report_{}.json".format(name)
    print("TEST", report_filename)
    out = {}
    try:
        assert obj_out == obj_ref
        out["regr"] = "PASSED"
    except(AssertionError):
        out["regr"] = "FAILED"

    with open(report_filename, "w") as f:
        json.dump(out, f)


if __name__ == '__main__':
    from argparse import ArgumentParser, RawTextHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-out", dest="file_out",
                        help="file with the output for testing")
    parser.add_argument("-ref", dest="file_ref",
                        help="file with the reference output")
    parser.add_argument("-name", dest="name",
                        help="name of the test provided by a user")
    args = parser.parse_args()

    test_obj_eq(**vars(args))
