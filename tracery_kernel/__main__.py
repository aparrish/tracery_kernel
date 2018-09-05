from ipykernel.kernelapp import IPKernelApp
from . import TraceryKernel

IPKernelApp.launch_instance(kernel_class=TraceryKernel)
