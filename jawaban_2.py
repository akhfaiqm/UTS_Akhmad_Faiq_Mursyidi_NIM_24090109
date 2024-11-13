while True:
    inputtahun = str(input('Masukan Tahun')
                     )
    
    if inputtahun:
        inputtahun % 400
        print(f'Tahun : {inputtahun} termasuk tahun KABISAT ')

        if inputtahun:
            inputtahun % 4
            print(f'Tahun {inputtahun} Termasuk tahun KABISAT')