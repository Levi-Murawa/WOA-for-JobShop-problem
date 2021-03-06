import collections
import random
import numpy
import datetime
import plotly.express as px
import pandas as pd
from ortools.sat.python import cp_model
import matplotlib.pyplot as plt

'''
Wektor maszyny = od 0 do n z wartościami True lub False, oznacza maszyny które pracują i wartością czasu, oznaczającą jak długo mają pracować, dodatkowo pozycje wykonywanego zadania
Min czas = najkrótsze zadanie w obecnym tiku



1. weź zadanie z wektora Rozwiązanie
2. sprawdź czy zadanie jest skończone
	- Jeśli jest to wróć do punktu 1 i weź następne
3. Jeśli nie jest, to sprawdź w Maszyny czy można zająć się zadaniem
	- Jeśli można to:
	Zmień status maszyny na zajęty
	Dodać współrzędne do wektora Maszyny
	- Jeśli nie to wróć do punktu 1 weź następne zadanie
4. Jeśli wszystkie zdania zostały sprawdzone przejdź do upływu czasu
- Czas który upłyną to czas najkrótszego zadania
5. Odejmij Min czas od pól oznaczonych przez współrzędne zapisane w wektorze Maszyny
6. W wektorze Maszyny
	- jeśli czas nie równe 0 odejmij Min Czas
	- po operacji, jeśli czas równy 0 zmień wartość na True
7. Jeśli wszystkie zadania mają czas 0 to zakończ pętlę



Input data, Number of maxiter and Population etc 
Initialize the whales population  Xi (i = 1, 2, ..., n) 
Initialize a, A, C, l and p
Calculate the fitness of each search agent
X*= the best search agent
while (it < Maxiter)
      for each search agent
             if (p < 0.5)  
                      if (|A| < 1)
                                Update the position of the current search agent by the equation (1)
                      else if (|A| ≥ 1)
                                Select a random search agent (X_rand)
                                Update the position of the current search agent by the equation (3)
                      end 
             else if (p ≥ 0.5) 
                   Update the position of the current search by the by the equation (2) 
             end 
      end
Calculate the fitness of each search agent
Update X* if there is a better solution 
it=it+1
Update a, A, C, l and p
end while
return X*
https://en.wikiversity.org/wiki/Whale_Optimization_Algorithm
'''


def symulacja(dane_pracy_org, rozwiazanie, L_maszyny):
    dane_pracy = numpy.copy(dane_pracy_org)
    rozw = numpy.copy(rozwiazanie)
    maszyny = []
    czas = 0
    dzis = datetime.date.today()
    harmonogram = []
    for i in range(L_maszyny):
        maszyny.append([True, 0, (0,0)])

    hamuj = True
    while(hamuj):
        for zad in rozw:
            x = zad[0]
            y = zad[1]
            if(dane_pracy[x][y][1] != 0):

                ### --------------------- czy wczesniejsze zadanie sa rozwiazane
                a = y
                mozna = False
                wczesniej = True
                while(wczesniej):
                    if(a != 0):
                        a = a - 1
                        if (dane_pracy[x][a][1] == 0):
                            1 == 1
                        else:
                            wczesniej = False
                            mozna = False
                    else:
                        mozna = True
                        wczesniej = False
                ### --------------------- czy wczesniejsze zadanie sa rozwiazane


                ### --------------------- Czy maszyna jest wolna
                if(mozna):
                    ktora_maszyna = dane_pracy[x][y][0]
                    if(maszyny[ktora_maszyna][0]):
                        maszyny[ktora_maszyna][0] = False
                        maszyny[ktora_maszyna][1] = int(numpy.copy(dane_pracy[x][y][1]))
                        maszyny[ktora_maszyna][2] = (x,y)

                ### --------------------- Czy maszyna jest wolna



        ### --------------------- Czas min
        czas_min = 100
        for i in maszyny:
            if (i[0] == False):
                if (i[1] < czas_min):
                    czas_min = i[1]
        ### --------------------- Czas min


        ### --------------------- Robienie tiku
        czas = czas + czas_min
        for i in range(len(maszyny)):
            if(maszyny[i][0] == False):
                maszyny[i][1] = maszyny[i][1] - czas_min
                y = maszyny[i][2][0]
                x = maszyny[i][2][1]
                dane_pracy[y][x][1] = dane_pracy[y][x][1] - czas_min
                if(maszyny[i][1] == 0):
                    maszyny[i][0] = True
                z_s = czas - czas_min
                zmiana_s = datetime.timedelta(days=int(z_s))
                zmiana_f = datetime.timedelta(days=int(czas))
                start = dzis + zmiana_s
                finish = dzis + zmiana_f

                harmonogram.append(dict(Task="Maszyna numer " + str(dane_pracy[y][x][0]),
                                        Start=str(start),
                                        Finish=str(finish),
                                        Praca=str(y)))

        ### --------------------- Robienie tiku


        ### --------------------- Sprawdzanie wykonania zadania
        hamuj = False
        for zadanie in dane_pracy:
            for etap in zadanie:
                if(etap[1] == 0):
                    1 == 1
                else:
                    hamuj = True
        ### --------------------- Sprawdzanie wykonania zadania




    return czas, harmonogram





def pod_rozw(dane_pracy):
    #print(len(dane_pracy))
    rozw = []
    for x in range(len(dane_pracy)):
        for y in range(len(dane_pracy[x])):
            dod = [x, y]
            rozw.append(dod)

    return rozw

def whale(dane, rozw, L_maszy, powt):
    n = 0
    job_da = numpy.copy(dane)

    min_czas, har = symulacja(job_da, rozw, L_maszy)
    naj_roz = rozw
    naj_har = har
    while(powt >= n):
        n = n + 1
        job_da = numpy.copy(dane)
        random.shuffle(rozw)
        czas, har = symulacja(job_da, rozw, L_maszy)
        if(czas < min_czas):
            min_czas = czas
            naj_roz = rozw
            naj_har = har
    return (min_czas, naj_har, naj_roz)

def harmo_plot(harmo):
    df = pd.DataFrame(harmo)
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Praca")
    fig.update_yaxes(autorange="reversed")  # otherwise tasks are listed from the bottom up
    fig.show()

def otaczanie(a):
    ##1
    return a

def babelki(dane_pracy, roz_naj, l_m, naj_czas):
    ##2
    odp2 = []
    dp = numpy.copy(dane_pracy)
    dl = len(roz_naj)
    rozw = pod_rozw(dp)
    jak_dal_od_celu, ha = symulacja(dp, rozw, l_m)
    poprawka = (dl*((jak_dal_od_celu - naj_czas)/(jak_dal_od_celu + naj_czas)))
    poprawka = round(poprawka)
    if(poprawka == 0):
        poprawka = 2
    elif(poprawka == 1):
        poprawka = 2
    gdzie_zaczac = random.randrange(0, dl - poprawka)
    gdzie_skonczyc = gdzie_zaczac + poprawka
    a = roz_naj[:gdzie_zaczac]
    b = roz_naj[gdzie_zaczac:gdzie_skonczyc]
    c = roz_naj[gdzie_skonczyc:]
    #print(a, "b", b,"c", c)
    random.shuffle(b)

    if(not a):
        if (not c):
            odp = b
        else:
            odp = numpy.concatenate((b, c))
    else:
        if(not b):
            odp = numpy.concatenate((a, b))
        else:
            odp = numpy.concatenate((a,b, c))

    for i in range(dl):
        odp2.append([odp[i][0], odp[i][1]])
    return odp2

def szukanie(a, roz_naj):
    ##3
    losowa = random.random()
    odp2 = []
    dl = len(roz_naj)
    A = a*2*losowa
    zmiana = dl*(A/4)
    zmiana = round(zmiana)
    if(zmiana<2):
        zmiana = 2
    if(((dl-zmiana)-1) <= 0):
        gdzie_zaczac = 0
    else:
        gdzie_zaczac = random.randrange(0, (dl-zmiana)-1)
    a = roz_naj[gdzie_zaczac:]
    b = roz_naj[:gdzie_zaczac]
    random.shuffle(a)

    if (not b):
        odp2 = a
    else:
        odp = numpy.concatenate((b, a))
        for i in range(dl):
            odp2.append([odp[i][0], odp[i][1]])


    return odp2

def woa(l_iteracji, rozw, dane, l_maszyn):
    naj_rozw = rozw
    naj_czas, naj_ha = symulacja(dane, rozw, l_maszyn)

    for i in range(l_iteracji):
        a = 2 * ((l_iteracji - i)/l_iteracji)
        p = random.random()
        if(p>0.5):
            rozw_t = babelki(dane, naj_rozw, l_maszyn, naj_czas)
            czas, ha = symulacja(dane, rozw_t, l_maszyn)
            if(czas < naj_czas):
                naj_czas = czas
                naj_ha = ha
            #print("bableki")

        else:
            rozw_t = szukanie(a, naj_rozw)
            czas, ha = symulacja(dane, rozw_t, l_maszyn)
            if (czas < naj_czas):
                naj_czas = czas
                naj_ha = ha
            ##print("szukanie")

    return naj_czas, naj_ha


jobs_data = [  # task = (machine_id, processing_time).
        [[0, 3], [1, 2], [2, 2]],  # Job0
        [[0, 2], [2, 1], [1, 4]],  # Job1
        [[1, 4], [2, 3], [0, 5]] # Job2
    ]

jobs_data2 = [
[[3,1], [1,3], [2,6], [4,7], [6,3], [5,6]],
[[2,8], [3,5], [5,10], [6,10], [1,10], [4,4]],
[[3,5], [4,4], [6,8], [1,9], [2,1], [5,7]],
[[2,5], [1,5], [3,5], [4,3], [5,8], [6,9]],
[[3,9], [2,3], [5,5], [6,4], [1,3], [4,1]],
[[2,3], [4,3], [6,9], [1,10], [5,4], [3,1]],
]

jobs_data3 = [  # task = (machine_id, processing_time).
        [[0, 3]],  # Job0
        [[1, 3]]  # Job1
    ]

###-----------------------------------------------MAIN
zadanie = jobs_data

liczenie_maszyn = 1 + max(task[0] for job in zadanie for task in job)
wszystkie_maszyny = range(liczenie_maszyn)

rozw = pod_rozw(zadanie)


#a, b = symulacja(zadanie,rozw, liczenie_maszyn)
a, b, c = whale(zadanie, rozw, liczenie_maszyn, 10)

woa(200,rozw,zadanie, liczenie_maszyn)

#print(a)
#harmo_plot(b)
#print(rozw)
#print(szukanie(0.34, rozw))
#rozw2 = szukanie(0.34, rozw)
#rozw2 = szukanie(0.32, rozw2)



#print(whale(zadanie, rozw2, liczenie_maszyn, 1))
#czas, ha = symulacja(zadanie,rozw2, liczenie_maszyn)

#print(babelki(zadanie, rozw2, liczenie_maszyn, czas))