import os
import getpass

os.system("tput setaf 4")
print("\t \t \t WELCOME TO IRIS")
os.system("tput setaf 7")
print("\t \t ---------------------------------")
#x=getpass.getpass()
#if(x!="root"):
#	print("Password incorrect.....bye")
#	exit()
login=input("How do you wanna work (local/remote)!! : ")

if(login=="l"):
	while True:
		input("Hit ENTER...")
		os.system("clear")
		print("""
		\tpress 1 : To do Partition...
		\tpress 2 : LVM Console...
		\tpress 3 : Docker...
		\tpress 4 : To Get Started with hadoop...
		\tpress 5 : Quit...
		""")
		choice = int(input("!!! : "))

		if(choice==1):
			os.system("tput setaf 3")
			print("\n\t\t \t WELCOME TO PARTITION")
			os.system("tput setaf 7")
			print("\t \t ----------------------------------------")
			print("""
			press 1 : Create new Partition.
			press 2 : Mount...
			press 3 : Unmount...
			
			""")
			pch=int(input("What you would like to do !!! : "))
			if(pch==1):
				dev_loc=input("Enter the block name : ")
				os.system("fdisk {}".format(dev_loc))
				os.system("udevadm settle")
				part_loc=input("Enter the partition name : ")
				os.system("mkfs.ext4 {}".format(part_loc))
				print("Partition Created Successfully")
			elif(pch==2):
				par_name=input("Enter the partition device location : ")
				directory=input("Enter the directory to mount : ")
				os.system("mount {} {}".format(par_name,directory))
				os.system("lsblk")
			elif(pch==3):
				directory=input("Enter the directory to Unmount : ")
				os.system("umount {}".format(directory))
				os.system("lsblk")
		elif(choice==2):
			os.system("tput setaf 3")
			print("\n\t\t \t WELCOME TO LOGICAL VOLUME MANAGEMENT")
			os.system("tput setaf 7")
			print("\t \t ----------------------------------------")
			print("""
			press 1 : To Create Physical Volume...
			press 2 : To Create Volume Group...
			press 3 : To Create Logical Volume...
			press 4 : To extend size of volume...
			press 5 : To remove LV...
			press 6 : To remove VG...
			""")
			lvmch=int(input("What you would like to do !!! : "))
			if(lvmch==1):
				loc= input("Enter the device location.. : ")
				os.system("pvcreate /dev/{}".format(loc))
			elif(lvmch==2):
				pv=input("Enter the physical volume.. : ")
				vg_name=input("Enter the volume group name.. : ")
				os.system("vgcreate {} /dev/{}".format(vg_name,pv))
			elif(lvmch==3):
				size=input("Enter the size of LV.. : ")
				lv_name=input("Enter the LV name.. : ")
				vg_name=input("Enter the VG name.. : ")
				os.system("lvcreate --size +{} --name {} {}".format(size,lv_name,vg_name))
				os.system("lsblk")
			elif(lvmch==4):
				size=input("Enter the size of LV.. : ")
				lv_name=input("Enter the LV name.. : ")
				vg_name=input("Enter the VG name.. : ")
				os.system("lvextend --size +{} /dev/{}/{}".format(size,vg_name,lv_name))
				os.system("resize2fs /dev/{}/{}".format(vg_name,lv_name))
				os.system("lsblk")
			elif(lvmch==5):
				lv_name=input("Enter the LV name.. : ")
				vg_name=input("Enter the VG name.. : ")
				os.system("lvremove -f {}/{}".format(vg_name,lv_name))
				os.system("lsblk")
			elif(lvmch==6):
				vg_name=input("Enter the VG name.. : ")
				os.system("vgchange -an {}".format(vg_name))
				os.system("vgremove {}".format(vg_name))
		elif(choice==3):
			os.system("tput setaf 3")
			print("\n\t\t \t WELCOME TO Docker")
			os.system("tput setaf 7")
			print("\t \t ----------------------------------------")
			print("""
			press 1 : Check how many os running on docker
			press 2 : Run new os
			press 3 : To remove os
			press 4 : Start or Stop os
			press 5 : Get terminal of docker os
			press 6 : To copy files from baseOS to Docker
			press 8 : To remove all OS on Docker
			press 9 : To delete the images
			""")
			dch=int(input("What you would like to do !!! : "))
			if(dch==1):
				os.system("docker ps -a")
			elif(dch==2):
				os_type=input("Enter OS flavour and version : ")
				os_name=input("Enter the name of OS : ")
				os.system("docker run -it --name {} {}".format(os_name,os_type))
			elif(dch==3):
				os_name=input("Enter the name of OS.. : ")
				os.system("docker rm {} ".format(os_name))
			elif(dch==4):
				cmd=input("start or stop : ")
				os_name=input("OS name : ")    
				os.system("docker {} {}".format(cmd,os_name))
			elif(dch==5):
				os_name=input("Enter the OS name to get terminal.. : ")	
				os.system("docker attach {}".format(os_name))
			elif(dch==6):
				source_loc=input("Enter the source location... : ")
				os_name=input("Enter the os_name... : ")
				destination=input("Enter the destination... : ")
				os.system("docker cp {} {}:{}".format(source_loc,os_name,destination))
			elif(dch==7):
				os.system("docker rm -f `docker ps -a`")
			elif(dch==8):
				os.system("docker images")
				image_name=input("Enter the image that you want to pull out... : ")
				os.system("docker rmi {}".format(image_name))	
		elif(choice==4):
			os.system("tput setaf 3")
			print("\n\t\t \t WELCOME TO HADOOP SETUP")
			os.system("tput setaf 7")
			print("\t \t ----------------------------------------")
			print("""
			press 1 : To Start Hadoop Master.
			press 2 : To configure Hadoop Master.
			press 3 : To Stop Hadoop Master. 	
			""")
			hdc=int(input("What You Would Like To Do!!! : "))
			
			if(hdc==1):
				os.system("hadoop-daemon.sh start namenode")
			elif(hdc==2):
				os.system("tput setaf 5")
				os.system("vi /etc/hadoop/hdfs-site.xml")
				os.system("vi /etc/hadoop/core-site.xml")
				print("\t Now you can lauch hadoop master...")
				os.system("tput setaf 7")
			elif(hdc==3):
				os.system("hadoop-daemon.sh stop namenode")
		elif (choice==5):
			print("Thank you.....")
			os.system("clear")
			exit()	
elif login == "r":
	ip = input("Enter the ip : ")
	usr_name=input("Enter the username : ")
	pws = input("Enter the pass : ")
	os.system("sshpass -p {} ssh -o StrictHostKeyChecking=no {}@{}".format(pws,usr_name,ip))	





