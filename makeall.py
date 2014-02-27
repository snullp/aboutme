#!/usr/local/bin/python3

import os
import fnmatch
import datetime

header='header.template.html'
footer='footer.template.html'

contents=[]

def gentitle(name):
    if name=='index':
        return 'Homepage'
    else:
        return name.capitalize()

def genpage(name):
    names=''
    for filename in contents:
        if name==filename[1]:
            names += '<li class="active"><a href="#">'+gentitle(filename[1])+'</a></li>\n'
        else:
            names += '<li><a href="'+filename[1]+'.html">'+gentitle(filename[1])+'</a></li>\n'
    return names


def main():
    for file in sorted(os.listdir()):
        if fnmatch.fnmatch(file,'*.content.html'):
            contents.append((file,file.split('.')[1]))
    for filename in contents:
        target=filename[1]+'.html'
        w=open('./target/'+target,'w');
        for name in [header,filename[0],footer]:
            r=open(name,'r')
            w.write(r.read().format(subtitle=gentitle(filename[1]),pages=genpage(filename[1]),updatetime=datetime.date.today()))
        print (target + ' done.')

if __name__ == "__main__":
    main()
