# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 20:27:44 2023

@author: Robb
"""
import os

#path='C:\\Users\\Robb\\Documents\\GitHub\\MetaboliteNER'
os.chdir('..')

print(os.getcwd())

import metabolistem_model
json_path = 'Models\\metabolistem.json'
model_path = 'Models\\metabolistem.h5'
mm = metabolistem_model.MetaboListem()

mm.load(json_path,model_path)
text='Glucose, glutamine and lactate are the most frequently mentioned metabolites in cancer studies. '
a=mm.process(text)

texts=['We found that 1-methyl-6,7-dihydroxy-1,2,3,4-tetrahydroisoquinoline,', 
       'Morphine and hippuric acid were higher in the disease group.']
b=mm.batchprocess(texts)