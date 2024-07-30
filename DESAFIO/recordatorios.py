recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
     ['2021-12-25', "00:00", "Navidad"]
 ]


recordatorios.insert(1,['2021-01-02', '06:00', 'Emprezar el año'])
recordatorios[3][0] = "2021-07-16"
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])
recordatorios.pop(2)


# Output
print(recordatorios)