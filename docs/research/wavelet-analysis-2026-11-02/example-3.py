import numpy as np
import pywt
t = np.arange(1024) / 1024
x = np.cos(2*np.pi*160*t)
wp = pywt.WaveletPacket(x, 'haar', mode='periodization', maxlevel=3)
nodes = wp.get_level(3, order='freq')
energy = np.array([np.sum(node.data**2) for node in nodes])
assert [node.path for node in nodes] == ['aaa', 'aad', 'add', 'ada',
                                        'dda', 'ddd', 'dad', 'daa']
assert np.isclose(energy.sum(), x @ x)
assert nodes[int(energy.argmax())].path == 'add'
for i, node in enumerate(nodes):
    print(node.path, f'nominal {64*i}-{64*(i+1)} Hz', energy[i]/energy.sum())
