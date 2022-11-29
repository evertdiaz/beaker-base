from pyteal import *
from beaker import *

# Create a class, subclassing Application from beaker
class MyApplication(Application):
  # Add an external method with ABI method signature `hello(string)string`
  @external
  def hello(self, name: abi.String, *, output: abi.String):
    # Set output to the result of `Hello, `+name
    return output.set(Concat(Bytes("Hello World, "), name.get()))
