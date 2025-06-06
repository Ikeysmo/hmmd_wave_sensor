import esphome.codegen as cg
from esphome.components import binary_sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_HAS_MOVING_TARGET,
    CONF_HAS_STILL_TARGET,
    CONF_HAS_TARGET,
    DEVICE_CLASS_MOTION,
    DEVICE_CLASS_OCCUPANCY,
    DEVICE_CLASS_PRESENCE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_ACCOUNT,
    ICON_MOTION_SENSOR,
)

from . import CONF_HMMD_WAVE_ID, HMMD_WAVEComponent

DEPENDENCIES = ["HMMD_WAVE"]
CONF_OUT_PIN_PRESENCE_STATUS = "out_pin_presence_status"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_HMMD_WAVE_ID): cv.use_id(HMMD_WAVEComponent),
    cv.Optional(CONF_HAS_TARGET): binary_sensor.binary_sensor_schema(
        device_class=DEVICE_CLASS_OCCUPANCY,
        icon=ICON_ACCOUNT,
    ),
    cv.Optional(CONF_HAS_MOVING_TARGET): binary_sensor.binary_sensor_schema(
        device_class=DEVICE_CLASS_MOTION,
        icon=ICON_MOTION_SENSOR,
    ),
    cv.Optional(CONF_HAS_STILL_TARGET): binary_sensor.binary_sensor_schema(
        device_class=DEVICE_CLASS_OCCUPANCY,
        icon=ICON_MOTION_SENSOR,
    ),
    cv.Optional(CONF_OUT_PIN_PRESENCE_STATUS): binary_sensor.binary_sensor_schema(
        device_class=DEVICE_CLASS_PRESENCE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_ACCOUNT,
    ),
}


async def to_code(config):
    HMMD_WAVE_component = await cg.get_variable(config[CONF_HMMD_WAVE_ID])
    if has_target_config := config.get(CONF_HAS_TARGET):
        sens = await binary_sensor.new_binary_sensor(has_target_config)
        cg.add(HMMD_WAVE_component.set_target_binary_sensor(sens))
    if has_moving_target_config := config.get(CONF_HAS_MOVING_TARGET):
        sens = await binary_sensor.new_binary_sensor(has_moving_target_config)
        cg.add(HMMD_WAVE_component.set_moving_target_binary_sensor(sens))
    if has_still_target_config := config.get(CONF_HAS_STILL_TARGET):
        sens = await binary_sensor.new_binary_sensor(has_still_target_config)
        cg.add(HMMD_WAVE_component.set_still_target_binary_sensor(sens))
    if out_pin_presence_status_config := config.get(CONF_OUT_PIN_PRESENCE_STATUS):
        sens = await binary_sensor.new_binary_sensor(out_pin_presence_status_config)
        cg.add(HMMD_WAVE_component.set_out_pin_presence_status_binary_sensor(sens))
