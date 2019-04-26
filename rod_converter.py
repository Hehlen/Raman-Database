import pandas as pd
import numpy as np
import sys
import rod_tools as rtl

def main():
    # GET THE INPUT ARGUMENTS
    
    name = sys.argv[1]
    path_in = sys.argv[2]
    path_out = sys.argv[3]
    
    print("Treating CIF data name "+name)

    name_spectra = name+".txt"
    print("Spectra filename is "+name_spectra)

    name_out = path_out+name+".rod"
    print("ROD file will be outputed as "+name_out)

    info_file = pd.read_csv(path_in+name+".csv").set_index("index")
    
    # grabing details of the various parts
    journal_details = info_file.filter(regex=r'^_journal', axis=0)
    raman_details = info_file.filter(regex=r'^_raman_measurement_device', axis=0)
    raman_environment = info_file.filter(regex=r'_raman_measurement\.', axis=0)
    
    # read spectra
    spectra = rtl.read_spectra_file(path_in+name_spectra)
    
    spacing = 80 #characters
    
    print("Writing the ROD file (will overwrite any existing one)")
    f = open(name_out,"w")

    # 
    # Journal details
    #
    f.write("_publ_author_name\n")
    str_authors = info_file.loc["_publ_author_name"].value
    authors = rtl.authors_split(str_authors)
    for i in authors:
        f.write("'"+i+"'"+"\n")
    f.write("_publ_section_title\n")
    f.write(";\n")
    f.write(info_file.loc["_publ_section_title"].value+"\n")
    f.write(";\n")

    for i in journal_details.index:
        f.write(i+(spacing-len(i))*" "+str(journal_details.loc[i].value)+"\n")

    #
    # Chemical Formula
    #
    f.write("_chemical_compound_source"+(spacing-len("_chemical_compound_source"))*" "+str(info_file.loc["_chemical_compound_source"].value)+"\n")
    f.write("_chemical_formula_sum"+(spacing-len("_chemical_formula_sum"))*" "+rtl.chemical_formula(info_file)+"\n")
    f.write("_chemical_name_mineral"+(spacing-len("_chemical_name_mineral"))*" "+info_file.loc["_chemical_name_mineral"].value+"\n")

    #
    # Raman spectrometer details
    #

    for i in raman_details.index:
        f.write(i+(spacing-len(i))*" "+str(raman_details.loc[i].value)+"\n")

    #
    # Raman environment measurement details
    #
    for i in raman_environment.index:
        if i == "_raman_measurement.environment_details":
            f.write(";\n")
            f.write(i+(spacing-len(i))*" "+str(raman_environment.loc[i].value)+"\n")
            f.write(";\n")
        else:
            f.write(i+(spacing-len(i))*" "+str(raman_environment.loc[i].value)+"\n")

    #
    # Source file details
    #
    f.write("_rod_data_source.file"+(spacing-len("_rod_data_source.file"))*" "+name+"\n")
    # Writing spectra
    #
    f.write("loop_\n")
    f.write("_raman_spectrum.raman_shift\n")
    f.write("_raman_spectrum.intensity\n")

    for i,j in spectra:
        f.write(str(i)+" "+str(j)+"\n")

    f.close()
    print("Done, existing.")

if __name__ == '__main__':
    main()