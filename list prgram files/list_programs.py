import os

py_current_dir = os.getcwd()
print('Which directory?')
input_dir = input()
dir_program_file = os.chdir('%s:/Program Files' %(input_dir))
list_programs = os.listdir(os.curdir)

dir_program_file_x86 = os.chdir('%s:/Program Files (x86)' %(input_dir))
list_programs_x86 = os.listdir(os.curdir)


text = os.chdir(py_current_dir)
text_file = open('List %s Program Files Name.txt' %(input_dir), 'w')
text_file.write('Program in %s \n\n' %(input_dir))
for program_name  in list_programs:
    text_file.write(program_name)
    text_file.write('\n')

text_file.write(('\n')+ ('-' * 30) + ('\n'))
text_file.write('Program_x86 in %s \n\n' %(input_dir))
for program_name_x86  in list_programs_x86:
    text_file.write(program_name_x86)
    text_file.write('\n')


text_file.close()
