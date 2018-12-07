import maya.cmds as cmds

#cubegator as a function
#and now with classes
#by dylan lau

cmds.file(new = 1, force = 1)#makes a new file every execution
class Shapes(object):
    def __init__(self,objname,scale,position,rotation,shapeobjtype,parent):
        self.objectname = objname
        self.objectscale = scale
        self.objectposition = position
        self.objectrotation = rotation
        self.objecttype = shapeobjtype
        self.objectparent = parent
        self.setShapeLook()
    def setShapeLook(self): #sets object shape. input takes Name,Scale,Position,Rotation,what shape it is, and who is it's parent.
        if (self.objecttype is "Cube"): # if it is a cube, it makes a cube
            obj = cmds.polyCube(name = self.objectname)[0]
        elif (self.objecttype is "Sphere"):
            obj = cmds.polySphere(name = self.objectname)[0]
        elif (self.objecttype is "Cylinder"):
            obj = cmds.polyCylinder(name = self.objectname)[0]
        elif (self.objecttype is "Cone"):
            obj = cmds.polyCone(name = self.objectname)[0]
        cmds.scale(self.objectscale[0],self.objectscale[1],self.objectscale[2],obj) #sets scale
        cmds.move(self.objectposition[0],self.objectposition[1],self.objectposition[2],obj) #sets position
        if(self.objectrotation is "none"): #if there is rotation or not
            pass
        else:
            cmds.rotate(self.objectrotation[0],self.objectrotation[1],self.objectrotation[2],obj) #sets rotation
        cmds.makeIdentity(obj,a=1,r=1,s=1,t=1) #freezes all transforms
        if (self.objectparent is "none"): #if there is a parent or not
            pass
        else:
            cmds.parent(obj,self.objectparent) #sets parent
        print "Set Look of " + self.objectname + ", which is a " + self.objecttype + ", and parented it to " + self.objectparent + "." #writes a message of what it did.
    def animateObject(self,section,time,value):
        for i in range(len(time)):
            if (time[i] is s000):
                cmds.setKeyframe(self.objectname+section,t=time[i],v=ZeroNull)
                print "set zerod keyframe"
            else:
                if (value is RightFootRZ or value is LeftFootRZ):
                    if (i % 4 == 1):
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[0])
                    elif (i % 4 == 2):
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[1])
                    elif (i % 4 == 3):
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[2])
                    elif (i % 4 == 0):
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[3])
                else:
                    if (i % 2 == 0): #even
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[0])
                    else:
                        cmds.setKeyframe(self.objectname+section,t=time[i],v=value[1])
            #print "Animated " + self.objectname + "'s " + section + " at " + str(time[i]) + " seconds."
    def setRotate(self,rotation): #seperate rotation function for jaw
        cmds.rotate(rotation[0],rotation[1],rotation[2],self.objectname)
        print "rotated "+ self.objectname + " by " + str(rotation) + " degrees."
class Teeth(object):
    def __init__(self,amount,scale,position,offset,roof):
        self.teethamount = amount
        self.teethscale = scale
        self.teethposition = position
        self.teethoffset = offset
        self.teethroof = roof
        self.setTeeth()
    def setTeeth(self): #function that sets the teeth.
        for i in range(self.teethamount): # a loop that will make teeth based on how many there is (amount)
            tooth = cmds.polyCone(name = 'Teeth1')[0] #sets tooth to cone shape
            cmds.scale(self.teethscale[0],self.teethscale[1],self.teethscale[2],tooth) #sets scale
            if (self.teethroof is True): #if roof is true, it will execute this block
                cmds.rotate(180,0,0,tooth) #flips tooth over 
                if(self.teethamount is TopFrontTeethAmount):# if it is top and front of mouth
                    cmds.move(self.teethposition[0],self.teethposition[1],self.teethposition[2]-(self.teethoffset*i),tooth) #simple math of offsetting each tooth by number of teeth chosen
                elif(self.teethamount is TopSideTeethAmount): #if tooth is side
                    cmds.move(self.teethposition[0] - self.teethoffset*(i/2), self.teethposition[1], self.teethposition[2]*((-1)**i), tooth)
                    #the i is also used as an exponent to make the second one of every pair mirror the first
                    #also flips every other tooth
                cmds.parent(tooth,"Head") #parents tooth to head
            else:
                if (self.teethamount is BottomFrontTeethAmount):
                    cmds.move(self.teethposition[0],self.teethposition[1],self.teethposition[2]-(self.teethoffset*i),tooth)	
                elif(self.teethamount is BottomSideTeethAmount):
                    cmds.move(self.teethposition[0] + self.teethoffset*(i/2), self.teethposition[1], self.teethposition[2]*((-1)**i), tooth)
                cmds.parent(tooth,"Jaw")

class UI():
    def __init__(self,name,title):
        self.window = name
        self.windowTitle = title
        self.createUI()
    def createUI(self):
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window)
        cmds.window(self.window,title = self.windowTitle)
        self.windowColumn = cmds.columnLayout(adj=True,bgc = (0.207, 0.129, 0.431))
        self.spawnWindowCommands()
        self.animateWindowCommands()
        self.colorWindowCommands()
        cmds.showWindow(self.window)
    def spawnWindowCommands(self,args = 0):
        blueColor = (0.603, 0.745, 0.956)
        redColor = (0.584, 0.094, 0.168)
        cmds.text("Cubegator by Dylan Lau",bgc = (0.505, 0.396, 0.823),height=25)
        self.createCharacter = cmds.button(label = "Create Character",command = self.spawnAll)
        self.createHead = cmds.button(label = "Create Head",command = self.spawnHead)
        self.createChest = cmds.button(l = "Create Body",c = self.spawnBody)

        self.createArms = cmds.button(l = "Create Arms",c = self.spawnArms)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2,cl2 = ["center","center"],ct2 = ["both","both"])
        self.createLeftArm = cmds.button(l = "Create Left Arm",c = self.spawnLeftArm,bgc = blueColor)
        self.createRightArm = cmds.button(l = "Create Right Arm",c = self.spawnRightArm,bgc = redColor)

        cmds.setParent('..')
        cmds.columnLayout(adj=True,bgc = (0.207, 0.129, 0.431))
        self.createLegs = cmds.button(l = "Create Legs",c = self.spawnLegs)
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=2)
        self.createLeftLeg = cmds.button(l = "Create Left Leg",c = self.spawnLeftLeg,bgc = blueColor)
        self.createRightLeg = cmds.button(l = "Create Right Leg",c = self.spawnRightLeg,bgc = redColor)

        cmds.setParent('..')
        cmds.columnLayout(adj=True,bgc = (0.207, 0.129, 0.431))
        self.createTailSlider = cmds.intSliderGrp(v=4,min=1,max=4,dc = self.getTailNumberValue)
        self.getTailNumberValue()
        self.createTail = cmds.button(l = "Create Tail",c = self.spawnTail)
    def animateWindowCommands(self,args = 0):
        animbgc = (0.921, 0.309, 0.078)
        cmds.text("Make Him Run",bgc = (0.913, 0.631, 0.525),height = 25)
        self.animateCharacter = cmds.button(l = "Animate Character",c = self.animAll,bgc = animbgc)
        self.animateHead = cmds.button(label = "Animate Head",command = self.animHead,bgc = animbgc)
        self.animateChest = cmds.button(l = "Animate Body",c = self.animBody,bgc = animbgc)
        self.animateArms = cmds.button(l = "Animate Arms",c = self.animArms,bgc = animbgc)
        self.animateLegs = cmds.button(l = "Animate Legs",c = self.animLegs,bgc = animbgc)
        self.animateTail = cmds.button(l = "Animate Tail",c = self.animTail,bgc = animbgc)
    def colorWindowCommands(self,args = 0):
        cmds.text("Color Him",bgc = (0.2,0.76,0.55),height = 25)
        self.setSeperateShader = cmds.button(l = "Press to set New Shader",c = self.setNewShader,bgc = (0.282, 0.556, 0.431))
        self.colorpanel = cmds.colorInputWidgetGrp (label = "Color",changeCommand = self.changeColor,bgc = (0.125, 0.352, 0.247))
    def spawnAll(self,args = 0):
        self.spawnHead()
        self.spawnBody()
        self.spawnArms()
        self.spawnLegs()
        self.spawnTail()
        self.repairParents()
    def spawnHead(self,args = 0):
        global Head 
        Head = Shapes("Head",(HeadSCL[0],HeadSCL[1],HeadSCL[2]),(HeadPOS[0],HeadPOS[1],HeadPOS[2]),"none","Cube","none")
        Jaw = Shapes("Jaw",(JawSCL[0],JawSCL[1],JawSCL[2]),(JawPOS[0],JawPOS[1],JawPOS[2]),"none","Cube","Head")
        
        RightEyeSocket = Shapes("RightEyeSocket",(EyeSocketSCL[0],EyeSocketSCL[1],EyeSocketSCL[2]),(EyeSocketPOS[0],EyeSocketPOS[1],EyeSocketPOS[2]),"none","Cube","Head")
        LeftEyeSocket = Shapes("LeftEyeSocket",(EyeSocketSCL[0],EyeSocketSCL[1],EyeSocketSCL[2]),(EyeSocketPOS[0],EyeSocketPOS[1],-EyeSocketPOS[2]),"none","Cube","Head")
        RightEye = Shapes("RightEye", (EyeBallSCL,EyeBallSCL,EyeBallSCL), (EyeBallPOS,EyeSocketPOS[1],EyeSocketPOS[2]),"none", "Sphere","RightEyeSocket")
        LeftEye = Shapes("LeftEye", (EyeBallSCL,EyeBallSCL,EyeBallSCL), (EyeBallPOS,EyeSocketPOS[1],-EyeSocketPOS[2]),"none", "Sphere","LeftEyeSocket")

        Teeth(BottomFrontTeethAmount, TeethSCL,BottomFrontTeethPOS,TeethOffset,False)
        Teeth(BottomSideTeethAmount, TeethSCL, BottomSideTeethPOS,TeethOffset,False)
        Teeth(TopFrontTeethAmount,TeethSCL,TopFrontTeethPOS,TeethOffset,True)
        Teeth(TopSideTeethAmount,TeethSCL,TopSideTeethPOS,TeethOffset,True)

        Jaw.setRotate((JawROT[0],JawROT[1],JawROT[2]))
    def spawnBody(self,args = 0):
        global Butt 
        Butt = Shapes("Butt",(ButtSCL[0],ButtSCL[1],ButtSCL[2]),(ButtPOS[0],ButtPOS[1],ButtPOS[2]),"none","Cube","none")
        Gut = Shapes("Gut",(GutSCL[0],GutSCL[1],GutSCL[2]),(GutPOS[0],GutPOS[1],GutPOS[2]),(GutROT[0],GutROT[1],GutROT[2]),"Cube","Butt")
        global Torso 
        Torso = Shapes("Torso",(TorsoSCL[0],TorsoSCL[1],TorsoSCL[2]),(TorsoPOS[0],TorsoPOS[1],TorsoPOS[2]),(TorsoROT[0],TorsoROT[1],TorsoROT[2]),"Cube","Gut")
        global Chest 
        Chest = Shapes("Chest",(ChestSCL[0],ChestSCL[1],ChestSCL[2]),(ChestPOS[0],ChestPOS[1],ChestPOS[2]),"none","Cube","Torso")
    def spawnRightArm(self,args = 0):
        global RightShoulder 
        RightShoulder = Shapes("RightShoulder",(ShoulderSCL,ShoulderSCL,ShoulderSCL),(ShoulderPOS[0],ShoulderPOS[1],-ShoulderPOS[2]),(ShoulderROT[0],ShoulderROT[1],ShoulderROT[2]),"Cylinder", "none")
        RightArm = Shapes("RightArm",(ArmSCL[0],ArmSCL[1],ArmSCL[2]),(ArmPOS[0],ArmPOS[1],-ArmPOS[2]),(ArmROT[0],ArmROT[1],ArmROT[2]),"Cube","RightShoulder")
        RightElbow = Shapes("RightElbow",(EbwSCL[0],EbwSCL[1],EbwSCL[2]),(EbwPOS[0],EbwPOS[1],-EbwPOS[2]),(EbwROT[0],EbwROT[1],EbwROT[2]),"Cylinder","RightArm")
        RightWrist = Shapes("RightWrist",(WristSCL[0],WristSCL[1],WristSCL[2]),(WristPOS[0],WristPOS[1],-WristPOS[2]),(WristROT[0],WristROT[1],WristROT[2]),"Cube","RightElbow")
        RightHand = Shapes("RightHand",(HandSCL[0],HandSCL[1],HandSCL[2]),(HandPOS[0],HandPOS[1],-HandPOS[2]),(HandROT[0],HandROT[1],HandROT[2]),"Sphere","RightWrist")
        RightFinger1 = Shapes("RightFinger1",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger1POS[0],Finger1POS[1],-Finger1POS[2]),(-Finger1ROT[0],-Finger1ROT[1],Finger1ROT[2]),"Cylinder","RightHand")
        RightFinger2 = Shapes("RightFinger2",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger2POS[0],Finger2POS[1],-Finger2POS[2]),(-Finger2ROT[0],-Finger2ROT[1],Finger2ROT[2]),"Cylinder","RightHand")
        RightFinger3 = Shapes("RightFinger3",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger3POS[0],Finger3POS[1],-Finger3POS[2]),(-Finger3ROT[0],-Finger3ROT[1],Finger3ROT[2]),"Cylinder","RightHand")
    def spawnLeftArm(self,args = 0):
        global LeftShoulder
        LeftShoulder = Shapes("LeftShoulder",(ShoulderSCL,ShoulderSCL,ShoulderSCL),(ShoulderPOS[0],ShoulderPOS[1],ShoulderPOS[2]),(ShoulderROT[0],ShoulderROT[1],ShoulderROT[2]),"Cylinder", "none")
        LeftArm = Shapes("LeftArm",(ArmSCL[0],ArmSCL[1],ArmSCL[2]),(ArmPOS[0],ArmPOS[1],ArmPOS[2]),(ArmROT[0],ArmROT[1],ArmROT[2]),"Cube","LeftShoulder")
        LeftElbow = Shapes("LeftElbow",(EbwSCL[0],EbwSCL[1],EbwSCL[2]),(EbwPOS[0],EbwPOS[1],EbwPOS[2]),(EbwROT[0],EbwROT[1],EbwROT[2]),"Cylinder","LeftArm")
        LeftWrist = Shapes("LeftWrist",(WristSCL[0],WristSCL[1],WristSCL[2]),(WristPOS[0],WristPOS[1],WristPOS[2]),(WristROT[0],WristROT[1],WristROT[2]),"Cube","LeftElbow")
        LeftHand = Shapes("LeftHand",(HandSCL[0],HandSCL[1],HandSCL[2]),(HandPOS[0],HandPOS[1],HandPOS[2]),(HandROT[0],HandROT[1],HandROT[2]),"Sphere","LeftWrist")
        LeftFinger1 = Shapes("LeftFinger1",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger1POS[0],Finger1POS[1],Finger1POS[2]),(Finger1ROT[0],Finger1ROT[1],Finger1ROT[2]),"Cylinder","LeftHand")
        LeftFinger2 = Shapes("LeftFinger2",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger2POS[0],Finger2POS[1],Finger2POS[2]),(Finger2ROT[0],Finger2ROT[1],Finger2ROT[2]),"Cylinder","LeftHand")
        LeftFinger3 = Shapes("LeftFinger3",(FingerSCL[0],FingerSCL[1],FingerSCL[2]),(Finger3POS[0],Finger3POS[1],Finger3POS[2]),(Finger3ROT[0],Finger3ROT[1],Finger3ROT[2]),"Cylinder","LeftHand")
    def spawnArms(self,args = 0):
        self.spawnRightArm()
        self.spawnLeftArm()
    def spawnRightLeg(self,args = 0):
        global RightHip 
        RightHip = Shapes("RightHip",(HipSCL[0],HipSCL[1],HipSCL[2]),(HipPOS[0],HipPOS[1],-HipPOS[2]),(HipROT[0],HipROT[1],HipROT[2]),"Cylinder","none")
        RightThigh = Shapes("RightThigh",(ThighSCL[0],ThighSCL[1],ThighSCL[2]),(ThighPOS[0],ThighPOS[1],-ThighPOS[2]),(ThighROT[0],ThighROT[1],ThighROT[2]),"Cube","RightHip")
        global RightFoot 
        RightFoot = Shapes("RightFoot",(FootSCL[0],FootSCL[1],FootSCL[2]),(FootPOS[0],FootPOS[1],-FootPOS[2]),"none","Cube","RightThigh")
    def spawnLeftLeg(self,args = 0):
        global LeftHip 
        LeftHip = Shapes("LeftHip",(HipSCL[0],HipSCL[1],HipSCL[2]),(HipPOS[0],HipPOS[1],HipPOS[2]),(HipROT[0],HipROT[1],HipROT[2]),"Cylinder","none")
        LeftThigh = Shapes("LeftThigh",(ThighSCL[0],ThighSCL[1],ThighSCL[2]),(ThighPOS[0],ThighPOS[1],ThighPOS[2]),(ThighROT[0],ThighROT[1],ThighROT[2]),"Cube","LeftHip")
        global LeftFoot
        LeftFoot = Shapes("LeftFoot",(FootSCL[0],FootSCL[1],FootSCL[2]),(FootPOS[0],FootPOS[1],FootPOS[2]),"none","Cube","LeftThigh")
    def spawnLegs(self,args = 0):
        self.spawnRightLeg()
        self.spawnLeftLeg()
    def spawnTail(self,args = 0):
        global Tail1
        global Tail2
        global Tail3
        global Tail4
        if (self.tailNumberValue == 1):
            Tail1 = Shapes("Tail1",(Tail1SCL[0],Tail1SCL[1],Tail1SCL[2]),(Tail1POS[0],Tail1POS[1],Tail1POS[2]),(Tail1ROT[0],Tail1ROT[1],Tail1ROT[2]),"Cone","none")
        elif (self.tailNumberValue == 2):
            Tail1 = Shapes("Tail1",(Tail1SCL[0],Tail1SCL[1],Tail1SCL[2]),(Tail1POS[0],Tail1POS[1],Tail1POS[2]),(Tail1ROT[0],Tail1ROT[1],Tail1ROT[2]),"Cone","none")
            Tail2 = Shapes("Tail2",(Tail2SCL[0],Tail2SCL[1],Tail2SCL[2]),(Tail2POS[0],Tail2POS[1],Tail2POS[2]),(Tail2ROT[0],Tail2ROT[1],Tail2ROT[2]),"Cone","Tail1")
        elif (self.tailNumberValue == 3):
            Tail1 = Shapes("Tail1",(Tail1SCL[0],Tail1SCL[1],Tail1SCL[2]),(Tail1POS[0],Tail1POS[1],Tail1POS[2]),(Tail1ROT[0],Tail1ROT[1],Tail1ROT[2]),"Cone","none")
            Tail2 = Shapes("Tail2",(Tail2SCL[0],Tail2SCL[1],Tail2SCL[2]),(Tail2POS[0],Tail2POS[1],Tail2POS[2]),(Tail2ROT[0],Tail2ROT[1],Tail2ROT[2]),"Cone","Tail1")
            Tail3 = Shapes("Tail3",(Tail3SCL[0],Tail3SCL[1],Tail3SCL[2]),(Tail3POS[0],Tail3POS[1],Tail3POS[2]),(Tail3ROT[0],Tail3ROT[1],Tail3ROT[2]),"Cone","Tail2")
        elif(self.tailNumberValue == 4):
            Tail1 = Shapes("Tail1",(Tail1SCL[0],Tail1SCL[1],Tail1SCL[2]),(Tail1POS[0],Tail1POS[1],Tail1POS[2]),(Tail1ROT[0],Tail1ROT[1],Tail1ROT[2]),"Cone","none")
            Tail2 = Shapes("Tail2",(Tail2SCL[0],Tail2SCL[1],Tail2SCL[2]),(Tail2POS[0],Tail2POS[1],Tail2POS[2]),(Tail2ROT[0],Tail2ROT[1],Tail2ROT[2]),"Cone","Tail1")
            Tail3 = Shapes("Tail3",(Tail3SCL[0],Tail3SCL[1],Tail3SCL[2]),(Tail3POS[0],Tail3POS[1],Tail3POS[2]),(Tail3ROT[0],Tail3ROT[1],Tail3ROT[2]),"Cone","Tail2")
            Tail4 = Shapes("Tail4",(Tail4SCL[0],Tail4SCL[1],Tail4SCL[2]),(Tail4POS[0],Tail4POS[1],Tail4POS[2]),(Tail4ROT[0],Tail4ROT[1],Tail4ROT[2]),"Cone","Tail3")
    def getTailNumberValue(self,args = 0):
        self.tailNumberValue = cmds.intSliderGrp(self.createTailSlider,query = True,value = True)
    def repairParents(self,args = 0):
        cmds.parent("Head","Chest")
        cmds.parent("Right Shoulder", "Chest")
        cmds.parent("Left Shoulder", "Chest")
        cmds.parent("Left Hip","Butt")
        cmds.parent("Right Hip","Butt")
        cmds.parent("Tail1","Butt")
    
    def animAll(self,args = 0):
        self.animHead()
        self.animBody()
        self.animArms()
        self.animLegs()
        self.animTail()
    def animHead(self,args = 0):
        Head.animateObject(".tz",halftimelist,HeadTZ)
        Head.animateObject(".rx",halftimelist,HeadRX)
    def animBody(self,args = 0):
        Butt.animateObject(".rx",halftimelist,ButtRX)
        Butt.animateObject(".ty",quartertimelist,ButtTY)
        Torso.animateObject(".rz",quartertimelist,TorsoRZ)
        Chest.animateObject(".ty",quartertimelist,ChestTY)
    def animArms(self,args = 0):
        RightShoulder.animateObject(".rz",halftimelist,RightShoulderRZ)
        LeftShoulder.animateObject(".rz",halftimelist,LeftShoulderRZ)
        RightShoulder.animateObject(".ty",halftimelist,RightShoulderTY)
        LeftShoulder.animateObject(".ty",halftimelist,LeftShoulderTY)
    def animLegs(self,args = 0):
        RightHip.animateObject(".rz",halftimelist,RightHipRZ)
        LeftHip.animateObject(".rz",halftimelist,LeftHipRZ)
        RightFoot.animateObject(".rz",quartertimelist,RightFootRZ)
        LeftFoot.animateObject(".rz",quartertimelist,LeftFootRZ)
    def animTail(self,args = 0):
        if (self.tailNumberValue == 1):
            Tail1.animateObject(".ry",halftimelist,TailRY)
        elif (self.tailNumberValue == 2):
            Tail1.animateObject(".ry",halftimelist,TailRY)
            Tail2.animateObject(".ry",halftimelist,TailRY)
        elif (self.tailNumberValue == 3):
            Tail1.animateObject(".ry",halftimelist,TailRY)
            Tail2.animateObject(".ry",halftimelist,TailRY)
            Tail3.animateObject(".ry",halftimelist,TailRY)
        elif (self.tailNumberValue == 4):
            Tail1.animateObject(".ry",halftimelist,TailRY)
            Tail2.animateObject(".ry",halftimelist,TailRY)
            Tail3.animateObject(".ry",halftimelist,TailRY)
            Tail4.animateObject(".ry",halftimelist,TailRY)
    
    def changeColor(self,args = 0):
        try:
            self.getObject = cmds.ls(sl=True)[0]
        except IndexError:
            pass
        bodyColor = cmds.colorInputWidgetGrp(self.colorpanel, query=True, rgb=True)
        try:
            self.getShader(self.getObject)
            cmds.setAttr(self.shader+".color",bodyColor[0],bodyColor[1],bodyColor[2],type="double3")
        except AttributeError:
            pass
         
    def setColorShader(self,Aobject): #sets the shader color to a tuple value
        CColor = (0.5,0.5,0.5)
        self.setShader(Aobject)
        cmds.setAttr(getBlinn+".color", CColor[0], CColor[1],CColor[2],type='double3')
    
    def setShader(self,Bobject,args = 0): #gets the shape node, then sets the shader node to a blinn
        self.getShape = cmds.listRelatives(Bobject,shapes=True)[0]
        getBlinn = cmds.shadingNode('blinn',asShader=True) 
        getNewSet = cmds.sets(renderable=True,noSurfaceShader=True,empty=True) 
        cmds.connectAttr(getBlinn+'.outColor',getNewSet+'.surfaceShader',f=True)
        cmds.defaultNavigation(source=getBlinn,destination=self.getShape+'.instObjGroups[0]',connectToExisting=True)
        
    def getShader(self,Bobject): #gets the shader node of the current selected object
        try:
            self.getNewShape = cmds.listRelatives(Bobject,shapes=True)[0]
        except AttributeError and TypeError:
            pass
        getConnect = cmds.listConnections(self.getNewShape)
        for node in getConnect:
            if cmds.nodeType(node) == 'shadingEngine':
                self.shadingEngine = node
        shaderConnect = cmds.listConnections(self.shadingEngine)     
        for node in shaderConnect:
            if cmds.nodeType(node) in ['blinn','lambert','phong']:
                self.shader = node
                return self.shader
    
    def setNewShader(self,args = 0):
        self.currentObject = cmds.ls(sl=1)[0]
        print self.currentObject
        self.setShader(self.currentObject)
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

TopSideTeethAmount = 12
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
ThighPOS = (-2.15,-4,-1.15)
ThighROT = (0,0,20)

FootSCL = (1.74,0.5,1)
FootPOS = (-1.75,-4.6,-1.15)

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

#animation variables
#time
s000=1
s025=6
s050=12
s075=18
s100=24
s125=30
s150=36
s175=42
s200=48
s225=54
s250=60
s275=66
s300=72
s325=78
s350=84
s375=90
s400=96
s425=102
s450=108
s475=114
s500=120
s525=126
s550=132
#time list variables
quartertimelist = (
	s000,
	s025,s050,s075,s100,
	s125,s150,s175,s200,
	s225,s250,s275,s300,
	s325,s350,s375,s400,
	s425,s450,s475,s500,
	s525,s550) #list of quarter times
QTLN = len(quartertimelist) #

halftimelist = (
	s000,
	s050,s100,
	s150,s200,
	s250,s300,
	s350,s400,
	s450,s500,
	s550)#list of half times
HTLN = len(halftimelist)

ZeroNull = 0

BSwayForward = 5
BSwayBackward = -5
BUp = 0.125
BUMax = 0.45

HipRotate = 20

ArmSwayUp = 0.35 #arm sway up value
ArmSwayDown = -0.5 #arm sway down value
ArmRotateBack = -20
ArmRotateFront = 75

HeadLeft = 0.5 #head swing left value
HeadRight = -0.5 #head swing right value
HeadRotate = 15 #headrotate left value

LTorsoSwayUp = 10 #lower torso sway up value
LTorsoSwayDown = -0.5 #lower torso sway down value

BodyDown = -1 #body vertical sway down value
BodyUp = 0 #gbody vertical rest value

FootRotateLift = 20 #foot rotate value
FootRotateDrag = -10 #foot drag value
FootRotateFlat = 10

TailTurn = 15

#list variables
ButtRX = (BSwayForward,BSwayBackward)
ButtTY = (BUp,BUMax)

TorsoRZ = (LTorsoSwayUp,LTorsoSwayDown)
ChestTY = (BodyDown,BodyUp)
HeadTZ = (HeadLeft,HeadRight)
HeadRX = (-HeadRotate,HeadRotate)

RightHipRZ = (-HipRotate,HipRotate)
LeftHipRZ = (HipRotate,-HipRotate)

RightShoulderRZ = (ArmRotateBack,ArmRotateFront)
LeftShoulderRZ = (ArmRotateFront,ArmRotateBack)

RightShoulderTY = (ArmSwayDown,ArmSwayUp)
LeftShoulderTY = (ArmSwayUp,ArmSwayDown)

RightFootRZ = (FootRotateFlat,FootRotateDrag,FootRotateFlat,FootRotateLift)
LeftFootRZ = (FootRotateFlat,FootRotateLift,FootRotateFlat,FootRotateDrag)

TailRY = (TailTurn,-TailTurn)


TheUI = UI("GATOR","CubeGator UI")