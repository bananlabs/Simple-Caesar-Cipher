# Simple-Caesar-Cipher

- This is a simple cryptographic tool based on caesar cipher algorithm.
- I took out this example from the book: *Hacking Secret Ciphers with Python - Invent with Python*
- I made a bit of change to the original version, by getting input from user.
- **pyperclip** is a module created by the author of the book. 
  The *pyperclip* file need to be in the same folder of the main file.
  
  This simple caesar cipher algorithm doesn't encrypt non-letters. 
  If a try to encrypt this string _'In age of Bitcoin, countries will never have to rely on others to store their assets! 03-09-2017'_ 
  with the key 4, it will encrypt to _'MR EKI SJ FMXGSMR, GSYRXVMIW AMPP 
  RIZIV LEZI XS VIPC SR SXLIVW XS WXSVI XLIMV EWWIXW! 03-09-2017'_
  
  ### STEPS:
  - Write a sentence to be encrypted or decrypted;
  - Choose a key between 1 and 25;
  - Choose a mode: 'encrypt' or 'decrypt'
