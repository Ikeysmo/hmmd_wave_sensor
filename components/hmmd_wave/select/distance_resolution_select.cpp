#include "distance_resolution_select.h"

namespace esphome {
namespace HMMD_WAVE {

void DistanceResolutionSelect::control(const std::string &value) {
  this->publish_state(value);
  this->parent_->set_distance_resolution(state);
}

}  // namespace HMMD_WAVE
}  // namespace esphome
