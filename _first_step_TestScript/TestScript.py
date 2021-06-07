#Author-Misha
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, math
from .scripts import temp

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        params = {"d":300, "D":620, "B":185, "r":10,"r1":7.5}

        # GOST8328_75(design, "2000", params)
        # bearing12000(design)
        # bearing20001(design)
        temp.bearing20001(design)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def test(design):
    return 0

def GOST8328_75(design,type,params):
    d = params["d"] * 0.1
    D = params["D"] * 0.1
    B = params["B"] * 0.1
    r = params["r"] * 0.1
    r1 = params["r1"] * 0.1

    ADA = B*0.25
    BID1 = d + (D-d)/3.33333333
    KAD1 = BID1 + 1.33333 * (D-d)/3.33333333
    KID1 = BID1 / 1.11111111111

    CylCount = round(math.pi * (KID1 + 0.5*(KAD1-KID1)) / ((KAD1-KID1)/2)/2)

    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component

    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)


    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines

    # Draw upper ring lines
    if(type == "2000"):
        UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-B*0.25, KAD1*0.5, 0), adsk.core.Point3D.create(B*0.25, KAD1*0.5, 0))
        dlina = B*0.25 * math.tan(math.pi/180 * 10)
        UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-B*0.5, KAD1*0.5 + dlina, 0))
        UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-B*0.5, D*0.5, 0))
        UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(B*0.5, D*0.5, 0))
        UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(B*0.5, KAD1*0.5 + dlina, 0))
        UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, UR_line1.endSketchPoint)

    elif(type == "12000"):
        UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-B*0.25, KAD1*0.5, 0), adsk.core.Point3D.create(B*0.25, KAD1*0.5, 0))
        dlina = B*0.25 * math.tan(math.pi/180 * 10)
        UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-B*0.5, KAD1*0.5 + dlina, 0))
        UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-B*0.5, D*0.5, 0))
        UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(B*0.5, D*0.5, 0))
        
        UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
        UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 4 + dlina, 0))
        UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, UR_line1.endSketchPoint)

    elif(type == "32000" or type == "42000"):
        UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
        UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
        UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
        UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
        UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
        UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
        UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
        UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw down ring lines
    if(type == "2000"):
        DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-B*0.5, BID1*0.5, 0), adsk.core.Point3D.create(-B*0.25, BID1*0.5, 0))
        DR_line2 = lines.addByTwoPoints(DR_line1.endSketchPoint, adsk.core.Point3D.create(-B*0.25, KID1*0.5, 0))
        DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(B*0.25, KID1*0.5, 0))
        DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(B*0.25, BID1*0.5, 0))
        DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(B*0.5, BID1*0.5, 0))
        DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(B*0.5, d*0.5, 0))
        DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(-B*0.5, d*0.5, 0))
        DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.startSketchPoint)
        
    elif(type == "12000"):
        DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-B*0.5, BID1*0.5, 0), adsk.core.Point3D.create(-B*0.25, BID1*0.5, 0))
        DR_line2 = lines.addByTwoPoints(DR_line1.endSketchPoint, adsk.core.Point3D.create(-B*0.25, KID1*0.5, 0))
        DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(B*0.25, KID1*0.5, 0))
        DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(B*0.25, BID1*0.5, 0))
        DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(B*0.5, BID1*0.5, 0))
        DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(B*0.5, d*0.5, 0))
        DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(-B*0.5, d*0.5, 0))
        DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.startSketchPoint)

    elif(type == "32000"):
        dlina = 0.5 * math.tan(math.pi/180 * 10)
        DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
        DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-1, 2.5 - dlina, 0))
        DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
        DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
        DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
        DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, DR_line1.endSketchPoint)
    elif(type == "42000"):
        dlina = 0.5 * math.tan(math.pi/180 * 10)
        DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
        DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3, 0))
        DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3, 0))
        DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
        DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
        DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
        DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-B*0.25, (KAD1-KID1)*0.25+KID1*0.5, 0), adsk.core.Point3D.create(B*0.25,(KAD1-KID1)*0.25+KID1*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

        
    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(CylCount)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    if(type == "2000"):
        UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
        DownRingEdges = comp.bRepBodies.item(1).faces.item(7).edges
    elif(type == "12000"):
        UpperRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
        DownRingEdges = comp.bRepBodies.item(0).faces.item(7).edges
    elif(type == "32000"):
        UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
        DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    elif(type == "42000"):
        UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
        DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges

    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection = adsk.core.ObjectCollection.create()

    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(r1)
    DownFilletRadius = adsk.core.ValueInput.createByReal(r)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - " + type

def bearing2000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component

    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)


    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-1, 4 + dlina, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 4 + dlina, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 3, 0), adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.endSketchPoint, adsk.core.Point3D.create(-0.5, 2.5, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(0.5, 3, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 3, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.startSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

        
    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(7).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 2000"

def bearing12000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)


    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 4 + dlina, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 3, 0), adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.endSketchPoint, adsk.core.Point3D.create(-0.5, 2.5, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(0.5, 3, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 3, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.startSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

        
    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(0).faces.item(7).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 12000"

def bearing32000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)

    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
    UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-1, 2.5 - dlina, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 32000"

def bearing42000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)

    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
    UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 42000"

def bearing52000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)

    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
    UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-1, 2.5 - dlina, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

    # Draw connected lines.    
    FR_line1 = lines.addByTwoPoints(DR_line1.endSketchPoint,adsk.core.Point3D.create(0.5, 2.75 , 0))
    FR_line2 = lines.addByTwoPoints(FR_line1.endSketchPoint,adsk.core.Point3D.create(1.25, 2.75 , 0))
    FR_line3 = lines.addByTwoPoints(FR_line2.endSketchPoint,adsk.core.Point3D.create(1.25, 2 , 0))
    FR_line4 = lines.addByTwoPoints(FR_line3.endSketchPoint,DR_line4.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(3))
    
    FRProof = sketch.profiles.item(2)

    CilinderProf = sketch.profiles.item(1)

    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputFasRing = revolves.createInput(FRProof, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputFasRing.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputFasRing)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    FasRingEdges = comp.bRepBodies.item(2).faces.item(5).edges
    FasRingEdgeCollection = adsk.core.ObjectCollection.create()
    FasRingEdgeCollection.add(FasRingEdges.item(0))
    FasRingEdgeCollection.add(FasRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)
    FasRingFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True

    FasRingFilletInput = fillets.createInput()  
    FasRingFilletInput.addConstantRadiusEdgeSet(FasRingEdgeCollection, FasRingFilletRadius, True)
    FasRingFilletInput.isG2 = False
    FasRingFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)
    fillets.add(FasRingFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 52000"

def bearing62000(design):

    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)

    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
    UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    dlina = 0.5 * math.tan(math.pi/180 * 10)
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 2.5-dlina, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

    # Draw connected lines.    
    FR_line1 = lines.addByTwoPoints(DR_line1.endSketchPoint,adsk.core.Point3D.create(0.5, 2.75 , 0))
    FR_line2 = lines.addByTwoPoints(FR_line1.endSketchPoint,adsk.core.Point3D.create(1.25, 2.75 , 0))
    FR_line3 = lines.addByTwoPoints(FR_line2.endSketchPoint,adsk.core.Point3D.create(1.25, 2 , 0))
    FR_line4 = lines.addByTwoPoints(FR_line3.endSketchPoint,DR_line4.endSketchPoint)
    
        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

    FRProof = sketch.profiles.item(3)

    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputFasRing = revolves.createInput(FRProof, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)
    revInputFasRing.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputFasRing)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(3).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    FasRingEdges = comp.bRepBodies.item(2).faces.item(5).edges
    FasRingEdgeCollection = adsk.core.ObjectCollection.create()
    FasRingEdgeCollection.add(FasRingEdges.item(0))
    FasRingEdgeCollection.add(FasRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)
    FasRingFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True

    FasRingFilletInput = fillets.createInput()  
    FasRingFilletInput.addConstantRadiusEdgeSet(FasRingEdgeCollection, FasRingFilletRadius, True)
    FasRingFilletInput.isG2 = False
    FasRingFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)
    fillets.add(FasRingFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 62000"

def bearing92000(design):
    # Get the root component of the active design.
    rootComp = design.rootComponent
    # Get all components
    components = design.allComponents

    # Create new bearing component
    occurence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
    # Get link for new bearing component
    comp = occurence.component
    
    # Get extrudes for bearing component
    extrudes = comp.features.extrudeFeatures

    # Create a new sketch on the xy plane.
    sketches = comp.sketches
    xyPlane = comp.xYConstructionPlane
    yzPlane = comp.yZConstructionPlane
    sketch = sketches.add(xyPlane)

    # Draw connected lines.
    lines = sketch.sketchCurves.sketchLines
    
    UR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 4, 0), adsk.core.Point3D.create(0.5, 4, 0))
    UR_line2 = lines.addByTwoPoints(UR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3.5, 0))
    UR_line3 = lines.addByTwoPoints(UR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3.5, 0))
    UR_line4 = lines.addByTwoPoints(UR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 5, 0))
    UR_line5 = lines.addByTwoPoints(UR_line4.endSketchPoint, adsk.core.Point3D.create(1, 5, 0))
    UR_line6 = lines.addByTwoPoints(UR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3.5, 0))
    UR_line7 = lines.addByTwoPoints(UR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3.5, 0))
    UR_line8 = lines.addByTwoPoints(UR_line7.endSketchPoint, UR_line1.endSketchPoint)

    # Draw connected lines.
    DR_line1 = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, 2.5, 0), adsk.core.Point3D.create(0.5, 2.5, 0))
    DR_line2 = lines.addByTwoPoints(DR_line1.startSketchPoint, adsk.core.Point3D.create(-0.5, 3, 0))
    DR_line3 = lines.addByTwoPoints(DR_line2.endSketchPoint, adsk.core.Point3D.create(-1, 3, 0))
    DR_line4 = lines.addByTwoPoints(DR_line3.endSketchPoint, adsk.core.Point3D.create(-1, 2, 0))
    DR_line5 = lines.addByTwoPoints(DR_line4.endSketchPoint, adsk.core.Point3D.create(1, 2, 0))
    DR_line6 = lines.addByTwoPoints(DR_line5.endSketchPoint, adsk.core.Point3D.create(1, 3, 0))
    DR_line7 = lines.addByTwoPoints(DR_line6.endSketchPoint, adsk.core.Point3D.create(0.5, 3, 0))
    DR_line8 = lines.addByTwoPoints(DR_line7.endSketchPoint, DR_line1.endSketchPoint)

    # Draw connected lines.
    clAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-0.5, (4+2.5)*0.5 , 0), adsk.core.Point3D.create(0.5, (4+2.5)*0.5, 0))
    
    CL_line1 = lines.addByTwoPoints(clAxisLine.startSketchPoint,UR_line1.startSketchPoint)
    CL_line2 = lines.addByTwoPoints(clAxisLine.endSketchPoint,UR_line1.endSketchPoint)

        
    # Draw a line to use as the axis of revolution.
    RingsAxisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-1, 0, 0), adsk.core.Point3D.create(1, 0, 0))

    # Get the profile defined by the circle collection.
    RingProfs = adsk.core.ObjectCollection.create()
    RingProfs.add(sketch.profiles.item(0))
    RingProfs.add(sketch.profiles.item(2))

    CilinderProf = sketch.profiles.item(1)

    # Create an revolution input to be able to define the input needed for a revolution
    # while specifying the profile and that a new component is to be created
    revolves = comp.features.revolveFeatures
    revInputRings = revolves.createInput(RingProfs, RingsAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    revInputCilinder = revolves.createInput(CilinderProf, clAxisLine, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

    # Define that the extent is an angle of pi to get half of a torus.
    RevAngle = adsk.core.ValueInput.createByReal(math.pi*2)
    revInputRings.setAngleExtent(False, RevAngle)
    revInputCilinder.setAngleExtent(False, RevAngle)

    # Create the extrusion.
    revolves.add(revInputRings)
    revolves.add(revInputCilinder)

    # Get cilinder body
    CilinderBody = comp.bRepBodies.item(comp.bRepBodies.count - 1)

    # Create input entities for circular pattern
    inputEntites = adsk.core.ObjectCollection.create()
    inputEntites.add(CilinderBody)

    # Get X axis for circular pattern
    xAxis = comp.xConstructionAxis

    # Create the input for circular pattern
    circularFeats = comp.features.circularPatternFeatures
    circularFeatInput = circularFeats.createInput(inputEntites, xAxis)

    # Set the quantity of the elements
    circularFeatInput.quantity = adsk.core.ValueInput.createByReal(6)

    # Set symmetry of the circular pattern
    circularFeatInput.isSymmetric = True

    # Create the circular pattern
    circularFeat = circularFeats.add(circularFeatInput)

    # Get fillet features
    fillets = comp.features.filletFeatures

    # Create constant-radius fillet
    UpperRingEdges = comp.bRepBodies.item(0).faces.item(2).edges
    UpperRingEdgeCollection = adsk.core.ObjectCollection.create()
    UpperRingEdgeCollection.add(UpperRingEdges.item(0))
    UpperRingEdgeCollection.add(UpperRingEdges.item(1))

    DownRingEdges = comp.bRepBodies.item(1).faces.item(4).edges
    DownEdgeCollection = adsk.core.ObjectCollection.create()
    DownEdgeCollection.add(DownRingEdges.item(0))
    DownEdgeCollection.add(DownRingEdges.item(1))

    UpperFilletRadius = adsk.core.ValueInput.createByReal(0.3)
    DownFilletRadius = adsk.core.ValueInput.createByReal(0.1)

    UpperFilletInput = fillets.createInput()  
    UpperFilletInput.addConstantRadiusEdgeSet(UpperRingEdgeCollection, UpperFilletRadius, True)
    UpperFilletInput.isG2 = False
    UpperFilletInput.isRollingBallCorner = True

    DownFilletInput = fillets.createInput()  
    DownFilletInput.addConstantRadiusEdgeSet(DownEdgeCollection, DownFilletRadius, True)
    DownFilletInput.isG2 = False
    DownFilletInput.isRollingBallCorner = True
        
    fillets.add(UpperFilletInput) 
    fillets.add(DownFilletInput)

    # Change component name
    comp.name = "ГОСТ 8328-75 - 92000"
