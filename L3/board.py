import os
import sys
import time
import math

def Solve(plugins_folder, solution):
    os.system('cls')
    mods = [os.path.join(plugins_folder, fn) for fn in os.listdir(plugins_folder) if fn.endswith('.py') or fn.endswith('.pyc')]    
    modules = []
    for mod in mods:
        path, fname = os.path.split(mod)
        modulename, _ = os.path.splitext(fname)    
        if path not in sys.path:    
            sys.path.insert(0, path)
        modules += [__import__(modulename)]            
    
    path, fname = os.path.split(solution)
    modulename, _ = os.path.splitext(fname)        
    if path not in sys.path:    
        sys.path.insert(0, path)
    solutie_corecta = __import__(modulename)

    input_files = [os.path.join('input', data_file) for data_file in os.listdir('input')]
    scores = [0] * len(mods)    
    j = 1
    for item in input_files:        
        print(f'{j:<2}. Total cuvinte in fisier: [{item}]')
        i = 0
        eu_name = solutie_corecta.name()
        t1 = time.time()
        eu_sol = solutie_corecta.solutie(item)            
        t2 = time.time()
        dif_eu = math.trunc((t2-t1) * 100) / 100
        for mod in modules:
            player_name = mod.name()
            t1 = time.time()
            player_sol = mod.solutie(item)
            t2 = time.time()
            dif_el = math.trunc((t2-t1) * 100) / 100
            eroare = 100 - player_sol / (eu_sol / 100)
            if eu_sol == player_sol:
                scores[i] += 10  
                result = 10
            elif eroare <= 1:
                scores[i] += 9  
                result = 9
            elif eroare <= 5 and eroare > 1:
                scores[i] += 7
                result = 7                
            elif eroare <= 10 and eroare > 5:
                scores[i] += 3
                result = 3
            else:
                result = 0
            print(f"{player_name:<10}: {player_sol:<7} ({dif_el:<5} s) | {eu_name:<3}: {eu_sol:<7} ({dif_eu:<5} s) --> {result}")
            i+=1      
        print('')  
        j += 1

    i = 0
    print('Rezultate finale:')
    for mod in modules:
        player_name = mod.name()
        print(f"{player_name:<10}: {scores[i]:<7}")
        i+=1    
    
Solve('plugins', 'solution\\sol.py')

