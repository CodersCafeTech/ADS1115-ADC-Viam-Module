import asyncio
import sys

from viam.module.module import Module
from viam.components.generic import Generic
from .ads1115 import ads1115

async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `__init__.py` file.
    """
    module = Module.from_args()
    module.add_model_from_registry(Generic.SUBTYPE, ads1115.MODEL)
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())
