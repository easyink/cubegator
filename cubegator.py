import maya.cmds as cmds

#Cube-gator
#Maya Python character

#create new file every execute
cmds.file(new = True, force = True)

#body of gator
CBody = cmds.polyCube(name = 'body') #create cube body
CBs = CBody[0]
cmds.scale(3,3,3,CBs) #scaled body up
cmds.makeIdentity(CBs,a=1,r=1,s=1)
#head
CHead = cmds.polyCube(name = 'head') #create base head
CHs = CHead[0]
cmds.scale(2,0.85,1.3,CHs) #scale head into shape
cmds.move(2.5,0.25,0,CHs) #move head to front of body
cmds.makeIdentity(CHs,a=1,r=1,s=1,t=1)

cmds.parent(CHead,CBody) #parent head to body

#jaw
CJaw = cmds.polyCube(name = 'jaw') #create jaw
CJs = CJaw[0]
cmds.move(2.4,-0.4,0,CJs) #move jaw
cmds.scale(2,0.15,1.3,CJs) #scale jaw


#Jaw Teeth
TeethSCL = [0.04,0.1,0.04] #scale of teeth
TSvar = -0.228 #teeth y translate var
TZvar = 0.5 #teeth z translate var

#Bottom Teeth
CTooth1 = cmds.polyCone() #create tooth 
CT1s = CTooth1[0] #shape node select var
cmds.move (3.25, TSvar,TZvar, CT1s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT1s) #scaled tooth

CTooth2 = cmds.polyCone() #create tooth 
CT2s = CTooth2[0] #shape node
cmds.move (3.25, TSvar, -TZvar, CT2s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT2s)

CTooth3 = cmds.polyCone() #create tooth 
CT3s = CTooth3[0] #shape node
cmds.move (3.25, TSvar, 0.1, CT3s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT3s)

CTooth4 = cmds.polyCone() #create tooth 
CT4s = CTooth4[0] #shape node
cmds.move (3.25, TSvar, -0.1, CT4s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT4s)

CTooth5 = cmds.polyCone() #create tooth 
CT5s = CTooth5[0] #shape node
cmds.move (3.25, TSvar, -0.3, CT5s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT5s)

CTooth6 = cmds.polyCone() #create tooth 
CT6s = CTooth6[0] #shape node
cmds.move (3.25, TSvar, 0.3, CT6s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT6s)

#side teeth
CTooth7 = cmds.polyCone() #create tooth 
CT7s = CTooth7[0] #shape node
cmds.move (2.2, TSvar, TZvar, CT7s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT7s)

CTooth8 = cmds.polyCone() #create tooth 
CT8s = CTooth8[0] #shape node
cmds.move (2.2, TSvar, -TZvar, CT8s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT8s)

CTooth9 = cmds.polyCone() #create tooth 
CT9s = CTooth9[0] #shape node
cmds.move (2.4, TSvar, TZvar, CT9s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT9s)

CTooth10 = cmds.polyCone() #create tooth 
CT10s = CTooth10[0] #shape node
cmds.move (2.4, TSvar, -TZvar, CT10s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT10s)

CTooth11 = cmds.polyCone() #create tooth 
CT11s = CTooth11[0] #shape node
cmds.move (2.6, TSvar, TZvar, CT11s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT11s)

CTooth12 = cmds.polyCone() #create tooth 
CT12s = CTooth12[0] #shape node
cmds.move (2.6, TSvar, -TZvar, CT12s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT12s)

CTooth13 = cmds.polyCone() #create tooth 
CT13s = CTooth13[0] #shape node
cmds.move (2.8, TSvar, TZvar, CT13s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT13s)

CTooth14 = cmds.polyCone() #create tooth 
CT14s = CTooth14[0] #shape node
cmds.move (2.8, TSvar, -TZvar, CT14s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT14s)

CTooth15 = cmds.polyCone() #create tooth 
CT15s = CTooth15[0] #shape node
cmds.move (3, TSvar, TZvar, CT15s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT15s)

CTooth16 = cmds.polyCone() #create tooth 
CT16s = CTooth16[0] #shape node
cmds.move (3, TSvar, -TZvar, CT16s)
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], CT16s)

CTeeth = [CT1s,CT2s,CT3s,CT4s,CT5s,CT6s,CT7s,CT8s,CT9s,CT10s,CT11s,CT12s,CT13s,CT14s,CT15s,CT16s] #variable representing all teeth
cmds.parent(CTeeth, CJaw) #parenting teeth to the jaw

cmds.rotate(0,0,-9.25,CJs) #rotate jaw after teeth are parented

cmds.makeIdentity(CJs,a=1,r=1,s=1,t=1) #freeze rotation of jaw

#top teeth
TTooth1 = cmds.polyCone() #create tooth 
TT1s = TTooth1[0] #shape node select var
cmds.move (3.25, TSvar,0.4, TT1s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT1s)
cmds.rotate(180,0,0,TT1s)

TTooth2 = cmds.polyCone() #create tooth 
TT2s = TTooth2[0] #shape node select var
cmds.move (3.25, TSvar,0.2, TT2s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT2s)
cmds.rotate(180,0,0,TT2s)

TTooth3 = cmds.polyCone() #create tooth 
TT3s = TTooth3[0] #shape node select var
cmds.move (3.25, TSvar,0, TT3s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT3s)
cmds.rotate(180,0,0,TT3s)

TTooth4 = cmds.polyCone() #create tooth 
TT4s = TTooth4[0] #shape node select var
cmds.move (3.25, TSvar,-0.2, TT4s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT4s)
cmds.rotate(180,0,0,TT4s)

TTooth5 = cmds.polyCone() #create tooth 
TT5s = TTooth5[0] #shape node select var
cmds.move (3.25, TSvar,-0.4, TT5s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT5s)
cmds.rotate(180,0,0,TT5s)
#top side teeth
TTooth6 = cmds.polyCone() #create tooth 
TT6s = TTooth6[0] #shape node select var
cmds.move (3.125, TSvar,TZvar, TT6s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT6s)
cmds.rotate(180,0,0,TT6s)

TTooth7 = cmds.polyCone() #create tooth 
TT7s = TTooth7[0] #shape node select var
cmds.move (2.9, TSvar,TZvar, TT7s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT7s)
cmds.rotate(180,0,0,TT7s)

TTooth8 = cmds.polyCone() #create tooth 
TT8s = TTooth8[0] #shape node select var
cmds.move (2.7, TSvar,TZvar, TT8s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT8s)
cmds.rotate(180,0,0,TT8s)

TTooth9 = cmds.polyCone() #create tooth 
TT9s = TTooth9[0] #shape node select var
cmds.move (2.5, TSvar,TZvar, TT9s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT9s)
cmds.rotate(180,0,0,TT9s)

TTooth10 = cmds.polyCone() #create tooth 
TT10s = TTooth10[0] #shape node select var
cmds.move (2.3, TSvar,TZvar, TT10s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT10s)
cmds.rotate(180,0,0,TT10s)

#side teeth left
TTooth11 = cmds.polyCone() #create tooth 
TT11s = TTooth11[0] #shape node select var
cmds.move (3.125, TSvar,-TZvar, TT11s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT11s)
cmds.rotate(180,0,0,TT11s)

TTooth12 = cmds.polyCone() #create tooth 
TT12s = TTooth12[0] #shape node select var
cmds.move (2.9, TSvar,-TZvar, TT12s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT12s)
cmds.rotate(180,0,0,TT12s)

TTooth13 = cmds.polyCone() #create tooth 
TT13s = TTooth13[0] #shape node select var
cmds.move (2.7, TSvar,-TZvar, TT13s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT13s)
cmds.rotate(180,0,0,TT13s)

TTooth14 = cmds.polyCone() #create tooth 
TT14s = TTooth14[0] #shape node select var
cmds.move (2.5, TSvar,-TZvar, TT14s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT14s)
cmds.rotate(180,0,0,TT14s)

TTooth15 = cmds.polyCone() #create tooth 
TT15s = TTooth15[0] #shape node select var
cmds.move (2.3, TSvar,-TZvar, TT15s) #move tooth
cmds.scale(TeethSCL[0],TeethSCL[1],TeethSCL[2], TT15s)
cmds.rotate(180,0,0,TT15s)
TTeeth = [TT1s,TT2s,TT3s,TT4s,TT5s,TT6s,TT7s,TT8s,TT9s,TT10s,TT11s,TT12s,TT13s,TT14s,TT15s]
cmds.parent(TTeeth, CHead)#parents top teeth to head

cmds.parent(CJaw, CHead) #parents jaw to head
#Eyes
EyeScale = 0.3 #scale of eyes obj
EyeBallScale = 0.1

RightEye = cmds.polyCube(name = 'REye') #creates eye
REs = RightEye[0] #creates var for shape node of eye
cmds.move (1.8,0.825,0.375,REs) #moves eye into position
cmds.scale(EyeScale,EyeScale,EyeScale,REs) #scales eye down
cmds.makeIdentity(REs,a=1,s=1,t=1)

LeftEye = cmds.polyCube(name = 'LEye')
LEs = LeftEye[0]
cmds.move (1.8,0.825,-0.375,LEs)
cmds.scale(EyeScale,EyeScale,EyeScale,LEs)
cmds.makeIdentity(LEs,a=1,s=1,t=1)
#Eyeballs
RightEyeBall = cmds.polySphere(name = 'RBall')
REBs = RightEyeBall[0]
cmds.move (1.95,0.825,0.375,REBs)
cmds.scale(EyeBallScale,EyeBallScale,EyeBallScale,REBs)
cmds.parent(RightEyeBall,RightEye)
cmds.makeIdentity(REBs,a=1,s=1,t=1)

LeftEyeBall = cmds.polySphere(name = 'LBall')
LEBs = LeftEyeBall[0]
cmds.move (1.95,0.825,-0.375,LEBs)
cmds.scale(EyeBallScale,EyeBallScale,EyeBallScale,LEBs)
cmds.parent(LeftEyeBall,LeftEye)
cmds.makeIdentity(LEBs,a=1,s=1,t=1)

Eyes = [REs,LEs]
cmds.parent(Eyes,CHead)

#Shoulders
ShoulderS = 0.5 #Scale of Shoulders X,Y,Z
ArmS = [1.6,0.5,0.5]
EbwS = [0.35,0.3]
WrtS = [1.35,0.35]
HndS = 0.4
FingS = [0.06,0.2]

LeftShoulder = cmds.polyCylinder(name = 'LShoulder')
LACs = LeftShoulder[0]
cmds.move (0,0,-2,LACs)
cmds.rotate (90,0,0,LACs)
cmds.scale (ShoulderS,ShoulderS,ShoulderS,LACs)
cmds.makeIdentity(LACs,a=1,r=1,s=1,t=1)

LeftArm = cmds.polyCube(name = 'LArm')
LAs = LeftArm[0]
cmds.move (-0.5,-0.75,-2,LAs)
cmds.rotate (0,0,60,LAs)
cmds.scale (ArmS[0],ArmS[1],ArmS[2],LAs)
cmds.makeIdentity(LAs,a=1,r=1,s=1,t=1)

LeftElbow = cmds.polyCylinder(name = 'LElbow')
LEs = LeftElbow[0]
cmds.move(-1,-1.5,-2,LEs)
cmds.rotate(90,0,0,LEs)
cmds.scale(EbwS[0],EbwS[1],EbwS[0],LEs)
cmds.makeIdentity(LEs,a=1,r=1,s=1,t=1)

LeftWrist = cmds.polyCube(name = 'LWrist')
LWs = LeftWrist[0]
cmds.move(-0.35,-2,-2,LWs)
cmds.rotate(0,0,-32,LWs)
cmds.scale(WrtS[0],WrtS[1],WrtS[1],LWs)
cmds.makeIdentity(LWs,a=1,r=1,s=1,t=1)

LeftHand = cmds.polySphere(name = 'LHand')
LHs = LeftHand[0]
cmds.move(0.15,-2.3,-2,LHs)
cmds.rotate(0,0,-32,LHs)
cmds.scale(HndS,HndS,HndS,LHs)
cmds.makeIdentity(LHs,a=1,r=1,s=1,t=1)

LeftFinger1 = cmds.polyCylinder(name = 'LFinger1')
LF1s = LeftFinger1[0]
cmds.move(0.4,-2.5,-2.3,LF1s)
cmds.rotate(-65,-40,-80,LF1s)
cmds.scale(FingS[0],FingS[1],FingS[0],LF1s)

LeftFinger2 = cmds.polyCylinder(name = 'LFinger2')
LF2s = LeftFinger2[0]
cmds.move(0.55,-2.25,-2,LF2s)
cmds.rotate(0,-3,-80,LF2s)
cmds.scale(FingS[0],FingS[1],FingS[0],LF2s)

LeftFinger3 = cmds.polyCylinder(name = 'LFinger2')
LF3s = LeftFinger3[0]
cmds.move(0.5,-2.5,-1.8,LF3s)
cmds.rotate(16,-14,-117,LF3s)
cmds.scale(FingS[0],FingS[1],FingS[0],LF3s)

LeftFingers = [LF1s,LF2s,LF3s] #defining fingers
cmds.makeIdentity(LeftFingers,a=1,r=1,s=1,t=1)

#Left Arm Parent commands
cmds.parent(LeftFingers,LeftHand)
cmds.parent(LeftHand,LeftWrist)
cmds.parent(LeftWrist,LeftElbow)
cmds.parent(LeftElbow,LeftArm)
cmds.parent(LeftArm,LeftShoulder)
#Right Arm
RightShoulder = cmds.polyCylinder(name = 'RShoulder')
RACs = RightShoulder[0]
cmds.move (0,0,2,RACs)
cmds.rotate (90,0,0,RACs)
cmds.scale (ShoulderS,ShoulderS,ShoulderS,RACs)
cmds.makeIdentity(RACs,a=1,r=1,s=1,t=1)
RightArm = cmds.polyCube(name = 'RArm')

RAs = RightArm[0]
cmds.move (-0.5,-0.75,2,RAs)
cmds.rotate (0,0,60,RAs)
cmds.scale (ArmS[0],ArmS[1],ArmS[2],RAs)
cmds.makeIdentity(RAs,a=1,r=1,s=1,t=1)

RightElbow = cmds.polyCylinder(name = 'RElbow')
REs = RightElbow[0]
cmds.move(-1,-1.5,2,REs)
cmds.rotate(90,0,0,REs)
cmds.scale(EbwS[0],EbwS[1],EbwS[0],REs)
cmds.makeIdentity(REs,a=1,r=1,s=1,t=1)

RightWrist = cmds.polyCube(name = 'RWrist')
RWs = RightWrist[0]
cmds.move(-0.35,-2,2,RWs)
cmds.rotate(0,0,-32,RWs)
cmds.scale(WrtS[0],WrtS[1],WrtS[1],RWs)
cmds.makeIdentity(RWs,a=1,r=1,s=1,t=1)

RightHand = cmds.polySphere(name = 'RHand')
RHs = RightHand[0]
cmds.move(0.15,-2.3,2,RHs)
cmds.rotate(0,0,-32,RHs)
cmds.scale(HndS,HndS,HndS,RHs)
cmds.makeIdentity(RHs,a=1,r=1,s=1,t=1)

RightFinger1 = cmds.polyCylinder(name = 'RFinger1')
RF1s = RightFinger1[0]
cmds.move(0.4,-2.5,2.3,RF1s)
cmds.rotate(65,40,-80,RF1s)
cmds.scale(FingS[0],FingS[1],FingS[0],RF1s)

RightFinger2 = cmds.polyCylinder(name = 'RFinger2')
RF2s = RightFinger2[0]
cmds.move(0.55,-2.25,2,RF2s)
cmds.rotate(0,3,-80,RF2s)
cmds.scale(FingS[0],FingS[1],FingS[0],RF2s)

RightFinger3 = cmds.polyCylinder(name = 'RFinger2')
RF3s = RightFinger3[0]
cmds.move(0.5,-2.5,1.8,RF3s)
cmds.rotate(-16,14,-117,RF3s)
cmds.scale(FingS[0],FingS[1],FingS[0],RF3s)

RightFingers = [RF1s,RF2s,RF3s]
#Right Arm Parent Commands
cmds.parent(RightFingers,RightHand)
cmds.parent(RightHand,RightWrist)
cmds.parent(RightWrist,RightElbow)
cmds.parent(RightElbow,RightArm)
cmds.parent(RightArm,RightShoulder)
#Parenting Arms to Body
cmds.parent(RightShoulder,CBody)
cmds.parent(LeftShoulder,CBody)
#Lower Body
LowerTorso = cmds.polyCube(name = 'LTorso')
LTs = LowerTorso[0]
cmds.move(-1.3,-1.1,0,LTs)
cmds.rotate(0,0,33,LTs)
cmds.scale(2,2,2,LTs)
cmds.makeIdentity(LTs,a=1,r=1,s=1,t=1)
#Lower Gut
Gut = cmds.polyCube(name = 'Gut')
Gs = Gut[0]
cmds.move(-2.3,-2.3,0,Gs)
cmds.rotate(0,0,-25,Gs)
cmds.scale(1.6,1.8,1.5,Gs)
cmds.makeIdentity(Gs,a=1,r=1,s=1,t=1)

Butt = cmds.polyCube(name = 'Butt') #heh, buttocks
Bs = Butt[0]
cmds.move(-2.5,-3.15,0,Bs)
cmds.scale(2,0.8,2,Bs)

#Left Leg
LeftHip = cmds.polyCylinder(name = 'LeftHip')
LHPs = LeftHip[0]
cmds.move(-2.5,-3.1,-1.1,LHPs)
cmds.rotate(90,0,0,LHPs)
cmds.scale(0.6,0.25,0.6,LHPs)
cmds.makeIdentity(LHPs,a=1,r=1,s=1,t=1)

LeftThigh = cmds.polyCube(name = 'LeftThigh')
LTGHs = LeftThigh[0]
cmds.move(-2.15,-4,-1.15,LTGHs)
cmds.rotate(0,0,20,LTGHs)
cmds.scale(0.75,1.4,0.25,LTGHs)
cmds.makeIdentity(LTGHs,a=1,r=1,s=1,t=1)

LeftFoot = cmds.polyCube(name = 'LeftFoot')
LFTs = LeftFoot[0]
cmds.move(-1.75,-4.6,-1.15,LFTs)
cmds.scale(1.74,0.5,1,LFTs)
cmds.makeIdentity(LFTs,a=1,r=1,s=1,t=1)

cmds.parent(LeftFoot,LeftThigh)
cmds.parent(LeftThigh,LeftHip)
cmds.parent(LeftHip,Butt)

#Right Leg
RightHip = cmds.polyCylinder(name = 'RightHip')
RHPs = RightHip[0]
cmds.move(-2.5,-3.1,1.1,RHPs)
cmds.rotate(90,0,0,RHPs)
cmds.scale(0.6,0.25,0.6,RHPs)
cmds.makeIdentity(RHPs,a=1,r=1,s=1,t=1)

RightThigh = cmds.polyCube(name = 'RightThigh')
RTGHs = RightThigh[0]
cmds.move(-2.15,-4,1.15,RTGHs)
cmds.rotate(0,0,20,RTGHs)
cmds.scale(0.75,1.4,0.25,RTGHs)
cmds.makeIdentity(RTGHs,a=1,r=1,s=1,t=1)

RightFoot = cmds.polyCube(name = 'RightFoot')
RFTs = RightFoot[0]
cmds.move(-1.75,-4.6,1.15,RFTs)
cmds.scale(1.74,0.5,1,RFTs)
cmds.makeIdentity(RFTs,a=1,r=1,s=1,t=1)

cmds.parent(RightFoot,RightThigh)
cmds.parent(RightThigh,RightHip)
cmds.parent(RightHip,Butt)

#Tail
Tail1 = cmds.polyCone(name = 'Tail_1')
TL1s = Tail1[0]
cmds.move(-3.6,-3.6,0,TL1s)
cmds.rotate(0,0,132,TL1s)
cmds.scale(0.6,0.78,0.65,TL1s)
cmds.makeIdentity(TL1s,a=1,r=1,s=1,t=1)

Tail2 = cmds.polyCone(name = 'Tail_2')
TL2s = Tail2[0]
cmds.move(-4,-3.85,0,TL2s)
cmds.rotate(0,0,127,TL2s)
cmds.scale(0.6,0.65,0.6,TL2s)
cmds.makeIdentity(TL2s,a=1,r=1,s=1,t=1)

Tail3 = cmds.polyCone(name = 'Tail_3')
TL3s = Tail3[0]
cmds.move(-4.6,-4,0,TL3s)
cmds.rotate(0,0,116,TL3s)
cmds.scale(0.5,0.73,0.5,TL3s)
cmds.makeIdentity(TL3s,a=1,r=1,s=1,t=1)

Tail4 = cmds.polyCone(name = 'Tail_4')
TL4s = Tail4[0]
cmds.move(-5.3,-4.2,0,TL4s)
cmds.rotate(0,0,110,TL4s)
cmds.scale(0.4,0.8,0.4,TL4s)
cmds.makeIdentity(TL4s,a=1,r=1,s=1,t=1)

cmds.parent(Tail4,Tail3)
cmds.parent(Tail3,Tail2)
cmds.parent(Tail2,Tail1)
cmds.parent(Tail1,Butt)

#final parents
cmds.parent(CBody,LowerTorso)
cmds.parent(LowerTorso,Gut)
cmds.parent(Gut,Butt)

cmds.move(0,1.75,0,Bs)#moves entire body above ground
cmds.makeIdentity(Bs,a=1,s=1,t=1) #sets attributes of butt scale to 1,1,1 so legs can rotate properly

cmds.group(Butt,name = 'Gator') #groups Butt aka entire model and names it gator

#animation time
BSway = 5 #butt sway value
BUp = 0.125
BUMax = 0.45

ArmSwayUp = 0.35 #arm sway up value
ArmSwayDown = -0.5 #arm sway down value
ArmRotateBack = -20
ArmRotateFront = 75

HeadLeft = 0.5 #head swing left value
HeadRight = -0.5 #head swing right value
HeadRotateLeft = 15 #headrotate left value
HeadRotateRight = -15 #headrotate right value

LTorsoSwayUp = 10 #lower torso sway up value
LTorsoSwayDown = -0.5 #lower torso sway down value

BodyDown = -1 #body vertical sway down value
BodyUp = 0 #gbody vertical rest value

FootRotateLift = 20 #foot rotate value
FootRotateDrag = -10 #foot drag value
FootRotateFlat = 10

TailTurn = 15

s00=1 #time is frame 1
cmds.setKeyframe(Bs+".rx",t=s00,v=0)#butt keyframe
cmds.setKeyframe(Bs+".ty",t=s00,v=0)#butt move up 

cmds.setKeyframe(CBs+".ty",t=s00,v=0)#body keyframe

cmds.setKeyframe(RHPs+".rz",t=s00,v=0)#right hip leg
cmds.setKeyframe(LHPs+".rz",t=s00,v=0)#left hip leg

cmds.setKeyframe(RACs+".ty",t=s00,v=0)#right shoulder
cmds.setKeyframe(LACs+".ty",t=s00,v=0)#left shoulder

cmds.setKeyframe(RACs+".rz",t=s00,v=0)#right shoulder rotate
cmds.setKeyframe(LACs+".rz",t=s00,v=0)#left shoulder

cmds.setKeyframe(CHs+".tz",t=s00,v=0)#head z move
cmds.setKeyframe(CHs+".rx",t=s00,v=0)#head z rotate

cmds.setKeyframe(LTs+".rz",t=s00,v=0) #lower torso rotate

cmds.setKeyframe(RFTs+".rz",t=s00,v=0)#right foot rotate
cmds.setKeyframe(LFTs+".rz",t=s00,v=0)#left foot rotate

cmds.setKeyframe(TL1s+".ry",t=s00,v=0)#tail rotates
cmds.setKeyframe(TL2s+".ry",t=s00,v=0)#tail2 rotates
cmds.setKeyframe(TL3s+".ry",t=s00,v=0)#tail3 rotates
cmds.setKeyframe(TL4s+".ry",t=s00,v=0)#tail4 rotates

s025=6
cmds.setKeyframe(Bs+".ty",t=s025,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s025,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s025,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s025,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s025,v=FootRotateFlat)

s05=12 #time is frame 12 aka half a second in
cmds.setKeyframe(Bs+".rx",t=s05,v=BSway)
cmds.setKeyframe(Bs+".ty",t=s05,v=BUMax)

cmds.setKeyframe(CBs+".ty",t=s05,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s05,v=-20)
cmds.setKeyframe(LHPs+".rz",t=s05,v=20)

cmds.setKeyframe(RACs+".ty",t=s05,v=ArmSwayDown)
cmds.setKeyframe(RACs+".rz",t=s05,v=ArmRotateBack)
cmds.setKeyframe(LACs+".ty",t=s05,v=ArmSwayUp)
cmds.setKeyframe(LACs+".rz",t=s05,v=ArmRotateFront)

cmds.setKeyframe(CHs+".tz",t=s05,v=HeadLeft)
cmds.setKeyframe(CHs+".rx",t=s05,v=HeadRotateLeft)

cmds.setKeyframe(LTs+".rz",t=s05,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s05,v=FootRotateDrag)
cmds.setKeyframe(LFTs+".rz",t=s05,v=FootRotateLift)

cmds.setKeyframe(TL1s+".ry",t=s05,v=TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s05,v=TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s05,v=TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s05,v=TailTurn)

s075=18
cmds.setKeyframe(Bs+".ty",t=s075,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s075,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s075,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s075,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s075,v=FootRotateFlat)

s10=24 #sNUMBER is time = frame number
cmds.setKeyframe(Bs+".rx",t=s10,v=-BSway)
cmds.setKeyframe(Bs+".ty",t=s10,v=BUMax)

cmds.setKeyframe(CBs+".ty",t=s10,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s10,v=20)
cmds.setKeyframe(LHPs+".rz",t=s10,v=-20)

cmds.setKeyframe(RACs+".ty",t=s10,v=ArmSwayUp)
cmds.setKeyframe(RACs+".rz",t=s10,v=ArmRotateFront)
cmds.setKeyframe(LACs+".ty",t=s10,v=ArmSwayDown)
cmds.setKeyframe(LACs+".rz",t=s10,v=ArmRotateBack)

cmds.setKeyframe(CHs+".tz",t=s10,v=HeadRight)
cmds.setKeyframe(CHs+".rx",t=s10,v=HeadRotateRight)

cmds.setKeyframe(LTs+".rz",t=s10,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s10,v=FootRotateLift)
cmds.setKeyframe(LFTs+".rz",t=s10,v=FootRotateDrag)

cmds.setKeyframe(TL1s+".ry",t=s10,v=-TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s10,v=-TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s10,v=-TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s10,v=-TailTurn)

s125=30
cmds.setKeyframe(Bs+".ty",t=s125,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s125,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s125,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s125,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s125,v=FootRotateFlat)

s15=36
cmds.setKeyframe(Bs+".ty",t=s15,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s15,v=BSway)

cmds.setKeyframe(CBs+".ty",t=s15,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s15,v=-20)
cmds.setKeyframe(LHPs+".rz",t=s15,v=20)

cmds.setKeyframe(RACs+".ty",t=s15,v=ArmSwayDown)
cmds.setKeyframe(RACs+".rz",t=s15,v=ArmRotateBack)
cmds.setKeyframe(LACs+".ty",t=s15,v=ArmSwayUp)
cmds.setKeyframe(LACs+".rz",t=s15,v=ArmRotateFront)

cmds.setKeyframe(CHs+".tz",t=s15,v=HeadLeft)
cmds.setKeyframe(CHs+".rx",t=s15,v=HeadRotateLeft)

cmds.setKeyframe(LTs+".rz",t=s15,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s15,v=FootRotateDrag)
cmds.setKeyframe(LFTs+".rz",t=s15,v=FootRotateLift)

cmds.setKeyframe(TL1s+".ry",t=s15,v=TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s15,v=TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s15,v=TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s15,v=TailTurn)

s175=42
cmds.setKeyframe(Bs+".ty",t=s175,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s175,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s175,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s175,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s175,v=FootRotateFlat)

s20=48
cmds.setKeyframe(Bs+".ty",t=s20,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s20,v=-BSway)

cmds.setKeyframe(CBs+".ty",t=s20,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s20,v=20)
cmds.setKeyframe(LHPs+".rz",t=s20,v=-20)

cmds.setKeyframe(RACs+".ty",t=s20,v=ArmSwayUp)
cmds.setKeyframe(RACs+".rz",t=s20,v=ArmRotateFront)
cmds.setKeyframe(LACs+".ty",t=s20,v=ArmSwayDown)
cmds.setKeyframe(LACs+".rz",t=s20,v=ArmRotateBack)

cmds.setKeyframe(CHs+".tz",t=s20,v=HeadRight)
cmds.setKeyframe(CHs+".rx",t=s20,v=HeadRotateRight)

cmds.setKeyframe(LTs+".rz",t=s20,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s20,v=FootRotateLift)
cmds.setKeyframe(LFTs+".rz",t=s20,v=FootRotateDrag)

cmds.setKeyframe(TL1s+".ry",t=s20,v=-TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s20,v=-TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s20,v=-TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s20,v=-TailTurn)

s225=54
cmds.setKeyframe(Bs+".ty",t=s225,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s225,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s225,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s225,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s225,v=FootRotateFlat)

s25=60
cmds.setKeyframe(Bs+".ty",t=s25,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s25,v=BSway)

cmds.setKeyframe(CBs+".ty",t=s25,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s25,v=-20)
cmds.setKeyframe(LHPs+".rz",t=s25,v=20)

cmds.setKeyframe(RACs+".ty",t=s25,v=ArmSwayDown)
cmds.setKeyframe(RACs+".rz",t=s25,v=ArmRotateBack)
cmds.setKeyframe(LACs+".ty",t=s25,v=ArmSwayUp)
cmds.setKeyframe(LACs+".rz",t=s25,v=ArmRotateFront)

cmds.setKeyframe(CHs+".tz",t=s25,v=HeadLeft)
cmds.setKeyframe(CHs+".rx",t=s25,v=HeadRotateLeft)

cmds.setKeyframe(LTs+".rz",t=s25,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s25,v=FootRotateDrag)
cmds.setKeyframe(LFTs+".rz",t=s05,v=FootRotateLift)

cmds.setKeyframe(TL1s+".ry",t=s25,v=TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s25,v=TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s25,v=TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s25,v=TailTurn)

s275=66
cmds.setKeyframe(Bs+".ty",t=s275,v=BUp)

cmds.setKeyframe(LTs+".rz",t=s275,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s275,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s275,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s275,v=FootRotateFlat)

s30=72
cmds.setKeyframe(Bs+".ty",t=s30,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s30,v=-BSway)

cmds.setKeyframe(CBs+".ty",t=s30,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s30,v=20)
cmds.setKeyframe(LHPs+".rz",t=s30,v=-20)

cmds.setKeyframe(RACs+".ty",t=s30,v=ArmSwayUp)
cmds.setKeyframe(RACs+".rz",t=s30,v=ArmRotateFront)
cmds.setKeyframe(LACs+".ty",t=s30,v=ArmSwayDown)
cmds.setKeyframe(LACs+".rz",t=s30,v=ArmRotateBack)

cmds.setKeyframe(CHs+".tz",t=s30,v=HeadRight)
cmds.setKeyframe(CHs+".rx",t=s30,v=HeadRotateRight)

cmds.setKeyframe(LTs+".rz",t=s30,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s30,v=FootRotateLift)
cmds.setKeyframe(LFTs+".rz",t=s30,v=FootRotateDrag)

cmds.setKeyframe(TL1s+".ry",t=s30,v=-TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s30,v=-TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s30,v=-TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s30,v=-TailTurn)

s325=78
cmds.setKeyframe(Bs+".ty",t=s325,v=BUp)
cmds.setKeyframe(LTs+".rz",t=s325,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s325,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s325,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s325,v=FootRotateFlat)

s35=84
cmds.setKeyframe(Bs+".ty",t=s35,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s35,v=BSway)

cmds.setKeyframe(CBs+".ty",t=s35,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s35,v=-20)
cmds.setKeyframe(LHPs+".rz",t=s35,v=20)

cmds.setKeyframe(RACs+".ty",t=s35,v=ArmSwayDown)
cmds.setKeyframe(RACs+".rz",t=s35,v=ArmRotateBack)
cmds.setKeyframe(LACs+".ty",t=s35,v=ArmSwayUp)
cmds.setKeyframe(LACs+".rz",t=s35,v=ArmRotateFront)

cmds.setKeyframe(CHs+".tz",t=s35,v=HeadLeft)
cmds.setKeyframe(CHs+".rx",t=s35,v=HeadRotateLeft)

cmds.setKeyframe(LTs+".rz",t=s35,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s35,v=FootRotateDrag)
cmds.setKeyframe(LFTs+".rz",t=s35,v=FootRotateLift)

cmds.setKeyframe(TL1s+".ry",t=s35,v=TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s35,v=TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s35,v=TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s35,v=TailTurn)

s375=90
cmds.setKeyframe(Bs+".ty",t=s375,v=BUp)
cmds.setKeyframe(LTs+".rz",t=s375,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s375,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s375,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s375,v=FootRotateFlat)

s40=96
cmds.setKeyframe(Bs+".ty",t=s40,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s40,v=-BSway)

cmds.setKeyframe(CBs+".ty",t=s40,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s40,v=20)
cmds.setKeyframe(LHPs+".rz",t=s40,v=-20)

cmds.setKeyframe(RACs+".ty",t=s40,v=ArmSwayUp)
cmds.setKeyframe(RACs+".rz",t=s40,v=ArmRotateFront)
cmds.setKeyframe(LACs+".ty",t=s40,v=ArmSwayDown)
cmds.setKeyframe(LACs+".rz",t=s40,v=ArmRotateBack)

cmds.setKeyframe(CHs+".tz",t=s40,v=HeadRight)
cmds.setKeyframe(CHs+".rx",t=s40,v=HeadRotateRight)

cmds.setKeyframe(LTs+".rz",t=s40,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s40,v=FootRotateLift)
cmds.setKeyframe(LFTs+".rz",t=s40,v=FootRotateDrag)

cmds.setKeyframe(TL1s+".ry",t=s40,v=-TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s40,v=-TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s40,v=-TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s40,v=-TailTurn)

s425=102
cmds.setKeyframe(Bs+".ty",t=s425,v=BUp)
cmds.setKeyframe(LTs+".rz",t=s425,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s425,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s425,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s425,v=FootRotateFlat)

s45=108
cmds.setKeyframe(Bs+".ty",t=s45,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s45,v=BSway)

cmds.setKeyframe(CBs+".ty",t=s45,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s45,v=-20)
cmds.setKeyframe(LHPs+".rz",t=s45,v=20)

cmds.setKeyframe(RACs+".ty",t=s45,v=ArmSwayDown)
cmds.setKeyframe(RACs+".rz",t=s45,v=ArmRotateBack)
cmds.setKeyframe(LACs+".ty",t=s45,v=ArmSwayUp)
cmds.setKeyframe(LACs+".rz",t=s45,v=ArmRotateFront)

cmds.setKeyframe(CHs+".tz",t=s45,v=HeadLeft)
cmds.setKeyframe(CHs+".rx",t=s45,v=HeadRotateLeft)

cmds.setKeyframe(LTs+".rz",t=s45,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s45,v=FootRotateDrag)
cmds.setKeyframe(LFTs+".rz",t=s45,v=FootRotateLift)

cmds.setKeyframe(TL1s+".ry",t=s45,v=TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s45,v=TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s45,v=TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s45,v=TailTurn)

s475=114
cmds.setKeyframe(Bs+".ty",t=s475,v=BUp)
cmds.setKeyframe(LTs+".rz",t=s475,v=LTorsoSwayUp)

cmds.setKeyframe(CBs+".ty",t=s475,v=BodyDown)

cmds.setKeyframe(RFTs+".rz",t=s475,v=FootRotateFlat)
cmds.setKeyframe(LFTs+".rz",t=s475,v=FootRotateFlat)

s50=120
cmds.setKeyframe(Bs+".ty",t=s50,v=BUMax)
cmds.setKeyframe(Bs+".rx",t=s50,v=-BSway)

cmds.setKeyframe(CBs+".ty",t=s50,v=BodyUp)

cmds.setKeyframe(RHPs+".rz",t=s50,v=20)
cmds.setKeyframe(LHPs+".rz",t=s50,v=-20)

cmds.setKeyframe(RACs+".ty",t=s50,v=ArmSwayUp)
cmds.setKeyframe(RACs+".rz",t=s50,v=ArmRotateFront)
cmds.setKeyframe(LACs+".ty",t=s50,v=ArmSwayDown)
cmds.setKeyframe(LACs+".rz",t=s50,v=ArmRotateBack)

cmds.setKeyframe(CHs+".tz",t=s50,v=HeadRight)
cmds.setKeyframe(CHs+".rx",t=s50,v=HeadRotateRight)

cmds.setKeyframe(LTs+".rz",t=s50,v=LTorsoSwayDown)

cmds.setKeyframe(RFTs+".rz",t=s50,v=FootRotateLift)
cmds.setKeyframe(LFTs+".rz",t=s50,v=FootRotateDrag)

cmds.setKeyframe(TL1s+".ry",t=s50,v=-TailTurn)
cmds.setKeyframe(TL2s+".ry",t=s50,v=-TailTurn)
cmds.setKeyframe(TL3s+".ry",t=s50,v=-TailTurn)
cmds.setKeyframe(TL4s+".ry",t=s50,v=-TailTurn)

s55=132 #ending keyframe, set everything back to 0 so it can loop
cmds.setKeyframe(Bs+".rx",t=s55,v=0)
cmds.setKeyframe(Bs+".ty",t=s55,v=0)

cmds.setKeyframe(CBs+".ty",t=s55,v=0)

cmds.setKeyframe(RHPs+".rz",t=s55,v=0)
cmds.setKeyframe(LHPs+".rz",t=s55,v=0)

cmds.setKeyframe(RACs+".ty",t=s55,v=0)
cmds.setKeyframe(RACs+".rz",t=s55,v=0)
cmds.setKeyframe(LACs+".ty",t=s55,v=0)
cmds.setKeyframe(LACs+".rz",t=s55,v=0)

cmds.setKeyframe(CHs+".tz",t=s55,v=0)
cmds.setKeyframe(CHs+".rx",t=s55,v=0)

cmds.setKeyframe(LTs+".rz",t=s55,v=0)

cmds.setKeyframe(RFTs+".rz",t=s55,v=0)
cmds.setKeyframe(LFTs+".rz",t=s55,v=0)

cmds.setKeyframe(TL1s+".ry",t=s55,v=0)
cmds.setKeyframe(TL2s+".ry",t=s55,v=0)
cmds.setKeyframe(TL3s+".ry",t=s55,v=0)
cmds.setKeyframe(TL4s+".ry",t=s55,v=0)
