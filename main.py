from grammar_converter import readGrammarFile, convertGrammar, mapGrammar
from lexAnalysis import lexicalAnalysis
from cyk import cyk
import re, os, sys, argparse
from rules import lex_rule
import time

def main():
  # Argparse, mengambil argument dari CLI //
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Proses parsing script JavaScript
  print()
  print("==============JavaScript Parser============")
  print("Loading Your Code...")
  time.sleep(2)
  print()
  
  # Convert code dalam file script menjadi token 
  token = lexicalAnalysis(args.file.name,lex_rule)


  # Buat CNF berdasarkan grammar cfg yang telah dibuat
  CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("cfg.txt"))))
  print("Result : ", end ="")
  cyk(token, CNFgrammar)
  print("===========================================")

if __name__ == "__main__":
  main()