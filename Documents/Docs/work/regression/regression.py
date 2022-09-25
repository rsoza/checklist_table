
import os

class Config:

    def __init__(self, name, array, host, cfw=[], nvsram=[], vki=[], smid=[], bios=[], 
                smIntstaller=[], um=[], dfw=[], iom=[], hba=[], hostType=[], smash=[],
                asup=[], arrayList=[], hostList=[], flag=0):
        self.name = name
        self.array = array
        self.host = host
        self.cfw = cfw
        self.nvsram = nvsram
        self.vki = vki
        self.smid = smid
        self.bios = bios
        self.smInstaller = smIntstaller
        self.um = um
        self.dfw = dfw
        self.iom = iom
        self.hba = hba
        self.hostType = hostType
        self.smash = smash
        self.asup = asup
        self.arrayList = arrayList
        self.hostList = hostList
        self.flag = flag
    
    def verify_cfw(self):

        #TODO:YAML INFO ON LATEST BUILD 
        print('''
        Please update Controller Firmware(CFW) to the latest build.
        Record the CFW of each array in %s.
        ''' % (self.name))

        for n in range(len(self.array)):
            self.cfw.append(input("CFW on %s: " % (self.array[n])))
        
    def verify_nvsram(self):
        #TODO:YAML INFO ON LATEST BUILD 
        print('''
        Please update Non-Volatile Random-Access Memory(NVSRAM) to the latest build.
        For %s record the NVSRAM of each array.
        ''' % (self.name))

        for n in range(len(self.array)):
            self.nvsram.append(input("NVSRAM on %s: " % (self.array[n])))
    
    def edit_vki(self):
        print('''
        Access serial connection for each controller to perform all of the following steps.

        - Type VKI_EDIT_OPTIONS into serial. 
        - If not already done, disable this. 

        The following steps are to clear settings on the controllers: 

        M    <- Boot Operations Menu 
        13   <- Development Options Menu 
        R    <- Reset Development Options Modes 
        E    <- Edit Application Development Script
        C    <- Clear all options
        Y    <- Confirm clear 
        Q    <- Quit edit mode 
        Y    <- Commit changes to NVSRAM 
        Q    <- Quit Menu 
        Q    <- Quit Menu 

        *MAKE SURE TO DO THIS TO ALL CONTROLLERS*

        Type 'd' for done when VKI_EDIT_OPTIONS and DEBUG OPTIONS are completed for the following arrays in %s. 
        ''' % (self.name))
    #TODO: Exception on d
        for n in range(len(self.array)):
            self.vki.append(input('%s: ' % (self.array[n])))

    def verify_smid(self):
        print('''
        Check SMID on controllers, make sure they match. 

        On serial: Type fbmShow
        On SAM: in Support tab look for "Current sub-model ID"

        To verify this is the right SMID go to cfwweb.eng.netapp.com

        *MAKE SURE TO DO THIS TO ALL ARRAYS* 

        Please type in SMID for each array in %s
        ''' % (self.name))

        while True:
            try:
                for n in range(len(self.array)):
                    self.smid.append(int(input('%s: ' % (self.array[n]))))
                break
            except ValueError:
                print("Not a number, try again...\n")
            
    def update_bios(self):
    #TODO: YAML FILE CONTAINING BIOS LIST
        print('''
        Verify BIOS is up-to-date.

        On serial: Type biosShow

        *MAKE SURE TO DO THIS TO ALL ARRAYS*

        Please type in BIOS for each array in %s
        ''' % (self.name))
        for n in range(len(self.array)):
            self.bios.append(input('%s: ' % (self.array[n])))

    def update_SMinstaller(self):
        #TODO: %s replaced with YAML contents
        print('''
        There are many ways to get the SMinstaller.

        Verify the host that you are on:
        - Linux: cat /etc/os-release
        - Windows: System Information > OS Name/build

        To install latest:
        - sftp sso@cyclict.eng.netapp.com
        - go to directory for the respective host

        # MSW: /u/symsm/sym/sminstaller/* (Agent and Util only)
        Windows DSM: /u/symsm/sym/dsminstaller/*
        # MSW: /u/symsm/sym/sminstaller/*
        NOTE: Make sure to use .exe file but .exe.orig for Windows ONLY

        *MAKE SURE TO DO THIS TO ALL HOSTS*

        Please type in the SMinstaller version for each host in %s.
        ''' % (self.name))
        for n in range(len(self.host)):
            self.smInstaller.append(input('%s: ' % (self.host[n])))
        
    def update_um(self):
        #TODO: YAML contents
        print('''
        Latest Unified Manager can be found here:
        http://nexus-master.eng.netapp.com:8081/nexus/content/repositories/OfficialRelease/com/netapp/eseries/webapiinstall/

        *MAKE SURE TO DO THIS TO ALL HOSTS*

        Please type in the Unified Manager version for each host in %s.
        ''' % (self.name))
        for n in range(len(self.host)):
            self.um.append(input('%s: ' % (self.host[n])))

    def verify_dfw(self):
    # TODO: YAML file
        print('''
        The Disk Firmware(DFW) can be found easiest via SAM, please note there are
        other ways.

        On SAM go to :
        - Support tab > Support Center > Software and Firmware Inventory > Drives
        OR
        - Support tab > Support Center > Upgrade Center > Driver Firmware Upgrade: Begin Upgrade

        These two options will show the DFW for each drive in the array. Compare
        the firmware to the DFW website outside of VED:
        https://mysupport.netapp.com/site/downloads/firmware/e-series-disk-firmware
        
        *MAKE SURE TO DO THIS TO ALL ARRAYS*

        Please type y or n if all DFW were upgraded for each array in %s
        ''' % (self.name))
        #TODO: create a y or n exception
        for n in range(len(self.array)):
            self.dfw.append(input('%s: ' % (self.array[n])))

    def verify_iom(self):
    #TODO: YAML CONTENTS
        print('''
        IOM firmware version can be found in many ways. This way is via SAM.
        
        On SAM go to:
        - Support tab > Support Center > Software and Firmware Inventory > IOM(ESM)
        - Verify Firmware version is correct accroding to flavor of IOM/ESM.
        -LIST IOM/ESM VERSIONS

        *MAKE SURE TO DO THIS TO ALL ARRAYS*

        Please type in firmware version of IOM/ESM for each array in %s.
        ''' % (self.name))
        for n in range(len(self.array)):
            self.iom.append(input('%s: ' % (self.array[n])))

    def verify_hba(self):
    #TODO: maybe yaml contents?
        print('''
        Verify HBA on host is compatible.

        On host find the HBA:
        Linux: lspci | grep <brand>
        Windows: Device manager > Network Adaptors

        Then go to IOM matrix to compare:
        - Outside of VED go to https://imt.netapp.com/matrix/#welcome
        - Go to Advanced Search.
        - Type in “Netapp OS” in the search box.
        - Select Netapp OS" and click on the "Browse" link. This will show all the available programs.
        - For our current release, select "SANtricity OS 11.70" and add.
        - Click “Next >> Refine Search Criteria”.
        - Check everything that is applicable to your name and click "View Results" when done filtering.
        - Click on all tabs; Details, Info, Alert for HBA FW/BIOS/Drivers and it's setting.
        - It may also have acceptable host kernel.

        Please note, here you would also update your host to the alerts/notes 
        accordingly to results displayed. There may be critical updates for your
        host that have not been made evident.

        *MAKE SURE TO DO THIS TO ALL HOSTS*

        Please type in the HBA for each host in %s.
        ''' % (self.name))

        for n in range(len(self.host)):
            self.hba.append(input('%s: ' % (self.host[n])))

    def host_type(self):
        print('''
        Verify the host that you are on:
        - Linux: cat /etc/os-release
        - Windows: System Information > OS Name/build

        Verify on host is compatible with the config on IMT.
        https://imt.netapp.com/matrix/#welcome

        *MAKE SURE TO DO THIS TO ALL HOSTS*

        Please type in the host type for each host in %s.
        ''' % (self.name))

        for n in range(len(self.host)):
            self.hostType.append(input('%s: ' % (self.host[n])))

    def verify_smash(self):
    #TODO: TAML CONTENTS ON FIRST TWO %s
        print('''
        Smash setting should abide by the protocol and/or stress you are currently 
        running. This is a good time to check your parameters.

        The latest smash and cache is located in the cycle server:
        Linux:      /u/acristhi/BLDS/smashbuilds/linuxIX64/%s
        Windows:    /u/acristhi/BLDS/smashbuilds/win64/%s

        All hosts must run mixed IO (both raw and filesystem)
        If you have DULBE drive + volumes, please create filesystem with deleteFiles option.

        Verify RHEL is not running BTRF fileSystem.
        If you don't know how to check BTRF fileSystem. Check with Tasking Engineer before your config audit.

        *MAKE SURE TO DO THIS TO ALL HOSTS*

        Please type in y or n if smash/cache was updated to each host in %s.
        ''' % (self.name))
        for n in range(len(self.host)):
            self.smash.append(input('%s: ' % (self.host[n])))

    def verify_asup(self):
        #TODO: EXCEPTION D
        print('''
        Verify ASUP is enabled on all arrays.
        
        On SAM > Support > AutoSupport > Configure AutoSupport Delivery Method 
        > Show destination address
        
        Verify this is the same as: 
        https://testbed.netapp.com/put/AsupPut/

        To change the ASUP configuration:
        SMcli <controllerIP-a> <controllerIP-b> -u admin -p infiniti -k -c "set storageArray autoSupport featurePhase=Test;"
        Using SAM, from the Support tab, navigate to Support Center > AutoSupport tab > Configure AutoSupport Delivery Method > Show destination address.
        Verify the address is set to  https://testbed.netapp.com/put/AsupPut/

        
        *MAKE SURE TO DO THIS TO ALL ARRAYS*

        Please type in "d" for done if each array in %s has the right ASUP.
        ''' % (self.name))
        for n in range(len(self.array)):
            self.asup.append(input('%s: ' % (self.array[n])))

    def table(self, choice):

        if self.flag == 0:
            arrays = []
            arrays.append("")
            arrays.extend(self.array)
            self.arrayList.append(arrays)
            

            hosts = []
            hosts.append("")
            hosts.extend(self.host)
            self.hostList.append(hosts)
            
            self.flag = 1

        checklist_dict = {
            "1": self.cfw,
            "2": self.nvsram,
            "3": self.vki,  
            "4": self.smid,  
            "5": self.bios,  
            "6": self.smInstaller,
            "7": self.um,  
            "8": self.dfw,  
            "9": self.iom,
            "10":self.hba,
            "11":self.hostType,
            "12":self.smash,
            "13":self.asup,
        }
        arrayList_dict = {
            "1":  "CFW",
            "2":  "NVSRAM",
            "3":  "VKI_EDIT_OPTIONS and DEBUG OPTIONS",
            "4":  "SMID",
            "5":  "FPGA/BIOS/BMC",
            "8":  "DFW",
            "9":  "IOM/ESM FW",
            "13": "ASUP"
        }
        hostList_dict = {
            "6":  "SMinstaller",
            "7":  "Unified Manager",
            "10": "HBA FW/BIOS/Driver and HBA Settings",
            "11": "Host Type",
            "12": "Smash Settings",
        }

        if choice in arrayList_dict:
            checklist_dict[choice].insert(0, arrayList_dict[choice])
            self.arrayList.append(checklist_dict[choice])

        if choice in hostList_dict:
            checklist_dict[choice].insert(0, hostList_dict[choice])
            self.hostList.append(checklist_dict[choice])

        elif choice == 'T' or choice == 't':
            n = max(len(arrLen) for item in self.arrayList for arrLen in item)
            print("\n\nArray Information in %s: " % (self.name))
            for row in self.arrayList:
                print(''.join(arrLen.ljust(n + 2) for arrLen in row))
           
            n = max(len(hostLen) for item in self.hostList for hostLen in item)
            print("\n\nHost Information in %s: " % (self.name))
            for row in self.hostList:
                print(''.join(hostLen.ljust(n + 2) for hostLen in row))

    def menu(self):
        
        checklist_dict = {
            "1": self.verify_cfw,
            "2": self.verify_nvsram,
            "3": self.edit_vki,  
            "4": self.verify_smid,  
            "5": self.update_bios,  
            "6": self.update_SMinstaller,
            "7": self.update_um,  
            "8": self.verify_dfw,  
            "9": self.verify_iom,
            "10":self.verify_hba,
            "11":self.host_type,
            "12":self.verify_smash,
            "13":self.verify_asup,
        }
            
        print("\n************Regression Checklist for %s**************" % (self.name))

        print('''
            1:  CFW
            2:  NVSRAM
            3:  VKI_EDIT_OPTIONS and DEBUG OPTIONS
            4:  SMID
            5:  FPGA/BIOS/BMC
            6:  SMinstaller
            7:  Unified Manager
            8:  DFW
            9:  IOM/ESM FW
            10: HBA FW/BIOS/Driver and HBA Settings
            11: Host Type
            12: Smash Settings
            13: ASUP

            Q: Quit
            ''')
        choice = input('Please enter your choice: ')


        if choice in checklist_dict:
            checklist_dict[choice]()
            self.table(choice)
            self.menu()
        elif choice == 'T' or choice == 't':
            self.table(choice)
            self.menu()
        elif choice == 'Q' or choice == 'q':
            exit
        else:
            print("Not an option...")
            print("Please try again.")
            self.menu()
    


def defaultQuestion(word, config):
    group = []
    while True:
        try:
            value = int(input("\nHow many %s(s) are there in %s? \n" % (word, config)))
            for n in range(value):
                group.append(input('%s %s: ' % (word, n+1)))
            return group
        except ValueError:
            print("Not a number, try again...\n")

def main():
    config_name = input('What is the name of your config?\n')
    host = defaultQuestion("host", config_name)
    arrs = defaultQuestion("array", config_name)

    config = Config(config_name, arrs, host)
    config.menu()


os.system('cls')
main()
