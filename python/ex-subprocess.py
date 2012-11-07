import os
import sys
import subprocess

if __name__ == '__main__':

  #
  # correct case
  #
  cmd = ['ls', '-al']
  child = subprocess.Popen(cmd,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)
  cstdout, cstderr  = child.communicate()
  ret  = child.returncode


  print '------------------------------------\n'
  print 'cmd:%s' %(cmd)
  print 'return: %s'%(ret)
  print 'stdout: \n%s'%(cstdout)

  #
  # error case
  #
  cmd = ['ls', '--ggg']
  child = subprocess.Popen(cmd,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)
  cstdout, cstderr  = child.communicate()
  ret  = child.returncode

  print '------------------------------------\n'
  print 'cmd:%s' %(cmd)
  print 'return: %s'%(ret)
  print 'stderr: %s'%(cstderr)
  print '------------------------------------\n'

