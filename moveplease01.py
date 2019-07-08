#!/usr/bin/ver python3
import shutil
import os
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_srorage')
xname = input('enter the new name')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
