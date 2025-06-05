#include "query_button.h"

namespace esphome {
namespace HMMD_WAVE {

void QueryButton::press_action() { this->parent_->read_all_info(); }

}  // namespace HMMD_WAVE
}  // namespace esphome
