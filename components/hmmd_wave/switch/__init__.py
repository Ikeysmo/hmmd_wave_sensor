import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ENTITY_CATEGORY_CONFIG,
    ICON_BLUETOOTH,
    ICON_PULSE,
)

from .. import CONF_HMMD_WAVE_ID, HMMD_WAVEComponent, HMMD_WAVE_ns

BluetoothSwitch = HMMD_WAVE_ns.class_("BluetoothSwitch", switch.Switch)
EngineeringModeSwitch = HMMD_WAVE_ns.class_("EngineeringModeSwitch", switch.Switch)

CONF_ENGINEERING_MODE = "engineering_mode"
CONF_BLUETOOTH = "bluetooth"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_HMMD_WAVE_ID): cv.use_id(HMMD_WAVEComponent),
    cv.Optional(CONF_ENGINEERING_MODE): switch.switch_schema(
        EngineeringModeSwitch,
        device_class=DEVICE_CLASS_SWITCH,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_PULSE,
    ),
    cv.Optional(CONF_BLUETOOTH): switch.switch_schema(
        BluetoothSwitch,
        device_class=DEVICE_CLASS_SWITCH,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_BLUETOOTH,
    ),
}


async def to_code(config):
    HMMD_WAVE_component = await cg.get_variable(config[CONF_HMMD_WAVE_ID])
    if engineering_mode_config := config.get(CONF_ENGINEERING_MODE):
        s = await switch.new_switch(engineering_mode_config)
        await cg.register_parented(s, config[CONF_HMMD_WAVE_ID])
        cg.add(HMMD_WAVE_component.set_engineering_mode_switch(s))
    if bluetooth_config := config.get(CONF_BLUETOOTH):
        s = await switch.new_switch(bluetooth_config)
        await cg.register_parented(s, config[CONF_HMMD_WAVE_ID])
        cg.add(HMMD_WAVE_component.set_bluetooth_switch(s))
