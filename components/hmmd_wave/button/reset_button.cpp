#include "reset_button.h"

namespace esphome {
namespace HMMD_WAVE {

void ResetButton::press_action() { this->parent_->factory_reset(); }

}  // namespace HMMD_WAVE
}  // namespace esphome
