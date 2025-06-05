#pragma once

#include "esphome/core/automation.h"
#include "esphome/core/component.h"
#include "HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

template<typename... Ts> class BluetoothPasswordSetAction : public Action<Ts...> {
 public:
  explicit BluetoothPasswordSetAction(HMMD_WAVEComponent *HMMD_WAVE_comp) : HMMD_WAVE_comp_(HMMD_WAVE_comp) {}
  TEMPLATABLE_VALUE(std::string, password)

  void play(Ts... x) override { this->HMMD_WAVE_comp_->set_bluetooth_password(this->password_.value(x...)); }

 protected:
  HMMD_WAVEComponent *HMMD_WAVE_comp_;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
