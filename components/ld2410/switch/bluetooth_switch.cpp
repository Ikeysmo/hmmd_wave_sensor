#include "bluetooth_switch.h"

namespace esphome {
namespace HMMD_WAVE {

void BluetoothSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_bluetooth(state);
}

}  // namespace HMMD_WAVE
}  // namespace esphome
