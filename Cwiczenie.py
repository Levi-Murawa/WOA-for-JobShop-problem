import WOA_TM
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ##------------- podstawy korzystania z biblioteki
    print('\n', "Podstawy biblioteki:")
    przyklad1 = WOA_TM.jobs_data2
    liczenie_maszyn = 1 + max(task[0] for job in przyklad1 for task in job)
    rozw = WOA_TM.pod_rozw(przyklad1)
    min_czas, naj_har, naj_roz = WOA_TM.woa(przyklad1, rozw, liczenie_maszyn, 10)
    print("Najmniejszy znaleziony czas:", min_czas)
    print("Wektor rozwiazania:", naj_roz)
    print("Rysowanie Diagramu Gantta ")
    WOA_TM.harmo_plot(naj_har)

    ##------------ Badanie skuteczności w zależności od ilości testów
    print('\n', "Badanie skuteczności w zależności od ilości testów:")
    przyklad2 = WOA_TM.jobs_data4
    liczenie_maszyn = 1 + max(task[0] for job in przyklad2 for task in job)
    rozw = WOA_TM.pod_rozw(przyklad2)
    min_czas1, naj_har, naj_roz = WOA_TM.woa(przyklad2, rozw, liczenie_maszyn, 1)
    min_czas2, naj_har, naj_roz = WOA_TM.woa(przyklad2, rozw, liczenie_maszyn, 10)
    min_czas3, naj_har, naj_roz = WOA_TM.woa(przyklad2, rozw, liczenie_maszyn, 100)
    print("Czas rozwiązania dla pojedyńczego przebiegu:", min_czas1)
    print("Czas rozwiązania dla dziesięciu przebiegów:", min_czas2)
    print("Czas rozwiązania dla stu przebiegów:", min_czas3)

    ##------------ Badanie stabilności wyników dla różnych ilości przebiegów
    print('\n', "Badanie stabilności wyników dla różnych ilości przebiegów:")
    przyklad3 = WOA_TM.jobs_data4
    liczenie_maszyn = 1 + max(task[0] for job in przyklad3 for task in job)
    rozw = WOA_TM.pod_rozw(przyklad3)
    wektor_z_czasami = []
    wektor_sredni = []
    zakres_badania = range(30)
    for i in zakres_badania:
        wynik1 = WOA_TM.woa(przyklad3, rozw, liczenie_maszyn, i)
        wynik2 = WOA_TM.woa(przyklad3, rozw, liczenie_maszyn, i)
        wynik3 = WOA_TM.woa(przyklad3, rozw, liczenie_maszyn, i)
        wynik4 = WOA_TM.woa(przyklad3, rozw, liczenie_maszyn, i)
        wynik_s = (wynik1[0]+wynik2[0]+wynik3[0]+wynik4[0])/4
        wektor_z_czasami.append([wynik1[0], wynik2[0], wynik3[0], wynik4[0]])
        wektor_sredni.append(wynik_s)

    fig, ax = plt.subplots()
    ax.plot(zakres_badania, wektor_z_czasami, linewidth=2.0)
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(zakres_badania, wektor_sredni, linewidth=2.0)
    plt.show()
