import os
i=0
for filename in os.listdir("follow"):
    new_name="follow"+"_"+str(i)+".wav"
    os.rename("follow/"+filename, "follow/"+new_name)
    i=i+1
for filename in os.listdir("leftc"):
    new_name="leftc"+"_"+str(i)+".wav"
    os.rename("leftc/"+filename, "leftc/"+new_name)
    i=i+1
for filename in os.listdir("rightc"):
    new_name="rightc"+"_"+str(i)+".wav"
    os.rename("rightc/"+filename, "rightc/"+new_name)
    i=i+1
for filename in os.listdir("forwardc"):
    new_name="forwardc"+"_"+str(i)+".wav"
    os.rename("forwardc/"+filename, "forwardc/"+new_name)
    i=i+1
for filename in os.listdir("followc"):
    new_name="followc"+"_"+str(i)+".wav"
    os.rename("followc/"+filename, "followc/"+new_name)
    i=i+1