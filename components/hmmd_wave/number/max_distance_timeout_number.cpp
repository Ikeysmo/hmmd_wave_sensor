#include "max_distance_timeout_number.h"

namespace esphome {
namespace HMMD_WAVE {

void MaxDistanceTimeoutNumber::control(float value) {
  this->publish_state(value);
  this->parent_->set_max_distances_timeout();
}

}  // namespace HMMD_WAVE
}  // namespace esphome
