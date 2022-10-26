import yaml
atoms_num = 640                                                   #the atom number of POSCAR
with open('qpoints.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)                                      # Load the yaml file and convert it to a dictionary
    phonon = data.get('phonon')                              # get phonon dictionary
    out  =  [ ]
    fre  =  []
    for phonon2 in phonon:
        for ev in phonon2['band']:
            fre.append(ev['frequency'])
            time = 0
            out2 = []
            for atom in ev['eigenvector']:
                x = atom[0][0]  # Build  plural
                y = atom[1][0]
                z = atom[2][0]
                time += 1
                xyz = [x,y,z]
                out2.append(xyz) 
                if time == atoms_num:
                    out.append(out2)
                    out2 = []
                    time = 0
lammps=open('data1','r')
num = 0
fre_num = 1599                                                       ###the number determine the phonon frequency
print(fre[fre_num])
lammps2=open('data2','w')
atom = 0 
while True:
    line = lammps.readline()
    num += 1
    if len(line) == 0:
        break
    elif num < 11:
        lammps2.write(line)
    else:
        lammps2.write(line.split()[0]+' ')
        lammps2.write(line.split()[1]+' ')
        lammps2.write(str(float(line.split()[2]) + float(out[fre_num][atom][0])) + ' ')
        lammps2.write(str(float(line.split()[3]) + float(out[fre_num][atom][1])) + ' ')
        lammps2.write(str(float(line.split()[4]) + float(out[fre_num][atom][2])) + '\n') 
        atom += 1
lammps.close()
lammps2.close()
