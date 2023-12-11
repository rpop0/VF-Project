First error:

 File "/Marabou/vnn-comp-scripts/../maraboupy/../maraboupy/MarabouNetworkONNX.py", line 163, in makeGraphEquations
 => => #     self.makeMarabouEquations(nodeName, makeEquations)
 => => #   File "/Marabou/vnn-comp-scripts/../maraboupy/../maraboupy/MarabouNetworkONNX.py", line 213, in makeMarabouEquations
 => => #     raise NotImplementedError("Operation {} not implemented".format(node.op_type))
 => => # NotImplementedError: Operation Split not implemented
 
 sh: line 33: /vnncomp2022/vnncomp_scripts/../maraboupy/prepare_instance.py: No such file or 

Fixed by using last version

2 missing files from the last version
 maraboupy.VNNLibParser'
 => => # prepare_instance.sh exit code: 1, runtim
 
 
Last error (missing operation) 
 repeated 9 more times]
 => => #   File "/Marabou/maraboupy/../maraboupy/MarabouNetworkONNX.py", line 220, in makeGraphEquations
 => => #     self.makeMarabouEquations(nodeName, makeEquations)
 => => #   File "/Marabou/maraboupy/../maraboupy/MarabouNetworkONNX.py", line 276, in makeMarabouEquations
 => => #     raise NotImplementedError("Operation {} not implemented".format(node.op_type))
 => => # NotImplementedError: Operation Slice not implemented
 
about missing operation
 https://github.com/NeuralNetworkVerification/Marabou/issues/581
 
 
Main
https://github.com/NeuralNetworkVerification/Marabou/tree/master

Scripts for vnn-comp-22 old version:
https://github.com/NeuralNetworkVerification/Marabou/tree/vnn-comp-22

Used for run_in_docker
https://github.com/stanleybak/vnncomp2021/tree/main

Benchmarks link:
https://github.com/ChristopherBrix/vnncomp2023_benchmarks/tree/main