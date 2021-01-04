import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x1l = []
y1l = []
x2l = []
y2l = []
xbl = []
ybl = []
Ekl = []
Epl = []
Ecl = []


#STALE
G = float(40)
t = float(0)
dt = float(0.001)
tmax = float(2)
fr = int((tmax - t) / dt)

#Cialo 1
m1 = float(1)
x1 = float(1)
y1 = float(0)
vx1 = float(0)
vy1 = float(9)

#Cialo 2
m2 = float(3)
x2 = float(0)
y2 = float(1)
vx2 = float(0)
vy2 = float(-3)

while t < tmax:
    xb = (m1 * x1 + m2 * x2) / (m1 + m2)
    yb = (m1 * y1 + m2 * y2) / (m1 + m2)

    x1l.append(x1)
    y1l.append(y1)
    x2l.append(x2)
    y2l.append(y2)
    xbl.append(xb)
    ybl.append(yb)

    r1 = m.sqrt(x1 * x1 + y1 * y1)
    r2 = m.sqrt(x2 * x2 + y2 * y2)

    r13 = r1 * r1 * r1
    r23 = r2 * r2 * r2

    r1r2 = m.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    r2r1 = m.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    r1r23 = r1r2 * r1r2 * r1r2
    r2r13 = r2r1 * r2r1 * r2r1

    dv1x = -G * m2 * dt * (x1 - x2) / r1r23
    dv1y = -G * m2 * dt * (y1 - y2) / r1r23
    dv2x = -G * m1 * dt * (x2 - x1) / r1r23
    dv2y = -G * m1 * dt * (y2 - y1) / r1r23

    Ek = (m1 * (vx1 * vx1 + vy1 * vy1) + m2 * (vx2 * vx2 + vy2 * vy2)) / 2
    Ep = -1 * G * m1 * m2 / m.fabs(r2r1)
    Ec = Ek + Ep

    Ekl.append(Ek)
    Epl.append(Ep)
    Ecl.append(Ec)

    vx1 = vx1 + dv1x
    vy1 = vy1 + dv1y
    vx2 = vx2 + dv2x
    vy2 = vy2 + dv2y

    x1 = x1 + vx1 * dt
    y1 = y1 + vy1 * dt
    x2 = x2 + vx2 * dt
    y2 = y2 + vy2 * dt


    print('%s %s | %s %s | %s %s | %s %s %s' % (x1, y1, x2, y2, xb, yb, Ek, Ep, Ec))

    t = t + dt

#plt.plot(x1l, y1l, 'bs', x2l, y2l, 'g^')
#plt.xlabel('Time (hr)')
#plt.ylabel('Position (km)')
#plt.show()


i = 0
def _update_plot(i, fig, scat1, scat2, scatb):
    scat1.set_offsets(([x1l[i], y1l[i]]))
    scat2.set_offsets(([x2l[i], y2l[i]]))
    scatb.set_offsets(([xbl[i], ybl[i]]))
    print('Frames: %d' % i)

    return scat1, scat2, scatb


fig = plt.figure()

x1 = [x1l[i]]
y1 = [y1l[i]]
x2 = [x2l[i]]
y2 = [y2l[i]]
xb = [xbl[i]]
yb = [ybl[i]]

ax = fig.add_subplot(111)
ax.grid(True, linestyle='-', color='0.75')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])

scat1 = plt.scatter(x1, y1, c='black', s= 10 * m1)
scat2 = plt.scatter(x2, y2, c='black', s= 10 * m2)
scatb = plt.scatter(xb, yb, c='red', s=1)

scat1.set_alpha(0.8)
scat2.set_alpha(0.8)
scatb.set_alpha(0.8)


anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig, scat1, scat2, scatb),
                               frames=fr, interval=10)

plt.show()