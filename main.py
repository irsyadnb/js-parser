from grammar_converter import readGrammarFile, convertGrammar, mapGrammar
from lexAnalysis import lexicalAnalysis
from cyk import cykParse
import re, os, sys, argparse
from rules import lex_rule


def main():
  # Argparse, mengambil argument dari CLI
  parser = argparse.ArgumentParser()
  parser.add_argument('file', type = argparse.FileType('r'))
  args = parser.parse_args()

  # Proses parsing script JavaScript
  print()
  print("==========================JavaScript Parser==========================")
  print("Loading...")
  print("Checking your codes...")
  print("File name: " + str(args.file.name))
  print()
  
  # Convert code dalam file script menjadi token 
  token = lexicalAnalysis(args.file.name,lex_rule)
  print("Readed Token :")
  print(token)
  print()

  # Buat CNF berdasarkan grammar cfg yang telah dibuat
  CNFgrammar = mapGrammar(convertGrammar((readGrammarFile("cfg.txt"))))
  print("Result : ", end ="")
  cykParse(token, CNFgrammar)
  print("=====================================================================")

if __name__ == "__main__":
  main()