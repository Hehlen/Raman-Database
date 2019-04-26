import numpy as np
import pandas as pd

import chemistry

def chemical_formula(info_file):

    print("\nReading the chemical formula...")

    number_compounds = int(info_file.loc["number of compounds"].value)
    
    chem = {}

    for j in range(number_compounds):
        chem[info_file.iloc[4+j].name] = float(info_file.iloc[4+j].value)

    compounds = list(chem)
    print("\nFound %i compounds:" % len(compounds))

    df = {}
    for i in compounds:
        print("\n"+str(i)+" "+str(chem[i]))
        d = chemistry.decompose_molecule(i)
        for j in d.keys():
            print("%s %i " % (j,d[j]*chem[i]))
            try:
                df[j] += d[j]*chem[i]
            except:
                df[j] = d[j]*chem[i]
    print("")
    print(df)
    sorteddf=sorted(df.keys(), key=lambda x:x.lower())
    out_formula = ""
    for i in sorteddf:
        out_formula += i+str(round(float(df[i])/df["O"]*100,2))+" "
    print("")
    print("Formula is:")
    print(out_formula)
    return out_formula

def authors_split(str_authors):
    authors=[]
    idx = str_authors.find(";")
    if idx == -1:
        raise ValueError("No authors found or you did not use the author proper delimiter: ;")
    count = 0
    while count <= 1:
        authors.append(str_authors[0:idx])
        str_authors = str_authors[idx+1:-1]
        idx = str_authors.find(";")
        if idx == -1:
            count += 1
    return authors

def read_spectra_file(name_spectra):

    f = open(name_spectra,"r")

    record = False
    data_recorded = []
    for i in f:
       # print(i)
        if i == '# START\n':
            record = True

        if i == "# STOP\n":
            record = False

        if record == True:
            data_recorded.append(i)
    spectra = np.genfromtxt(data_recorded)
    
    return spectra