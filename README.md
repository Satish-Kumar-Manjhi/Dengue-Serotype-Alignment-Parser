Dengue-Serotype-Alignment-Parser


Overview

A lightweight Python script for parsing CLUSTAL multiple sequence alignment (MSA) files of Dengue virus serotypes (DENV1–4) and converting the alignment into a position-wise CSV format.

The script reconstructs aligned protein sequences and extracts conservation symbols (*, :, .) for comparative analysis.

Input

CLUSTAL formatted alignment file (.aln or .txt)

Sequence labels must include:

Dengue1

Dengue2

Dengue3

Dengue4

Output

Generates:

output.csv

Format:

| No. | Dengue_4 | Dengue_3 | Dengue_2 | Dengue_1 | similarity |

Each row corresponds to one aligned position.

Usage
python dengue_alignment_parser.py alignment_file.aln

Example:

python dengue_alignment_parser.py MSA_dengue_serotype_protein_W.txt
Requirements

Python 3.x

Standard libraries only (sys, csv)

Purpose

This tool enables:

Position-wise mutation comparison

Conserved residue identification

Serotype divergence inspection
