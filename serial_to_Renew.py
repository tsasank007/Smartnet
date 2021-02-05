
import re
import netmiko
from netmiko import ConnectHandler, SCPConn
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
import string
import sys
import os
import datetime
#
# sys.path.insert(0, "/etc/adi")
# from nsg_hosts import get_hosts


def whenConnected(output):
    # print('im inside the whenConnected')
    addSplitOut = []
    for line in output.splitlines():
        if ('show' not in line) and (line != ''):
            print (line)
        splitOut = line.split(' ')
        addSplitOut.append(splitOut[0])
    # print(f'splitOut in whenConnected is {type(addSplitOut)}')
    return addSplitOut



def getSerial(node=None, username = None, password = None):
    # print(f'what is the value at intf{intf} and the type is {type(intf)}')

        try:
            # regx = ['[G,P,E,F}[A-Za-z]{2,3}[0-9]{1,3}.[0-9]{1,2}[\/][0-9]{1,2}', '[G,P,E,F}[A-Za-z]{2,3}[0-9]{1,3}.[0-9]{1,2}','[G,P,E,F}[A-Za-z]{2,3}[0-9]{1,3}']
            # regx = '[A-Za-z]{2,3}[0-9]{1,3}.[0-9]{1,2}[\/][0-9]{1,2}'
            eachLine = []
            # int_for_device = []

            hostname = str(node)
            device = {
            'device_type': 'cisco_ios',#'autodetect',
            'ip': hostname,
            'username': username,
            'password': password,
            'verbose': False
            }

            ssh_session = netmiko.ConnectHandler(**device)
            scp_conn = SCPConn(ssh_session)

            #add commands you wish run here.
            # cmdList = [
            #       'show ver | in Proc',
            #       'show int des | in up'+' ',
            #     ]
            cmdList = [
                 'show ver | in Proc',
                 'show int status | in connected'
                ]
            for cmd in cmdList:
                print(hostname + ': ' + cmd)
                output = ssh_session.send_command(cmd)

                # if output == '':
                #     cmdList = [
                #          'show ver | in Proc',
                #          'show int status | in connected'
                #         ]
                #     for cmd in cmdList:
                #         print(hostname + ': ' + cmd)
                #         outputToSend = ssh_session.send_command(cmd)
                          # eachLine = whenConnected(outputToSend)
                # else:
                eachLine = whenConnected(output)

                for intf in eachLine:
                    if intf == '' or intf == 'Processor':
                        break
                    else:
                        intfCmd = [
                            'show int '+intf+' | in rate|errors|Desc',
                            ]
                        for cmd in intfCmd:
                            # print(hostname + ': ' + cmd)
                            print(cmd)
                            output = ssh_session.send_command(cmd)
                            for linedesc in output.splitlines():
                                print (linedesc)
                            print('')

            #close the connections
            scp_conn.close()
            ssh_session.disconnect()
            # print(line)



        except IOError as eWriteFile:
            print(f'here is the exception : {eWriteFile}')
            scp_conn.close()
            ssh_session.disconnect()

def main():
    try:
        #reach the first switch and get the details
        username = input('Username:')
        password = getpass()

        with open("/home/few7/pythonScripts/SmartNet/Hosts_NOT_Renw.txt") as fo:
            nodes = fo.read().splitlines()
            print(nodes)
        nodes.sort()
        # print(f'Nodes from a file : {nodes}')

        for node in nodes:
            # print(f'each Node from nodes : {node}')
            out = getSerial(node, username, password)


    except IOError as eWriteFile:
        print(f'here is the exception : {eWriteFile}')
        scp_conn.close()
        ssh_session.disconnect()




if __name__ == '__main__':
    main()
