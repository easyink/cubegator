import maya.cmds as cmds

#cubegator as a function
#by dylan lau

cmds.file(new = 1, force = 1)#makes a new file every execution

def setShapeLook(objname,scale,position,rotation,shapeobj,parent): #sets object shape. input takes Name,Scale,Position,Rotation,what shape it is, and who is it's parent.
	if (shapeobj is "Cube"): # if it is a cube, it makes a cube
		obj = cmds.polyCube(name = objname)[0]
	elif (shapeobj is "Sphere"):
		obj = cmds.polySphere(name = objname)[0]
	elif (shapeobj is "Cylinder"):
		obj = cmds.polyCylinder(name = objname)[0]
	elif (shapeobj is "Cone"):
		obj = cmds.polyCone(name = objname)[0]
	cmds.scale(scale[0],scale[1],scale[2],obj) #sets scale
	cmds.move(position[0],position[1],position[2],obj) #sets position
	if(rotation is "none"): #if there is rotation or not
		pass
	else:
		cmds.rotate(rotation[0],rotation[1],rotation[2],obj) #sets rotation
	cmds.makeIdentity(obj,a=1,r=1,s=1,t=1) #freezes all transforms
	if (parent is "none"): #if there is a parent or not
		pass
	else:
		cmds.parent(obj,parent) #sets parent
	print "Set Look of " + objname + ", which is a " + shapeobj + ", and parented it to " + parent + "." #writes a message of what it did.

def setTeeth(amount,scale,position,offset,roof=True): #function that sets the teeth.
	for i in range(amount): # a loop that will make teeth based on how many there is (amount)
		tooth = cmds.polyCone(name = 'Teeth1')[0] #sets tooth to cone shape
		cmds.scale(scale[0],scale[1],scale[2],tooth) #sets scale
		if (roof): #if roof is true, it will execute this block
			cmds.rotate(180,0,0,tooth) #flips tooth over 
			if(amount is TopFrontTeethAmount):# if it is top and front of mouth
				cmds.move(position[0],position[1],position[2]-(offset*i),tooth) #simple math of offsetting each tooth by number of teeth chosen
			elif(amount is TopSideTeethAmount): #if tooth is side
				cmds.move(position[0] - offset*(i/2), position[1], position[2]*((-1)**i), tooth)
				#the i is also used as an exponent to make the second one of every pair mirror the first
				#also flips every other tooth
			cmds.parent(tooth,"Head") #parents tooth to head
			print "Made a top tooth number." #prints message
		else:
			if (amount is BottomFrontTeethAmount):
				cmds.move(position[0],position[1],position[2]-(offset*i),tooth)	
			elif(amount is BottomSideTeethAmount):
				cmds.move(position[0] + offset*(i/2), position[1], position[2]*((-1)**i), tooth)
			cmds.parent(tooth,"Jaw")
			print "Made a bottom tooth."
def setRotate( objname , rotation ): #seperate rotation function for jaw
	cmds.rotate(rotation[0],rotation[1],rotation[2],objname)
	print "rotated "+ objname + " by " + str(rotation) + " degrees."

def animateObject(obj,section,time,value):
	cmds.setKeyframe(obj+section,t=time,v=value)
	print "Animated " + obj + "'s " + section + " at " + str(time) + " seconds."
#variables

#SCL is SCALE
#ROT is ROTATION
#POS is POSITION

ChestSCL = (3,3,3) #chest scale
ChestPOS = (0,0,0) #chest position

HeadSCL = (2.0,0.85,1.3) #head scale
HeadPOS = (2.5,0.25,0) #head position

JawSCL = (2.0,0.15,1.3) #jaw scale
JawPOS = (2.4,-0.4,0)
JawROT = (0,0,-9.25)

EyeSocketSCL = (0.3,0.3,0.3)
EyeSocketPOS = (1.8,0.825,0.375)
EyeBallSCL = (0.1)
EyeBallPOS = 1.95

TeethSCL = (0.04,0.1,0.04)
TeethYZ = (-0.228,0.5) # positions of just Y and Z of each tooth
TeethOffset = 0.2 #spacing between each tooth

BottomFrontTeethAmount = 6 #number of teeth for bottom front
BottomFrontTeethPOS = (3.25,TeethYZ[0],TeethYZ[1])

BottomSideTeethAmount = 10
BottomSideTeethPOS = (2.25,TeethYZ[0],TeethYZ[1])

TopFrontTeethAmount = 5
TopFrontTeethPOS = (3.25,TeethYZ[0],0.4)

TopSideTeethAmount = 10
TopSideTeethPOS = 3.15,TeethYZ[0],TeethYZ[1]

ShoulderSCL = 0.5 #Scale of Shoulders X,Y,Z
ShoulderPOS = (0, 0, -2)
ShoulderROT = (90,0,0)

ArmSCL = (1.6,0.5,0.5)
ArmPOS = (-0.5,-0.75,-2)
ArmROT = (0,0,60)

EbwSCL = (0.35,0.3,0.35)
EbwPOS = (-1,-1.5,-2)
EbwROT = (90,0,0)

WristSCL = (1.35,0.35,0.35)
WristPOS = (-0.35,-2,-2)
WristROT = (0,0,-32)

HandSCL = (0.4,0.4,0.4)
HandPOS = (0.15,-2.3,-2)
HandROT = (0,0,-32)

FingerSCL = (0.06,0.2,0.06)
Finger1POS = (0.4,-2.5,-2.3)
Finger1ROT = (-65,-40,-80)
Finger2POS = (0.55,-2.25,-2)
Finger2ROT = (0,-3,-80)
Finger3POS = (0.5,-2.5,-1.8)
Finger3ROT = (16,-14,-117)

TorsoPOS = (-1.3,-1.1,0)
TorsoROT = (0,0,33)
TorsoSCL = (2,2,2)

GutPOS = (-2.3,-2.3,0)
GutROT = (0,0,-25)
GutSCL = (1.6,1.8,1.5)

ButtPOS = (-2.5,-3.15,0)
ButtSCL = (2,0.8,2)

HipSCL = (0.6,0.25,0.6)
HipPOS = (-2.5,-3.1,-1.1)
HipROT = (90,0,0)

ThighSCL = (0.75,1.4,0.25)
ThighPOS = (-2.15,-4,1.15)
ThighROT = (0,0,20)

FootSCL = (1.74,0.5,1)
FootPOS = (-1.75,-4.6,1.15)

Tail1SCL = (0.6,0.78,0.65)
Tail1POS = (-3.6,-3.6,0)
Tail1ROT = (0,0,132)


Tail2SCL = (0.6,0.65,0.6)
Tail2POS = (-4,-3.85,0)
Tail2ROT = (0,0,127)


Tail3SCL = (0.5,0.73,0.5)
Tail3POS = (-4.6,-4,0)
Tail3ROT = (0,0,116)

Tail4SCL = (0.4,0.8,0.4)
Tail4POS = (-5.3,-4.2,0)
Tail4ROT = (0,0,110)

s00=1
s025=6
s05=12
s075=18
s10=24
s125=30
s15=36
s175=42
s20=48
s225=54
s25=60
s275=66
s30=72
s325=78
s35=84
s375=90
s40=96
s425=102
s45=108
s475=114
s50=120
s55=132
#using the functions
setShapeLook("Butt",(ButtSCL[0],ButtSCL[1],ButtSCL[2]),(ButtPOS[0],ButtPOS[1],ButtPOS[2]),"none","Cube","none")
setShapeLook("Gut",(GutSCL[0],GutSCL[1],GutSCL[2]),(GutPOS[0],GutPOS[1],GutPOS[2]),(GutROT[0],GutROT[1],GutROT[2]),"Cube","Butt")
setShapeLook("Torso",(TorsoSCL[0],TorsoSCL[1],TorsoSCL[2]),(TorsoPOS[0],TorsoPOS[1],TorsoPOS[2]),(TorsoROT[0],TorsoROT[1],TorsoROT[2]),"Cube","Gut")
setShapeLook("Chest",(ChestSCL[0],ChestSCL[1],ChestSCL[2]),(ChestPOS[0],ChestPOS[1],ChestPOS[2]),"none","Cube","Torso")
setShapeLook("Head",(HeadSCL[0],HeadSCL[1],HeadSCL[2]),(HeadPOS[0],HeadPOS[1],HeadPOS[2]),"none","Cube","Chest")
setShapeLook("Jaw",(JawSCL[0],JawSCL[1],JawSCL[2]),(JawPOS[0],JawPOS[1],JawPOS[2]),"none","Cube", "Head")
setShapeLook("RightEyeSocket",(EyeSocketSCL[0],EyeSocketSCL[1],EyeSocketSCL[2]),(EyeSocketPOS[0],EyeSocketPOS[1],EyeSocketPOS[2]),"none","Cube","Head")
setShapeLook("LeftEyeSocket",(EyeSocketSCL[0],EyeSocketSCL[1],EyeSocketSCL[2]),(EyeSocketPOS[0],EyeSocketPOS[1],-EyeSocketPOS[2]),"none","Cube","Head")
setShapeLook("RightEye", (EyeBallSCL,EyeBallSCL,EyeBallSCL), (EyeBallPOS,EyeSocketPOS[1],EyeSocketPOS[2]),"none", "Sphere","RightEyeSocket")
setShapeLook("LeftEye", (EyeBallSCL,EyeBallSCL,EyeBallSCL), (EyeBallPOS,EyeSocketPOS[1],-EyeSocketPOS[2]),"none", "Sphere","LeftEyeSocket")

setShapeLook("LeftShoulder",(ShoulderSCL,ShoulderSCL,ShoulderSCL),(ShoulderPOS[0],ShoulderPOS[1],ShoulderPOS[2]),(ShoulderROT[0],ShoulderROT[1],ShoulderROT[2]),"Cylinder", "Chest")
setShapeLook("RightShoulder",(ShoulderSCL,ShoulderSCL,ShoulderSCL),(ShoulderPOS[0],ShoulderPOS[1],-ShoulderPOS[2]),(ShoulderROT[0],ShoulderROT[1],ShoulderROT[2]),"Cylinder", "Chest")
setShapeLook("LeftArm",(ArmSCL[0],ArmSCL[1],ArmSCL[2]),(ArmPOS[0],ArmPOS[1],ArmPOS[2]),(ArmROT[0],ArmROT[1],ArmROT[2]),"Cube","LeftShoulder")
setShapeLook("RightArm",(ArmSCL[0],ArmSCL[1],ArmSCL[2]),(ArmPOS[0],ArmPOS[1],-ArmPOS[2]),(ArmROT[0],ArmROT[1],ArmROT[2]),"Cube","RightShoulder")
setShapeLook("LeftElbow",(EbwSCL[0],EbwSCL[1],EbwSCL[2]),(EbwPOS[0],EbwPOS[1],EbwPOS[2]),(EbwROT[0],EbwROT[1],EbwROT[2]),"Cylinder","LeftArm")
setShapeLook("RightElbow",(EbwSCL[0],EbwSCL[1],EbwSCL[2]),(EbwPOS[0],EbwPOS[1],-EbwPOS[2]),(EbwROT[0],EbwROT[1],EbwROT[2]),"Cylinder","RightArm")
setShapeLook("LeftWrist",(WristSCL[0],WristSCL[1],WristSCL[2]),(WristPOS[0],WristPOS[1],WristPOS[2]),(WristROT[0],WristROT[1],WristROT[2]),"Cube","LeftElbow")
setShapeLook("RightWrist",(WristSCL[0],WristSCL[1],WristSCL[2]),(WristPOS[0],WristPOS[1],-WristPOS[2]),(WristROT[0],WristROT[1],WristROT[2]),"Cube","RightElbow")
setShapeLook("LeftHand",(HandSCL[0],HandSCL[1],HandSCL[2]),(HandPOS[0],HandPOS[1],HandPOS[2]),(HandROT[0],HandROT[1],HandROT[2]),"Sphere","LeftWrist")
setShapeLook("RightHand",(HandSCL[0],HandSCL[1],HandSCL[2]),(HandPOS[0],HandPOS[1],-HandPOS[2]),(HandROT[0],HandROT[1],HandROT[2]),"Sphere","RightWrist")
setShapeLook("LeftFinger1",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger1POS[0],Finger1POS[1],Finger1POS[2]),(Finger1ROT[0],Finger1ROT[1],Finger1ROT[2]),"Cylinder","LeftHand")
setShapeLook("RightFinger1",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger1POS[0],Finger1POS[1],-Finger1POS[2]),(-Finger1ROT[0],-Finger1ROT[1],Finger1ROT[2]),"Cylinder","RightHand")
setShapeLook("LeftFinger2",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger2POS[0],Finger2POS[1],Finger2POS[2]),(Finger2ROT[0],Finger2ROT[1],Finger2ROT[2]),"Cylinder","LeftHand")
setShapeLook("RightFinger2",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger2POS[0],Finger2POS[1],-Finger2POS[2]),(-Finger2ROT[0],-Finger2ROT[1],Finger2ROT[2]),"Cylinder","RightHand")
setShapeLook("LeftFinger3",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger3POS[0],Finger3POS[1],Finger3POS[2]),(Finger3ROT[0],Finger3ROT[1],Finger3ROT[2]),"Cylinder","LeftHand")
setShapeLook("RightFinger3",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger3POS[0],Finger3POS[1],-Finger3POS[2]),(-Finger3ROT[0],-Finger3ROT[1],Finger3ROT[2]),"Cylinder","RightHand")

setShapeLook("LeftHip",(HipSCL[0],HipSCL[1],HipSCL[2]),(HipPOS[0],HipPOS[1],HipPOS[2]),(HipROT[0],HipROT[1],HipROT[2]),"Cylinder","Butt")
setShapeLook("RightHip",(HipSCL[0],HipSCL[1],HipSCL[2]),(HipPOS[0],HipPOS[1],-HipPOS[2]),(HipROT[0],HipROT[1],HipROT[2]),"Cylinder","Butt")
setShapeLook("LeftThigh",(ThighSCL[0],ThighSCL[1],ThighSCL[2]),(ThighPOS[0],ThighPOS[1],ThighPOS[2]),(ThighROT[0],ThighROT[1],ThighROT[2]),"Cube","LeftHip")
setShapeLook("RightThigh",(ThighSCL[0],ThighSCL[1],ThighSCL[2]),(ThighPOS[0],ThighPOS[1],-ThighPOS[2]),(ThighROT[0],ThighROT[1],ThighROT[2]),"Cube","RightHip")
setShapeLook("LeftFoot",(FootSCL[0],FootSCL[1],FootSCL[2]),(FootPOS[0],FootPOS[1],FootPOS[2]),"none","Cube","LeftThigh")
setShapeLook("RightFoot",(FootSCL[0],FootSCL[1],FootSCL[2]),(FootPOS[0],FootPOS[1],-FootPOS[2]),"none","Cube","RightThigh")

setShapeLook("Tail1",(Tail1SCL[0],Tail1SCL[1],Tail1SCL[2]),(Tail1POS[0],Tail1POS[1],Tail1POS[2]),(Tail1ROT[0],Tail1ROT[1],Tail1ROT[2]),"Cone","Butt")
setShapeLook("Tail2",(Tail2SCL[0],Tail2SCL[1],Tail2SCL[2]),(Tail2POS[0],Tail2POS[1],Tail2POS[2]),(Tail2ROT[0],Tail2ROT[1],Tail2ROT[2]),"Cone","Tail1")
setShapeLook("Tail3",(Tail3SCL[0],Tail3SCL[1],Tail3SCL[2]),(Tail3POS[0],Tail3POS[1],Tail3POS[2]),(Tail3ROT[0],Tail3ROT[1],Tail3ROT[2]),"Cone","Tail2")
setShapeLook("Tail4",(Tail4SCL[0],Tail4SCL[1],Tail4SCL[2]),(Tail4POS[0],Tail4POS[1],Tail4POS[2]),(Tail4ROT[0],Tail4ROT[1],Tail4ROT[2]),"Cone","Tail3")

setTeeth(BottomFrontTeethAmount, TeethSCL,BottomFrontTeethPOS,TeethOffset,False)
setTeeth(BottomSideTeethAmount, TeethSCL, BottomSideTeethPOS,TeethOffset,False)
setTeeth(TopFrontTeethAmount,TeethSCL,TopFrontTeethPOS,TeethOffset,True)
setTeeth(TopSideTeethAmount,TeethSCL,TopSideTeethPOS,TeethOffset,True)
setRotate("Jaw",(JawROT[0],JawROT[1],JawROT[2]))

#animation

animateObject("Butt",".rx",0,0)

animateObject("Butt",".ty",0,0)
animateObject("Torso",".rz",0,0)
animateObject("Chest",".ty",0,0)
animateObject("Head",".tz",0,0)
animateObject("Head",".rz",0,0)
animateObject("Head",".rx",0,0)

animateObject("RightHip",".rz",0,0)
animateObject("LeftHip",".rz",0,0)

animateObject("RightShoulder",".rz",0,0)
animateObject("LeftShoulder",".rz",0,0)
animateObject("RightShoulder",".ty",0,0)
animateObject("LeftShoulder",".ty",0,0)

animateObject("RightFoot",".rz",0,0)
animateObject("LeftFoot",".rz",0,0)

animateObject("Tail1",".ry",0,0)
animateObject("Tail2",".ry",0,0)
animateObject("Tail3",".ry",0,0)
animateObject("Tail4",".ry",0,0)
#####
animateObject("Butt",".ty", s025, BUp)

animateObject("Torso",".rz", s025, LTorsoSwayUp)

animateObject("Chest",".ty", s025, BodyDown)

animateObject("RightFoot",".rz", s025, FootRotateFlat)
animateObject("LeftFoot",".rz", s025, FootRotateFlat)

animateObject("Butt",".rx", s05, BSway)
animateObject("Butt",".ty", s05, BUMax)

animateObject("Chest",".ty", s05, BodyUp)

animateObject("RightHip",".rz", s05, -20)
animateObject("LeftHip",".rz", s05, 20)

animateObject("RightShoulder",".ty", s05, ArmSwayDown)
animateObject("RightShoulder",".rz", s05, ArmRotateBack)
animateObject("LeftShoulder",".ty", s05, ArmSwayUp)
animateObject("LeftShoulder",".rz", s05, ArmRotateFront)

animateObject("Head",".tz", s05, HeadLeft)
animateObject("Head",".rx", s05, HeadRotateLeft)

animateObject("Torso",".rz", s05, LTorsoSwayDown)

animateObject("RightFoot",".rz", s05, FootRotateDrag)
animateObject("LeftFoot",".rz", s05, FootRotateLift)

animateObject("Tail1",".ry", s05, TailTurn)
animateObject("Tail2",".ry", s05, TailTurn)
animateObject("Tail3",".ry", s05, TailTurn)
animateObject("Tail4",".ry", s05, TailTurn)

animateObject("Butt",".ty", s075, BUp)

animateObject("Torso",".rz", s075, LTorsoSwayUp)

animateObject("Chest",".ty", s075, BodyDown)

animateObject("RightFoot",".rz", s075, FootRotateFlat)
animateObject("LeftFoot",".rz", s075, FootRotateFlat)
 #sNUMBER is time = frame number
animateObject("Butt",".rx", s10, -BSway)
animateObject("Butt",".ty", s10, BUMax)

animateObject("Chest",".ty", s10, BodyUp)

animateObject("RightHip",".rz", s10, 20)
animateObject("LeftHip",".rz", s10, -20)

animateObject("RightShoulder",".ty", s10, ArmSwayUp)
animateObject("RightShoulder",".rz", s10, ArmRotateFront)
animateObject("LeftShoulder",".ty", s10, ArmSwayDown)
animateObject("LeftShoulder",".rz", s10, ArmRotateBack)

animateObject("Head",".tz", s10, HeadRight)
animateObject("Head",".rx", s10, HeadRotateRight)

animateObject("Torso",".rz", s10, LTorsoSwayDown)

animateObject("RightFoot",".rz", s10, FootRotateLift)
animateObject("LeftFoot",".rz", s10, FootRotateDrag)

animateObject("Tail1",".ry", s10, -TailTurn)
animateObject("Tail2",".ry", s10, -TailTurn)
animateObject("Tail3",".ry", s10, -TailTurn)
animateObject("Tail4",".ry", s10, -TailTurn)

animateObject("Butt",".ty", s125, BUp)

animateObject("Torso",".rz", s125, LTorsoSwayUp)

animateObject("Chest",".ty", s125, BodyDown)

animateObject("RightFoot",".rz", s125, FootRotateFlat)
animateObject("LeftFoot",".rz", s125, FootRotateFlat)

animateObject("Butt",".ty", s15, BUMax)
animateObject("Butt",".rx", s15, BSway)

animateObject("Chest",".ty", s15, BodyUp)

animateObject("RightHip",".rz", s15, -20)
animateObject("LeftHip",".rz", s15, 20)

animateObject("RightShoulder",".ty", s15, ArmSwayDown)
animateObject("RightShoulder",".rz", s15, ArmRotateBack)
animateObject("LeftShoulder",".ty", s15, ArmSwayUp)
animateObject("LeftShoulder",".rz", s15, ArmRotateFront)

animateObject("Head",".tz", s15, HeadLeft)
animateObject("Head",".rx", s15, HeadRotateLeft)

animateObject("Torso",".rz", s15, LTorsoSwayDown)

animateObject("RightFoot",".rz", s15, FootRotateDrag)
animateObject("LeftFoot",".rz", s15, FootRotateLift)

animateObject("Tail1",".ry", s15, TailTurn)
animateObject("Tail2",".ry", s15, TailTurn)
animateObject("Tail3",".ry", s15, TailTurn)
animateObject("Tail4",".ry", s15, TailTurn)

animateObject("Butt",".ty", s175, BUp)

animateObject("Torso",".rz", s175, LTorsoSwayUp)

animateObject("Chest",".ty", s175, BodyDown)

animateObject("RightFoot",".rz", s175, FootRotateFlat)
animateObject("LeftFoot",".rz", s175, FootRotateFlat)

animateObject("Butt",".ty", s20, BUMax)
animateObject("Butt",".rx", s20, -BSway)

animateObject("Chest",".ty", s20, BodyUp)

animateObject("RightHip",".rz", s20, 20)
animateObject("LeftHip",".rz", s20, -20)

animateObject("RightShoulder",".ty", s20, ArmSwayUp)
animateObject("RightShoulder",".rz", s20, ArmRotateFront)
animateObject("LeftShoulder",".ty", s20, ArmSwayDown)
animateObject("LeftShoulder",".rz", s20, ArmRotateBack)

animateObject("Head",".tz", s20, HeadRight)
animateObject("Head",".rx", s20, HeadRotateRight)

animateObject("Torso",".rz", s20, LTorsoSwayDown)

animateObject("RightFoot",".rz", s20, FootRotateLift)
animateObject("LeftFoot",".rz", s20, FootRotateDrag)

animateObject("Tail1",".ry", s20, -TailTurn)
animateObject("Tail2",".ry", s20, -TailTurn)
animateObject("Tail3",".ry", s20, -TailTurn)
animateObject("Tail4",".ry", s20, -TailTurn)

animateObject("Butt",".ty", s225, BUp)

animateObject("Torso",".rz", s225, LTorsoSwayUp)

animateObject("Chest",".ty", s225, BodyDown)

animateObject("RightFoot",".rz", s225, FootRotateFlat)
animateObject("LeftFoot",".rz", s225, FootRotateFlat)

animateObject("Butt",".ty", s25, BUMax)
animateObject("Butt",".rx", s25, BSway)

animateObject("Chest",".ty", s25, BodyUp)

animateObject("RightHip",".rz", s25, -20)
animateObject("LeftHip",".rz", s25, 20)

animateObject("RightShoulder",".ty", s25, ArmSwayDown)
animateObject("RightShoulder",".rz", s25, ArmRotateBack)
animateObject("LeftShoulder",".ty", s25, ArmSwayUp)
animateObject("LeftShoulder",".rz", s25, ArmRotateFront)

animateObject("Head",".tz", s25, HeadLeft)
animateObject("Head",".rx", s25, HeadRotateLeft)

animateObject("Torso",".rz", s25, LTorsoSwayDown)

animateObject("RightFoot",".rz", s25, FootRotateDrag)
animateObject("LeftFoot",".rz", s05, FootRotateLift)

animateObject("Tail1",".ry", s25, TailTurn)
animateObject("Tail2",".ry", s25, TailTurn)
animateObject("Tail3",".ry", s25, TailTurn)
animateObject("Tail4",".ry", s25, TailTurn)

animateObject("Butt",".ty", s275, BUp)

animateObject("Torso",".rz", s275, LTorsoSwayUp)

animateObject("Chest",".ty", s275, BodyDown)

animateObject("RightFoot",".rz", s275, FootRotateFlat)
animateObject("LeftFoot",".rz", s275, FootRotateFlat)

animateObject("Butt",".ty", s30, BUMax)
animateObject("Butt",".rx", s30, -BSway)

animateObject("Chest",".ty", s30, BodyUp)

animateObject("RightHip",".rz", s30, 20)
animateObject("LeftHip",".rz", s30, -20)

animateObject("RightShoulder",".ty", s30, ArmSwayUp)
animateObject("RightShoulder",".rz", s30, ArmRotateFront)
animateObject("LeftShoulder",".ty", s30, ArmSwayDown)
animateObject("LeftShoulder",".rz", s30, ArmRotateBack)

animateObject("Head",".tz", s30, HeadRight)
animateObject("Head",".rx", s30, HeadRotateRight)

animateObject("Torso",".rz", s30, LTorsoSwayDown)

animateObject("RightFoot",".rz", s30, FootRotateLift)
animateObject("LeftFoot",".rz", s30, FootRotateDrag)

animateObject("Tail1",".ry", s30, -TailTurn)
animateObject("Tail2",".ry", s30, -TailTurn)
animateObject("Tail3",".ry", s30, -TailTurn)
animateObject("Tail4",".ry", s30, -TailTurn)

animateObject("Butt",".ty", s325, BUp)
animateObject("Torso",".rz", s325, LTorsoSwayUp)

animateObject("Chest",".ty", s325, BodyDown)

animateObject("RightFoot",".rz", s325, FootRotateFlat)
animateObject("LeftFoot",".rz", s325, FootRotateFlat)

animateObject("Butt",".ty", s35, BUMax)
animateObject("Butt",".rx", s35, BSway)

animateObject("Chest",".ty", s35, BodyUp)

animateObject("RightHip",".rz", s35, -20)
animateObject("LeftHip",".rz", s35, 20)

animateObject("RightShoulder",".ty", s35, ArmSwayDown)
animateObject("RightShoulder",".rz", s35, ArmRotateBack)
animateObject("LeftShoulder",".ty", s35, ArmSwayUp)
animateObject("LeftShoulder",".rz", s35, ArmRotateFront)

animateObject("Head",".tz", s35, HeadLeft)
animateObject("Head",".rx", s35, HeadRotateLeft)

animateObject("Torso",".rz", s35, LTorsoSwayDown)

animateObject("RightFoot",".rz", s35, FootRotateDrag)
animateObject("LeftFoot",".rz", s35, FootRotateLift)

animateObject("Tail1",".ry", s35, TailTurn)
animateObject("Tail2",".ry", s35, TailTurn)
animateObject("Tail3",".ry", s35, TailTurn)
animateObject("Tail4",".ry", s35, TailTurn)

animateObject("Butt",".ty", s375, BUp)
animateObject("Torso",".rz", s375, LTorsoSwayUp)

animateObject("Chest",".ty", s375, BodyDown)

animateObject("RightFoot",".rz", s375, FootRotateFlat)
animateObject("LeftFoot",".rz", s375, FootRotateFlat)

animateObject("Butt",".ty", s40, BUMax)
animateObject("Butt",".rx", s40, -BSway)

animateObject("Chest",".ty", s40, BodyUp)

animateObject("RightHip",".rz", s40, 20)
animateObject("LeftHip",".rz", s40, -20)

animateObject("RightShoulder",".ty", s40, ArmSwayUp)
animateObject("RightShoulder",".rz", s40, ArmRotateFront)
animateObject("LeftShoulder",".ty", s40, ArmSwayDown)
animateObject("LeftShoulder",".rz", s40, ArmRotateBack)

animateObject("Head",".tz", s40, HeadRight)
animateObject("Head",".rx", s40, HeadRotateRight)

animateObject("Torso",".rz", s40, LTorsoSwayDown)

animateObject("RightFoot",".rz", s40, FootRotateLift)
animateObject("LeftFoot",".rz", s40, FootRotateDrag)

animateObject("Tail1",".ry", s40, -TailTurn)
animateObject("Tail2",".ry", s40, -TailTurn)
animateObject("Tail3",".ry", s40, -TailTurn)
animateObject("Tail4",".ry", s40, -TailTurn)

animateObject("Butt",".ty", s425, BUp)
animateObject("Torso",".rz", s425, LTorsoSwayUp)

animateObject("Chest",".ty", s425, BodyDown)

animateObject("RightFoot",".rz", s425, FootRotateFlat)
animateObject("LeftFoot",".rz", s425, FootRotateFlat)

animateObject("Butt",".ty", s45, BUMax)
animateObject("Butt",".rx", s45, BSway)

animateObject("Chest",".ty", s45, BodyUp)

animateObject("RightHip",".rz", s45, -20)
animateObject("LeftHip",".rz", s45, 20)

animateObject("RightShoulder",".ty", s45, ArmSwayDown)
animateObject("RightShoulder",".rz", s45, ArmRotateBack)
animateObject("LeftShoulder",".ty", s45, ArmSwayUp)
animateObject("LeftShoulder",".rz", s45, ArmRotateFront)

animateObject("Head",".tz", s45, HeadLeft)
animateObject("Head",".rx", s45, HeadRotateLeft)

animateObject("Torso",".rz", s45, LTorsoSwayDown)

animateObject("RightFoot",".rz", s45, FootRotateDrag)
animateObject("LeftFoot",".rz", s45, FootRotateLift)

animateObject("Tail1",".ry", s45, TailTurn)
animateObject("Tail2",".ry", s45, TailTurn)
animateObject("Tail3",".ry", s45, TailTurn)
animateObject("Tail4",".ry", s45, TailTurn)

animateObject("Butt",".ty", s475, BUp)
animateObject("Torso",".rz", s475, LTorsoSwayUp)

animateObject("Chest",".ty", s475, BodyDown)

animateObject("RightFoot",".rz", s475, FootRotateFlat)
animateObject("LeftFoot",".rz", s475, FootRotateFlat)

animateObject("Butt",".ty", s50, BUMax)
animateObject("Butt",".rx", s50, -BSway)

animateObject("Chest",".ty", s50, BodyUp)

animateObject("RightHip",".rz", s50, 20)
animateObject("LeftHip",".rz", s50, -20)

animateObject("RightShoulder",".ty", s50, ArmSwayUp)
animateObject("RightShoulder",".rz", s50, ArmRotateFront)
animateObject("LeftShoulder",".ty", s50, ArmSwayDown)
animateObject("LeftShoulder",".rz", s50, ArmRotateBack)

animateObject("Head",".tz", s50, HeadRight)
animateObject("Head",".rx", s50, HeadRotateRight)

animateObject("Torso",".rz", s50, LTorsoSwayDown)

animateObject("RightFoot",".rz", s50, FootRotateLift)
animateObject("LeftFoot",".rz", s50, FootRotateDrag)

animateObject("Tail1",".ry", s50, -TailTurn)
animateObject("Tail2",".ry", s50, -TailTurn)
animateObject("Tail3",".ry", s50, -TailTurn)
animateObject("Tail4",".ry", s50, -TailTurn)

animateObject("Butt",".rx", s55, 0)
animateObject("Butt",".ty", s55, 0)

animateObject("Chest",".ty", s55, 0)

animateObject("RightHip",".rz", s55, 0)
animateObject("LeftHip",".rz", s55, 0)

animateObject("RightShoulder",".ty", s55, 0)
animateObject("RightShoulder",".rz", s55, 0)
animateObject("LeftShoulder",".ty", s55, 0)
animateObject("LeftShoulder",".rz", s55, 0)

animateObject("Head",".tz", s55, 0)
animateObject("Head",".rx", s55, 0)

animateObject("Torso",".rz", s55, 0)

animateObject("RightFoot",".rz", s55, 0)
animateObject("LeftFoot",".rz", s55, 0)

animateObject("Tail1",".ry", s55, 0)
animateObject("Tail2",".ry", s55, 0)
animateObject("Tail3",".ry", s55, 0)
animateObject("Tail4",".ry", s55, 0)