import re
a = 'CONFIG_MY_NAME_IS="aaa"\n' + \
    'CONFIG_MY_NAME_IS="bbb"\n' + \
    'CONFIG_MY_NAME_IS="ccc"\n' + \
    'CONFIG_MY_NAME_IS_MIPS=y\n' + \
    'CONFIG_MY_COMPANY_RE=y\n' + \
    '# CONFIG_MY_COMPANY_BQ is not set\n' + \
    'CONFIG_MY_ID_IS_AB1074=y\n'

lines = a.split('\n')

for l in lines:
  match = re.search('CONFIG_MY_NAME_IS="(\w+)"', l)
  if match:
    print match.group(1)
  match = re.search('CONFIG_MY_ID_IS_(AB|RC|QQ)(5551|1074|B5566)=y', l)
  if match:
    print match.group(2)

  match = re.search('CONFIG_MY_COMPANY_(BQ|RE)=y', l)
  if match:
    print match.group(1)


