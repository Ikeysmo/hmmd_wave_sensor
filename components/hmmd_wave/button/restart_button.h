#pragma once

#include "esphome/components/button/button.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class RestartButton : public button::Button, public Parented<HMMD_WAVEComponent> {
 public:
  RestartButton() = default;

 protected:
  void press_action() override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
