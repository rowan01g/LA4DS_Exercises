#%%
import numpy as np

def FrobeniusNorm(A): 
    norm = np.linalg.norm(A, 'fro')
    return norm

def TraceNorm(A):
    trace_norm = (np.trace(A.T@A))**0.5
    return trace_norm

def TraceNorm2(A):
    trace_norm = (np.trace(A@A.T))**0.5
    return trace_norm

A = np.random.randn(10,10)

if FrobeniusNorm(A) == TraceNorm(A):
    print(f'The trace norm, {TraceNorm(A)} and frobenius norm, {FrobeniusNorm(A)} are equal for A.T@A')
else: 
    print('yo something went wrong')

if FrobeniusNorm(A) == TraceNorm2(A):
    print(f'The trace norm, {TraceNorm2(A)} and frobenius norm, {FrobeniusNorm(A)} are equal for A@A.T')
else: 
    print('yo they not equal')





# %%