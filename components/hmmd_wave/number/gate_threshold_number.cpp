#include "gate_threshold_number.h"

namespace esphome {
namespace HMMD_WAVE {

GateThresholdNumber::GateThresholdNumber(uint8_t gate) : gate_(gate) {}

void GateThresholdNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_gate_threshold(this->gate_);
}

}  // namespace HMMD_WAVE
}  // namespace esphome
