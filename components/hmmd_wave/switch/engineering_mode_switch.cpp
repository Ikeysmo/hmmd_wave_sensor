#include "engineering_mode_switch.h"

namespace esphome {
namespace HMMD_WAVE {

void EngineeringModeSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_engineering_mode(state);
}

}  // namespace HMMD_WAVE
}  // namespace esphome
