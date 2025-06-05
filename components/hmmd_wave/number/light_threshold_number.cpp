#include "light_threshold_number.h"

namespace esphome {
namespace HMMD_WAVE {

void LightThresholdNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_light_out_control();
}

}  // namespace HMMD_WAVE
}  // namespace esphome
