#!/usr/bin/python
import subprocess as sub
import json
## print all disks
command="fdisk -l |grep ^Dis|awk '{print $2}'|grep -v mapp|grep /de|sed 's/://'"
result=sub.Popen(command,shell=True,stdout=sub.PIPE)
output,error =result.communicate()

result=str(output).split("\n")
my_list=[x for x in result if x]
## find root disk  and exclude from LVM creation
root_disk_cmd="df -h |grep boot|awk '{print $1}'|sed 's/[0-9]//g'"
root=sub.Popen(root_disk_cmd,shell=True,stdout=sub.PIPE)
root_result,error=root.communicate()
root_result=str(root_result).strip("\n")
for a in my_list:
     if str(root_result) == str(a):
          my_list.remove(a)

my_dict={'disk': list(my_list)}
my_result=json.dumps(my_dict)
print (my_result)

