import math

A,B,H,M = map(int, input().split())

A_angle = (H*60+M)*0.5
B_angle = M*6

#中心角度
angle = abs(A_angle - B_angle)

#cos
angle_rad = math.radians(angle)
cos = math.cos(angle_rad)
#余弦定理
ansans = A**2+B**2-2*A*B*cos
ans = math.sqrt(ansans)
print(ans)
