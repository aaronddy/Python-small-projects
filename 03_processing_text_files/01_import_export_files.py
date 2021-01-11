import os

# 해당 파일의 경로 확인
print(os.getcwd())                     # C:\Learning\Python\eleven_projects_python\03_processing_text_files
print(os.listdir())                    # ['01_import_export_files.py']

folderfile = os.listdir()
print(type(folderfile))                # <class 'list'>
print(folderfile)                      # ['01_import_export_files.py']



# 새로운 파일 생성 및 쓰기
'''
f = open('a.txt', 'w', encoding='utf-8')     # a라는 텍스트 문서에 utf-8로 인코딩
f.write('잘 진행될까?')
f.close()
'''


# 해당 파일 읽기
'''
f = open('a.txt', 'r', encoding='utf-8')
print(f.read())
print(f.read())

f.seek(0)                              # 커서 위치를 가장 처음으로 이동
print(f.read())

f.close()
'''


# 해당 파일에 내용 추가하기
'''
f = open('a.txt', 'a', encoding='utf-8')
f.write('\n인코딩 param을 추가하니 작동이 잘 됩니다')

f.close()

f = open('a.txt', 'r', encoding='utf-8')
print(f.read())

f.close()
'''

# close를 하지 않으면?
'''
f = open('b.txt', 'w', encoding='utf-8')
f.write('어떤 일이 발생할까요?')

해당 파일을 지우려고 하면 파일이 열려 있어서 지울 수 없다는 메시지가 나온다지만... vscode 에서는 잘 지워짐. 
'''

# with문으로 파일 실행하기
'''
with open('b.txt', 'a', encoding='utf-8') as f:         # f는 정의해줘야 작동합니다.
  f.write('\n잘 적히는군요')

with문을 사용하면 close를 하지 않아도 됩니다. 
'''