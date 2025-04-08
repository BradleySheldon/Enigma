"""
Enigma Cipher
(polyalphabetic substitution cipher) 
Bradley Sheldon
04/08/2025
"""

import string
from typing import List

ALPHABET = string.ascii_uppercase

class Rotor:
    def __init__(self, wiring: str, notch: str, position: int = 0):
        self.wiring = wiring
        self.inverse_wiring = ''.join(sorted(ALPHABET, key=lambda c: wiring.index(c)))
        self.position = position
        self.notch = ALPHABET.index(notch)

    def encode_forward(self, c: str) -> str:
        idx = (ALPHABET.index(c) + self.position) % 26
        return self.wiring[idx]

    def encode_backward(self, c: str) -> str:
        idx = (self.inverse_wiring.index(c) - self.position + 26) % 26
        return ALPHABET[idx]

    def step(self) -> bool:
        self.position = (self.position + 1) % 26
        return self.position == self.notch

class Reflector:
    def __init__(self, wiring: str):
        self.mapping = dict(zip(ALPHABET, wiring))

    def reflect(self, c: str) -> str:
        return self.mapping[c]

class EnigmaMachine:
    def __init__(self, rotors: List[Rotor], reflector: Reflector):
        self.rotors = rotors
        self.reflector = reflector

    def _step_rotors(self):
        rotate_next = self.rotors[0].step()
        for i in range(1, len(self.rotors)):
            if rotate_next:
                rotate_next = self.rotors[i].step()
            else:
                break

    def process_char(self, c: str) -> str:
        if c not in ALPHABET:
            return c

        self._step_rotors()

        for rotor in self.rotors:
            c = rotor.encode_forward(c)

        c = self.reflector.reflect(c)

        for rotor in reversed(self.rotors):
            c = rotor.encode_backward(c)

        return c

    def encrypt(self, message: str) -> str:
        message = message.upper().replace(" ", "")
        return ''.join(self.process_char(c) for c in message)

if __name__ == '__main__':
    rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch='Q')
    rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", notch='E')
    rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", notch='V')
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    mode = input("Would you like to encode or decode? ").strip().lower()
    message = input("Enter your message: ").strip()

    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector)
    result = enigma.encrypt(message)
    print(f"Result: {result}")

    # Decryption
    if mode == 'decode':
        rotor1.position = rotor2.position = rotor3.position = 0
        enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector)
        result = enigma.encrypt(result)
        print(f"Decoded: {result}")
