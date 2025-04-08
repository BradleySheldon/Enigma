# Enigma

polyalphabetic substitution cipher

This project is a Python-based simulation of the Enigma machine, a historic electro-mechanical cipher device used primarily during WWII. The simulation replicates key aspects of the original machine: rotors, reflector, stepping mechanism, and bidirectional encryption.

Features

    Multi-rotor encryption with cascading stepping

    Symmetric encryption and decryption

    Plug-and-play rotors and reflector logic

    Interactive prompt for user message input and cipher mode

 Components
 Rotors
Each rotor is a 26-letter permutation of the English alphabet with a defined notch position that causes the next rotor to advance. This simulation uses 3 historically inspired rotors:

    Rotor I: "EKMFLGDQVZNTOWYHXUSPAIBRCJ" (Notch: Q)

    Rotor II: "AJDKSIRUXBLHWTMCQGZNPYFVOE" (Notch: E)

    Rotor III: "BDFHJLCPRTXVZNYEIWGAKMUSQO" (Notch: V)

 Reflector

A reflector maps each letter to another in a fixed 1:1 reverse mapping. The reflector used is historically known as Reflector B:

    Reflector B: "YRUHQSLDPXNGOKMIEBFZCWVJAT"

 How It Works

    Each input character steps the first rotor.

    The signal passes forward through all rotors.

    It reflects through the reflector.

    It returns backward through the rotors.

    The final output letter is emitted.

Encryption and decryption use the same algorithm if the rotors are reset to the original positions.
 Usage

$ python enigma_cipher.py
Would you like to encode or decode? encode
Enter your message: HELLO WORLD
Result: KQFVRXNCFT

For decryption, provide the same settings and run again with decode.
