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
  print 'stderr: %s'%(cstderr)

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
  print 'stdout: %s'%(cstdout)
  print 'stderr: %s'%(cstderr)
  print '------------------------------------\n'

  #
  # file case
  #
  fd = open('./test.log', 'a')
  cmd = ['ls', '--ggg']
  child = subprocess.Popen(cmd,
                           stdout = fd,
                           stderr = subprocess.STDOUT)
  child.communicate()
  ret  = child.returncode
  fd.close()

  print '------------------------------------\n'
  print 'cmd:%s' %(cmd)
  print 'return: %s'%(ret)
  print 'stderr: %s'%(cstderr)
  print '------------------------------------\n'


