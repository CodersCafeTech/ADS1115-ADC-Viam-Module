# [ads1115 modular service](https://app.viam.com/module/coderscafe/adc-ads1115)

This module implements the [rdk generic API](https://github.com/rdk/generic-api) in a [`coderscafe:generic:ads1115`](https://app.viam.com/module/coderscafe/adc-ads1115) model.
With this model, you can read the analog values from different channel on the ADS1115 ADC.

## Requirements

Please make sure that [I2C communication is enabled](https://docs.viam.com/operate/reference/prepare/rpi-setup/#enable-communication-protocols) on the device to which the ADC is connected.

## Build and Run

To use this module, follow these instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the [`coderscafe:generic:ads1115` module](https://app.viam.com/module/coderscafe/adc-ads1115).

## Configure your generic

> [!NOTE]  
> Before configuring your generic, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

* Navigate to the **Config** tab of your robot’s page in [the Viam app](https://app.viam.com/).
* Click on the **Components** subtab and click on the `generic` subtab.
* Select the `coderscafe:generic:ads1115` model. 
* Enter a name for your ADC component and click **Create**.
* On the new component panel, copy and paste the following attribute template into your generic’s **Attributes** box:

```json
{
  "address": "48",
  "busnum": 1,
  "gain":1
}
```
* Save and wait for the component to finish setup

> [!NOTE]  
> For more information, see [Configure a Robot](https://docs.viam.com/manage/configuration/).

### Attributes

The following attributes are available for `coderscafe:generic:ads1115` component:

| Name | Type | Inclusion | Description |
| ---- | ---- | --------- | ----------- |
| `address` | string | Optional |  I2C address |
| `busnum` | integer | Optional |  I2C Bus Number |
| `gain` | float | Optional |  Gain Configuration (2/3, 1, 2, 4, 8, 16)|

### Example Configuration

```json
{
  "address": "48",
  "busnum": 1,
  "gain":1
}
```

### Do Command
To read the analog values from the 0th channel of the ADC, navigate to the **Control** tab in Viam and enter the following command in the **Do Command** tab.

```json
{
"read_channel":
  {
    "channel":0
  }
}
```
