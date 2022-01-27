from pydantic import BaseModel, Field


class ChirpstackUp(BaseModel):
    dev_eui: str = Field(alias="devEUI")
    fport: int = Field(alias="fPort")
    data: str

    class Config:
        schema_extra = {
            "example": {
                "applicationID": "123",
                "applicationName": "temperature-sensor",
                "deviceName": "garden-sensor",
                "devEUI": "AgICAgICAgI=",
                "rxInfo": [
                    {
                        "gatewayID": "AwMDAwMDAwM=",
                        "time": "2019-11-08T13:59:25.048445Z",
                        "timeSinceGPSEpoch": None,
                        "rssi": -48,
                        "loRaSNR": 9,
                        "channel": 5,
                        "rfChain": 0,
                        "board": 0,
                        "antenna": 0,
                        "location": {
                            "latitude": 52.3740364,
                            "longitude": 4.9144401,
                            "altitude": 10.5
                        },
                        "fineTimestampType": "NONE",
                        "context": "9u/uvA==",
                        "uplinkID": "jhMh8Gq6RAOChSKbi83RHQ=="
                    }
                ],
                "txInfo": {
                    "frequency": 868100000,
                    "modulation": "LORA",
                    "loRaModulationInfo": {
                        "bandwidth": 125,
                        "spreadingFactor": 11,
                        "codeRate": "4/5",
                        "polarizationInversion": False
                    }
                },
                "adr": True,
                "dr": 1,
                "fCnt": 10,
                "fPort": 5,
                "data": "3q2+7w==",
                "objectJSON": "{\"temperatureSensor\":25,\"humiditySensor\":32}",
                "tags": {
                    "key": "value"
                }
            }
        }
