#%%
import numpy as np
import matplotlib.pyplot as plt

import math
#%%
def taylor_sine_appx(x,n=20,es=0.5e-1):
    ex_appx = 1; i = 1; ea = 100  # noqa: E702
    
    while True:
        ex_appx_prev = ex_appx
        coef = (-1)**(i-1) #changed to folow sine
        numerator = x**(2*i)
        denominator = math.factorial(2*i - 1) #changed to follow sine
        
        ex_appx += (coef) * (( numerator) / (denominator))
        
        i += 1
        
        if ex_appx != 0 : ea = abs((ex_appx - ex_appx_prev) / ex_appx) * 100  # noqa: E701
        
        if ea < es or i ==n:
            break
        
    value_approx = ex_appx
        
    return value_approx,ea,i,x
    
test_angle = math.pi / 3
ty_func_sine_results = taylor_sine_appx(test_angle,10)
    
approxvalue = ty_func_sine_results[0]
ea = ty_func_sine_results[1]
angle_radians = ty_func_sine_results[3]  # noqa: F841
    
truevalue_radians = math.radians(60)
truevalue = math.sin(truevalue_radians)
    
et = abs((truevalue - approxvalue)/truevalue) * 100

print('\nTest for angle theta = π/3:')
print('Approximate Value Sine an Angle in Radians = {0:2.14f}'.format(approxvalue))
print('Approximate Relative Error(Ea) = {0:2.14f} '.format(ea))
print('True Value Sine of an Angle in Radians = {0:2.14f}'.format(truevalue))
print('AbsoluteTrue Percent Relative Error(Et) = {0:2.14f}'.format(et))

test_angle_1 = 2*math.pi + math.pi/3
ty_func_sine_results_1 = taylor_sine_appx(test_angle_1,10)
    
approxvalue_1 = ty_func_sine_results_1[0]
ea1 = ty_func_sine_results_1[1]
angle_radians_1 = ty_func_sine_results_1[3]  # noqa: F841
    
truevalue_radians_1 = math.radians(420)
truevalue_1 = math.sin(truevalue_radians_1)
    
et = abs((truevalue_1 - approxvalue_1)/truevalue_1) * 100

print('\nTest for 7π/3::')
print('Approximate Value Sine an Angle in Radians = {0:2.14f}'.format(approxvalue_1))
print('Approximate Relative Error(Ea) = {0:2.14f} '.format(ea1))
print('True Value Sine of an Angle in Radians = {0:2.14f}'.format(truevalue_1))
print('AbsoluteTrue Percent Relative Error(Et) = {0:2.14f}'.format(et))
    
    
angles = np.arange(-2*np.pi, 2*np.pi, 0.1)
true_sin = np.sin(angles)
ty_sin = [taylor_sine_appx(angles,3)[0] for angles in angles]
    
fig,ax = plt.subplots()
ax.plot(angles, true_sin)
ax.plot(angles, ty_sin)
ax.set_ylim([-2,2])
ax.legend(['True Sine Function','Taylor Series Approx with 3 terms'])
    
plt.show()
    
        