#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici

    resultat = ""

    for i in mot:

        resultat += chr(ord(i) - 32)

    mot = resultat

    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
