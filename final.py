# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *           
import __main__                         
import section                          #Added to script
import regionToolset                    #Added to script
import displayGroupMdbToolset as dgm    #Added to script
import part                             #Added to script
import material                         #Added to script
import assembly                         #Added to script
import step                             #Added to script
import interaction                      #Added to script
import load                             #Added to script
import mesh                             #Added to script
import optimization                     #Added to script
import job                              #Added to script
import sketch                           #Added to script
import visualization                    #Added to script
import xyPlot                           #Added to script
import displayGroupOdbToolset as dgo    #Added to script
import connectorBehavior                #Added to script
import odbAccess                        #Added to script
from odbAccess import *                 #Added to script
from textRepr import *                  #Added to script


def m_part():
    
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.04, 0.00215), point2=(-0.04, -0.00215))
    p = mdb.models['Model-1'].Part(name='sample', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['sample']
    p.BaseSolidExtrude(sketch=s, depth=0.0133)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['sample']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.CircleByCenterPerimeter(center=(0.05, 0.0), point1=(0.05, 0.00525))
    s1.CircleByCenterPerimeter(center=(0.05, 0.0), point1=(0.05, 0.00475))
    p = mdb.models['Model-1'].Part(name='roller', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['roller']
    p.BaseSolidExtrude(sketch=s1, depth=0.03)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['roller']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


def m_property():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='pp')
    mdb.models['Model-1'].materials['pp'].Density(table=((910.0, ), ))
    mdb.models['Model-1'].materials['pp'].Elastic(table=((1500000000.0, 0.33), ))
    mdb.models['Model-1'].materials['pp'].DruckerPrager(table=((25.0, 0.8, 15.0), 
        ))
    mdb.models['Model-1'].materials['pp'].druckerPrager.DruckerPragerHardening(
        table=((40000000.0, 0.0), (41000000.0, 0.1)))
    mdb.models['Model-1'].Material(name='steel')
    mdb.models['Model-1'].materials['steel'].Density(table=((7800.0, ), ))
    mdb.models['Model-1'].materials['steel'].Elastic(table=((200000000000.0, 0.3), 
        ))
    p = mdb.models['Model-1'].parts['sample']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-pp', material='pp', 
        thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-steel', 
        material='steel', thickness=None)
    p = mdb.models['Model-1'].parts['sample']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['sample']
    p.SectionAssignment(region=region, sectionName='Section-pp', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['roller']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['roller']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['roller']
    p.SectionAssignment(region=region, sectionName='Section-steel', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def m_assembly():  
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['sample']
    a.Instance(name='sample-1', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['sample-1'].edges
    a.DatumPointByMidPoint(point1=a.instances['sample-1'].InterestingPoint(
        edge=e1[4], rule=MIDDLE), 
        point2=a.instances['sample-1'].InterestingPoint(edge=e1[6], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a = mdb.models['Model-1'].rootAssembly
    e11 = a.instances['sample-1'].edges
    a.DatumPointByOffset(point=a.instances['sample-1'].InterestingPoint(
        edge=e11[3], rule=MIDDLE), vector=(-0.0125, 0.0, 0.0))
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['sample-1'].edges
    a.DatumPointByOffset(point=a.instances['sample-1'].InterestingPoint(edge=e1[8], 
        rule=MIDDLE), vector=(0.0125, 0.0, 0.0))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['roller']
    a1.Instance(name='roller-1', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.177963, 
        farPlane=0.260278, width=0.105395, height=0.0450919, 
        viewOffsetX=0.00198799, viewOffsetY=-0.00166594)
    a = mdb.models['Model-1'].rootAssembly
    v11 = a.instances['roller-1'].vertices
    a.DatumPointByMidPoint(point1=v11[1], point2=v11[0])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('roller-1', ), vector=(-0.05, -0.0074, -0.00835))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['roller']
    a1.Instance(name='roller-2', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.1992, 
        farPlane=0.217716, width=0.0165993, height=0.00710178, 
        viewOffsetX=0.0360781, viewOffsetY=0.0154746)
    a = mdb.models['Model-1'].rootAssembly
    e11 = a.instances['roller-2'].edges
    a.DatumPointByMidPoint(point1=a.instances['roller-2'].InterestingPoint(
        edge=e11[1], rule=MIDDLE), 
        point2=a.instances['roller-2'].InterestingPoint(edge=e11[0], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.197769, 
        farPlane=0.219147, width=0.105901, height=0.045308, 
        viewOffsetX=0.0329109, viewOffsetY=0.00467463)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('roller-2', ), vector=(-0.0225, 0.0074, -0.00835))
    a1 = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['roller']
    a1.Instance(name='roller-3', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.19876, 
        farPlane=0.224246, width=0.00500698, height=0.00214216, 
        viewOffsetX=0.0398277, viewOffsetY=0.0179252)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['roller-3'].edges
    a.DatumPointByMidPoint(point1=a.instances['roller-3'].InterestingPoint(
        edge=e1[1], rule=MIDDLE), 
        point2=a.instances['roller-3'].InterestingPoint(edge=e1[0], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.197148, 
        farPlane=0.225858, width=0.10383, height=0.0444219, 
        viewOffsetX=0.0293994, viewOffsetY=0.0131749)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a1 = mdb.models['Model-1'].rootAssembly
    a1.translate(instanceList=('roller-3', ), vector=(-0.0775, 0.0074, -0.00835))


def m_step():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    mdb.models['Model-1'].ImplicitDynamicsStep(name='Step-1', previous='Initial', 
        maxNumInc=100000, application=QUASI_STATIC, initialInc=0.001, 
        minInc=1e-12, nohaf=OFF, amplitude=RAMP, alpha=DEFAULT, 
        initialConditions=OFF, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    del mdb.models['Model-1'].fieldOutputRequests['F-Output-1']
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['roller-3'].edges
    a.ReferencePoint(point=a.instances['roller-3'].InterestingPoint(edge=e1[0], 
        rule=CENTER))
    a = mdb.models['Model-1'].rootAssembly
    e11 = a.instances['roller-1'].edges
    a.ReferencePoint(point=a.instances['roller-1'].InterestingPoint(edge=e11[0], 
        rule=CENTER))
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['roller-2'].edges
    a.ReferencePoint(point=a.instances['roller-2'].InterestingPoint(edge=e1[0], 
        rule=CENTER))
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[17], )
    a.Set(referencePoints=refPoints1, name='Set-rp2')
    regionDef=mdb.models['Model-1'].rootAssembly.sets['Set-rp2']
    mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=(
        'UT', 'RF2'), numIntervals=200, region=regionDef, 
        sectionPoints=DEFAULT, rebar=EXCLUDE)


def m_interaction():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['roller-3'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(cells=cells1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[16], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-1', refPointRegion=region1, 
        bodyRegion=region2)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['roller-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(cells=cells1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[17], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-2', refPointRegion=region1, 
        bodyRegion=region2)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['roller-2'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    region2=regionToolset.Region(cells=cells1)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[18], )
    region1=regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].RigidBody(name='Constraint-3', refPointRegion=region1, 
        bodyRegion=region2)
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.3, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    mdb.models['Model-1'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON, 
        constraintEnforcementMethod=DEFAULT)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['roller-3'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region1=regionToolset.Region(side1Faces=side1Faces1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['sample-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
    region2=regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1', 
        createStepName='Step-1', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['roller-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region1=regionToolset.Region(side1Faces=side1Faces1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['sample-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    region2=regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-2', 
        createStepName='Step-1', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['roller-2'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region1=regionToolset.Region(side1Faces=side1Faces1)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['sample-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
    region2=regionToolset.Region(side1Faces=side1Faces1)
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-3', 
        createStepName='Step-1', main=region1, secondary=region2, 
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1', 
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)


def m_load():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[16], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[17], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.03, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[18], )
    region = regionToolset.Region(referencePoints=refPoints1)
    mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)


def m_mesh():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['sample-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    c2 = a.instances['roller-1'].cells
    cells2 = c2.getSequenceFromMask(mask=('[#1 ]', ), )
    c3 = a.instances['roller-2'].cells
    cells3 = c3.getSequenceFromMask(mask=('[#1 ]', ), )
    c4 = a.instances['roller-3'].cells
    cells4 = c4.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions = cells1+cells2+cells3+cells4
    a.setMeshControls(regions=pickedRegions, technique=SWEEP, 
        algorithm=MEDIAL_AXIS)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['sample-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    c2 = a.instances['roller-1'].cells
    cells2 = c2.getSequenceFromMask(mask=('[#1 ]', ), )
    c3 = a.instances['roller-2'].cells
    cells3 = c3.getSequenceFromMask(mask=('[#1 ]', ), )
    c4 = a.instances['roller-3'].cells
    cells4 = c4.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =((cells1+cells2+cells3+cells4), )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['sample-1'], a.instances['roller-1'], 
        a.instances['roller-2'], a.instances['roller-3'], )
    a.seedPartInstance(regions=partInstances, size=0.00055, deviationFactor=0.1, 
        minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['sample-1'], a.instances['roller-1'], 
        a.instances['roller-2'], a.instances['roller-3'], )
    a.generateMesh(regions=partInstances)



def m_job():
        
    # import section
    # import regionToolset
    # import displayGroupMdbToolset as dgm
    # import part
    # import material
    # import assembly
    # import step
    # import interaction
    # import load
    # import mesh
    # import optimization
    # import job
    # import sketch
    # import visualization
    # import xyPlot
    # import displayGroupOdbToolset as dgo
    # import connectorBehavior

    #   mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    #       atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    #       memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    #       explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    #       modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    #       scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    #       multiprocessingMode=DEFAULT, numCpus=16, numDomains=16, numGPUs=0)
    #   mdb.jobs['Job-1'].submit(consistencyChecking=OFF)

    job = mdb.Job(name='Job-'+str(n), model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
        multiprocessingMode=DEFAULT, numCpus=16, numDomains=16, numGPUs=0)      #Added to script
    job.submit(consistencyChecking=OFF)     #Added to script
    job.waitForCompletion()                 #Added to script


def m_report():

    #odb = session.odbs['C:/Users/User-111/Desktop/codes/Job-1.odb']
    odb = openOdb(path='C:/Users/User-111/Desktop/codes/Job-'+str(n)+'.odb')    #Added to script replaced the above line
    
    session.XYDataFromHistory(name='U2 PI: rootAssembly N: 2 NSET SET-RP2-1', 
        odb=odb, 
        outputVariableName='Spatial displacement: U2 PI: rootAssembly Node 2 in NSET SET-RP2', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    #odb = session.odbs['C:/Users/User-111/Desktop/codes/Job-1.odb']
    session.XYDataFromHistory(name='RF2 PI: rootAssembly N: 2 NSET SET-RP2-1', 
        odb=odb, 
        outputVariableName='Reaction force: RF2 PI: rootAssembly Node 2 in NSET SET-RP2', 
        steps=('Step-1', ), __linkedVpName__='Viewport: 1')
    xy1 = session.xyDataObjects['U2 PI: rootAssembly N: 2 NSET SET-RP2-1']
    xy2 = session.xyDataObjects['RF2 PI: rootAssembly N: 2 NSET SET-RP2-1']
    xy3 = combine(xy1, xy2)
    xy3.setValues(
        sourceDescription='combine ( "U2 PI: rootAssembly N: 2 NSET SET-RP2-1", "RF2 PI: rootAssembly N: 2 NSET SET-RP2-1" )')
    tmpName = xy3.name
    
    #session.xyDataObjects.changeKey(tmpName, 'X-F')
    session.xyDataObjects.changeKey(tmpName, 'X-F'+str(n))    #Added to script replaced the above line
    
    #x0 = session.xyDataObjects['X-F']
    x0 = session.xyDataObjects['X-F'+str(n)]                  #Added to script replaced the above line
    
    #    session.writeXYReport(fileName='C:/Users/User-111/Desktop/codes/result-1.csv', 
    #        xyData=(x0, ))
    session.writeXYReport(fileName='C:/Users/User-111/Desktop/codes/result-'+str(n)+'.csv', 
        xyData=(x0, ))                  #Added to script replaced the above line


#     from this line onwards, all the code has been added and was not present in the macros

n=0    # << n >> is a counter for naming jobs and naming output xy plots and naming csvs 

for an_Optional_variable in An_arbitrary_interval_and_an_arbitrary_module:
    
    Mdb()     # this command clears all previous simulations and prepares Abaqus to define new conditions
    
    n=n+1   
    
    #       Calling functions    

    m_part()
    m_property()
    m_assembly()
    m_step()
    m_interaction()
    m_load()
    m_mesh()
    m_job()

    #  in the next part, Python checks if the simulation was successful then receives the outputs

    with open('Job-'+str(n)+'.sta') as f:
        lines = f.readlines()
        Message = lines[len(lines)-1].split()
        if(Message[-1]=='SUCCESSFULLY'):
            m_report() 
        else:
            continue   










 