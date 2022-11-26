class Memory:

    def __init__(self, name, hz, volume):
        self.name = name
        self.hz = str(hz)
        self.volume = str(volume)
        print(name, hz, volume)

print('До сортировки:')
mass =[
Memory("A-Data", 3600, 8),
Memory("CRUCIAL", 4000, 32),
Memory("AMD", 2666, 4),
Memory("KINGSTON", 3200, 16),
Memory("G.Skill", 3800, 16),
Memory("Patriot", 2666, 8),
Memory("HyperX", 3600, 32)
    ]
f = open("ZADAN1.txt", "w")
f.write('Before sort:')
f.write('\n')
for obj in mass:
    f.write(obj.name)
    f.write(' ')
    f.write(obj.hz)
    f.write('Hz')
    f.write(' ')
    f.write(obj.volume)
    f.write('Gb')
    f.write(' ')
    f.write('\n')

f.write('\n')
print('\n')
print('После сортировки по частоте и объему памяти:')
mass.sort(key=lambda x: (x.hz, x.volume))
f.write('After sort:')
f.write('\n')
for obj in mass:
    print(obj.name, obj.hz, "Hz", obj.volume, "Gb", sep=' ')
    f.write(obj.name)
    f.write(' ')
    f.write(obj.hz)
    f.write('Hz')
    f.write(' ')
    f.write(obj.volume)
    f.write('Gb')
    f.write(' ')
    f.write('\n')

f.close()








