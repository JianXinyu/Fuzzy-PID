# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:02:39 2017

@author: jianx
"""

import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

#Generate universe variables 
#   *Error on subjective ranges [-30, 30]
#   *Change rate of Error on subjective ranges [-3, 3]
#   *Deltak_p on subjective ranges [-0.3, 0.3]
#   *Deltak_i on subjective ranges [-0,06, 0.06]
#   *Deltak_d on subjective ranges [-3, 3]

# New Antecedent/Consequent objects hold universe variables and membership functions

e = ctrl.Antecedent(np.arange(-30, 31, 1), 'error')
ec = ctrl.Antecedent(np.arange(-3, 4, 1), 'error_c')
kp = ctrl.Consequent(np.arange(-0.3, 0.4, 0.1), 'deltak_p')
ki = ctrl.Consequent(np.arange(-0.06, 0.07, 0.01), 'deltak_i')
kd = ctrl.Consequent(np.arange(-3, 4, 1), 'deltak_d')

# Auto-membership function population is possible with .automf(3, 5, or 7)
names = ['NB', 'NM', 'NS', 'ZE', 'PS', 'PM', 'PB']
e.automf(names = names)
ec.automf(names = names)
kp.automf(names = names)
ki.automf(names = names)
kd.automf(names = names)

#built custom membership functions

#e['NB'] = fuzz.trimf(e.universe, [-30, -30, -10])
#e['NM'] = fuzz.trimf(e.universe, [-30, -20, 0])
#e['NS'] = fuzz.trimf(e.universe, [-30, -10, 10])
#e['Z'] = fuzz.trimf(e.universe, [-20, 0, 20])
#e['PS'] = fuzz.trimf(e.universe, [-10, 10, 30])
#e['PM'] = fuzz.trimf(e.universe, [0, 20, 30])
#e['PB'] = fuzz.trimf(e.universe, [10, 30, 30])
#
#ec['NB'] = fuzz.trimf(ec.universe, [-3, -3, -1])
#ec['NM'] = fuzz.trimf(ec.universe, [-3, -2, 0])
#ec['NS'] = fuzz.trimf(ec.universe, [-3, -1, 1])
#ec['Z'] = fuzz.trimf(ec.universe, [-2, 0, 2])
#ec['PS'] = fuzz.trimf(ec.universe, [-1, 1, 3])
#ec['PM'] = fuzz.trimf(ec.universe, [0, 2, 3])
#ec['PB'] = fuzz.trimf(ec.universe, [1, 3, 3])
#
#kd['NB'] = fuzz.trimf(kd.universe, [-3, -3, -1])
#kd['NM'] = fuzz.trimf(kd.universe, [-3, -2, 0])
#kd['NS'] = fuzz.trimf(kd.universe, [-3, -1, 1])
#kd['Z'] = fuzz.trimf(kd.universe, [-2, 0, 2])
#kd['PS'] = fuzz.trimf(kd.universe, [-1, 1, 3])
#kd['PM'] = fuzz.trimf(kd.universe, [0, 2, 3])
#kd['PB'] = fuzz.trimf(kd.universe, [1, 3, 3])

#Visualization
#e.view() 
#ec.view()
#kp.view()
#ki.view()
#kd.view()
#Emphasize a property
#e['NB'].view()


#rule base
rule0 = ctrl.Rule(antecedent = (e['NB'] & ec['NB']),
                  consequent = (kp['PB'], ki['NB'], kd['PS']), label='rule NBNB') #unweighted mutiple outputs(to be thinking)
#                  consequent=kp['PB'], label='rule ')

rule1 = ctrl.Rule(antecedent = (e['NB'] & ec['NM']),
                  consequent = (kp['PB'], ki['NB'], kd['NS']), label='rule NBNM')

rule2 = ctrl.Rule(antecedent = (e['NB'] & ec['NS']),
                  consequent = (kp['PM'], ki['NM'], kd['NB']), label='rule NBNS')

rule3 = ctrl.Rule(antecedent = (e['NB'] & ec['ZE']),
                  consequent = (kp['PM'], ki['NM'], kd['NB']), label='rule NBZE')

rule4 = ctrl.Rule(antecedent = (e['NB'] & ec['PS']),
                  consequent = (kp['PS'], ki['NS'], kd['NB']), label='rule NBPS')

rule5 = ctrl.Rule(antecedent = (e['NB'] & ec['PM']),
                  consequent = (kp['ZE'], ki['ZE'], kd['NM']), label='rule NBPM')

rule6 = ctrl.Rule(antecedent = (e['NB'] & ec['PB']),
                  consequent = (kp['ZE'], ki['ZE'], kd['PS']), label='rule NBPB')

rule7 = ctrl.Rule(antecedent = (e['NM'] & ec['NB']),
                  consequent = (kp['PB'], ki['NB'], kd['PS']), label='rule NMNB')

rule8 = ctrl.Rule(antecedent = (e['NM'] & ec['NM']),
                  consequent = (kp['PB'], ki['NB'], kd['NS']), label='rule NMNM')

rule9 = ctrl.Rule(antecedent = (e['NM'] & ec['NS']),
                  consequent = (kp['PM'], ki['NM'], kd['NB']), label='rule NMNS')

rule10 = ctrl.Rule(antecedent = (e['NM'] & ec['ZE']),
                  consequent = (kp['PS'], ki['NS'], kd['NM']), label='rule NMZE')

rule11 = ctrl.Rule(antecedent = (e['NM'] & ec['PS']),
                  consequent = (kp['PS'], ki['NS'], kd['NM']), label='rule NMPS')

rule12 = ctrl.Rule(antecedent = (e['NM'] & ec['PM']),
                  consequent = (kp['ZE'], ki['ZE'], kd['NS']), label='rule NMPM')

rule13 = ctrl.Rule(antecedent = (e['NM'] & ec['PB']),
                  consequent = (kp['NS'], ki['ZE'], kd['ZE']), label='rule NMPB')

rule14 = ctrl.Rule(antecedent = (e['NS'] & ec['NB']),
                  consequent = (kp['PM'], ki['NB'], kd['ZE']), label='rule NSNB')

rule15 = ctrl.Rule(antecedent = (e['NS'] & ec['NM']),
                  consequent = (kp['PM'], ki['NM'], kd['NS']), label='rule NSNM')

rule16 = ctrl.Rule(antecedent = (e['NS'] & ec['NS']),
                  consequent = (kp['PM'], ki['NS'], kd['NM']), label='rule NSNS')

rule17 = ctrl.Rule(antecedent = (e['NS'] & ec['ZE']),
                  consequent = (kp['PS'], ki['NS'], kd['NM']), label='rule NSZE')

rule18 = ctrl.Rule(antecedent = (e['NS'] & ec['PS']),
                  consequent = (kp['ZE'], ki['ZE'], kd['NS']), label='rule NSPS')

rule19 = ctrl.Rule(antecedent = (e['NS'] & ec['PM']),
                  consequent = (kp['NS'], ki['PS'], kd['NS']), label='rule NSPM')

rule20 = ctrl.Rule(antecedent = (e['NS'] & ec['PB']),
                  consequent = (kp['NS'], ki['PS'], kd['ZE']), label='rule NSPB')

rule21 = ctrl.Rule(antecedent = (e['ZE'] & ec['NB']),
                  consequent = (kp['PM'], ki['NM'], kd['ZE']), label='rule ZENB')

rule22 = ctrl.Rule(antecedent = (e['ZE'] & ec['NM']),
                  consequent = (kp['PM'], ki['NM'], kd['NS']), label='rule ZENM')

rule23 = ctrl.Rule(antecedent = (e['ZE'] & ec['NS']),
                  consequent = (kp['PM'], ki['NS'], kd['NS']), label='rule ZENS')

rule24 = ctrl.Rule(antecedent = (e['ZE'] & ec['ZE']),
                  consequent = (kp['ZE'], ki['ZE'], kd['NS']), label='rule ZEZE')

rule25 = ctrl.Rule(antecedent = (e['ZE'] & ec['PS']),
                  consequent = (kp['NS'], ki['PS'], kd['NS']), label='rule ZEPS')

rule26 = ctrl.Rule(antecedent = (e['ZE'] & ec['PM']),
                  consequent = (kp['NM'], ki['PM'], kd['NS']), label='rule ZEPM')

rule27 = ctrl.Rule(antecedent = (e['ZE'] & ec['PB']),
                  consequent = (kp['NM'], ki['PM'], kd['ZE']), label='rule ZEPB')

rule28 = ctrl.Rule(antecedent = (e['PS'] & ec['NB']),
                  consequent = (kp['PS'], ki['NM'], kd['ZE']), label='rule PSNB')

rule29 = ctrl.Rule(antecedent = (e['PS'] & ec['NM']),
                  consequent = (kp['PS'], ki['NS'], kd['ZE']), label='rule PSNM')

rule30 = ctrl.Rule(antecedent = (e['PS'] & ec['NS']),
                  consequent = (kp['ZE'], ki['ZE'], kd['ZE']), label='rule PSNS')

rule31 = ctrl.Rule(antecedent = (e['PS'] & ec['ZE']),
                  consequent = (kp['NS'], ki['PS'], kd['ZE']), label='rule PSZE')

rule32 = ctrl.Rule(antecedent = (e['PS'] & ec['PS']),
                  consequent = (kp['NS'], ki['PS'], kd['ZE']), label='rule PSPS')

rule33 = ctrl.Rule(antecedent = (e['PS'] & ec['PM']),
                  consequent = (kp['NM'], ki['PM'], kd['ZE']), label='rule PSPM')

rule34 = ctrl.Rule(antecedent = (e['PS'] & ec['PB']),
                  consequent = (kp['NM'], ki['PB'], kd['ZE']), label='rule PSPB')

rule35 = ctrl.Rule(antecedent = (e['PM'] & ec['NB']),
                  consequent = (kp['PS'], ki['ZE'], kd['PS']), label='rule PMNB')

rule36 = ctrl.Rule(antecedent = (e['PM'] & ec['NM']),
                  consequent = (kp['ZE'], ki['ZE'], kd['PS']), label='rule PMNM')

rule37 = ctrl.Rule(antecedent = (e['PM'] & ec['NS']),
                  consequent = (kp['NS'], ki['PS'], kd['PS']), label='rule PMNS')

rule38 = ctrl.Rule(antecedent = (e['PM'] & ec['ZE']),
                  consequent = (kp['NM'], ki['PS'], kd['PS']), label='rule PMZE')

rule39 = ctrl.Rule(antecedent = (e['PM'] & ec['PS']),
                  consequent = (kp['NM'], ki['PM'], kd['PS']), label='rule PMPS')

rule40 = ctrl.Rule(antecedent = (e['PM'] & ec['PM']),
                  consequent = (kp['NM'], ki['PB'], kd['PS']), label='rule PMPM')

rule41 = ctrl.Rule(antecedent = (e['PM'] & ec['PB']),
                  consequent = (kp['NB'], ki['PB'], kd['PB']), label='rule PMPB')

rule42 = ctrl.Rule(antecedent = (e['PB'] & ec['NB']),
                  consequent = (kp['ZE'], ki['ZE'], kd['PB']), label='rule PBNB')

rule43 = ctrl.Rule(antecedent = (e['PB'] & ec['NM']),
                  consequent = (kp['ZE'], ki['ZE'], kd['PM']), label='rule PBNM')

rule44 = ctrl.Rule(antecedent = (e['PB'] & ec['NS']),
                  consequent = (kp['NM'], ki['PS'], kd['PM']), label='rule PBNS')

rule45 = ctrl.Rule(antecedent = (e['PB'] & ec['ZE']),
                  consequent = (kp['NM'], ki['PM'], kd['PM']), label='rule PBZE')

rule46 = ctrl.Rule(antecedent = (e['PB'] & ec['PS']),
                  consequent = (kp['NM'], ki['PM'], kd['PS']), label='rule PBPS')

rule47 = ctrl.Rule(antecedent = (e['PB'] & ec['PM']),
                  consequent = (kp['NB'], ki['PB'], kd['PS']), label='rule PBPM')

rule48 = ctrl.Rule(antecedent = (e['PB'] & ec['PB']),
                  consequent = (kp['NB'], ki['PB'], kd['PB']), label='rule PBPB')

#Create a control system
sys = ctrl.ControlSystem(rules=[rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48])
#Simulate this system
simsys = ctrl.ControlSystemSimulation(sys)

# Simulate our control system by simply specifying the inputs and calling the compute method. 
# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
simsys.input['error'] = 20
simsys.input['error_c'] = 3
# Crunch the numbers
simsys.compute()

#View the result
print(simsys.output['deltak_p'])
print(simsys.output['deltak_i'])
print(simsys.output['deltak_d'])
kp.view(sim=simsys)
ki.view(sim=simsys)
kd.view(sim=simsys)
