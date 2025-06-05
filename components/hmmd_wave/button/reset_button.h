#pragma once

#include "esphome/components/button/button.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class ResetButton : public button::Button, public Parented<HMMD_WAVEComponent> {
 public:
  ResetButton() = default;

 protected:
  void press_action() override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
