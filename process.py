import os
import sys

dir_ = 'image'
dest_dir = 'Annotations.txt'
write_file = open(dest_dir,'w')
for each_dir in os.listdir(dir_):
    with open(os.path.join(dir_,each_dir),'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().split('<')[1].split('>')[0]=='filename':
            file_name = dir_+"/"+line.strip().split('>')[1].split('<')[0]
            write_file.write(file_name)
        if line.strip().split('<')[1].split('>')[0] in ['xmin', 'xmax', 'ymin', 'ymax']:
            write_file.write(' '+line.strip().split('>')[1].split('<')[0])
    write_file.write('\n')


