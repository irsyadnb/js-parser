# TUGAS BESAR TBFO
Javascript Parser in Python

Anggota :
  - Irsyad Nurwidianto Basuki (13521072)
  - Hobert Anthony Jonathan (13521079)
  - Maylani (10022169)

## Table of Contents
* [General Information](#general-information)
* [Technology Used](#technologies-used)
* [Setup](#setup)
* [Acknowledgements](#acknowledgements)

## General Information
Program ini dapat melakukan parsing file Javascript atau kode Javascript di dalam Python. Algoritma yang digunakan dalam program ini untuk melakukan parsing adalah algoritma Cocke-Younger-Kasami (CYK) yang memanfaatkan penggunaan CFG, CNF, dan Lexical Analysis.

Garis besar algoritma program ini dapat diandaikan pemrosesan depan-belakang. Depan, yaitu pembacaan suatu file dengan bahasa Javascript lalu dilakukan Lexical Analysis untuk mendapatkan token yang sesuai dengan Lex Rules. Belakang, yaitu pemrosesan grammar yang telah dibuat - Context Free Grammar (CFG)- lalu diubah menjadi CNF (Chomsky Normal Form). Di akhir, hasil token dan CNF tersebut akan diproses dengan algoritma Cocke-Younger-Kasami (CYK) untuk menentukan apakah file tersebut dapat di-compile atau tidak.

> Catatan : Program ini tidak 100% sesuai dengan grammar yang ada pada Javascript, sehingga terdapat beberapa syntax yang dapat dideteksi benar ataupun salah.


## Technology Used
Bahasa yang digunakan :
- Python (100%)

Libray yang digunakan : 
- re (Regular Expressions)
- os
- sys


## Setup
Berikut adalah langkah - langkah penggunaan program :
1. Buka terminal
2. Pastikan directory terletak pada js-parser
3. Jalankan program dengan cara "python main.py <namafile>.txt" atau "python main.py <namafile>.js"


## Acknowledgements
- Terima kasih kepada Tuhan Yang Maha Esa
- Terima kasih kepada para dosen pengampu : Ibu Dr.Eng. Ayu Purwarianti ST,MT., Bapak Ir.Rila Mandala, M.Eng.,Ph.D, dan Bapak Andreas Bara
- Terima kasih kepada Tim Asisten Kuliah IF2124
- Terima kasih kepada teman - teman yang telah membantu
