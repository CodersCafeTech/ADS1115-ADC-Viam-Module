from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self
from typing import Final
from Adafruit_ADS1x15 import ADS1115
from typing import Mapping, Optional
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.logging import getLogger
from viam.components.generic import Generic

from viam.resource.types import RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, Subtype

import asyncio
import time

LOGGER = getLogger(__name__)

class ads1115(Generic, Reconfigurable):
    """
    Viam Generic component for reading analog values from ADS1115.
    """

    MODEL: ClassVar[Model] = Model(ModelFamily("coderscafe", "generic"), "ads1115")

    def __init__(self, name: str):
        super().__init__(name)
        self.adc = None

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        instance = cls(config.name)
        instance.reconfigure(config, dependencies)
        return instance

    @classmethod
    def validate(cls, config: ComponentConfig):
        """Validate configuration."""
        # Example validation logic (customize as needed)
        return

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        """Reconfigure the ADS1115 instance with new parameters."""

        self.address = config.attributes.fields["address"].string_value if "address" in config.attributes.fields else 0x48
        self.busnum = int(config.attributes.fields["busnum"].number_value) if "busnum" in config.attributes.fields else 1
        self.gain = int(config.attributes.fields["gain"].number_value) if "gain" in config.attributes.fields else 1

        # Initialize the ADS1115 with updated parameters
        self.adc = ADS1115(address=self.address, busnum=self.busnum)
        LOGGER.info(f"ADS1115 initialized at address {self.address} on bus {self.busnum} with gain {self.gain}")


    async def read_channel(self, channel: int, gain: int) -> int:
        """Read analog value from the specified channel.

        Args:
            channel (int): ADC channel number (0-3).
            gain (int, optional): Gain configuration. If not provided, uses the default gain.

        Returns:
            int: Raw analog value from the ADS1115.
        """
        if not self.adc:
            raise Exception("ADS1115 not initialized. Please ensure it is configured correctly.")

        if channel < 0 or channel > 3:
            raise ValueError("Channel must be between 0 and 3.")

        raw_value = self.adc.read_adc(channel, gain=gain)
        LOGGER.info(f"Read raw value {raw_value} from channel {channel} with gain {gain}")
        return raw_value

    async def do_command(self, command: Mapping[str, any], *, timeout: Optional[float] = None, **kwargs) -> Mapping[str, any]:
        """Execute a command.

        Args:
            command (Mapping[str, any]): Command to execute.
            timeout (Optional[float], optional): Timeout for the command. Defaults to None.

        Returns:
            Mapping[str, any]: Command result.
        """
        if "read_channel" in command:
            channel = int(command["read_channel"].get("channel"))
            gain = int(command["read_channel"].get("gain")) if "gain" in command["read_channel"] else self.gain
            value = await self.read_channel(channel, gain=gain)
            return {"value": value}

        raise ValueError("Unknown command.")


    SUBTYPE: Final = Subtype(  # pyright: ignore [reportIncompatibleVariableOverride]
        RESOURCE_NAMESPACE_RDK, RESOURCE_TYPE_COMPONENT, "generic"
    )

