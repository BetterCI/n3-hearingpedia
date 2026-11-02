"""Original calculus teaching models; no listener, biological or device measurements."""
import json,math
import numpy as np
from scipy import integrate
def pulse(t,A=1.,tau=.002):
    return A*np.exp(-np.asarray(t)**2/(2*tau*tau))
def pulse_derivative(t,A=1.,tau=.002):
    return -np.asarray(t)/(tau*tau)*pulse(t,A,tau)
def secants():
    a=.002;h=np.array([.002,.001,.0002,.00002])
    return a,h,(pulse(a+h)-pulse(a))/h,float(pulse_derivative(a))
def taylor(u,degree):
    return sum((-np.asarray(u))**k/math.factorial(k) for k in range(degree+1))
def riemann(N):
    return float(np.sum(((np.arange(N)+.5)/N)**2)/N)
def cycle():
    T=.01;t=np.linspace(0,T,481);p=np.sin(2*np.pi*t/T)
    signed=T/(2*np.pi)*(1-np.cos(2*np.pi*t/T))
    square=t/2-T/(8*np.pi)*np.sin(4*np.pi*t/T)
    return dict(T=T,t=t,p=p,signed=signed,square=square,
        signed_integral=float(integrate.trapezoid(p,x=t)),
        square_integral=float(integrate.trapezoid(p*p,x=t)),
        absolute_integral_exact=2*T/np.pi,RMS=float(np.sqrt(integrate.trapezoid(p*p,x=t)/T)))
def objective(a,b):
    return (np.asarray(a)-1)**2+4*(np.asarray(b)+.5)**2
def objective_gradient(a,b):
    return np.array([2*(a-1),8*(b+.5)])
def partial_counterexample(x,y):
    x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
    den=x*x+y*y
    return np.divide(x*y,den,out=np.zeros_like(den),where=den!=0)
def disk(R=3.,sigma=1.):
    return 2*np.pi*sigma*sigma*(1-np.exp(-R*R/(2*sigma*sigma)))
def decay_step(t,y0=0.,tau=.005):
    return 1+(y0-1)*np.exp(-np.asarray(t)/tau)
def euler(dt,T=.06,tau=.005):
    n=np.arange(int(round(T/dt))+1);t=n*dt;y=np.zeros(len(t))
    for k in range(len(t)-1):y[k+1]=y[k]+dt*(1-y[k])/tau
    return t,y
def difference_errors():
    h=np.logspace(-16,-1,181);a=1.;true=np.exp(a)
    forward=(np.exp(a+h)-np.exp(a))/h
    central=(np.exp(a+h)-np.exp(a-h))/(2*h)
    return h,abs(forward-true),abs(central-true)
def noise_difference():
    rng=np.random.default_rng(20261102);sigma=1e-6;h=np.logspace(-5,-1,9)
    # Independent additive noise at the two samples, no noisy baseline shared.
    pair=rng.normal(0,sigma,(100000,2));noise=pair[:,0]-pair[:,1]
    observed=np.array([np.std(noise/(2*hi),ddof=1) for hi in h])
    return sigma,h,observed,sigma/(np.sqrt(2)*h)
def quadrature():
    out=[]
    for N in [8,16,32,64]:
        x=np.linspace(0,1,N+1)
        out.append(dict(intervals=N,trapezoid=float(integrate.trapezoid(x**4,x=x)),
            Simpson=float(integrate.simpson(x**4,x=x))))
    return out
def ode_solution():
    tau=.005;t=np.linspace(0,.03,301)
    sol=integrate.solve_ivp(lambda t,y:(1-y)/tau,(0,.03),[.4],method='RK45',
        t_eval=t,rtol=1e-9,atol=1e-12,max_step=.001)
    assert sol.success
    exact=decay_step(t,.4,tau)
    return t,sol.y[0],exact,float(np.max(abs(sol.y[0]-exact)))
def summary():
    a,h,slopes,true=secants();c=cycle();_,_,_,err=ode_solution();sigma,nh,obs,theory=noise_difference()
    return dict(gaussian=dict(amplitude_Pa=1,tau_s=.002,tangent_t_s=a,derivative_Pa_per_s=true,
                    secant_h_s=h.tolist(),secant_slopes_Pa_per_s=slopes.tolist()),
        taylor_exp_minus=dict(u=.2,linear=float(taylor(.2,1)),exact=float(np.exp(-.2)),
            linear_absolute_error=float(abs(taylor(.2,1)-np.exp(-.2))),linear_error_bound=.2**2/2),
        riemann_x_squared=[dict(N=N,midpoint=riemann(N),exact=1/3) for N in [4,16,64]],
        cycle={k:v for k,v in c.items() if k not in ['t','p','signed','square']},
        gradient_at_2_and_point25=objective_gradient(2,.25).tolist(),
        double_integral=dict(sigma=1,R=3,disk_integral=float(disk()),whole_plane=2*np.pi),
        quadrature_x_fourth=quadrature(),ode=dict(tau_s=.005,initial_value=.4,RK45_max_absolute_error=err,
            Euler_h_s=[.001,.008,.012],Euler_h_over_tau=[.2,1.6,2.4]),
        noise_difference=dict(sigma=sigma,seed=20261102,draws=100000,
            maximum_relative_SD_deviation=float(np.max(abs(obs/theory-1)))))
if __name__=='__main__':print(json.dumps(summary(),ensure_ascii=True,indent=2))
