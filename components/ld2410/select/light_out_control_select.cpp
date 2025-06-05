#include "light_out_control_select.h"

namespace esphome {
namespace HMMD_WAVE {

void LightOutControlSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_light_out_control();
}

}  // namespace HMMD_WAVE
}  // namespace esphome
