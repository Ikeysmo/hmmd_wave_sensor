#include "baud_rate_select.h"

namespace esphome {
namespace HMMD_WAVE {

void BaudRateSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_baud_rate(state);
}

}  // namespace HMMD_WAVE
}  // namespace esphome
