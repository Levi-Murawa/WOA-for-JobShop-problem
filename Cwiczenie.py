import WOA_TM

if __name__ == '__main__':
    ##------------- podstawy korzystania z biblioteki
    print('\n', "Podstawy biblioteki:")
    przyklad1 = WOA_TM.jobs_data2
    liczenie_maszyn = 1 + max(task[0] for job in przyklad1 for task in job)
    rozw = WOA_TM.pod_rozw(przyklad1)
    min_czas, naj_har, naj_roz = WOA_TM.whale(przyklad1, rozw, liczenie_maszyn, 10)
    print("Najmniejszy znaleziony czas:", min_czas)
    print("Wektor rozwiazania:", naj_roz)
    print("Rysowanie Diagramu Gantta ")
    WOA_TM.harmo_plot(naj_har)

    ##------------ Badanie skuteczności
    print('\n', "Badanie skuteczności:")
    przyklad2 = WOA_TM.jobs_data4
    liczenie_maszyn = 1 + max(task[0] for job in przyklad2 for task in job)
    rozw = WOA_TM.pod_rozw(przyklad2)
    min_czas1, naj_har, naj_roz = WOA_TM.whale(przyklad2, rozw, liczenie_maszyn, 1)
    min_czas2, naj_har, naj_roz = WOA_TM.whale(przyklad2, rozw, liczenie_maszyn, 10)
    min_czas3, naj_har, naj_roz = WOA_TM.whale(przyklad2, rozw, liczenie_maszyn, 100)
    print("Czas rozwiązania dla pojedyńczego przebiegu:", min_czas1)
    print("Czas rozwiązania dla dziesięciu przebiegów:", min_czas2)
    print("Czas rozwiązania dla stu przebiegów:", min_czas3)