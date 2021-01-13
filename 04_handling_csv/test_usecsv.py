import usecsv, os

os.chdir('C:\Learning\Python\eleven_projects_python\\04_handling_csv\\test')
subjects = [['korean', 'english', 'math'], [34, 56, 44]]

usecsv.writecsv('test_return.csv', subjects)

