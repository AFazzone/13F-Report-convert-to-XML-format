# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:58:38 2020

@author: alf11
"""


infile = open("name_file.txt", "r")   
name_file = infile.read()

infile = open("cusip_file.txt", "r")   
cusip_file = infile.read()
    
infile = open("shares_file.txt", "r")   
shares_file = infile.read()

infile = open("value_file.txt", "r")   
value_file = infile.read()
    
name = list(name_file.split("\n"))
cusip = list(cusip_file.split("\n"))
shares = list(shares_file.split("\n"))
value = list(value_file.split("\n"))

str1 = """
<infoTable>
  <nameOfIssuer>"""
str2 = """</nameOfIssuer>
  <titleOfClass>ETF</titleOfClass>
  <cusip>"""
str3 = """</cusip>
  <value>"""
str4 = """</value>
  <shrsOrPrnAmt>
    <sshPrnamt>"""  
str5 = """</sshPrnamt>
    <sshPrnamtType>SH</sshPrnamtType>
  </shrsOrPrnAmt>
  <investmentDiscretion>SOLE</investmentDiscretion>
  <votingAuthority>
    <Sole>0</Sole>
    <Shared>0</Shared>
    <None>"""
str6 = """</None>
  </votingAuthority>
</infoTable> """
    
for i in range(len(name)):
    print(str1, name[i], str2, cusip[i], str3, value[i], str4, shares[i],
          str5,shares[i],str6)




