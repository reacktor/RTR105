#!/usr/bin/python
#-*- coding: utf-8 -*-

a = input("Cienījamais lietotāj, lūdzu, ievadi skaitli: ")
#3. python'ā visi input rezultāti ir ar str datu tipu
# tapēc ievadīta lieluma datu tips vēlāk ir jāparveido
a = int(a)

print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa= a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

