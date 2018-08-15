#!/usr/bin/env python

import sys
import os

aside_array = []
zside_array = []
desc_array = []
a_agg_array = []
z_agg_array = []
a_testip_array = []
z_testip_array = []
cap_type_array = []
cid_array = []
#--------------------------------------------------------------------------------------
#This provides the capacity mop
def the_mop():
        aside_array = []
        zside_array = []
        desc_array = []
        a_agg_array = []
        z_agg_array = []
        a_testip = []
        z_testip = []
        cap_type_array = []
        cid_array = []
#-------------------------------------------------------------------------------------

i=0
t=0

print("\n=============================================================================")
print("Cox C4 Capacity Script")
print("Version 1")
print("By: T.C. Covert")
print("=============================================================================")

print("\n\nPlease answer the following questions.") 
device = raw_input("Enter device name: ")
int =int(raw_input("How many circuits do you have?"))
for i in range(0, int):
        aside_array.append((raw_input("Enter A-Side interface for Circuit #" + str(i +1) +":")))
        zside_array.append((raw_input("Enter Z-Side interface for Circuit #" + str(i +1) +":")))
        desc_array.append((raw_input("Enter the testing description for Circuit #" + str(i +1) +":")))
        a_testip_array.append((raw_input("Enter A-Side test IP only '/31' for Circuit #" + str(i +1) +":")))
        z_testip_array.append((raw_input("Enter Z-Side test IP only '/31' for Circuit #" + str(i +1) +":")))
        a_agg_array.append((raw_input("Enter A-Side aggerate number for Circuit #" + str(i +1) +":")))
        z_agg_array.append((raw_input("Enter Z-Side aggerate number for Circuit #" + str(i +1) +":")))
        if i ==0:
                    cap_type = raw_input("Enter project type (RDC, SYST, or C4): ")
        if cap_type == str("C4"):
                    cid_array.append((raw_input("Enter C4 circuit id for Circuit #" + str(i +1) +":")))
        if i ==0:
                    cap_speed = raw_input("Enter link speed (10 or 100): ")
        i = i + 1

end_device = raw_input("Enter Z-Side device: ")
agg_update = raw_input("Enter updated agg speed: ")
ecr = raw_input("Enter ECR: ")




########################################################################################################################################################################

#A-Side Hardware Install MOP

print("\n-----------------------------------------------------------------------")
print("\nH/W Testing MOP for A-Side " + device.upper())
print("\n-----------------------------------------------------------------------")
print("\n"+ device.upper() + " Pre-Checks:")
print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse |no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more ")
for t in range(0, i):
 
        print("\nshow interfaces " +  str(aside_array[t]) + " extensive | no-more")
        print("show interfaces diagnostics optics " +  str(aside_array[t]) + " | match "'"power *:"'"")
        print("clear interface statistics " +  str(aside_array[t]) )

print("\n")
print("\n"+ device.upper())
print("\nCONFIGURATION COMMANDS:")
print("\n\nconfigure exclusive")

for t in range(0, i):
 
        print("\n\ndelete interfaces " +  str(aside_array[t]) )
        print("\nset interfaces " +  str(aside_array[t]) + " description "+ '"'+str(desc_array[t]).upper()+'"')
        print("set interfaces " +  str(aside_array[t]) + " unit 0 family inet address " + str(a_testip_array[t]) + "/31")
        print("set interfaces " +  str(aside_array[t]) + " mtu 9100")

print("\n\nshow | compare | no-more\ncommit check \ncommit synchronize and-quit comment " + ecr)


########################################################################################################################################################################


#Z-Side Hardware Install MOP

print("\n-----------------------------------------------------------------------")
print("\nH/W Testing MOP for Z-Side " + end_device.upper())
print("\n-----------------------------------------------------------------------")
print("\n"+ end_device.upper() + " Pre-Checks:")
print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse |no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more ")
for t in range(0, i):
 
        print("\nshow interfaces " +  str(zside_array[t]) + " extensive | no-more")
        print("show interfaces diagnostics optics " +  str(zside_array[t]) + " | match "'"power *:"'"")
        print("clear interface statistics " +  str(zside_array[t]) )
        
print("\n")
print("\n"+ end_device.upper())
print("\nCONFIGURATION COMMANDS:")
print("\n\nconfigure exclusive")

for t in range(0, i):
 
        print("\ndelete interfaces " +  str(zside_array[t]) )
        print("\nset interfaces " +  str(zside_array[t]) + " description "+ '"'+str(desc_array[t]).upper()+'"')
        print("set interfaces " +  str(zside_array[t]) + " unit 0 family inet address " + str(z_testip_array[t]) + "/31")
        print("set interfaces " +  str(zside_array[t]) + " mtu 9100")

print("\n\nshow | compare | no-more\ncommit check \ncommit synchronize and-quit comment " + ecr)



########################################################################################################################################################################

#A-Side TRAFFIC ADD
print("\n\n-----------------------------------------------------------------------")
print("\nTraffic Add MOP for A-Side " + device.upper())
print("\n-----------------------------------------------------------------------")
print("\n"+ device.upper() + " Pre-Checks:")
print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse |no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more ")
for t in range(0, i):
        print("\nshow interfaces diagnostics optics " +  str(aside_array[t]) + " | match "'"power *:"'"")
        print("ping rapid count 500 " + str(z_testip_array[t]))
        print("show interfaces " + str(aside_array[t]) + " extensive | no-more")
        print("clear interface statistics " +  str(aside_array[t]) )



print("\n")
print("\n"+ device.upper())
print("\nCONFIGURATION COMMANDS:")
print("\n\nconfigure exclusive")

for t in range(0, i):
        print("\n\ndelete interfaces " +  str(aside_array[t]) )
        if cap_type == str("C4"):
               print("\nset interfaces " +  str(aside_array[t]) + " description "+ '"'+ "COX;" + str(cid_array[t]) +";" + str(cap_type).upper() + " " + end_device.upper() + ";" +  str(zside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')
        if cap_type == str("RDC"):
               print("\nset interfaces " +  str(aside_array[t]) + " description "+ '"'+ "COX;"";" + str(cap_type).upper() + " " + end_device.upper() + ";" +  str(zside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')
        if cap_type == str("SYST"):
               print("\nset interfaces " +  str(aside_array[t]) + " description "+ '"'+ "COX;"";" + str(cap_type).upper() + " " + end_device.upper() + ";" +  str(zside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')       
               
        print("set interfaces " +  str(aside_array[t]) + " gigether-options 802.3ad ae" + str(a_agg_array[t]))
        print("set interfaces " +  str(aside_array[t]) + " disable")

print("\nset interfaces ae" + str(a_agg_array[t]) + " description "+ '"'+ ";;" + str(cap_type).upper() + ' ' + end_device.upper() + ";ae" + str(z_agg_array[t]) + ";" + agg_update + "G;MR;;" + '"')
print("set interfaces ae" + str(a_agg_array[t]) + " unit 0 " + "description "+ '"'+ ";;" + str(cap_type).upper() + ' ' +  end_device.upper() + ";ae" + str(z_agg_array[t]) + ";" + agg_update + "G;MR;;" + '"')
       
print("\n\nshow | compare \ncommit check \ncommit synchronize and-quit comment " + ecr)


########################################################################################################################################################################


#Z-Side TRAFFIC ADD
print("\n\n-----------------------------------------------------------------------")
print("\nTraffic Add MOP for Z-Side " + end_device.upper())
print("\n-----------------------------------------------------------------------")
print("\n"+ end_device.upper() + " Pre-Checks:")
print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse |no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more ")
for t in range(0, i):
        print("\nshow interfaces diagnostics optics " +  str(zside_array[t]) + " | match "'"power *:"'"")
        print("ping rapid count 500 " + str(a_testip_array[t]))
        print("show interfaces " + str(zside_array[t]) + " extensive | no-more")
        print("clear interface statistics " +  str(zside_array[t]) )



print("\n")
print("\n"+ end_device.upper())
print("\nCONFIGURATION COMMANDS:")
print("\n\nconfigure exclusive")

for t in range(0, i):
        print("\n\ndelete interfaces " +  str(zside_array[t]) )
        if cap_type == str("C4"):
               print("\nset interfaces " +  str(zside_array[t]) + " description "+ '"'+ "COX;" + str(cid_array[t]) +";" + str(cap_type).upper() + " " + device.upper() + ";" +  str(aside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')
        if cap_type == str("RDC"):
               print("\nset interfaces " +  str(zside_array[t]) + " description "+ '"'+ "COX;"";" + str(cap_type).upper() + " " + device.upper() + ";" +  str(aside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')
               
        #print("\nset interfaces " +  str(zside_array[t]) + " description "+ '"'+ "COX;;" + str(cap_type).upper() + " " + device.upper() + ";" +  str(aside_array[t]) + ";" + str(cap_speed) + "G;MR;;" + '"')
        print("set interfaces " +  str(zside_array[t]) + " gigether-options 802.3ad ae" + str(z_agg_array[t]))

print("\nset interfaces ae" + str(z_agg_array[t]) + " description "+ '"'+ ";;" + str(cap_type).upper() + ' ' + device.upper() + ";ae" + str(a_agg_array[t]) + ";" + agg_update + "G;MR;;" + '"')
print("set interfaces ae" + str(z_agg_array[t]) + " unit 0 " + "description "+ '"'+ ";;" + str(cap_type).upper() + ' ' +  device.upper() + ";ae" + str(a_agg_array[t]) + ";" + agg_update + "G;MR;;" + '"')
       
print("\n\nshow | compare \ncommit check \ncommit synchronize and-quit comment " + ecr)

 
########################################################################################################################################################################


#End of A-Side TRAFFIC ADD

       
print("\n\n-----------------------------------------------------------------------")
print("\nTraffic Add MOP for A-Side " + device.upper())
print("\n-----------------------------------------------------------------------")

print("\n") 
print("\n"+ device.upper())
print("\nCONFIGURATION COMMANDS:")
print("\nconfigure exclusive\n")

for t in range(0, i):
        print("delete interfaces " +  str(aside_array[t]) + " disable")

print("\n\nshow | compare | no-more \ncommit check \ncommit synchronize and-quit comment " + ecr)


print("\n\n-----------------------------------------------------------------------")
print ("\n\nPost-Checks for A-Side " + device.upper())
print("\n-----------------------------------------------------------------------")

print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse | no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more\n ")
print("\n")

for t in range(0, i):
        print("show interfaces " + str(aside_array[t]) + " extensive | no-more")
print("\n")
print("show interfaces ae" + str(z_agg_array[t]) + " extensive | no-more")
print("show log messages | last 300 | no-more")

print("\n\n-----------------------------------------------------------------------")
print ("\n\nPost-Checks for Z-Side " + end_device.upper())
print("\n-----------------------------------------------------------------------")

print("\n\nshow interfaces descriptions | match down | no-more \nshow interfaces terse | no-more \nshow rsvp interface | no-more \nshow mpls interface | no-more \nshow ospf neighbor | no-more \nshow pim neighbors | no-more \nshow ldp interface | no-more \nshow ldp session | no-more \nshow ldp neighbor | no-more \nshow mpls lsp | match down | no-more \nshow igmp interface | no-more\n ")
print("\n")

for t in range(0, i):
        print("show interfaces " + str(zside_array[t]) + " extensive | no-more")
print("\n")
print("show interfaces ae" + str(z_agg_array[t]) + " extensive | no-more")
print("show log messages | last 300 | no-more")

#Run the script
the_mop()