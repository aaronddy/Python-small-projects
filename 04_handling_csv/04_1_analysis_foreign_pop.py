import os, re
import usecsv

os.chdir('C:\Learning\Python\eleven_projects_python\data_sources')

total = usecsv.opencsv('popSeoul.csv')

new_pop = usecsv.switch(total)
print("new_pop",new_pop)

'''
for i in new_pop:
  for j in i:
    try:
      i[i.index(j)] = float(re.sub(',', '', j))

    except:
      pass

print("all", new_pop)
'''