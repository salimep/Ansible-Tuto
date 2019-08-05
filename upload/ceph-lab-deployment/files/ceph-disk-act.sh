#!/bin/bash
## this  will exicute as ceph user by script
cd ~

## zap  osd disks for osd nodes
ceph-deploy disk zap ceph-osd2:/dev/sdb ceph-osd2:/dev/sdc ceph-osd1:/dev/sdb ceph-osd1:/dev/sdc

 ## activate OSD disks
ceph-deploy osd prepare  ceph-osd2:/dev/sdb ceph-osd2:/dev/sdc  ceph-osd1:/dev/sdb ceph-osd1:/dev/sdc

## gather admin keys
ceph-deploy admin ceph-admin ceph-mon ceph-osd1 ceph-osd2

## admin node keyring permission

sudo chmod 644 /etc/ceph/ceph.client.admin.keyring
