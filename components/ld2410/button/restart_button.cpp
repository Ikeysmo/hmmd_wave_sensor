#include "restart_button.h"

namespace esphome {
namespace HMMD_WAVE {

void RestartButton::press_action() { this->parent_->restart_and_read_all_info(); }

}  // namespace HMMD_WAVE
}  // namespace esphome
