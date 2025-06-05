#pragma once

#include "esphome/components/number/number.h"
#include "../HMMD_WAVE.h"

namespace esphome {
namespace HMMD_WAVE {

class GateThresholdNumber : public number::Number, public Parented<HMMD_WAVEComponent> {
 public:
  GateThresholdNumber(uint8_t gate);

 protected:
  uint8_t gate_;
  void control(float value) override;
};

}  // namespace HMMD_WAVE
}  // namespace esphome
