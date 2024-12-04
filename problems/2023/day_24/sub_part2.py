import sympy
FILENAME = "input.txt"
lines = [tuple(map(int, line.replace("@",",").split(","))) for line in open(FILENAME).read().splitlines()]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []
for x,y,z,vx,vy,vz in lines:
    equations.append((x-xr)*(vyr-vy)-(vxr-vx)*(y-yr))
    equations.append((y-yr)*(vzr-vz)-(vyr-vy)*(z-zr))

sol = sympy.solve(equations)[0]

print(sol)
print(sol[xr]+sol[yr]+sol[zr])
    