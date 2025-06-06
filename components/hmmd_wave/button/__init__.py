import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv
from esphome.const import (
    CONF_FACTORY_RESET,
    CONF_RESTART,
    DEVICE_CLASS_RESTART,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_DATABASE,
    ICON_RESTART,
    ICON_RESTART_ALERT,
)

from .. import CONF_HMMD_WAVE_ID, HMMD_WAVEComponent, HMMD_WAVE_ns

QueryButton = HMMD_WAVE_ns.class_("QueryButton", button.Button)
ResetButton = HMMD_WAVE_ns.class_("ResetButton", button.Button)
RestartButton = HMMD_WAVE_ns.class_("RestartButton", button.Button)

CONF_QUERY_PARAMS = "query_params"

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_HMMD_WAVE_ID): cv.use_id(HMMD_WAVEComponent),
    cv.Optional(CONF_FACTORY_RESET): button.button_schema(
        ResetButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_RESTART_ALERT,
    ),
    cv.Optional(CONF_RESTART): button.button_schema(
        RestartButton,
        device_class=DEVICE_CLASS_RESTART,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_RESTART,
    ),
    cv.Optional(CONF_QUERY_PARAMS): button.button_schema(
        QueryButton,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        icon=ICON_DATABASE,
    ),
}


async def to_code(config):
    HMMD_WAVE_component = await cg.get_variable(config[CONF_HMMD_WAVE_ID])
    if factory_reset_config := config.get(CONF_FACTORY_RESET):
        b = await button.new_button(factory_reset_config)
        await cg.register_parented(b, config[CONF_HMMD_WAVE_ID])
        cg.add(HMMD_WAVE_component.set_reset_button(b))
    if restart_config := config.get(CONF_RESTART):
        b = await button.new_button(restart_config)
        await cg.register_parented(b, config[CONF_HMMD_WAVE_ID])
        cg.add(HMMD_WAVE_component.set_restart_button(b))
    if query_params_config := config.get(CONF_QUERY_PARAMS):
        b = await button.new_button(query_params_config)
        await cg.register_parented(b, config[CONF_HMMD_WAVE_ID])
        cg.add(HMMD_WAVE_component.set_query_button(b))
