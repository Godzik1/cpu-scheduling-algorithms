import random

odp_turnaround_time = odp_waiting_time = 0.0


# Generowanie losowych czasów przybycia i czasów wykonywania dla 100 procesów
data1 = [[0,2] , [1,8] , [3,4] , [5,3]]

# Listy do przechowywania czasów oczekiwania, czasów zakończenia i czasów przetwarzania
waiting_time = [0]  # Czas oczekiwania dla pierwszego procesu jest 0
finish_time = [data1[0][0] + data1[0][1]]  # Czas zakończenia dla pierwszego procesu
turnaround_time = [finish_time[0] - data1[0][0]]  # Czas przetwarzania dla pierwszego procesu

# Obliczenia dla pozostałych procesów
for i in range(1, len(data1)):
    arrival_time = data1[i][0]
    burst_time = data1[i][1]

    waiting_time.append(finish_time[i-1] - arrival_time)  # Czas oczekiwania
    finish_time.append(finish_time[i-1] + burst_time)  # Czas zakończenia
    turnaround_time.append(finish_time[i] - arrival_time)  # Czas przetwarzania

# Obliczenie średnich
average_turnaround = round(sum(turnaround_time) / len(turnaround_time), 2)
average_waiting_time = round(sum(waiting_time) / len(waiting_time), 2)


# Wyświetlenie wyników
print("Średni czas przetwarzania:", average_turnaround, "\nŚredni czas oczekiwania:", average_waiting_time , "\n")
