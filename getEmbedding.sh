#!/bin/bash
echo $1 | ./fasttext print-word-vectors data/bible-corpus/processed/EnglishModel.bin

