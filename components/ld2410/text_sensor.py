import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_MAC_ADDRESS,
    CONF_VERSION,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_BLUETOOTH,
    ICON_CHIP,
)

from . import CONF_HMMD_WAVE_ID, HMMD_WAVEComponent

DEPENDENCIES = ["HMMD_WAVE"]

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_HMMD_WAVE_ID): cv.use_id(HMMD_WAVEComponent),
    cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_CHIP
    ),
    cv.Optional(CONF_MAC_ADDRESS): text_sensor.text_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_BLUETOOTH
    ),
}


async def to_code(config):
    HMMD_WAVE_component = await cg.get_variable(config[CONF_HMMD_WAVE_ID])
    if version_config := config.get(CONF_VERSION):
        sens = await text_sensor.new_text_sensor(version_config)
        cg.add(HMMD_WAVE_component.set_version_text_sensor(sens))
    if mac_address_config := config.get(CONF_MAC_ADDRESS):
        sens = await text_sensor.new_text_sensor(mac_address_config)
        cg.add(HMMD_WAVE_component.set_mac_text_sensor(sens))
