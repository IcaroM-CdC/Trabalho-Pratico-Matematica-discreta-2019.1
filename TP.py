import itertools


def position(time):

    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]

    for contador in range(len(letras)):
        if time == letras[contador]:
            posicao = contador

            return posicao


TimeA, TimeB = map(str, input().split(","))

GolTimeA = int(input())
GolTimeB = int(input())

Times = [TimeA, TimeB]

if GolTimeA == 0 and GolTimeB == 0:
    print(0)

elif GolTimeA == 0 and GolTimeB != 0:
    for i in range(GolTimeB):
        print(TimeB, end="")

elif GolTimeA != 0 and GolTimeB == 0:
    for i in range(GolTimeA):
        print(TimeA, end="")

elif GolTimeA != 0 and GolTimeB != 0:
    Gol_AB = GolTimeB + GolTimeA

    Prob = list(itertools.product(Times, repeat=Gol_AB))

    if position(TimeA) < position(TimeB):
        for i in range(len(Prob)):
            if Prob[i].count(TimeA) == GolTimeA and Prob[i].count(TimeB) == GolTimeB:
                Resultado = "".join(map(str, Prob[i]))
                print(Resultado)

    if position(TimeA) > position(TimeB):
        for i in range(len(Prob)-1, -1, -1):
            if Prob[i].count(TimeA) == GolTimeA and Prob[i].count(TimeB) == GolTimeB:
                Resultado = "".join(map(str, Prob[i]))
                print(Resultado)
