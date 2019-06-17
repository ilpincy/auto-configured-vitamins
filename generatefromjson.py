import json

#
# Parse motor data
#
motors = json.load(open('motorOptions.json'))
print("\n%\n% Motors\n%")
print("M = [")
for mname,mdata in motors["data"].items():
    print("  % " + mname)
    print("  [", end='')
    print(mdata['MaxTorqueNewtonmeters'], end='')
    print(" ", end='')
    print(mdata['MaxFreeSpeedRadPerSec'], end='')
    print(" ", end='')
    print(mdata['price'], end='')
    print(" ", end='')
    print(mdata['massKg'], end='')
    print("],")
print("];")
print("M = transpose(M);")

#
# Useful constants
#
print("\n%\n% Useful constants\n%")
print("% Number of motor slots")
print("SLOTS = 3;")
print("% Number of motors in the catalog")
print("MOTORS = size(M,2);")

#
# Coefficients of objective function
#
print("\n%\n% Coefficients of objective function\n%")
print("c = [0 0 1 0] * M * repmat(eye(MOTORS), 1, SLOTS);")

#
# Basic constraints
#
print("\n%\n% Constraints\n%")
print("% Every slot must be occupied")
print("Aeq1 = repelem(eye(SLOTS), 1, MOTORS);")
print("beq1 = ones(SLOTS,1);")

#
# Other constraints
#
constraints = json.load(open('constraints1.json'))
print("% Required tip velocity")
print("V = " + str(constraints["requiredTipVelocityMeterPerSec"]) + ";")
print("% Required tip torque")
print("F = " + str(constraints["requiredTipForceNewtons"]) + ";")
print("% Gear ratio")
print("G = " + str(constraints["gearRatio"]) + ";")
print("% Maximum price")
print("P = " + str(constraints["maximumPrice"]) + ";")
