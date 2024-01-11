from piece import Piece
from random import Random

def main():

    repertoire = [
        Piece('Chopin', 'Waltz in A minor', 'first chopin piece'),
        Piece('Chopin', 'Prelude in B', 'Left hand melody'),
        Piece('Brahms', 'Waltz in G# minor', 'Sounds better on the electronic piano'),
        Piece('Gallant', 'Sarabande', 'modern and serene')
    ]
    random = Random()
    choice = random.randint(0, len(repertoire) - 1)
    print(repertoire[choice].get_info())


if __name__ == "__main__":
    main()

