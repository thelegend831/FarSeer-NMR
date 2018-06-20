"""
Copyright © 2017-2018 Farseer-NMR
Simon P. Skinner and João M.C. Teixeira

@ResearchGate https://goo.gl/z8dPJU
@Twitter https://twitter.com/farseer_nmr

This file is part of Farseer-NMR.

Farseer-NMR is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Farseer-NMR is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Farseer-NMR. If not, see <http://www.gnu.org/licenses/>.
"""
# variables necessary for the functions

from functools import reduce
import os

aal3tol1 = {
    "Ala": "A",
    "Arg": "R",
    "Asn": "N",
    "Asp": "D",
    "Cys": "C",
    "Glu": "E",
    "Gln": "Q",
    "Gly": "G",
    "His": "H",
    "Ile": "I",
    "Leu": "L",
    "Lys": "K",
    "Met": "M",
    "Phe": "F",
    "Pro": "P",
    "Ser": "S",
    "Thr": "T",
    "Trp": "W",
    "Tyr": "Y",
    "Val": "V"
}

aal1tol3 = {
    "A": "Ala",
    "R": "Arg",
    "N": "Asn",
    "D": "Asp",
    "C": "Cys",
    "E": "Glu",
    "Q": "Gln",
    "G": "Gly",
    "H": "His",
    "I": "Ile",
    "L": "Leu",
    "K": "Lys",
    "M": "Met",
    "F": "Phe",
    "P": "Pro",
    "S": "Ser",
    "T": "Thr",
    "W": "Trp",
    "Y": "Tyr",
    "V": "Val"
}

# peaklists that require FASTA files to complete information on residue type
peaklist_format_requires_fasta = ['nmrdraw', 'nmrview', 'user_pkl_2']

def combine_dicts(dictionaries):
    tmp_dict = {}
    for dictionary in dictionaries:
        tmp_dict.update(dictionary)
    return tmp_dict


def exp_set_is_valid(variables):
    if not variables["experimental_dataset"]:
        return False
    else:
        if variables["conditions"]["z"] in list(
                variables["experimental_dataset"].keys()):
            if all(variables["conditions"]["y"] in list(
                    variables["experimental_dataset"][z].keys())
                   for z in variables["conditions"]["z"]):
                if all(variables["conditions"]["x"] in list(
                        variables["experimental_dataset"][z][y].keys())
                       for z in variables["conditions"]["y"]):
                    return True


def get_nested_value(dictionary, *keys):
    return reduce(lambda dct, key: dct.get(key, None)
                  if isinstance(dct, dict) else None, *keys, dictionary)


def get_default_config_path():
    core_path = os.path.dirname(__file__)
    default_path = os.path.join(core_path, 'default_config.json')
    return default_path

def read_fasta_file(fasta_path):
    """
    Reads FASTA file.

    Parameters:
        - fasta_path: path to the FASTA file.

    Returns:
        - fasta: string containing the fasta sequence.
    """
    fasta_file = open(fasta_path, 'r')
    fl = fasta_file.readlines()
    fasta = ''

    for i in fl:
        if i.startswith('>'):
            continue

        else:
            fasta += i.replace(' ', '').replace('\n', '').upper()

    if ''.join(c for c in fasta if c.isdigit()):
        msg = \
'We found digits in your FASTA string coming from file {}. Be aware of \
mistakes resulting from wrong FASTA file. You may wish to abort \
and correct the file. \
If you choose continue, Farseer-NMR will parse out the digits.'.\
            format(fasta_path)
        self.log_r(fsw.gen_wet('WARNING', msg, 22))
        fsw.continue_abort()
        fasta = ''.join(c for c in fasta if not c.isdigit())

    return fasta
