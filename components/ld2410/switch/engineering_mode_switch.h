#pragma once

#include "esphome/components/switch/switch.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class EngineeringModeSwitch : public switch_::Switch, public Parented<HMMD_WAVEComponent> {
 public:
  EngineeringModeSwitch() = default;

 protected:
  void write_state(bool state) override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
