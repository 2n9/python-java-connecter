import sys

# pip install py4j
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
# new Scanner(System.in)
scanner = gateway.jvm.java.util.Scanner(gateway.jvm.java.util.System.in)
i = scanner.nextInt()
print(i)

# ver python
print(int(input()))


# shutdownしないとメモリが大変になるらしい
gateway.shutdown()
